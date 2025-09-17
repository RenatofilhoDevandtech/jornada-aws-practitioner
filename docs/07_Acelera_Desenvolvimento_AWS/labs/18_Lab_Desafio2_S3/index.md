# <img src="https://api.iconify.design/logos/aws-s3.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Cofre Colaborativo - Trabalhando com Permissões e Eventos do S3

### O Cenário (A "User Story")

> **Como** o administrador da nuvem de uma cafeteria, **EU QUERO** criar um bucket S3 seguro onde uma agência de mídia externa possa fazer o upload de fotos dos nossos produtos, **PARA QUE** eu possa receber o conteúdo de forma segura e ser notificado automaticamente sempre que um arquivo for adicionado ou removido.

### A Dor que o Lab Resolve

1.  **Compartilhamento Inseguro:** Enviar arquivos por e-mail ou usar serviços de compartilhamento de arquivos genéricos não é seguro nem escalável para um fluxo de trabalho profissional.
2.  **Falta de Visibilidade:** Como saber quando o fotógrafo enviou as novas fotos? Ficar perguntando por e-mail é ineficiente.
3.  **Permissões Excessivas:** Como dar acesso ao fotógrafo apenas à pasta de "imagens", sem que ele possa ver ou mexer em outras partes do nosso bucket?

Este laboratório resolve essas dores construindo uma "caixa de entrada" de arquivos inteligente, segura e que te avisa quando há novidades.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Criar um bucket S3 e um usuário IAM com permissões granulares via AWS CLI.
* [ ] Testar e verificar as permissões de um usuário externo.
* [ ] Configurar um tópico SNS para receber notificações por e-mail.
* [ ] Configurar Notificações de Eventos do S3 para acionar o tópico SNS.

### Duração
* Aproximadamente 45-60 minutos (sem contar os 90 minutos do lab original).

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Preparando o "Posto de Comando"
1.  **Conecte-se ao `Host da CLI (CLI Host)`** usando o EC2 Instance Connect.
2.  **Configure a AWS CLI** com o comando `aws configure`, usando as credenciais (`AccessKey`, `SecretKey`) e a região (`us-west-2`) fornecidas no painel de detalhes do laboratório.

#### Tarefa 2: Criando o "Cofre" e Colocando as Primeiras Fotos
**Analogia:** Vamos construir nosso "cofre de fotos" (bucket) e fazer o upload do acervo inicial.

1.  **Crie o Bucket:** Execute o comando `s3 mb` (make bucket). Substitua `<cafe-SEU-NOME-UNICO>` por um nome único.
    ```bash
    aws s3 mb s3://<cafe-SEU-NOME-UNICO> --region 'us-west-2'
    ```
2.  **Sincronize as Imagens Iniciais:**
    ```bash
    aws s3 sync ~/initial-images/ s3://<cafe-SEU-NOME-UNICO>/images/
    ```
    > **O "Porquê":** O comando `sync` é ótimo para fazer o upload de uma pasta inteira. Estamos criando um "prefixo" (uma "pasta") chamado `images/` dentro do nosso bucket.

#### Tarefa 3: Criando o "Crachá de Visitante" (Analisando as Permissões)
**Analogia:** Agora, vamos criar o "crachá de acesso" para nosso fotógrafo externo (`mediacouser`), garantindo que ele só possa entrar na "sala de fotos".

1.  **Analise as "Leis" do Crachá:** No console do **IAM**, vá para **Grupos de usuários (User groups)** e selecione `mediaco`. Na aba **Permissões (Permissions)**, expanda a política `mediaCoPolicy`.
    * **Observe a granularidade:** A política permite listar buckets, mas as ações de `GetObject` (ler), `PutObject` (escrever) e `DeleteObject` (deletar) são permitidas **APENAS** para o caminho `arn:aws:s3:::*/*/images/*`. Isso garante que ele só possa trabalhar na "pasta" de imagens.
2.  **Gere as Credenciais:** Vá para **Usuários (Users)** > `mediacouser` > aba **Credenciais de segurança (Security credentials)**.
    * Clique em **Criar chave de acesso (Create access key)**.
    * Selecione `Interface de linha de comando (CLI)`.
    * Confirme e clique em **Criar chave de acesso**.
    * **Ação Crítica:** Clique em **Baixar arquivo .csv (Download .csv file)**. Guarde este arquivo, pois ele contém as chaves de acesso do nosso "fotógrafo".

#### Tarefa 4: A Notificação Automática (Configurando Eventos S3 -> SNS)
**Analogia:** Vamos instalar um "sensor de movimento" na porta do nosso cofre que envia um alerta para o "grupo de e-mail do gerente" sempre que a porta é aberta.

1.  **Crie o "Grupo de E-mail" (Tópico SNS):**
    * No console do **SNS**, vá em **Tópicos (Topics)** e **Crie um tópico**.
    * **Tipo:** `Padrão (Standard)`.
    * **Nome:** `s3NotificationTopic`.
    * **Anote o ARN** do tópico criado.
    * **Adicione a Permissão para o S3:** Na aba **Política de acesso (Access policy)**, clique em **Editar**. Substitua o JSON pelo código fornecido no lab, **inserindo o ARN do seu tópico e o nome do seu bucket**.
        > **O "Porquê":** Esta política é uma **Política Baseada em Recurso**. Estamos dizendo ao SNS: "Você tem permissão para aceitar mensagens do serviço S3, mas somente se a mensagem vier daquele bucket específico."
    * **Inscreva-se:** Crie uma **inscrição (subscription)** para o seu e-mail e **confirme-a** na sua caixa de entrada.
2.  **Instale o "Sensor de Movimento" (Notificação de Eventos do S3):**
    * No seu terminal do **CLI Host**, crie um arquivo de configuração chamado `s3EventNotification.json`.
    ```bash
    vi s3EventNotification.json
    ```
    * Pressione `i` e cole o JSON fornecido no lab, **substituindo pelo ARN do seu tópico SNS**. Salve e saia (`Esc` > `:wq`).
        > **O "Porquê":** Este arquivo diz: "Monitore a 'pasta' `images/`. Se um objeto for **criado** (`s3:ObjectCreated:*`) ou **removido** (`s3:ObjectRemoved:*`), envie uma mensagem para este tópico SNS."
    * **Ative a Configuração:**
    ```bash
    aws s3api put-bucket-notification-configuration \
        --bucket <SEU_NOME_DE_BUCKET> \
        --notification-configuration file://s3EventNotification.json
    ```
    > Você receberá um e-mail de teste do S3 confirmando que o "sensor" está ativo.

#### Tarefa 5: Testando o Fluxo Completo
**Analogia:** Vamos pedir ao "fotógrafo" para usar seu crachá, entrar na sala de fotos e fazer seu trabalho. E vamos ver se o "gerente" é notificado.

1.  **Configure a CLI como `mediacouser`:** No terminal do **CLI Host**, execute `aws configure` novamente, mas desta vez, use as **chaves de acesso do arquivo `.csv` que você baixou**.
2.  **Teste o Upload (`PutObject`):**
    ```bash
    aws s3api put-object --bucket <SEU_NOME_DE_BUCKET> --key images/Caramel-Delight.jpg --body ~/new-images/Caramel-Delight.jpg
    ```
    * **Verificação:** Verifique seu e-mail. Você deve receber uma notificação do SNS dizendo que um `ObjectCreated:Put` ocorreu!
3.  **Teste a Exclusão (`DeleteObject`):**
    ```bash
    aws s3api delete-object --bucket <SEU_NOME_DE_BUCKET> --key images/Strawberry-Tarts.jpg
    ```
    * **Verificação:** Verifique seu e-mail. Você deve receber outra notificação, desta vez para um evento `ObjectRemoved:Delete`!
4.  **Teste a Violação de Permissão:** Tente alterar as permissões de um objeto.
    ```bash
    aws s3api put-object-acl --bucket <SEU_NOME_DE_BUCKET> --key images/Donuts.jpg --acl public-read
    ```
    * **Verificação:** O comando falhará com `AccessDenied`. Isso prova que nossa política do IAM está funcionando perfeitamente, e o "fotógrafo" só pode fazer o trabalho para o qual foi contratado.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você construiu uma solução de colaboração de arquivos segura e orientada a eventos. Você aprendeu a usar o IAM para conceder permissões granulares a um usuário externo e a usar as Notificações de Eventos do S3 para criar um fluxo de trabalho automatizado que te mantém informado sobre todas as atividades em seus dados.

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: Construindo uma Caixa de Entrada Inteligente na Nuvem

No mundo real, nossos sistemas não vivem isolados. Eles precisam interagir com parceiros, clientes e outros sistemas. O desafio de hoje no AWS re/Start foi exatamente sobre isso: como criar uma "caixa de entrada" de arquivos segura para um parceiro externo e, o mais importante, como ser notificado automaticamente sempre que um novo arquivo chegar.

Foi uma aula fantástica sobre segurança granular e automação orientada a eventos.

### A Jornada em 3 Atos

#### Ato 1: O Crachá de Visitante (Permissões Granulares com IAM)
* **A Dor:** Como dar acesso a um parceiro externo (no lab, uma agência de mídia) à sua conta AWS sem entregar as "chaves do reino"?
* **O Que Eu Fiz:** Analisei uma política do **IAM** que foi criada especificamente para o grupo de usuários da agência.
* **O "Aha!" Moment:** A política era uma obra de arte da segurança.
    * **Analogia:** Foi como criar um **"crachá de visitante"** super restrito. A regra dizia: "Este visitante pode entrar no prédio (listar os buckets S3), mas a chave do seu crachá só abre a porta da **'sala de marketing' (a 'pasta' `/images`)**. Ele pode colocar e tirar caixas (`Put/DeleteObject`) dessa sala, mas se tentar abrir qualquer outra porta, o alarme toca (`AccessDenied`)."
* **A Lição:** Ver o comando para alterar permissões falhar na prática me mostrou o poder do **Princípio do Menor Privilégio**. Você concede apenas o acesso mínimo necessário, nada mais.

#### Ato 2: O Sensor de Movimento (Notificações de Eventos do S3)
* **A Dor:** Como eu sei quando a agência enviou as novas fotos? Ficar atualizando a página do S3 o dia todo é improdutivo.
* **O Que Eu Fiz:** Configurei as **Notificações de Eventos** no bucket S3.
* **O "Aha!" Moment:**
    * **Analogia:** Foi como instalar um **"sensor de movimento"** na porta da "sala de marketing". Eu configurei o sensor para detectar duas ações: "porta abrindo para colocar algo dentro" (`ObjectCreated`) e "porta abrindo para tirar algo" (`ObjectRemoved`).
* **A Lição:** O S3 não é um armazenamento passivo. Ele é uma plataforma ativa que pode **iniciar fluxos de trabalho** com base em eventos.

#### Ato 3: O Alerta Imediato (Amazon SNS)
* **A Dor:** Ok, o sensor detectou movimento. Como ele me avisa?
* **O Que Eu Fiz:** Conectei o "sensor" do S3 a um **Tópico do Amazon SNS**.
* **O "Aha!" Moment:**
    * **Analogia:** Eu conectei o "sensor de movimento" a um **"sistema de alerta por pager" (o Tópico SNS)**. E eu "assinei" meu e-mail para receber as mensagens desse pager.
* **O Resultado:** O fluxo final foi perfeito. O fotógrafo fez o upload de um arquivo, o sensor do S3 detectou, o pager do SNS disparou, e meu celular vibrou com um e-mail em segundos. Tudo automático.

### A Grande Lição
Este lab foi uma masterclass em **arquitetura orientada a eventos** e **segurança**. Aprendi que a combinação de **IAM** (para permissões seguras), **S3** (para o gatilho) e **SNS** (para a notificação) cria um sistema desacoplado, seguro e incrivelmente eficiente.

Construir essa solução me fez sentir como um verdadeiro arquiteto. Eu não apenas configurei serviços, eu resolvi um problema de negócio real: como colaborar com um parceiro externo de forma segura e automatizada. Vê-lo funcionando de ponta a ponta foi a prova de que estou realmente começando a "pensar em nuvem".

#AWS #Cloud #S3 #IAM #SNS #Serverless #Automation #DevOps #AWSreStart