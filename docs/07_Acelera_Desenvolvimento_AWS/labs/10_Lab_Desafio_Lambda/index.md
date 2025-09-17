# <img src="https://api.iconify.design/logos/aws-lambda.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Relatório Automatizado - Trabalhando com AWS Lambda

### O Cenário (A "User Story")

> **Como** o dono de uma cafeteria, **EU QUERO** um sistema que automaticamente gere um relatório de análise de vendas todos os dias e o envie para o meu e-mail, **PARA QUE** eu possa tomar decisões de negócio baseadas em dados, sem precisar rodar relatórios manualmente ou manter um servidor para isso.

### A Dor que o Lab Resolve

1.  **Processos Manuais:** Gerar relatórios manualmente é uma tarefa repetitiva, demorada e propensa a erros humanos.
2.  **Custo de Infraestrutura:** Manter um servidor (EC2) ligado 24/7 apenas para executar uma tarefa que roda por poucos minutos por dia é um grande desperdício de dinheiro.

Este laboratório resolve essas dores construindo um pipeline de relatórios **100% serverless**, que só consome recursos quando está efetivamente trabalhando.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Criar uma **Camada (Layer)** do Lambda para gerenciar dependências de código.
* [ ] Criar uma função Lambda que se conecta a um banco de dados em uma VPC.
* [ ] Configurar um **gatilho agendado (Scheduled Trigger)** com o Amazon EventBridge.
* [ ] Orquestrar a chamada de uma função Lambda por outra.
* [ ] Usar o **CloudWatch Logs** para solucionar problemas (`troubleshoot`).


---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Analisando os "Crachás de Acesso" (As Funções do IAM)

**Analogia:** Antes de contratar nossos "gênios da lâmpada" (as funções Lambda), precisamos ir ao "departamento de segurança" (IAM) e pegar os crachás de acesso corretos para eles.

1.  No Console da AWS, navegue até **IAM > Funções (Roles)**.
2.  **Analise a `salesAnalysisReportRole`:**
    * **Relações de confiança (Trust relationships):** Veja que ela "confia" no `lambda.amazonaws.com`. Isso permite que o serviço Lambda "vista" este crachá.
    * **Permissões (Permissions):** Observe as políticas. Ela tem permissão para enviar notificações (`AmazonSNSFullAccess`), invocar outras Lambdas (`AWSLambdaRole`), etc.
3.  **Analise a `salesAnalysisReportDERole`:**
    * **Permissões:** Observe a política `AWSLambdaVPCAccessExecutionRole`. Este é o "passe especial" que permite que uma função Lambda se conecte a recursos dentro da sua rede privada (VPC), como nosso banco de dados.

#### Tarefa 2: Criando a "Mochila de Ferramentas" e o Primeiro "Gênio"

**Analogia:** Nosso primeiro gênio precisa de uma "ferramenta especial" (uma biblioteca Python) para falar com o banco de dados MySQL. Em vez de colocar a ferramenta dentro do livro de feitiços, vamos colocá-la em uma **"mochila de ferramentas" (Lambda Layer)** que ele pode usar.

1.  **Crie a Camada (Layer):**
    * Navegue até **AWS Lambda > Camadas (Layers)** e clique em **Criar camada (Create layer)**.
    * **Nome (Name):** `pymysqlLibrary`.
    * **Descrição (Description):** `Biblioteca PyMySQL`.
    * **Fazer upload de um arquivo .zip:** Faça o upload do arquivo `pymysql-v3.zip` que você baixou.
    * **Runtimes compatíveis:** Selecione `Python 3.9`.
    * Clique em **Criar (Create)**.
2.  **Crie a Função Extratora de Dados:**
    * Vá em **Funções (Functions)** e clique em **Criar função (Create function)**.
    * **Nome da função (Function name):** `salesAnalysisReportDataExtractor`.
    * **Tempo de execução (Runtime):** `Python 3.9`.
    * **Permissões (Permissions):** Expanda `Alterar a função de execução padrão`, selecione `Usar uma função existente (Use an existing role)` e escolha `salesAnalysisReportDERole`.
    * Clique em **Criar função**.
3.  **Anexe a "Mochila" à Função:**
    * Na página da sua nova função, no painel **Visão geral da função (Function overview)**, clique no nó **Camadas (Layers)**.
    * Clique em **Adicionar uma camada (Add a layer)**.
    * Selecione `Camadas personalizadas (Custom layers)`, escolha `pymysqlLibrary` e a `Versão (Version)` 1. Clique em **Adicionar (Add)**.
4.  **Faça o Upload do "Livro de Feitiços":**
    * Na aba **Código (Code)**, em **Origem do código (Code source)**, clique em **Fazer upload de (Upload from)** e selecione **Arquivo .zip**.
    * Faça o upload do arquivo `salesAnalysisReportDataExtractor-v3.zip`.
5.  **Configure o Ponto de Entrada (Handler):**
    * Ainda em **Código (Code)**, em **Configurações de runtime (Runtime settings)**, clique em **Editar (Edit)**.
    * Altere o **Manipulador (Handler)** para: `salesAnalysisReportDataExtractor.lambda_handler`. Salve.
6.  **Conecte a Função à Rede:**
    * Vá para a aba **Configuração (Configuration) > VPC**.
    * Clique em **Editar (Edit)** e conecte a função à `VPC da cafeteria (CafeVPC)`, à `Sub-rede pública 1 (Public Subnet 1)` e ao `Grupo de segurança (Security group)` `CafeSecurityGroup`. Salve.

#### Tarefa 3: Testando e Solucionando Problemas do "Gênio"

1.  **Prepare o Teste:**
    * Vá para o **Systems Manager > Parameter Store** e copie os valores dos parâmetros do banco de dados (`/cafe/dbUrl`, `dbName`, etc.).
    * Na sua função Lambda, vá para a aba **Testar (Test)**. Crie um novo evento de teste chamado `SARDETestEvent`.
    * Cole o JSON abaixo, substituindo os valores pelos que você copiou:
        ```json
        {
          "dbUrl": "<valor_do_dbUrl>",
          "dbName": "<valor_do_dbName>",
          "dbUser": "<valor_do_dbUser>",
          "dbPassword": "<valor_do_dbPassword>"
        }
        ```
    * Salve o evento de teste.
2.  **Execute o Teste:** Clique em **Testar (Test)**. Você verá um erro de **`Task timed out`**.
3.  **O Detetive:**
    * **A Dor:** A função não consegue se conectar ao banco de dados e o tempo se esgota.
    * **A Pista:** Conexões de banco de dados MySQL usam a porta `3306`. A função está na VPC, mas a "fechadura" (Security Group) está permitindo que ela entre no "prédio" do banco de dados?
    * **A Solução:** Vá para o **EC2 > Grupos de Segurança (Security Groups)**. Selecione o `CafeSecurityGroup`. Vá em **Editar regras de entrada (Edit inbound rules)**. Adicione uma nova regra que permita tráfego `MySQL/Aurora (porta 3306)` a partir do próprio `CafeSecurityGroup` (isso permite que recursos dentro do mesmo grupo de segurança conversem entre si).
4.  **Teste Novamente:** Volte para a função Lambda e execute o teste novamente. Agora ele deve passar!
5.  **Popule o Banco de Dados:** Acesse o site da cafeteria (o IP está nos detalhes do lab) e faça alguns pedidos para gerar dados.
6.  **Teste Final:** Execute o teste na função Lambda mais uma vez. Agora, a saída JSON no campo `body` deve conter os dados dos pedidos que você fez.

#### Tarefa 4 e 5: Criando o "Gênio Maestro" e o Gatilho

1.  **Crie o Tópico SNS:** Vá para o **Amazon SNS** e crie um tópico chamado `salesAnalysisReportTopic`. Crie uma **inscrição (subscription)** para o seu e-mail e **confirme-a** na sua caixa de entrada. Anote o **ARN** do tópico.
2.  **Crie a Função "Maestro":** Usando a **AWS CLI** no seu **CLI Host**, crie a segunda função.
    * Navegue até a pasta `activity-files`.
    * Obtenha o ARN da `salesAnalysisReportRole` no console do IAM.
    * Execute o comando `create-function` (substituindo os valores):
        ```bash
        aws lambda create-function \
        --function-name salesAnalysisReport \
        --runtime python3.9 \
        --zip-file fileb://salesAnalysisReport-v2.zip \
        --handler salesAnalysisReport.lambda_handler \
        --region us-west-2 \
        --role <ARN_DA_SUA_ROLE>
        ```
3.  **Configure a Função "Maestro":**
    * No console do Lambda, abra a função `salesAnalysisReport`.
    * Na aba **Configuração (Configuration) > Variáveis de ambiente (Environment variables)**, crie uma variável chamada `topicARN` e cole o ARN do seu tópico SNS como valor.
4.  **Teste a Função "Maestro":** Vá na aba **Testar (Test)**, crie um evento "hello-world" e execute.
    > **O Resultado:** Você deve receber um e-mail com o relatório de vendas! A função "maestro" invocou a função "extratora", pegou os dados e os enviou para você.
5.  **Crie o Gatilho Agendado:**
    * Na função `salesAnalysisReport`, clique em **+ Adicionar gatilho (+ Add trigger)**.
    * Selecione **EventBridge (CloudWatch Events)**.
    * Crie uma **nova regra** chamada `Gatilho-Relatorio-Diario`.
    * Selecione **Expressão de programação (Schedule expression)** e use uma expressão `cron` para que ela rode em 5 minutos (lembre-se que o horário é UTC!).
    * Ex: `cron(MINUTOS HORA ? * MON-SAT *)`
6.  **Verificação Final:** Aguarde o horário agendado. Você receberá o relatório de vendas no seu e-mail, desta vez disparado automaticamente pelo "relógio mágico" do EventBridge.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você construiu uma solução serverless de ponta a ponta, orquestrando múltiplos serviços da AWS. Você atuou como um verdadeiro engenheiro de nuvem, não apenas implantando, mas também diagnosticando e corrigindo problemas de configuração de rede e permissões.

---
# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: Ensinando a Nuvem a Trabalhar Sozinha

Hoje foi um daqueles laboratórios que te levam para o próximo nível. A missão era construir um sistema de relatórios de vendas totalmente automatizado, 100% serverless. A ideia era ter um "robô" que, toda noite, acessasse um banco de dados, gerasse um relatório e o enviasse para o meu e-mail.

O que eu não esperava era a quantidade de lições valiosas que eu aprenderia no caminho, especialmente quando as coisas deram errado.

### A Jornada em 4 Atos

#### Ato 1: A "Mochila de Ferramentas" (Lambda Layers)
* **A Dor:** Meu "assistente robô" (a função Lambda) precisava de uma ferramenta especial para falar com o banco de dados MySQL (a biblioteca `PyMySQL`). Como eu entrego essa ferramenta para ele?
* **O Que Eu Fiz:** Em vez de embutir a ferramenta no "cérebro" do robô, eu criei uma **Camada (Layer)** do Lambda.
* **O "Aha!" Moment:**
    * **Analogia:** Eu criei uma **"mochila de ferramentas"** com a `PyMySQL` dentro. Agora, qualquer um dos meus futuros robôs que precisem falar com um banco de dados pode simplesmente "vestir" essa mesma mochila. Isso mantém o código do robô limpo, focado na sua tarefa, e torna minhas ferramentas reutilizáveis.

#### Ato 2: O Detetive de Rede (O Bug do Timeout)
* **A Dor:** Eu executei minha função pela primeira vez e... falhou. A mensagem era `Task timed out`. O código parecia certo, o banco de dados estava no ar. O que estava acontecendo?
* **O Que Eu Fiz:** Fui investigar. A pista era que a função não conseguia *chegar* ao banco de dados.
* **O "Aha!" Moment:** A ficha caiu: minha função Lambda estava conectada à minha rede privada (VPC) para poder acessar o banco. Isso significa que ela estava **dentro** das minhas muralhas de segurança.
    * **Analogia:** Meu "robô" estava tentando falar com o "servidor do banco de dados", mas a **"fechadura eletrônica" (o Security Group)** da sala do banco de dados não reconhecia o crachá do robô. Ele estava sendo barrado na porta!
* **A Solução:** Eu tive que ir no Security Group do banco de dados e adicionar uma regra permitindo a entrada de tráfego vindo do Security Group da minha própria função Lambda. A segurança de rede se aplica até mesmo a recursos serverless!

#### Ato 3: O Maestro e o Músico (Orquestrando Funções)
* **A Dor:** Eu poderia ter escrito uma única função gigante que fazia tudo. Mas isso seria confuso e difícil de manter.
* **O Que Eu Fiz:** O lab me ensinou a separar as responsabilidades, criando duas funções.
* **O "Aha!" Moment:**
    * **Analogia:** Eu construí dois robôs. Um era um **"músico especialista" (`DataExtractor`)**, cujo único trabalho era tocar um instrumento perfeitamente (consultar o banco de dados). O outro era o **"maestro" (`salesAnalysisReport`)**. O maestro não toca um instrumento; seu trabalho é chamar o músico na hora certa, pegar a música, formatar o relatório e enviá-lo para a audiência (o tópico SNS). Essa separação de tarefas torna o sistema muito mais limpo.

#### Ato 4: O Relógio Mágico (O Gatilho Agendado)
* **A Dor:** Como fazer esse relatório rodar toda noite, sem que eu precise apertar o botão?
* **O Que Eu Fiz:** Criei um gatilho agendado com o **Amazon EventBridge**.
* **O "Aha!" Moment:**
    * **Analogia:** Eu configurei um **"relógio mágico"** para "esfregar a lâmpada" do meu robô maestro todo dia, em um horário específico. A automação estava completa.

### A Grande Lição
Este lab não foi apenas sobre codificação; foi sobre **arquitetura**. Ele me ensinou que "serverless" não significa "sem complexidade", mas sim construir sistemas poderosos juntando pequenos serviços especializados como peças de Lego.

Depurar o problema do Security Group foi frustrante no início, mas incrivelmente recompensador. Me forçou a entender que, mesmo que eu não gerencie o servidor, eu ainda sou o arquiteto responsável pela segurança e pela forma como os componentes interagem. Ver aquele e-mail automático chegar na minha caixa de entrada, disparado por um relógio que eu configurei... foi uma sensação fantástica de dever cumprido.

#AWS #Cloud #Serverless #Lambda #DevOps #Automation #AWSreStart