# <img src="https://api.iconify.design/logos/aws-ec2.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: A Torre de Vigia - Criando Instâncias EC2 via Console e CLI

### O Cenário (A "User Story")

> **Como** um engenheiro de nuvem, **EU QUERO** provisionar um ponto de acesso seguro (um Host Bastião) usando o Console e, a partir dele, automatizar a criação de um servidor web usando a AWS CLI, **PARA QUE** eu possa seguir as melhores práticas de segurança e automação.

### A Dor que o Lab Resolve

1.  **Acesso Inseguro:** Acessar todos os servidores diretamente da internet é um risco. O padrão do Host Bastião resolve isso criando um único ponto de entrada controlado.
2.  **Provisionamento Manual:** Criar servidores clicando no console é lento e propenso a erros. A automação via CLI resolve isso, tornando o processo rápido e repetível.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Lançar uma instância EC2 (Host Bastião) usando o Console da AWS.
* [ ] Conectar-se à instância usando o EC2 Instance Connect (uma alternativa ao SSH).
* [ ] Usar a AWS CLI de dentro do Bastião para lançar um segundo servidor web.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Construindo a "Torre de Vigia" (Lançar o Host Bastião via Console)

**Analogia:** Primeiro, vamos construir nossa torre de vigia fortificada, que será nosso único ponto de acesso seguro.

1.  No **Console de Gerenciamento da AWS (AWS Management Console)**, navegue até o serviço **EC2**.
2.  Clique em **Lançar instância (Launch instance)**.
3.  **Nome e tags (Name and tags):** Dê o nome de `Host-Bastiao`.
4.  **AMI:** Mantenha o padrão **Amazon Linux 2**.
5.  **Tipo de instância (Instance type):** Selecione `t3.micro`.
6.  **Par de chaves (Key pair):** Selecione **Prosseguir sem um par de chaves (Proceed without a key pair)**. Usaremos o Instance Connect.
7.  **Configurações de rede (Network settings):** Clique em **Editar (Edit)**.
    * **VPC:** `Lab VPC`.
    * **Sub-rede (Subnet):** `Sub-rede pública (Public Subnet)`.
    * **Atribuir IP público automaticamente (Auto-assign public IP):** Mantenha `Habilitar (Enable)`.
    * **Firewall (grupos de segurança):**
        * Selecione **Criar grupo de segurança (Create security group)**.
        * **Nome do grupo:** `SG-Bastiao`.
        * **Descrição:** `Permite acesso seguro ao bastiao`.
8.  **Detalhes avançados (Advanced details):**
    * **Perfil de instância do IAM (IAM instance profile):** Selecione `Bastion-Role`.
        > **O "Porquê":** Esta é a etapa crucial. Anexar esta `Função (Role)` dá à nossa instância permissão para "falar" com outros serviços da AWS, como o próprio EC2, para que possamos lançar nosso segundo servidor a partir dela.
9.  Revise o resumo e clique em **Lançar instância (Launch instance)**.

#### Tarefa 2: Entrando na Torre de Vigia (Conectar com Instance Connect)

1.  Na lista de instâncias, aguarde o `Host-Bastiao` estar no estado `Em execução (Running)`.
2.  Selecione a instância e clique em **Conectar (Connect)**.
3.  Na aba **EC2 Instance Connect**, mantenha os padrões e clique em **Conectar (Connect)**.
4.  Uma nova aba do navegador se abrirá com um terminal de linha de comando. **Você está dentro do seu Host Bastião!**

#### Tarefa 3: Construindo o Servidor Web de Dentro da Fortaleza (Usando a AWS CLI)

**Analogia:** Agora, de dentro da segurança da nossa torre de vigia, vamos dar a ordem via "rádio" (CLI) para construir um novo servidor web.

*Execute todos os comandos a seguir no terminal do Instance Connect.*

1.  **Passo 1: Descobrir a AMI mais recente**
    > **O "Porquê":** Em vez de "chumbar" um ID de AMI no nosso script, vamos perguntar à AWS qual é a versão mais recente e segura do Amazon Linux 2. Isso torna nosso script mais robusto.
    ```bash
    # Define a Região dinamicamente
    AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
    export AWS_DEFAULT_REGION=${AZ::-1}
    # Pega o ID da AMI mais recente e o guarda em uma variável
    AMI=$(aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2 --query 'Parameters[0].[Value]' --output text)
    echo $AMI
    ```

2.  **Passo 2: Descobrir os IDs da Rede**
    > **O "Porquê":** Vamos pegar os IDs da sub-rede e do security group dinamicamente, baseados em suas tags.
    ```bash
    SUBNET=$(aws ec2 describe-subnets --filters 'Name=tag:Name,Values=Public Subnet' --query 'Subnets[].SubnetId' --output text)
    SG=$(aws ec2 describe-security-groups --filters Name=group-name,Values=WebSecurityGroup --query 'SecurityGroups[].GroupId' --output text)
    echo $SUBNET
    echo $SG
    ```

3.  **Passo 3: Baixar o Script de Instalação**
    > **O "Porquê":** Vamos usar um script `User Data` para instalar nosso servidor web automaticamente no momento do lançamento.
    ```bash
    wget [https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-1-23732/171-lab-JAWS-create-ec2/s3/UserData.txt](https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-1-23732/171-lab-JAWS-create-ec2/s3/UserData.txt)
    cat UserData.txt
    ```

4.  **Passo 4: Lançar a Instância (A Ordem Final)**
    > **O "Porquê":** Este comando junta todas as variáveis que coletamos para construir nosso servidor web de forma 100% automatizada.
    ```bash
    INSTANCE=$(\
    aws ec2 run-instances \
    --image-id $AMI \
    --subnet-id $SUBNET \
    --security-group-ids $SG \
    --user-data file://UserData.txt \
    --instance-type t3.micro \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=Servidor-Web-via-CLI}]' \
    --query 'Instances[*].InstanceId' \
    --output text \
    )
    echo $INSTANCE
    ```

5.  **Passo 5: Verificar o Status**
    > Aguarde alguns minutos para a instância iniciar e o script User Data rodar.
    ```bash
    # Verifique o status até que ele mude de "pending" para "running"
    aws ec2 describe-instances --instance-ids $INSTANCE --query 'Reservations[].Instances[].State.Name' --output text
    ```

6.  **Passo 6: Testar o Servidor Web**
    ```bash
    # Pega o endereço público do novo servidor
    PUBLIC_DNS=$(aws ec2 describe-instances --instance-ids $INSTANCE --query 'Reservations[].Instances[].PublicDnsName' --output text)
    echo $PUBLIC_DNS
    ```
    * Copie o endereço DNS da saída do comando acima.
    * Cole em uma nova aba do navegador. **Seu servidor web, criado via CLI, está no ar!**

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você atuou como um verdadeiro engenheiro de nuvem. Usou o console para uma tarefa de configuração única (o Bastião) e, em seguida, usou o poder da automação com a AWS CLI para provisionar um novo recurso de forma dinâmica e repetível, tudo isso seguindo as melhores práticas de segurança.

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: O Arquiteto e o Robô Construtor

No início da minha jornada na nuvem, uma pergunta sempre vinha à mente: "Devo usar o Console da AWS, com sua interface visual, ou a Linha de Comando (CLI), que parece tão poderosa?". O laboratório de hoje me deu a resposta da forma mais clara possível: **use os dois, cada um para o que ele faz de melhor.**

A missão foi simular um cenário super realista: construir uma "torre de vigia" (um Host Bastião) de forma segura e, de dentro dela, automatizar a criação de um novo servidor. Foi uma lição sobre ser o "Arquiteto" e o "Comandante".

### O Arquiteto no Console (A Torre de Vigia)

A primeira parte foi usar o Console da AWS para criar o Host Bastião.

* **A Dor:** Como criar um ponto de acesso seguro para minha rede, sem expor todos os meus servidores à internet?
* **O Que Eu Fiz:** Eu agi como um arquiteto, usando a interface visual do console para projetar cuidadosamente cada detalhe da minha "torre de vigia". Escolhi a planta (AMI), o motor (tipo de instância) e, o mais importante, o sistema de segurança (Security Group).
* **O "Aha!" Moment:** A grande sacada foi anexar uma **Função do IAM (IAM Role)** à instância.
    * **Analogia:** Foi como dar um **"crachá de autoridade"** para a torre de vigia. Esse crachá deu a ela permissão para, em meu nome, dar ordens a outros serviços da AWS.

Usar o console para essa tarefa de configuração única e estratégica foi perfeito. Ele me deu a visibilidade para tomar as decisões certas com calma e precisão.

### O Comandante na CLI (O Robô Construtor)

Com a torre de vigia pronta e segura, a missão mudou. Agora eu precisava construir um novo servidor web.

* **A Dor:** Construir servidores um por um no console é lento e sujeito a erros. Como fazer isso de forma rápida e 100% repetível?
* **O Que Eu Fiz:** Conectei-me à minha "torre de vigia" e, de lá, agi como um comandante. Em vez de construir o novo servidor manualmente, eu escrevi uma **"ordem de construção"** (o comando `aws ec2 run-instances`) e a entreguei ao meu **"robô construtor"** (a AWS CLI).

* **O Resultado Incrível:** O "robô" foi genial. Ele usou os superpoderes da automação:
    1.  Primeiro, ele perguntou ao SSM qual era a "planta baixa" mais recente e segura (a última AMI do Amazon Linux).
    2.  Depois, ele identificou o "endereço" correto (a Sub-rede e o Security Group) automaticamente.
    3.  Finalmente, ele construiu o servidor perfeitamente, exatamente como ordenado.

### A Grande Lição

O lab de hoje me ensinou a lição fundamental do **"usar a ferramenta certa para o trabalho certo"**.

* O **Console da AWS** é perfeito para o **Arquiteto**: para o planejamento, a visualização e as configurações estratégicas que você faz uma vez.
* A **AWS CLI** é a ferramenta perfeita para o **Comandante**: para as tarefas repetitivas, para a automação e para dar ordens que precisam ser executadas com perfeição todas as vezes.

Conectar a uma instância para lançar outra foi uma simulação incrível de um processo operacional do mundo real. Mostrou como a segurança (o Bastião) e a automação (a CLI) não são inimigas, mas sim parceiras na construção de uma infraestrutura robusta.

#AWS #Cloud #EC2 #Automation #CLI #DevOps #Security #AWSreStart