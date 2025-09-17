# <img src="https://api.iconify.design/logos/aws-cli.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Terminal de Comando - Instalando e Configurando a AWS CLI

### O Cenário (A "User Story")

> **Como** um novo engenheiro de nuvem, **EU QUERO** instalar a AWS CLI em um servidor Linux e conectá-la à minha conta AWS, **PARA QUE** eu possa começar a gerenciar e automatizar meus recursos através da linha de comando.

### A Dor que o Lab Resolve

O Console da AWS é ótimo para tarefas visuais, mas clicar em botões não é escalável nem automatizável. A dor que este laboratório resolve é a **limitação das operações manuais**. A CLI é a ponte que conecta suas habilidades de linha de comando com o poder da AWS, permitindo que você crie scripts para automatizar tarefas repetitivas e gerenciar sua infraestrutura como código.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Conectar-se a uma instância EC2 Linux usando SSH.
* [ ] Instalar a AWS CLI em um ambiente Red Hat Linux.
* [ ] Configurar a CLI com credenciais de segurança (Chaves de Acesso).
* [ ] Usar a CLI para interagir com o serviço AWS IAM.

### Duração
* Aproximadamente 45 minutos.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Acessando o "Posto de Controle" (Conectar-se à Instância EC2)
Nossa primeira tarefa é acessar o servidor Linux onde instalaremos a CLI.

> **`!!! note "Instruções Específicas"`**
> O processo de conexão varia entre Windows e macOS/Linux. Siga o guia correspondente ao seu sistema operacional. As credenciais (IP Público e a chave `.pem` ou `.ppk`) são fornecidas no painel `Detalhes (Details)` do seu ambiente de laboratório.

!!! tab "macOS / Linux"
    1.  **Baixe a Chave:** No painel do laboratório, clique em **Detalhes > Mostrar (Details > Show)** e baixe o arquivo `labsuser.pem`.
    2.  **Abra o Terminal** e navegue até a pasta onde salvou a chave (geralmente `Downloads`).
        ```bash
        cd ~/Downloads
        ```
    3.  **Proteja sua Chave:** Altere as permissões do arquivo para "somente leitura". Este é um requisito de segurança do SSH.
        ```bash
        chmod 400 labsuser.pem
        ```
    4.  **Conecte-se:** Use o comando `ssh`, substituindo `<ip-address>` pelo `IP Público (Public IP)` da sua instância.
        ```bash
        ssh -i labsuser.pem ec2-user@<ip-address>
        ```
    5.  Digite `yes` quando solicitado.

!!! tab "Windows (usando PuTTY)"
    1.  **Baixe a Chave:** No painel do laboratório, clique em **Detalhes > Mostrar (Details > Show)** e baixe o arquivo `labsuser.ppk`.
    2.  **Abra o PuTTY.**
    3.  **Host Name:** Insira `ec2-user@<ip-address>`, substituindo pelo seu `IP Público (Public IP)`.
    4.  **Conexão > SSH > Auth (Connection > SSH > Auth):** Clique em `Browse...` (ou `Credentials` na versão nova) e selecione o arquivo `labsuser.ppk`.
    5.  **Clique em Open** para se conectar.

#### Tarefa 2: Instalando as Ferramentas (Instalar a AWS CLI)
Agora que estamos dentro do servidor Red Hat, vamos instalar o software da CLI.

1.  **Baixar o Instalador:** Usamos o `curl` para baixar o pacote de instalação da AWS.
    ```bash
    curl "[https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip](https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip)" -o "awscliv2.zip"
    ```
2.  **Descompactar o Pacote:** Usamos o `unzip` para extrair os arquivos.
    ```bash
    unzip awscliv2.zip
    ```
3.  **Executar a Instalação:** O comando `sudo` nos dá privilégios de administrador.
    ```bash
    sudo ./aws/install
    ```
4.  **Verificar a Instalação:**
    ```bash
    aws --version
    ```
    > Você deverá ver a versão da CLI instalada, confirmando que tudo funcionou.

#### Tarefa 3: Configurando as Credenciais (`aws configure`)
Agora, vamos "apresentar" as credenciais do usuário `awsstudent` para a CLI.

1.  Execute o comando de configuração:
    ```bash
    aws configure
    ```
2.  O terminal pedirá 4 informações. Volte ao painel `Detalhes (Details)` do seu laboratório para obtê-las:
    * **AWS Access Key ID:** Copie o valor `AccessKey (Chave de Acesso)` e cole.
    * **AWS Secret Access Key:** Copie o valor `SecretKey (Chave de Acesso Secreta)` e cole.
    * **Default region name:** `us-west-2`
    * **Default output format:** `json`

#### Tarefa 4: Testando a Conexão (Interagindo com o IAM)
Vamos dar uma ordem simples e segura para verificar se nossa configuração está funcionando.

1.  Peça à AWS para listar os `Usuários (Users)` do IAM na conta:
    ```bash
    aws iam list-users
    ```
2.  **Verificação:** Você deverá ver uma saída em JSON com os detalhes dos usuários. **Parabéns, você controlou a nuvem pela linha de comando!**

---

### <img src="https://api.iconify.design/mdi/puzzle-check-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Desafio da Atividade

> **Sua Missão:** Usando apenas a AWS CLI, encontre e salve a `política (policy)` do IAM chamada `lab_policy` em um arquivo JSON.
>
> **A Solução:**
> ```bash
> # 1. Liste as políticas com escopo Local para encontrar o ARN
> aws iam list-policies --scope Local
> 
> # 2. Use o ARN encontrado para obter a versão v1 da política
> aws iam get-policy-version --policy-arn <COLE_O_ARN_DA_POLITICA_AQUI> --version-id v1 > lab_policy.json
> ```

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Principais Lições
* A **AWS CLI** é uma ferramenta poderosa para gerenciar e automatizar serviços AWS.
* Para se conectar, a CLI precisa de um `ID de Chave de Acesso (Access Key ID)` e uma `Chave de Acesso Secreta (Secret Access Key)`, enquanto o Console precisa de um nome de usuário e senha.

---

# <img src="https://api.iconify.design/mdi/matrix.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: Saindo da Matrix - Meu Primeiro Contato com a AWS CLI

Sabe quando você usa um aplicativo com uma interface bonita, mas sempre se pergunta como as coisas funcionam de verdade por trás dos panos? Para mim, o console da AWS era um pouco assim. Clicar em botões é fácil e visual, mas eu sentia que estava vendo o mundo da nuvem através de um vidro.

Hoje, no laboratório do AWS re/Start, eu saí da "Matrix".

A pílula vermelha, nesse caso, foi a **AWS CLI**, ou Interface de Linha de Comando. É basicamente um "super terminal" que fala diretamente com a AWS, sem intermediários. E a experiência foi reveladora.

O lab foi simples, mas o conceito por trás é poderoso. A missão era acessar um servidor na nuvem e instalar essa ferramenta. Depois, a parte mais legal: a configuração.

O comando `aws configure` é como **apresentar seu crachá de acesso** para o sistema de segurança da nuvem. Você entrega duas informações super secretas: a `Chave de Acesso (Access Key)` — que é como o seu nome de usuário público — e a `Chave de Acesso Secreta (Secret Access Key)` — que é a sua senha para o mundo da automação.

Uma vez que a CLI tem o seu "crachá", ela pode agir em seu nome.

E aí veio o momento da verdade. Eu digitei um comando simples, `aws iam list-users`, pedindo para listar os usuários da conta. E... *boom*. O terminal me respondeu com uma lista de usuários, em código.

Naquele instante, a mágica aconteceu: eu não estava mais clicando em botões; eu estava **dando ordens diretas** para a nuvem. É uma sensação de poder e controle incrível.

### A Grande Lição

O lab de hoje me ensinou que o console da AWS é o "mapa turístico" — ótimo para passear e conhecer os pontos principais. Mas a CLI é o "GPS do explorador" — a ferramenta que te dá o poder de traçar suas próprias rotas e, o mais importante, **automatizá-las**.

Com a CLI, o caminho para a automação se abre. Posso criar scripts para tarefas repetitivas, gerenciar dezenas de recursos de uma vez e realmente começar a tratar minha infraestrutura como código. É a diferença entre saber dirigir um carro e entender como o motor funciona.

Foi um passo pequeno em termos de comandos, mas a sensação é de que uma porta gigante se abriu. Para quem, como eu, está nessa jornada de transição, ver essa conexão direta acontecer é um baita impulso na confiança.

#AWS #Cloud #CLI #Automacao #CarreiraEmTI #AWSreStart