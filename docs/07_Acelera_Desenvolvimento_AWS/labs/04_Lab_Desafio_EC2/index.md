# <img src="https://api.iconify.design/mdi/puzzle-check-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab [Desafio]: O Arquiteto em Ação - Construindo uma VPC e Servidor Web

### O Cenário (A "User Story")

> **Como** um arquiteto de nuvem, **EU QUERO** construir um novo ambiente de rede (VPC) do zero e lançar um servidor web funcional dentro dele, **PARA QUE** eu possa validar minhas habilidades de ponta a ponta na criação de uma infraestrutura web básica na AWS.

### A Dor que o Lab Resolve

É fácil lançar uma instância na VPC Padrão. Mas, no mundo real, os projetos exigem redes customizadas e isoladas. Este desafio resolve a "dor" de sair do ambiente "pronto para usar" e construir sua própria infraestrutura de rede e computação, um passo fundamental para se tornar um profissional.

### Objetivos de Aprendizado
Ao concluir este desafio, você terá provado sua capacidade de:

* [ ] Configurar uma rede virtual (VPC, Sub-rede, Internet Gateway, Tabela de Rotas).
* [ ] Lançar uma instância Amazon Linux EC2 em uma rede customizada.
* [ ] Instalar um servidor web usando User Data.
* [ ] Configurar a segurança de rede (Security Group) para permitir o acesso correto.
* [ ] Conectar-se a uma instância e implantar um arquivo web.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Plano de Ação do Arquiteto

Sua missão é construir um ambiente web funcional. A ordem das operações é crucial. A regra de ouro é: **primeiro a fundação (a rede), depois o prédio (o servidor)**.

#### Fase 1: A Fundação - Construindo a Rede (VPC)

**Analogia:** Antes de construir a casa, você precisa cercar o terreno, construir a rua de acesso e a portaria.

1.  **Vá para o Console da AWS** e navegue até o serviço **VPC**.
2.  **Crie uma nova VPC:**
    * Use o assistente **VPC e mais**.
    * Dê um nome, como `VPC-Desafio`.
    * Escolha um bloco CIDR IPv4 (ex: `10.10.0.0/16`).
    * Deixe em **1** o número de Zonas de Disponibilidade (AZs).
    * Deixe em **1** o número de **Sub-redes públicas**.
    * Deixe em **0** o número de Sub-redes privadas.
    * Para o Gateway NAT, selecione **Nenhum**.
    * Clique em **Criar VPC**.
    > **O "Porquê":** Este assistente é a forma mais rápida de criar uma VPC funcional. Ele automaticamente cria a VPC, a Sub-rede, o **Internet Gateway** e a **Tabela de Rotas** principal, já com a rota `0.0.0.0/0` apontando para o gateway.

3.  **Habilite o IP Público Automático:**
    * No menu da VPC, vá em **Sub-redes (Subnets)**.
    * Selecione a sub-rede que você acabou de criar.
    * Clique em **Ações (Actions)** > **Editar configurações da sub-rede (Edit subnet settings)**.
    * Marque a caixa de seleção **Habilitar atribuição automática de endereço IPv4 público (Enable auto-assign public IPv4 address)** e salve.

#### Fase 2: A Construção - Lançando o Servidor Web (EC2)

**Analogia:** Com o terreno e a rua prontos, é hora de construir a "casa modelo".

1.  Navegue até o serviço **EC2** e clique em **Lançar instância (Launch instance)**.
2.  **Nome:** `Servidor-Web-Desafio`.
3.  **AMI:** `Amazon Linux` (AMI do Amazon Linux 2).
4.  **Tipo de instância (Instance type):** `t3.micro`.
5.  **Par de chaves (Key pair):** Selecione **Prosseguir sem um par de chaves (Proceed without a key pair)**.
6.  **Configurações de rede (Network settings):** Clique em **Editar (Edit)**.
    * **VPC:** Selecione sua `VPC-Desafio`.
    * **Sub-rede (Subnet):** Selecione a sua sub-rede pública.
    * **Firewall (grupos de segurança):**
        * Selecione **Criar grupo de segurança (Create security group)**.
        * **Nome:** `SG-Servidor-Web`.
        * **Descrição:** `Permite acesso HTTP e SSH`.
        * **Regras de entrada (Inbound rules):**
            * Adicione uma regra para `HTTP` com a Origem `Anywhere (0.0.0.0/0)`.
            * Adicione uma regra para `SSH` com a Origem `My IP` (para sua segurança).
7.  **Configurar armazenamento (Configure storage):** Mantenha o padrão de 8 GiB `gp2`.
8.  **Detalhes avançados (Advanced details):** Role para baixo até o campo **Dados do usuário (User Data)** e cole o seguinte script:
    ```bash
    #!/bin/bash
    yum update -y
    yum install -y httpd
    systemctl start httpd
    systemctl enable httpd
    usermod -a -G apache ec2-user
    chown -R ec2-user:apache /var/www
    chmod 2775 /var/www
    find /var/www -type d -exec chmod 2775 {} \;
    find /var/www -type f -exec chmod 0664 {} \;
    ```
    > **O "Porquê" do Script:** Além de instalar e iniciar o servidor web (`httpd`), este script ajusta as permissões da pasta `/var/www/html` para que o `ec2-user` possa criar arquivos nela sem precisar usar `sudo`.
9.  Revise tudo e clique em **Lançar instância (Launch instance)**.

#### Fase 3: A Decoração - Publicando e Acessando o Site

1.  Aguarde a instância estar no estado `running`.
2.  Selecione a instância e clique em **Conectar (Connect)**.
3.  Use a aba **EC2 Instance Connect** para se conectar.
4.  No terminal, crie o arquivo `projects.html` com seu nome (substitua "SEU-NOME"):
    ```bash
    echo "<html><body><h1>Projeto re/Start de SEU-NOME</h1><p>Lab de Desafio da Instancia EC2</p></body></html>" > /var/www/html/projects.html
    ```
5.  **Verificação Final:**
    * No console do EC2, copie o **Endereço IPv4 público (Public IPv4 address)** da sua instância.
    * Abra uma nova aba no navegador e acesse `http://<SEU_IP_PUBLICO>/projects.html`.
    * **Tire um screenshot da sua página web funcionando!**

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você completou o desafio. Você provou que consegue aplicar os conceitos de VPC, Sub-redes, Internet Gateway, Tabelas de Rotas, Security Groups e EC2 para construir uma solução funcional do zero. Esta é a base de quase toda arquitetura web na AWS.

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: De um Terreno Vazio ao Primeiro Site no Ar

Até agora, na minha jornada com o AWS re/Start, eu vinha seguindo receitas, aprendendo sobre cada serviço de forma isolada. Hoje foi diferente. Hoje foi o dia do desafio: começar com uma "folha em branco" e construir uma infraestrutura web completa.

Confesso que a ideia de criar uma rede do zero parecia intimidante. Mas a experiência foi, de longe, a mais gratificante e a que mais solidificou meu conhecimento até agora.

### A Jornada em 3 Atos

O desafio me forçou a pensar como um verdadeiro arquiteto. A missão não era apenas "lançar um servidor", mas sim criar todo o ecossistema para que ele pudesse viver e se comunicar com o mundo de forma segura.

#### Ato 1: O Urbanista (Planejando a Rede)
* **A Dor:** "É fácil usar a rede que a AWS já te dá pronta. Mas e se eu precisar de uma rede customizada e isolada para um projeto de cliente?"
* **O Que Eu Fiz:** Eu tive que agir como um **urbanista**.
    * **Analogia:** Recebi um **"terreno vazio"** e precisei planejar tudo: cerquei o lote (criei a **VPC**), construí a primeira rua de acesso (a **Sub-rede**), instalei a portaria principal (o **Internet Gateway**) e, o mais importante, desenhei o mapa de trânsito (a **Tabela de Rotas**).
* **O "Aha!" Moment:** O momento em que a ficha caiu foi ao configurar a Tabela de Rotas. Eu entendi que, sem uma regra explícita dizendo *"para ir para a internet, passe pela portaria"*, a sub-rede, mesmo sendo "pública", estaria isolada. Foi a primeira vez que a relação entre esses componentes fez total sentido prático.

#### Ato 2: O Construtor (Lançando o Servidor)
* **A Dor:** "Com a rede pronta, como garantir que o servidor que vou construir seja seguro e se autoconfigure desde o início?"
* **O Que Eu Fiz:** Com a infraestrutura do "condomínio" pronta, virei o **construtor da casa modelo**.
* **O "Aha!" Moment:** No momento do lançamento, eu já defini a **"fechadura eletrônica" (Security Group)**, permitindo a entrada de "visitantes" (HTTP) e do "dono" (SSH do meu IP). O mais legal foi entregar as **"instruções de montagem" (User Data)** para a equipe. A "casa" já nasceu com o "sistema de som e luzes" (`httpd`) instalado e pronto para usar, tudo de forma automática.

#### Ato 3: O Decorador (Publicando o Conteúdo)
* **A Dor:** "O servidor está no ar, mas está vazio. Como eu coloco meu conteúdo lá dentro de forma segura?"
* **O Que Eu Fiz:** Usei o **EC2 Instance Connect**.
* **O "Aha!" Moment:**
    * **Analogia:** A casa estava pronta, mas sem móveis. O Instance Connect funcionou como um **"passe de mestre"** temporário e seguro para eu entrar na casa e fazer a decoração final. Criei minha página de boas-vindas e a coloquei na "sala de estar" (`/var/www/html`).

### A Grande Lição
O maior aprendizado deste desafio foi entender a **ordem das operações**. Na nuvem, a arquitetura é construída em camadas, de fora para dentro: **1º a Rede, 2º a Segurança da Rede, 3º o Servidor, 4º a Aplicação**. Ver isso na prática, a partir de uma tela em branco, foi a lição mais valiosa até agora.

Foi desafiador, mas ver a minha própria página web, rodando em um servidor que lancei, dentro de uma rede que eu mesmo projetei do zero, foi incrivelmente gratificante. É a sensação de que as peças do quebra-cabeça estão finalmente se encaixando.

#AWS #Cloud #VPC #EC2 #Networking #DevOps #AWSreStart #HandsOn #CloudPractitioner