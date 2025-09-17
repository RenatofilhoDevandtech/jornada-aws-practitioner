# <img src="https://api.iconify.design/logos/aws-systems-manager.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Painel de Controle da Frota - Usando o AWS Systems Manager

### O Cenário (A "User Story")

> **Como** um engenheiro de operações (SysOps), **EU QUERO** usar o AWS Systems Manager para instalar uma aplicação, gerenciar sua configuração e acessar o servidor de forma segura, **PARA QUE** eu possa gerenciar minha frota de instâncias EC2 de forma automatizada, escalável e sem expor portas de gerenciamento.

### A Dor que o Lab Resolve

1.  **A Cegueira Operacional:** "Eu não sei exatamente qual versão de software está rodando em cada uma das minhas 100 instâncias."
2.  **A Lentidão Manual:** "Instalar uma nova aplicação em toda a frota exige que eu me conecte a cada máquina, uma por uma."
3.  **Configurações Inseguras:** "A chave da API do nosso serviço de mapas está salva em um arquivo de texto dentro da nossa aplicação."
4.  **O Risco do SSH:** "Manter a porta 22 aberta e gerenciar chaves SSH para toda a equipe é complexo e cria uma grande superfície de ataque."

Este laboratório mostra como o Systems Manager resolve todas essas dores de forma elegante.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Usar o **Inventory** para verificar o software instalado em uma instância.
* [ ] Usar o **Run Command** para instalar uma aplicação remotamente.
* [ ] Usar o **Parameter Store** para gerenciar uma configuração de forma centralizada.
* [ ] Usar o **Session Manager** para acessar o terminal da instância sem SSH.

### Pré-requisitos
* Uma conta AWS.
* Uma instância EC2 com o **Amazon Linux** já em execução.
* **Importante:** A instância precisa de uma **Função do IAM (IAM Role)** anexada com a política `AmazonSSMManagedInstanceCore` para que o SSM possa se comunicar com ela.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: O Censo da Frota (Usando o Inventory)

**Analogia:** Vamos usar o "Painel de Controle" para fazer um **censo automático** de todos os "caminhões" (instâncias), listando tudo que está instalado neles.

1.  No Console da AWS, navegue até o serviço **Systems Manager**.
2.  No menu esquerdo, em `Gerenciamento de nós (Node Management)`, selecione `Fleet Manager`.
3.  No menu `Gerenciamento de contas (Account management)`, selecione `Configurar inventário (Setup Inventory)`.
4.  Para criar uma `associação (association)` que coletará informações, use as seguintes opções:
    * Na seção `Fornecer detalhes do inventário (Provide inventory details)`, em `Nome (Name)`, insira `Inventario-Geral`.
    * Na seção `Destinos (Targets)`, selecione `Selecionar instâncias manualmente (Specify targets by choosing instances manually)`.
    * Selecione a sua `Instância gerenciada (Managed instance)`.
5.  Clique em `Configurar inventário (Setup Inventory)`.
6.  **Verificação:**
    * Volte ao `Fleet Manager` e clique no `ID do Nó (Node ID)` da sua instância.
    * Navegue até a aba `Inventário (Inventory)`.
    * No menu suspenso `Tipo de inventário (Inventory type)`, selecione `AWS:Application`. Você verá uma lista de todo o software instalado na sua instância.

#### Tarefa 2: A Ordem Remota (Instalando com o Run Command)

**Analogia:** Em vez de ir até cada caminhão, vamos usar o "intercomunicador da sede" (**Run Command**) para enviar a ordem de instalação.

1.  No menu do Systems Manager, em `Gerenciamento de nós (Node Management)`, selecione `Run Command`.
2.  Clique em `Executar comando (Run command)`.
3.  Na caixa de busca de `Documento de comando (Command document)`, selecione o documento `AWS-RunShellScript`.
4.  Na seção `Comandos (Commands)`, cole o script que instala nossa aplicação.
5.  Na seção `Seleção do destino (Targets)`, escolha `Selecionar instâncias manualmente (Choose instances manually)` e marque sua `Instância gerenciada (Managed instance)`.
6.  Na seção `Opções de saída (Output options)`, desmarque `Habilitar um bucket do S3 (Enable an S3 bucket)`.
7.  Clique em `Executar (Run)`.
8.  Aguarde até que o `Status geral (Overall Status)` mude para `Êxito (Success)`.
9.  **Verificação:**
    * No painel do seu laboratório, clique em **Detalhes > Mostrar**.
    * Copie o valor do **ServerIP** (o IP Público).
    * Cole este IP em uma nova aba do navegador. O "Widget Manufacturing Dashboard" deve aparecer.

> **O Resultado:** Você instalou uma aplicação web completa em um servidor remoto sem usar SSH, sem abrir a porta 22 e sem usar chaves `.pem`.

#### Tarefa 3: O Cofre Central (Gerenciando com o Parameter Store)

**Analogia:** Vamos guardar uma configuração importante no "cofre central da sede" (**Parameter Store**).

1.  No menu do Systems Manager, em `Gerenciamento de aplicações (Application Management)`, selecione `Armazenamento de parâmetros (Parameter Store)`.
2.  Clique em `Criar parâmetro (Create parameter)`.
3.  Configure o parâmetro:
    * **Nome (Name):** `/dashboard/show-beta-features`
    * **Descrição (Description):** `Display beta features`
    * **Nível (Tier):** Deixe `Padrão (Standard)`.
    * **Tipo (Type):** Deixe `String`.
    * **Valor (Value):** `True`.
4.  Clique em `Criar parâmetro (Create parameter)`.
5.  **Verificação:**
    * Volte para a aba do navegador com o "Widget Manufacturing Dashboard" e **atualize a página**.
    * Um terceiro gráfico (o recurso beta) aparecerá. A aplicação leu o parâmetro no SSM e se reconfigurou em tempo real!

#### Tarefa 4: O Túnel Mágico (Acessando com o Session Manager)

**Analogia:** Vamos usar o "terminal de acesso seguro da sede" para nos conectar diretamente ao painel de um caminhão, sem precisar de uma chave física.

1.  No menu do Systems Manager, em `Gerenciamento de nós (Node Management)`, selecione `Session Manager`.
2.  Clique em `Iniciar sessão (Start session)`.
3.  Selecione sua `Instância gerenciada (Managed instance)` e clique em `Iniciar sessão (Start session)`.
4.  Uma nova aba se abrirá com um terminal de linha de comando totalmente funcional.
5.  **Verificação:**
    * Execute `ls /var/www/html`. Você verá os arquivos da aplicação.
    * Execute o seguinte comando para provar que a instância tem acesso à API da AWS:
    ```bash
    # Get region
    AZ=`curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone`
    export AWS_DEFAULT_REGION=${AZ::-1}

    # List information about EC2 instances
    aws ec2 describe-instances
    ```
    > A saída mostrará os detalhes da sua instância em formato JSON.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você usou o AWS Systems Manager para inspecionar, comandar, configurar e acessar uma instância EC2 de forma centralizada, automatizada e segura, demonstrando o poder de uma abordagem de operações moderna na nuvem.

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: Desvendando o AWS Systems Manager (Um Lab Prático)

Hoje, na minha jornada de estudos com o AWS re/Start, eu tive um daqueles "momentos a-ha!" que mudam a forma como você enxerga a tecnologia. A pergunta sempre foi: "Como as grandes empresas gerenciam centenas ou milhares de servidores de forma eficiente e segura?". A ideia de conectar via SSH em cada um para aplicar um patch ou instalar um software sempre me pareceu um pesadelo logístico.

Hoje, eu descobri a resposta, e o nome dela é **AWS Systems Manager (SSM)**.

Pense no SSM não como uma única ferramenta, mas como o **"Painel de Controle Central"** da sua frota de servidores na nuvem. No laboratório prático, eu pude vivenciar como ele resolve quatro dores gigantescas do dia a dia de qualquer equipe de operações (SysOps).

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> As 4 Descobertas do Lab e as Dores que Elas Curam

#### 1. <img src="https://api.iconify.design/mdi/clipboard-list-outline.svg?color=currentColor" width="20" /> O Fim da "Cegueira Operacional" com o Inventory
* **A Dor:** Em um ambiente com dezenas de servidores, é quase impossível saber com certeza qual versão de software está rodando em cada máquina. Isso é um pesadelo para a segurança e para a conformidade.
* **O Que Eu Fiz:** No lab, usei o recurso **Inventory** do SSM para criar uma "associação" com minha instância EC2.
* **O Resultado Incrível:** Em minutos, sem me conectar à máquina, eu tinha um inventário completo de todas as aplicações instaladas, visível em um painel central. É o fim do "achismo". Você tem uma fonte única da verdade sobre o estado da sua frota.

#### 2. <img src="https://api.iconify.design/mdi/play-box-outline.svg?color=currentColor" width="20" /> Automação de Tarefas com o Run Command
* **A Dor:** Instalar um software ou executar um script em uma frota inteira exige se conectar a cada servidor, um por um. É um processo lento e extremamente propenso a erros humanos.
* **O Que Eu Fiz:** Usei o **Run Command** para enviar um script de instalação de uma aplicação web inteira para minha instância.
* **O Resultado Incrível:** A aplicação foi instalada e configurada perfeitamente, **sem que eu precisasse de uma chave SSH e sem abrir a porta 22**. Para uma empresa, isso significa que as implantações são mais rápidas, padronizadas e, o mais importante, muito mais seguras.

#### 3. <img src="https://api.iconify.design/mdi/key-chain-variant.svg?color=currentColor" width="20" /> Gerenciamento Centralizado com o Parameter Store
* **A Dor:** Salvar senhas, chaves de API ou configurações importantes diretamente no código ou em arquivos de texto na aplicação é uma falha de segurança grave e dificulta a atualização.
* **O Que Eu Fiz:** Criei um parâmetro no **Parameter Store** para controlar a exibição de um recurso "beta" na aplicação que instalei.
* **O Resultado Incrível:** A aplicação leu a configuração diretamente do SSM. Eu pude "ligar" e "desligar" um recurso do site **sem fazer um novo deploy**, apenas alterando o valor no "cofre" central do Parameter Store. Isso muda o jogo para o gerenciamento de *feature flags* e segredos.

#### 4. <img src="https://api.iconify.design/mdi/lan-connect.svg?color=currentColor" width="20" /> Acesso Seguro com o Session Manager
* **A Dor:** O acesso SSH é poderoso, mas gerenciar chaves `.pem` para toda a equipe e deixar a porta 22 aberta são riscos de segurança significativos.
* **O Que Eu Fiz:** Usei o **Session Manager** para iniciar uma sessão de terminal na minha instância.
* **O Resultado Incrível:** Eu obtive um shell completo e funcional **diretamente do meu navegador**, sem chaves, sem software extra e sem portas abertas. Todo o acesso é autenticado via IAM e 100% auditável no CloudTrail. É a forma mais segura e prática de acesso administrativo que já vi.

---

### <img src="https://api.iconify.design/mdi/comment-quote-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Grande Lição
O lab de hoje me ensinou que o Systems Manager não é apenas uma coleção de ferramentas. É uma **mudança de filosofia**. É sobre tratar sua frota de servidores não como "animais de estimação" que você visita um a um, mas como um "rebanho" que você gerencia de forma centralizada, segura e automatizada.

Essa experiência prática solidificou meu entendimento de como a AWS resolve dores reais de operações em escala. Com o SSM, automação e segurança não são mais coisas separadas; elas andam de mãos dadas.