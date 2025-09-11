# <img src="https://api.iconify.design/logos/aws-ec2.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab 01: Introdução ao Amazon EC2

### O Cenário (A "User Story")
> **Como** um novo engenheiro de nuvem, **EU QUERO** lançar um servidor web simples na AWS, **PARA QUE** eu possa entender na prática o ciclo de vida completo de um servidor virtual, desde sua criação até sua destruição.

### A Dor que o Lab Resolve
No mundo tradicional, obter um novo servidor físico pode levar semanas ou meses (compra, entrega, instalação no data center). Este laboratório mostra como a nuvem reduz esse processo para **minutos**, permitindo uma agilidade sem precedentes.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Lançar (`Launch`) uma instância EC2 com um script de inicialização.
* [ ] Monitorar a saúde da sua instância.
* [ ] Modificar um firewall virtual (`Security Group`) para permitir acesso web.
* [ ] Redimensionar (`Resize`) sua instância para se adaptar a novas necessidades.
* [ ] Testar e desabilitar a proteção contra término acidental.
* [ ] Terminar (`Terminate`) sua instância para parar os custos.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Tarefa 1: Lançando sua Instância EC2

Nesta tarefa, vamos criar nosso primeiro servidor virtual e, durante sua inicialização, instalar automaticamente um servidor web.

1.  No Console de Gerenciamento da AWS, no menu **Services** (Serviços), escolha **EC2**.
2.  No painel de navegação esquerdo, clique em **EC2 Dashboard** (Painel do EC2) para garantir que você está na página principal.
3.  Clique em **Launch instance** (Lançar instância).

#### Passo 1: Nomeando sua Instância
> Dê um nome claro e descritivo. Isso cria uma *Tag* `Name`, que é a sua principal ferramenta de organização.

* No campo **Name** (Nome), digite `ServidorWeb`.

#### Passo 2: Escolhendo a Imagem (AMI)
> A **A**mazon **M**achine **I**mage (AMI) é a "planta baixa" do seu servidor. Ela define o sistema operacional e os softwares pré-instalados.

* Mantenha a seleção padrão: **Amazon Linux 2023**. É uma imagem otimizada, segura e mantida pela AWS.

#### Passo 3: Escolhendo o Tipo de Instância
> O "Tipo de Instância" é o "motor" do seu servidor. Define a quantidade de CPU, memória RAM e a capacidade de rede.

* Na lista **Instance type** (Tipo de instância), selecione `t3.micro`.
    > **`!!! tip "Dica do Free Tier"`**
    > A instância `t2.micro` (ou `t3.micro` em algumas regiões) geralmente faz parte do Nível Gratuito da AWS, sendo perfeita para aprendizado e testes.

#### Passo 4: Configurando o Par de Chaves
> O Par de Chaves é sua "chave criptografada" para acessar o servidor via SSH (para Linux) ou RDP (para Windows). Como este lab não exige acesso direto, podemos pular esta etapa.

* Em **Key pair (login)** (Par de chaves), selecione **Proceed without a key pair** (Prosseguir sem um par de chaves).

#### Passo 5: Configurando a Rede
> Aqui definimos em qual "bairro" (VPC e Sub-rede) nosso servidor vai morar e qual será seu "porteiro" (Security Group).

1.  Clique em **Edit** (Editar) na seção **Network settings** (Configurações de rede).
2.  Para **VPC**, selecione `Lab VPC`.
3.  Em **Firewall (security groups)** (Firewall (grupos de segurança)), selecione **Create security group** (Criar um grupo de segurança).
4.  Dê os nomes:
    * **Security group name** (Nome): `Firewall-Servidor-Web`
    * **Description** (Descrição): `Firewall para meu servidor web`
5.  **Ação Crítica:** Na seção **Inbound security groups rules** (Regras de entrada), encontre a regra de SSH (porta 22) que pode estar lá por padrão e clique em **Remove** (Remover).
    > **(COBIT - Segurança):** Por que removemos a regra? Pelo **Princípio do Menor Privilégio**. Se não vamos acessar o servidor via SSH neste lab, a porta de gerenciamento deve permanecer fechada para o mundo, reduzindo a superfície de ataque.

#### Passo 6: Adicionando Armazenamento
> Toda instância precisa de um "HD virtual", que na AWS é um volume **EBS (Elastic Block Store)**. Este é o volume raiz, onde o sistema operacional fica instalado.

* Mantenha a configuração padrão de armazenamento (8 GiB).

#### Passo 7: Configurando Detalhes Avançados
> Aqui está a mágica da automação na nuvem! Vamos usar um script **User Data** para configurar nosso servidor **automaticamente** durante a inicialização.

1.  Expanda a seção **Advanced details** (Detalhes avançados).
2.  Encontre a opção **Termination protection** (Proteção contra término) e, no menu suspenso, selecione **Enable** (Habilitar).
    > **(ITIL - Gerenciamento de Riscos):** Por que habilitamos isso? Para prevenir a exclusão acidental de um servidor de produção, que é um erro humano comum e de alto impacto. É um controle preventivo.
3.  Role para baixo até o campo **User data** (Dados do usuário) e cole o script abaixo:
    ```bash
    #!/bin/bash
    yum update -y
    yum -y install httpd
    systemctl enable httpd
    systemctl start httpd
    echo '<html><h1>Ola Mundo! Meu primeiro servidor web na AWS!</h1></html>' > /var/www/html/index.html
    ```
    > Este script atualiza o sistema, instala o servidor web Apache (`httpd`), o configura para iniciar no boot, inicia o serviço e cria uma página web simples.

#### Passo 8: Lançando a Instância
1.  No painel direito, revise o resumo e clique em **Launch instance** (Lançar instância).
2.  Clique em **View all instances** (Ver todas as instâncias).
3.  Aguarde até que o **Instance State** (Estado da instância) mude para `Running` e o **Status Checks** (Verificações de status) mostre `2/2 checks passed`. Pode ser necessário clicar no ícone de atualização.

---

### <img src="https://api.iconify.design/mdi/monitor-dashboard.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Tarefa 2: Monitorando sua Instância

> **A Dor que Resolve:** Como saber se meu servidor está saudável e funcionando corretamente?

1.  Selecione sua instância `ServidorWeb` na lista.
2.  Na parte inferior da tela, explore as abas:
    * **Status checks** (Verificações de status): O "check-up" da AWS. Mostra se a infraestrutura subjacente (System) e a instância em si (Instance) estão respondendo.
    * **Monitoring** (Monitoramento): O "eletrocardiograma". Aqui você vê os gráficos do **Amazon CloudWatch** para métricas como `CPU utilization` (Uso de CPU).
3.  No menu **Actions** (Ações) no topo, vá em **Monitor and troubleshoot** (Monitorar e solucionar problemas) > **Get instance screenshot** (Obter screenshot da instância). Isso te mostra o que apareceria em um monitor físico conectado ao servidor, útil para diagnosticar problemas de boot.

---

### <img src="https://api.iconify.design/mdi/wall-fire.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Tarefa 3: Atualizando o Firewall e Acessando o Site

1.  Com sua instância `ServidorWeb` selecionada, copie o valor do **Public IPv4 address** (Endereço IPv4 público) no painel de detalhes.
2.  Abra uma nova aba no seu navegador, cole o endereço IP e pressione Enter.
3.  **Pergunta:** O que aconteceu? **Resposta:** A conexão falhou (deu *timeout*).
    > **Por quê?** Porque nosso "porteiro" (`Firewall-Servidor-Web`) não tem nenhuma regra de entrada. Ele está bloqueando todo o tráfego.

4.  **Vamos corrigir:**
    1.  No painel de navegação esquerdo, em *Network & Security*, clique em **Security Groups** (Grupos de segurança).
    2.  Selecione o grupo `Firewall-Servidor-Web`.
    3.  Clique na aba **Inbound rules** (Regras de entrada) e depois em **Edit inbound rules** (Editar regras de entrada).
    4.  Clique em **Add rule** (Adicionar regra) e configure:
        * **Type** (Tipo): `HTTP` (isso preencherá automaticamente a porta 80).
        * **Source** (Origem): `Anywhere-IPv4` (isso preencherá `0.0.0.0/0`).
    5.  Clique em **Save rules** (Salvar regras).

5.  Volte para a aba do navegador onde você colou o IP e **atualize a página**. Agora você deve ver a mensagem "Ola Mundo!".

---

### <img src="https://api.iconify.design/mdi/arrow-up-down-bold-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Tarefa 4: Redimensionando sua Instância

> **A Dor que Resolve:** Sua aplicação cresceu e o servidor `t3.micro` ficou pequeno. Você precisa de mais potência (escalabilidade vertical) sem precisar criar um servidor novo do zero.

1.  **Pare a Instância:**
    * Volte para **Instances** (Instâncias), selecione seu `ServidorWeb`.
    * Clique em **Instance state** (Estado da instância) > **Stop instance** (Parar instância). Confirme.
    * Aguarde o estado mudar para `stopped`.

2.  **Mude o Tipo de Instância:**
    * Com a instância parada e selecionada, vá em **Actions** (Ações) > **Instance Settings** (Configurações da instância) > **Change instance type** (Alterar tipo de instância).
    * Selecione `t3.small` e clique em **Change instance type**.

3.  **Redimensione o Disco (Volume EBS):**
    * No menu esquerdo, em *Elastic Block Store*, clique em **Volumes**.
    * Selecione o volume de 8 GiB associado ao seu servidor.
    * Vá em **Actions** (Ações) > **Modify volume** (Modificar volume).
    * Altere o **Size** (Tamanho) para `10` e clique em **Modify**. Confirme.

4.  **Inicie a Instância:**
    * Volte para **Instances**, selecione seu servidor e vá em **Instance state** > **Start instance** (Iniciar instância).

Parabéns! Sua instância agora tem o dobro de memória e mais espaço em disco.

---

### <img src="https://api.iconify.design/mdi/shield-off-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Tarefa 5: Testando a Proteção contra Término

1.  Com seu servidor no estado `running`, selecione-o e vá em **Instance state** > **Terminate instance** (Terminar instância).
2.  **Observe a falha:** Você receberá uma mensagem de erro dizendo que a instância não pode ser terminada. A proteção que ativamos no Passo 1 funcionou!

3.  **Desabilite a Proteção:**
    * Vá em **Actions** > **Instance settings** > **Change termination protection** (Alterar proteção contra término).
    * Desmarque a caixa **Enable** (Habilitar) e clique em **Save** (Salvar).

4.  **Termine a Instância (Ação Final):**
    * Agora, vá novamente em **Instance state** > **Terminate instance**.
    * Confirme clicando em **Terminate**.

> **`!!! danger "Ação Irreversível"`**
> Terminar uma instância é um ato destrutivo. A instância e o volume EBS raiz (por padrão) são permanentemente excluídos.

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="18" /> Limpeza de Recursos
Neste lab, o ato de terminar a instância já limpou todos os recursos. Lembre-se sempre de deletar o Security Group criado (`Firewall-Servidor-Web`) se não for mais utilizá-lo.