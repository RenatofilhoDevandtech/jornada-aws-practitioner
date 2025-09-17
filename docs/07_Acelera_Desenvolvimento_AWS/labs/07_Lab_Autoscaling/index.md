# <img src="https://api.iconify.design/logos/aws-auto-scaling.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: A Fábrica de Servidores - Usando o Auto Scaling com a AWS CLI

### O Cenário (A "User Story")

> **Como** um engenheiro DevOps, **EU QUERO** usar a AWS CLI para criar uma imagem de servidor web padronizada e, em seguida, usar o console para construir uma frota de servidores que escala automaticamente, **PARA QUE** eu possa dominar tanto a automação via script quanto a orquestração visual de uma arquitetura resiliente.

### A Dor que o Lab Resolve

Construir uma arquitetura elástica envolve muitas peças móveis: AMIs, Launch Templates, Load Balancers, Grupos de Auto Scaling. É fácil se perder na complexidade. Este laboratório resolve a dor da **"orquestração complexa"**, mostrando o fluxo de trabalho de ponta a ponta, unindo o poder da linha de comando com a clareza do console.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Criar uma instância EC2 e uma AMI customizada usando a AWS CLI.
* [ ] Criar um Modelo de Lançamento (Launch Template).
* [ ] Configurar um Grupo de Auto Scaling (Auto Scaling group) que usa um ELB.
* [ ] Definir e testar políticas de escalabilidade para reagir a uma carga de trabalho variável.


### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: A "Receita" Automatizada (Criando a Instância e a AMI via CLI)

**Analogia:** Vamos usar nosso "terminal de comando" para construir nosso primeiro "pizzaiolo mestre" e depois tirar uma "fotografia" dele para criar a "receita padrão" (a AMI).

1.  **Conecte-se ao `Host de Comando (Command Host)`:** Use o EC2 Instance Connect.
2.  **Configure a AWS CLI:** Se necessário, execute `aws configure` e insira suas credenciais do laboratório.
3.  **Examine o Script de Instalação (`UserData.txt`):**
    ```bash
    cd /home/ec2-user/
    cat UserData.txt
    ```
    > Este script instala uma aplicação PHP que usaremos para simular carga de CPU.
4.  **Lance a Instância "Molde":**
    * No painel **Detalhes (Details)** do lab, copie os valores para `KEYNAME`, `AMIID`, `HTTPACCESS`, e `SUBNETID`.
    * Substitua os valores no comando abaixo e execute-o:
    ```bash
    aws ec2 run-instances --key-name <SEU_KEYNAME> --instance-type t3.micro --image-id <SEU_AMIID> --user-data file:///home/ec2-user/UserData.txt --security-group-ids <SEU_HTTPACCESS_SG_ID> --subnet-id <SEU_SUBNETID> --associate-public-ip-address --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=WebServer-Molde}]' --output text --query 'Instances[*].InstanceId'
    ```
5.  **Anote o `ID da Instância (InstanceId)`** que o comando retornou. Vamos chamá-lo de `NEW-INSTANCE-ID`.
6.  **Aguarde a Instância Ficar Pronta:**
    ```bash
    aws ec2 wait instance-running --instance-ids <SEU_NEW-INSTANCE-ID>
    ```
7.  **Crie a AMI a partir da Instância:**
    ```bash
    aws ec2 create-image --name WebServerAMI --instance-id <SEU_NEW-INSTANCE-ID>
    ```
    > **O "Porquê":** Este comando "fotografa" o estado da sua instância, com a aplicação já instalada, e cria um template (a AMI) que podemos reutilizar, garantindo a consistência.

#### Tarefa 2: Construindo a Arquitetura Elástica (Usando o Console)

Com nossa "receita" (AMI) pronta, vamos usar o console para montar a "fábrica de pizzas" (a arquitetura de Auto Scaling).

1.  **Crie o Application Load Balancer:**
    * Vá para **EC2 > Balanceadores de Carga (Load Balancers)** e crie um **Application Load Balancer** chamado `WebServerELB`.
    * Em `Mapeamento de rede (Network mapping)`, associe-o à `VPC do laboratório (Lab VPC)`, às **duas sub-redes públicas** e ao `Grupo de segurança (Security group)` `HTTPAccess`.
    * Em `Ouvintes e roteamento (Listeners and routing)`, crie um novo `Grupo de destino (Target Group)` chamado `webserver-app` para `Instâncias (Instances)`.
    * Configure o *Listener* do ELB para encaminhar o tráfego para este novo Target Group.
    * **Anote o Nome DNS (DNS name)** do seu ELB.

2.  **Crie o Modelo de Lançamento (Launch Template):**
    * Vá para **EC2 > Modelos de execução (Launch Templates)** e crie um novo modelo chamado `web-app-launch-template`.
    * Marque a caixa de **Orientação sobre o Auto Scaling (Auto Scaling guidance)**.
    * Em **AMI**, selecione a sua `WebServerAMI` na aba `Minhas AMIs (My AMIs)`.
    * **Tipo de instância (Instance type):** `t3.micro`.
    * **Grupos de segurança (Security groups):** Selecione o `HTTPAccess`.

3.  **Crie o Grupo de Auto Scaling:**
    * A partir do seu novo Launch Template, use o menu **Ações (Actions)** para **Criar grupo do Auto Scaling**.
    * **Nome do grupo:** `Web-App-Auto-Scaling-Group`.
    * **Rede:** Selecione a `Lab VPC` e as **duas sub-redes PRIVADAS**.
    * **Balanceamento de Carga:** Anexe ao seu Target Group `webserver-app` existente e habilite as **verificações de saúde do ELB**.
    * **Tamanho do Grupo e Políticas:**
        * **Capacidade desejada (Desired capacity):** `2`.
        * **Mínima (Minimum capacity):** `2`.
        * **Máxima (Maximum capacity):** `4`.
        * **Política (Policy):** `Política de escalabilidade de rastreamento de destino (Target tracking scaling policy)` com a métrica `Média de utilização da CPU (Average CPU utilization)` e o alvo `50`.

#### Tarefa 3: Verificando e Testando a Automação

1.  **Verifique os Alvos:** Vá para **EC2 > Grupos de destino (Target Groups)**, selecione `webserver-app` e verifique a aba `Destinos (Targets)`. Aguarde as duas novas instâncias ficarem com o status **`healthy` (íntegro)**.
2.  **Teste o ELB:** Cole o **Nome DNS** do seu Load Balancer no navegador. O site deve carregar.
3.  **Teste de Estresse:** Na página do site, clique em **Start Stress**.
4.  **Observe a Mágica:**
    * No console do **CloudWatch > Alarmes (Alarms)**, você verá o alarme de alta CPU disparar.
    * No console do **EC2 > Grupos do Auto Scaling (Auto Scaling Groups)**, na aba **Histórico de atividades (Activity history)**, você verá o ASG iniciando novas instâncias para lidar com a carga!

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos

* [ ] No **Auto Scaling**, delete o `Web-App-Auto-Scaling-Group`.
* [ ] Delete o **Launch Template**.
* [ ] Delete o **Load Balancer** `WebServerELB` e seu **Target Group**.
* [ ] Em **AMIs**, desregistre a `WebServerAMI` e delete o snapshot associado.
* [ ] Termine a instância `WebServer-Molde` original.

---

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: O Dia em que Minha Aplicação Ganhou Vida

Hoje foi um daqueles dias que marcam a jornada de aprendizado. Até agora, eu vinha construindo as "peças" da minha infraestrutura na AWS: um servidor aqui, um firewall ali. Mas hoje, no lab do AWS re/Start, eu juntei todas essas peças para criar algo que se parece com um organismo vivo: uma arquitetura que se adapta, cresce e se cura sozinha.

A missão foi usar tanto a linha de comando (CLI) quanto o console para construir uma aplicação web totalmente elástica. Foi a combinação perfeita da força da automação com a clareza da arquitetura visual.

### A Jornada em 3 Atos

#### Ato 1: A Receita Automatizada (A "Golden AMI" via CLI)

* **A Dor:** Se eu preciso de 10 servidores web, como garanto que todos sejam *exatamente* iguais? E como posso automatizar a criação desse "molde"?
* **O Que Eu Fiz:** A primeira parte foi usar a CLI para construir o "pizzaiolo mestre" (uma instância EC2) e tirar uma "fotografia" dele para criar a **"receita-mestra" (a AMI)**.
* **O "Aha!" Moment:** Fazer isso via linha de comando, de forma programática, foi o primeiro estalo. Eu não precisei de cliques; eu dei uma ordem. Isso me mostrou o poder da automação desde o início do processo.

#### Ato 2: O Arquiteto da Fábrica (ELB e ASG via Console)

* **A Dor:** Como eu pego essa "receita" e construo um sistema inteiro que distribui clientes e reage ao movimento da loja?
* **O Que Eu Fiz:** Mudei para o console para atuar como o **"arquiteto da fábrica de pizzas"**.
* **O "Aha!" Moment:** Foi aqui que as peças se encaixaram. Eu construí:
    1.  O **"Gerente do Balcão" (o Elastic Load Balancer)**, responsável por receber os clientes e distribuir os pedidos.
    2.  O **"Manual de Contratação" (o Launch Template)**, que usa a "receita-mestra" (nossa AMI) para criar pizzaiolos perfeitos.
    3.  E, finalmente, contratei o **"Gerente Geral Autônomo" (o Auto Scaling Group)**, dando a ele a regra de ouro: "Mantenha a 'taxa de estresse' da cozinha em 50%."

#### Ato 3: O Teste de Estresse (Ver a Mágica Acontecer)
* **A Experiência:** A melhor parte foi simular um pico de tráfego. Ver o alarme do CloudWatch disparar no monitor e, segundos depois, ver as novas instâncias aparecendo **sozinhas** na lista do EC2 foi... mágico.
* **A Prova Final:** O teste de "auto-cura". Eu deliberadamente **deletei** uma das instâncias em execução. Em vez de pânico, o "Gerente Geral" (ASG) calmamente detectou a falha, removeu o servidor "doente" e **contratou um novo clone saudável** para manter a meta.

### A Grande Lição
O lab de hoje me mostrou que a nuvem não é sobre servidores. É sobre construir **sistemas**. Cada serviço (AMI, ELB, ASG, CloudWatch) é uma peça de um quebra-cabeça, e a habilidade do arquiteto é saber como juntá-las para criar um organismo que se adapta e se cura sozinho.

Construir essa arquitetura elástica, combinando o poder da CLI para a preparação e a clareza do console para a orquestração, foi como ver o motor de um carro funcionando pela primeira vez. De repente, os conceitos de **Alta Disponibilidade** e **Elasticidade** deixaram de ser palavras em um slide e se tornaram algo real, que eu construí. É um divisor de águas na minha jornada.

#AWS #Cloud #AutoScaling #HighAvailability #DevOps #AWSreStart #CloudPractitioner