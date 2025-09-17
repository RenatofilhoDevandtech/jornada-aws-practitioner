# <img src="https://api.iconify.design/logos/aws-lambda.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab [Desafio]: O Contador de Palavras Serverless (S3 + Lambda + SNS)

### O Cenário (A "User Story")

> **Como** um desenvolvedor, **EU QUERO** criar um sistema automatizado que, ao receber um arquivo de texto, conte o número de palavras e me notifique por e-mail, **PARA QUE** eu possa processar dados de forma assíncrona e escalável, sem gerenciar nenhum servidor.

### A Dor que o Lab Resolve

Processar arquivos manualmente é lento e ineficiente. Construir um servidor que fica 24/7 "escutando" por novos arquivos é caro e complexo de escalar. Este laboratório resolve a dor do **processamento ineficiente**, criando um pipeline orientado a eventos que só consome recursos quando há trabalho a ser feito.

### Objetivos de Aprendizado
Ao final deste desafio, você terá construído:

* [ ] Um **Tópico SNS** para enviar notificações por e-mail.
* [ ] Um **Bucket S3** que servirá como gatilho.
* [ ] Uma **Função Lambda** em Python que se integra com S3 e SNS.
* [ ] Um pipeline de dados 100% serverless e automatizado.



---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Plano de Ação do Arquiteto

A ordem de criação dos recursos é importante. Vamos construir a arquitetura em três fases, de "trás para frente".

#### Fase 1: O Canal de Notificação (Configurando o SNS)

**Analogia:** Primeiro, vamos criar o **"grupo de notificação por e-mail"** para onde nosso robô enviará os relatórios.

1.  No Console da AWS, navegue até o serviço **Simple Notification Service (SNS)**.
2.  No menu esquerdo, clique em **Tópicos (Topics)**.
3.  Clique em **Criar tópico (Create topic)**.
4.  Selecione o tipo `Padrão (Standard)` e configure:
    * **Nome (Name):** `ContagemDePalavrasTopico`
5.  Clique em **Criar tópico**.
6.  Na página do seu novo tópico, na seção **Inscrições (Subscriptions)**, clique em **Criar inscrição (Create subscription)**.
    * **Protocolo (Protocol):** `E-mail`.
    * **Endpoint:** Insira seu endereço de e-mail pessoal.
7.  Clique em **Criar inscrição**.
8.  **AÇÃO CRÍTICA:** Vá para sua caixa de e-mail, encontre o e-mail da "AWS Notifications" e clique no link **Confirm subscription**. Sem isso, você não receberá os resultados do lab.

#### Fase 2: A Caixa de Entrada (Configurando o S3)

**Analogia:** Agora, vamos criar a **"caixa de entrada"** onde os "documentos" (arquivos de texto) serão depositados.

1.  Vá para o serviço **S3**.
2.  Clique em **Criar bucket (Create bucket)**.
3.  Dê um **nome de bucket globalmente único** (ex: `desafio-lambda-renato-` seguido de números aleatórios).
4.  Selecione a mesma **Região** do seu laboratório.
5.  Deixe todas as outras opções como padrão e clique em **Criar bucket**.

#### Fase 3: O Cérebro da Operação (Configurando o Lambda)

**Analogia:** É hora de construir e treinar nosso **"assistente robô inteligente"**.

1.  Vá para o serviço **AWS Lambda** e clique em **Criar função (Create function)**.
2.  Selecione **Criar do zero (Author from scratch)**.
3.  **Configuração básica:**
    * **Nome da função (Function name):** `contador-de-palavras`
    * **Runtime:** `Python 3.9` (ou a versão mais recente disponível).
    * **Permissões (Permissions):** Expanda a seção, selecione **Usar uma função existente (Use an existing role)** e escolha a `LambdaAccessRole` fornecida pelo laboratório.
4.  Clique em **Criar função**.

##### Adicionando o Gatilho (Conectando o S3 ao Lambda)
1.  Na página da sua função, na seção **Visão geral da função (Function overview)**, clique em **+ Adicionar gatilho (+ Add trigger)**.
2.  **Configuração do gatilho:**
    * **Fonte (Source):** Selecione **S3**.
    * **Bucket:** Selecione o bucket que você acabou de criar.
    * **Tipo de evento (Event type):** Mantenha `Todos os eventos de criação de objeto (All object create events)`.
    * Marque a caixa de confirmação de recursividade e clique em **Adicionar (Add)**.

##### Escrevendo o Código (O "Cérebro" do Robô)
1.  Vá para a aba **Código (Code)**.
2.  Apague o código de exemplo e **cole o seguinte código Python**:
    ```python
    import json
    import boto3
    import os

    # Cria clientes para interagir com o S3 e SNS
    s3_client = boto3.client('s3')
    sns_client = boto3.client('sns')

    # Pega o ARN do tópico SNS a partir das variáveis de ambiente
    SNS_TOPIC_ARN = os.environ['SNS_TOPIC_ARN']

    def lambda_handler(event, context):
        # 1. Extrai o nome do bucket e do arquivo do evento que o S3 enviou
        bucket_name = event['Records'][0]['s3']['bucket']['name']
        file_key = event['Records'][0]['s3']['object']['key']
        
        print(f"Novo arquivo detectado: {file_key} no bucket {bucket_name}")

        try:
            # 2. Faz o download do arquivo do S3
            response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
            file_content = response['Body'].read().decode('utf-8')
            
            # 3. Conta as palavras
            word_count = len(file_content.split())
            print(f"Contagem de palavras: {word_count}")

            # 4. Formata a mensagem de notificação
            subject = "Word Count Result"
            message = f"The word count in the {file_key} file is {word_count}."
            
            # 5. Publica a mensagem no tópico SNS
            sns_client.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject=subject,
                Message=message
            )
            
            return {'statusCode': 200, 'body': json.dumps('Processo concluído com sucesso!')}

        except Exception as e:
            print(f"Erro no processamento: {str(e)}")
            raise e
    ```
3.  Clique em **Deploy** para salvar seu código.

##### Configurando o Destino da Notificação
1.  Vá para a aba **Configuração (Configuration)** > **Variáveis de ambiente (Environment variables)** e clique em **Editar (Edit)**.
2.  Clique em **Adicionar variável de ambiente (Add environment variable)**.
    * **Chave (Key):** `SNS_TOPIC_ARN`
    * **Valor (Value):** Vá para a página do seu tópico SNS, copie o **ARN** e cole aqui.
3.  Clique em **Salvar (Save)**.

---

### <img src="https://api.iconify.design/mdi/check-all.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Teste Final

1.  No seu computador, crie um arquivo de texto simples chamado `teste.txt` e escreva algumas palavras nele (ex: "Olá mundo, este é um teste").
2.  Vá para o console do **S3**, abra seu bucket e clique em **Carregar (Upload)**.
3.  Adicione o arquivo `teste.txt` e finalize o upload.
4.  **Verificação:** Em alguns segundos, verifique seu e-mail. Você deverá receber uma notificação do SNS com o assunto "Word Count Result" e a mensagem formatada com a contagem de palavras correta!

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: Construindo meu Primeiro Robô Serverless

Hoje foi o "exame final" do meu módulo de computação serverless no AWS re/Start. A missão era mais do que apenas escrever um código; era construir um sistema, um pipeline de processamento de dados completo, juntando três dos serviços mais poderosos da AWS.

O desafio: criar uma função que conta as palavras de qualquer arquivo de texto enviado para um bucket S3 e notifica o resultado por e-mail. Parece simples, mas a arquitetura por trás é incrivelmente elegante e poderosa.

### A Jornada em 3 Atos

#### Ato 1: Preparando o Terreno
Antes de construir o "cérebro" da operação (a função Lambda), eu precisei montar o seu ambiente de trabalho.
* **Analogia:** Antes de contratar meu **"assistente robô" (a Lambda)**, eu precisei preparar duas coisas:
    1.  A **"Caixa de Entrada" (o bucket S3)**, onde os documentos para ele processar chegariam.
    2.  O **"Grupo de Notificação por E-mail" (o Tópico SNS)**, para onde ele enviaria seus relatórios.

Isso me ensinou uma lição de arquitetura: em sistemas orientados a eventos, muitas vezes você constrói os pontos de entrada e saída primeiro.

#### Ato 2: Construindo o Cérebro (A Função Lambda)
Esta foi a parte mais legal, onde tudo se conectou.
* **O Que Eu Fiz:** Criei a função Lambda em Python e configurei o **Gatilho (Trigger)**.
* **O "Aha!" Moment:** O gatilho é a mágica do serverless. Eu "liguei" a Caixa de Entrada (S3) diretamente ao "botão de ligar" do meu robô (Lambda). Agora, a simples chegada de um novo arquivo **automaticamente aciona** a função. Não há um programa rodando 24/7 esperando por arquivos; a computação só acontece quando é necessária.
* **A Lógica do Robô:** O código que escrevi era a "diretriz principal" do assistente:
    1.  "Quando ativado, identifique o novo documento que chegou."
    2.  "Faça o download e leia o conteúdo."
    3.  "Conte as palavras."
    4.  "Escreva um relatório formatado."
    5.  "Envie o relatório para o Grupo de Notificação."

#### Ato 3: O Teste (Ver a Mágica Acontecer)
O momento final foi simplesmente fazer o upload de um arquivo `teste.txt` no bucket S3. Eu não executei um comando, não iniciei um servidor... eu apenas arrastei um arquivo.

Segundos depois, meu celular vibrou. Era um e-mail: *"The word count in the teste.txt file is 7."*

Funcionou. Simplesmente funcionou.

### A Grande Lição
Este lab foi a lição definitiva sobre **arquitetura orientada a eventos**. Eu não construí um programa que *verifica* por trabalho. Eu construí um sistema que **reage** ao trabalho. A chegada do dado *é* o evento que invoca o poder computacional.

Isso é incrivelmente eficiente. Se eu enviar 1 arquivo, uma função roda. Se eu enviar 1.000 arquivos ao mesmo tempo, a AWS magicamente cria 1.000 "robôs" para fazer o trabalho em paralelo, e eu não preciso configurar absolutamente nada para que isso aconteça.

Construir essa solução de ponta a ponta, vendo como S3, Lambda e SNS se encaixam como peças de Lego para criar um pipeline automatizado sem um único servidor à vista... isso é um divisor de águas. Me deu a confiança de que, com esses blocos de construção, posso criar soluções realmente complexas e poderosas.

#AWS #Cloud #Serverless #Lambda #S3 #SNS #DevOps #AWSreStart
