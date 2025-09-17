# <img src="https://api.iconify.design/logos/aws-cli.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Terminal de Comando da Nuvem: Guia Prático da AWS CLI

Você já sabe como gerenciar a AWS clicando em botões no Console. Mas como os profissionais de nuvem gerenciam centenas de recursos de forma rápida, repetível e automatizada? A resposta é a **AWS CLI**.

A CLI é uma ferramenta que te permite controlar todo o seu ambiente AWS através de comandos de texto no seu terminal (Linux, macOS ou Windows).

**Analogia:** Pense em **controlar um robô industrial**. Existem três formas de fazer isso.

---

### <img src="https://api.iconify.design/mdi/compare-horizontal.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. As 3 Interfaces de Controle (Console vs. CLI vs. SDK)

| Interface | Analogia (Como controlar o Robô) | Ideal Para... |
| :--- | :--- | :--- |
| **Console de Gerenciamento da AWS** | O **"Painel de Controle com Botões e Joysticks"**. | **Humanos.** Ótimo para exploração visual, aprendizado e tarefas pontuais. |
| **AWS CLI** | O **"Terminal de Comandos do Robô"**. | **Scripts e Automação.** Perfeito para automatizar tarefas repetitivas com scripts (Shell, Python) e para administradores que preferem a velocidade do teclado. |
| **AWS SDKs (ex: Boto3)** | A **"Biblioteca de Programação do Cérebro do Robô"**. | **Aplicações Customizadas.** Para desenvolvedores que precisam integrar o poder da AWS diretamente dentro do seu código (Python, Java, .NET, etc.). |

> **`!!! note "A Base de Tudo: A API"`**
> Todas as três interfaces, no fundo, estão "conversando" com a mesma coisa: a **API da AWS**. Tudo na AWS é uma chamada de API. O Console, a CLI e os SDKs são apenas diferentes "tradutores" para essa linguagem universal.

---

### <img src="https://api.iconify.design/mdi/play-box-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. Primeiros Passos (Instalação e Configuração)

#### Instalação no Linux
Em um sistema como Amazon Linux ou CentOS, o comando geralmente é:
```bash
sudo yum install awscli -y
```
#### Em sistemas Debian/Ubuntu:
```bash
sudo apt install awscli -y
```
#### Configuração (`aws configure`)
Este é o passo mais importante. Após instalar, você precisa "apresentar" suas credenciais para a CLI.

```bash
aws configure
```
O terminal te pedirá 4 informações:

1.  **AWS Access Key ID:** O "nome de usuário" da sua chave.
2.  **AWS Secret Access Key:** A "senha" secreta da sua chave.
3.  **Default region name:** A Região onde você mais trabalha (ex: `sa-east-1`).
4.  **Default output format:** O formato da resposta (geralmente `json`).

> **`!!! danger "ALERTA DE SEGURANÇA"`**
> **NUNCA** use as chaves de acesso do seu usuário root! A melhor prática é criar um **usuário IAM** dedicado para o acesso programático, com o **mínimo de privilégios necessários**.

---

### <img src="https://api.iconify.design/mdi/code-tags.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. A Anatomia de um Comando

A sintaxe da CLI é simples e consistente: `aws <serviço> <comando> [--opções]`
* **Exemplo:** `aws ec2 describe-instances --region sa-east-1`

---

### <img src="https://api.iconify.design/mdi/filter-cog-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 4. Dominando a Saída (Os Superpoderes da CLI)

A CLI te dá ferramentas poderosas para controlar exatamente o que você vê.

* **`--query` (O Filtro de Relatório):**
    * **A Dor que Resolve:** A saída padrão em JSON é enorme e cheia de detalhes.
    * **Analogia:** Dizer ao robô: "Deste relatório de status com 100 campos, mostre-me **apenas** a 'temperatura_do_motor'."
    * **Exemplo:** Para ver apenas o ID e o Tipo das suas instâncias EC2:
        ```bash
        aws ec2 describe-instances --query 'Reservations[*].Instances[*].[InstanceId, InstanceType]'
        ```
* **`--filter` (O Filtro de Busca):**
    * **A Dor que Resolve:** O comando retorna 100 instâncias, mas eu só quero ver as do tipo `t2.micro`.
    * **Analogia:** Dizer ao robô: "De todos os 1000 parafusos na sua bandeja, traga-me **apenas** aqueles 'cujo diâmetro seja 5mm'."
    * **Exemplo:** Para listar apenas as instâncias que são `t2.micro`:
        ```bash
        aws ec2 describe-instances --filters "Name=instance-type,Values=t2.micro"
        ```

* **`--dry-run` (O Modo de Simulação):**
    * **A Dor que Resolve:** O medo de executar um comando destrutivo (como `terminate-instances`) por engano.
    * **Analogia:** Dizer ao robô: "**Simule** o movimento de furar esta placa, mas **não ligue a broca**."
    > **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Hack de Especialista:** Esta é a sua rede de segurança. Antes de rodar um comando que altera ou deleta algo, **sempre** adicione a flag `--dry-run` primeiro. O comando verificará suas permissões e a sintaxe. Se tudo estiver correto, ele retornará uma resposta `DryRunOperation`, confirmando que o comando *teria funcionado*, sem de fato fazer nada.

> **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação:** Para a prova:
> 1.  Saiba que existem **3 formas de interagir com a AWS**: Console, CLI e SDKs.
> 2.  Que a **CLI** é a principal ferramenta para **automação via scripts** (Shell, etc.).
> 3.  Que você precisa de **Chaves de Acesso (Access Keys)** de um usuário **IAM** para configurar a CLI.

---

### <img src="https://api.iconify.design/logos/aws-cli.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Cinto de Utilidades do Arquiteto: Guia Avançado da AWS CLI

Já sabemos que existem três formas de interagir com a AWS: o Console (visual), a CLI (linha de comando) e os SDKs (programação). Enquanto o Console é ótimo para aprender, a **CLI é a ferramenta de escolha dos profissionais para automação e eficiência**.

**Analogia:** Pense que você está controlando um **robô industrial**.
* **O Console:** É o painel com botões e joysticks.
* **A CLI:** É o terminal onde você digita comandos de texto precisos. É mais rápido, repetível e pode ser colocado em scripts.

---

### <img src="https://api.iconify.design/mdi/code-tags.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Gramática da Nuvem (A Anatomia de um Comando)

Todo comando da AWS CLI segue uma estrutura lógica e previsível.

`aws <serviço> <operação> [--parâmetros]`

* **`aws`**: O comando para "chamar" o robô.
* **`<serviço>`**: A "seção da fábrica" onde o robô deve ir (ex: `ec2`, `s3`, `iam`).
* **`<operação>`**: A "ação" que o robô deve executar (ex: `describe-instances`, `list-buckets`, `create-user`).
* **`[--parâmetros]`**: Os "detalhes" da ordem (ex: `--instance-id i-12345`).

**Exemplo:** `aws ec2 stop-instances --instance-id i-1234567890abcdef0`
* **Tradução:** "Robô (`aws`), vá para a seção de montagem de chassis (`ec2`), execute a operação de parar esteiras (`stop-instances`), especificamente na esteira de ID `i-1234567890abcdef0`."

---

### <img src="https://api.iconify.design/mdi/book-open-page-variant-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Manual Embutido (Dominando o Comando `help`)

**A Dor que Resolve:** "Existem milhares de comandos e parâmetros. Como eu vou lembrar de tudo?"
**A Solução:** Você não precisa. A CLI tem um manual de instruções completo dentro dela.

* **Analogia:** O comando `help` é o **"Manual de Operações"** do robô, acessível a qualquer momento.

#### O Fluxo de Descoberta:
1.  **Ver os serviços:** "Robô, o que você sabe fazer?"
    ```bash
    aws help
    ```
2.  **Ver os comandos de um serviço:** "Robô, na seção `ec2`, quais operações você executa?"
    ```bash
    aws ec2 help
    ```
3.  **Ver os detalhes de um comando:** "Robô, explique em detalhes como funciona a operação `describe-instances`."
    ```bash
    aws ec2 describe-instances help
    ```
    > **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> INSIGHT DE ESPECIALISTA:** Profissionais de nuvem experientes não memorizam todos os comandos; eles dominam o `help`. A capacidade de encontrar a informação que você precisa rapidamente no terminal é uma habilidade fundamental.

---

### <img src="https://api.iconify.design/mdi/file-document-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. Escolhendo sua Visão (Os Formatos de Saída)

Por padrão, a CLI responde em `json`. Mas você pode pedir o "relatório" em outros formatos.

| Formato | Analogia (Como o robô entrega o relatório) | Ideal Para... |
| :--- | :--- | :--- |
| **`json` (padrão)** | O **"Relatório de Telemetria Completo"**. | Ser processado por outros scripts e aplicações (ex: Python com Boto3). Fornece a informação mais detalhada. |
| **`table`** | A **"Tabela Resumo no Monitor"**. | Visualização rápida por humanos no terminal. Fácil de ler. |
| **`text`** | O **"Relatório Bruto, separado por tabulação"**. | Ser usado em scripts de shell com ferramentas como `grep`, `awk` e `cut`. |

* **Como Mudar o Formato para um Único Comando:** Adicione a opção `--output`.
    ```bash
    aws ec2 describe-instances --output table
    ```
* **Como Mudar o Formato Padrão:** Re-execute `aws configure` e mude o `Default output format`.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Resumo do Profissional

* **Configuração:** Use `aws configure` para salvar suas credenciais IAM (nunca as do root!).
* **Estrutura:** Lembre-se da gramática: `aws <serviço> <operação> --parâmetros`.
* **Ajuda:** Use `help` como seu guia de referência instantâneo.
* **Saída:** Escolha o formato de saída (`json`, `table`, `text`) mais adequado para a sua tarefa.

> **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação:** Para a prova Cloud Practitioner:
> 1.  Relembre as **3 formas de interagir com a AWS**: Console, CLI e SDKs.
> 2.  A **CLI** é a ferramenta-chave para **automação e scripting**.
> 3.  O comando para configurar as credenciais de um usuário IAM é **`aws configure`**.

A AWS CLI é a sua porta de entrada para a automação na nuvem. Dominá-la é um passo essencial para se tornar um engenheiro de nuvem eficiente e poderoso.

---

### <img src="https://api.iconify.design/logos/aws-cli.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Cinto de Utilidades do Arquiteto: Guia Avançado da AWS CLI

Já conhecemos a gramática básica da CLI (`aws <serviço> <operação>`). Agora, vamos aprender os truques que os especialistas usam para filtrar o ruído, extrair a informação exata que precisam e operar com a máxima segurança.

**Analogia:** Pense que você é um **pesquisador** pedindo documentos ao **arquivista-chefe** de uma biblioteca gigante (a API da AWS).

---

### <img src="https://api.iconify.design/mdi/filter-variant.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Arte de Filtrar: `--filter` vs. `--query`

Ambos servem para reduzir resultados, mas funcionam de formas fundamentalmente diferentes.

#### <img src="https://api.iconify.design/mdi/server-search.svg?color=currentColor" width="20" /> `--filter` (Filtragem no Servidor)
* **Analogia:** Você faz um **pedido específico** ao arquivista: "Por favor, vá até a seção 'EC2' e traga-me **APENAS** as fichas das instâncias que são do tipo `t2.micro`."
* **Como Funciona:** O trabalho de busca é feito **pela AWS, no lado do servidor**, *antes* de os dados serem enviados para você.
* **Vantagem:** **Muito mais eficiente**. Reduz a quantidade de dados transferidos pela rede, economizando tempo e, em alguns casos, dinheiro.

#### <img src="https://api.iconify.design/mdi/magnify-scan.svg?color=currentColor" width="20" /> `--query` (Filtragem no Cliente)
* **Analogia:** Você faz um **pedido genérico**: "Traga-me **TODAS** as fichas da seção 'EC2'". O arquivista te entrega um **carrinho de mão gigante** com milhares de fichas (a resposta JSON completa). Agora, **na sua mesa**, você usa uma **"lente de aumento mágica" (`--query`)** para extrair apenas os campos que te interessam de cada ficha.
* **Como Funciona:** A filtragem acontece **no seu computador (lado do cliente)**, *depois* que você já recebeu todos os dados.
* **Vantagem:** **Extremamente flexível**. Usa uma linguagem de consulta para JSON chamada **JMESPath**, que permite extrair, fatiar e remodelar qualquer parte da resposta.

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT DE ESPECIALISTA:** A melhor prática é **usar os dois juntos!**
> 1.  Use o `--filter` primeiro para pedir à AWS que te envie apenas o conjunto de dados relevante.
> 2.  Depois, use o `--query` para extrair os campos exatos que você precisa desse resultado já filtrado.
>
> **Exemplo:** "Peça à AWS apenas as instâncias t2.micro (`--filter`), e desse resultado, mostre-me apenas o ID de cada uma (`--query`)."
> ```bash
> aws ec2 describe-instances \
>   --filters "Name=instance-type,Values=t2.micro" \
>   --query "Reservations[*].Instances[*].InstanceId"
> ```

---

### <img src="https://api.iconify.design/mdi/security.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Rede de Segurança (`--dry-run`)

* **A Dor que Resolve:** O medo de executar um comando destrutivo (como `aws ec2 terminate-instances`) e apagar o recurso errado.
* **Analogia:** Dizer ao arquivista: "**Simule** o processo de incinerar o arquivo 'Banco-de-Dados-Producao', mas **não acenda o fogo**."
* **Como Funciona:** Ao adicionar a opção `--dry-run` a um comando que faz uma alteração, a CLI envia a solicitação para a API, mas a API apenas **verifica se você tem as permissões necessárias** e se os parâmetros são válidos, sem de fato executar a ação.
    * Se tudo estiver correto, ela retorna uma resposta `DryRunOperation`.
    * Se você não tiver permissão, ela retorna `UnauthorizedOperation`.

> **`!!! tip "Dica de Ouro"`**
> Antes de executar qualquer comando que **cria, modifica ou deleta** recursos, **SEMPRE** execute-o primeiro com a flag `--dry-run`. É a sua rede de segurança contra erros caros.

---

### <img src="https://api.iconify.design/mdi/clipboard-list-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O "Cheat Sheet" do Dia a Dia (Comandos Comuns)

| <img src="https://api.iconify.design/logos/aws-ec2.svg" /> Amazon EC2 e Relacionados | <img src="https://api.iconify.design/logos/aws-s3.svg" /> Amazon S3 |
| :--- | :--- |
| **`aws ec2 run-instances`** | **`aws s3 ls`** (Lista buckets ou objetos) |
| **`aws ec2 describe-instances`**| **`aws s3 cp`** (Copia arquivos) |
| **`aws ec2 stop-instances`** | **`aws s3 mv`** (Move arquivos) |
| **`aws ec2 start-instances`** | **`aws s3 rm`** (Remove objetos) |
| **`aws ec2 create-volume`** | |
| **`aws ec2 create-vpc`** | |

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Entenda a diferença conceitual: **`--filter`** atua no **lado do servidor** (mais eficiente), **`--query`** atua no **lado do cliente** (mais flexível).
> 2.  Saiba que **`--dry-run`** é uma verificação de permissões **sem executar a ação**.
> 3.  Lembre-se que o comando `help` (ex: `aws s3 cp help`) é a sua documentação embutida.

---

### <img src="https://api.iconify.design/logos/aws-cli.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Terminal de Comando - Instalando e Configurando a AWS CLI

### O Cenário (A "User Story")

> **Como** a dona de uma cafeteria em expansão (Sofía), **EU QUERO** instalar e configurar a AWS CLI, **PARA QUE** eu possa começar a automatizar tarefas de gerenciamento na minha conta AWS e não depender apenas de cliques no console.

### A Dor que o Lab Resolve

O Console da AWS é ótimo para tarefas visuais e pontuais. Mas imagine que você precise criar 10 usuários IAM ou verificar o status de 50 instâncias EC2. Fazer isso manualmente é lento, repetitivo e propenso a erros. A CLI é a ferramenta que resolve a dor da **operação manual em escala**, permitindo que você escreva scripts para automatizar qualquer tarefa.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Criar um usuário IAM para acesso programático e obter suas chaves de acesso.
* [ ] Conectar-se a uma instância EC2 Linux via SSH.
* [ ] Instalar a AWS CLI em um sistema Linux (baseado em Red Hat).
* [ ] Configurar a CLI com suas credenciais de forma segura.
* [ ] Executar comandos básicos para interagir com o serviço IAM.

### Pré-requisitos
* Acesso ao Console da AWS com um usuário administrativo.
* Uma instância EC2 com **Amazon Linux** ou **Red Hat** em execução.
* Acesso via **SSH** a esta instância.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

**Analogia:** Para usar o "terminal de comando do nosso robô" (a CLI), primeiro precisamos criar o "crachá eletrônico" (as chaves de acesso) para o operador.

#### Parte 1: A Preparação - Criando as Credenciais (IAM)

1.  No Console da AWS, navegue até o serviço **IAM**.
2.  No painel esquerdo, clique em **Users** (Usuários) e depois em **Add users**.
3.  **User name:** `cli-user`.
4.  **AWS credential type:** Selecione **Access key - Programmatic access** (Chave de acesso - Acesso programático).
5.  Clique em **Next: Permissions**.
6.  Selecione **Attach existing policies directly** (Anexar políticas existentes diretamente).
7.  Na lista, procure e marque a política `AdministratorAccess`.
    > **`!!! warning "Atenção"`**
    > Em um ambiente de produção real, você seguiria o Princípio do Menor Privilégio, criando uma política customizada apenas com as permissões necessárias. Para este lab, usaremos o acesso de administrador para simplificar.
8.  Clique em **Next: Tags**, **Next: Review**, e **Create user**.
9.  **PASSO CRÍTICO:** Na tela de sucesso, você verá o **Access key ID** e a **Secret access key**.
    * Clique no botão **Download .csv** para salvar estas credenciais em um lugar seguro no seu computador.
    * **Esta é a ÚNICA vez que você verá a Chave de Acesso Secreta.** Se você a perder, terá que criar uma nova.

#### Parte 2: A Instalação no Servidor (EC2)
1.  Conecte-se à sua instância EC2 via **SSH**.
2.  Vamos instalar a AWS CLI. Como o Amazon Linux é baseado em Red Hat, usamos o gerenciador de pacotes `yum`.
    ```bash
    sudo yum install aws-cli -y
    ```
3.  Verifique se a instalação foi bem-sucedida:
    ```bash
    aws --version
    ```

#### Parte 3: A Ativação do Terminal (`aws configure`)
Agora, vamos "apresentar" as credenciais que salvamos para a CLI.

1.  Execute o comando de configuração:
    ```bash
    aws configure
    ```
2.  O terminal pedirá 4 informações. Abra o arquivo `.csv` que você baixou no Passo 1 e copie e cole os valores:
    * **AWS Access Key ID:** Cole o seu Access Key ID.
    * **AWS Secret Access Key:** Cole a sua Secret Access Key.
    * **Default region name:** Digite a Região onde sua instância está (ex: `us-east-1` ou `sa-east-1`).
    * **Default output format:** Digite `json`.

#### Parte 4: A Primeira Ordem (Testando a Conexão)
> **`!!! tip "O Momento 'A-Ha!' da Automação"`**
> Agora vamos provar que tudo funcionou, controlando a nuvem a partir da nossa linha de comando.

1.  Dê uma ordem simples e segura. Peça à AWS para listar todos os usuários IAM na sua conta:
    ```bash
    aws iam list-users
    ```
2.  **Verificação:** Você deve ver uma saída em formato JSON listando os usuários da sua conta, incluindo o `cli-user` que criamos.

Parabéns! Você acabou de instalar, configurar e usar a AWS CLI para interagir com sua conta.

---

### <img src="https://api.iconify.design/mdi/comment-question-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Debriefing: Respondendo às Perguntas-Chave

* **1. Por que usar a AWS CLI em vez do Console?**
    * **Automação:** A CLI é a base para a automação. Você pode colocar comandos da CLI dentro de scripts (Shell, Python) para executar tarefas complexas de forma repetível.
    * **Velocidade:** Para profissionais experientes, executar um comando no terminal é muito mais rápido do que navegar por várias telas no console.
    * **Repetibilidade:** Garante que uma tarefa seja executada da mesma maneira todas as vezes, eliminando erros humanos.

* **2. A arquitetura da solução muda ao usar a AWS CLI?**
    * **Não.** A arquitetura **não muda**. A CLI, o Console e os SDKs são apenas **"controles remotos" diferentes** para a mesma "TV" (a API da AWS). O recurso que você cria (uma instância EC2, um bucket S3) será exatamente o mesmo, não importa qual "controle remoto" você usou.

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos
* [ ] No console do **IAM**, delete o usuário `cli-user`.
* [ ] Termine a instância **EC2** que você usou para o laboratório.