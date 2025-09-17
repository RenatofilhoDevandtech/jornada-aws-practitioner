# <img src="https://api.iconify.design/logos/aws-s3.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Site Automatizado - Criando um Site Estático no S3 com a AWS CLI

### O Cenário (A "User Story")

> **Como** dono de uma cafeteria, **EU QUERO** publicar o site da minha loja na AWS e ter uma forma fácil de atualizá-lo, **PARA QUE** eu possa ter uma presença online profissional, escalável e de baixo custo.

### A Dor que o Lab Resolve

1.  **Complexidade:** Hospedar um site simples não deveria exigir o gerenciamento de um servidor complexo (EC2).
2.  **Processo Manual:** Atualizar o site manualmente via console é lento e propenso a erros. Um clique errado pode tirar o site do ar.

Este laboratório mostra como o S3 resolve a complexidade e como a AWS CLI resolve o processo manual, criando um fluxo de trabalho de publicação automatizado.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Criar e configurar um bucket S3 para hospedagem de site estático via CLI.
* [ ] Criar um usuário IAM dedicado para gerenciar o site.
* [ ] Fazer o upload e definir permissões para os arquivos do site via CLI.
* [ ] Criar um script de shell (`.sh`) para automatizar futuras atualizações.

### Duração
* Aproximadamente 45 minutos.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Acessando o "Posto de Controle" (Conectar via Session Manager)
Nossa primeira tarefa é acessar o servidor Linux de onde executaremos nossos comandos.

1.  No painel do seu laboratório, clique em **Detalhes > Mostrar (Details > Show)**.
2.  Copie o valor de `InstanceSessionUrl` e cole em uma nova aba do navegador.
3.  Você terá um terminal conectado à instância. Execute os seguintes comandos para mudar para o usuário padrão do EC2:
    ```bash
    sudo su -l ec2-user
    pwd
    ```

#### Tarefa 2: Configurando as Credenciais (`aws configure`)
A instância Amazon Linux já vem com a AWS CLI pré-instalada. Precisamos apenas configurá-la com nossas credenciais.

1.  Execute o comando de configuração:
    ```bash
    aws configure
    ```
2.  No painel `Detalhes (Details)` do seu laboratório, copie e cole os valores:
    * **AWS Access Key ID:** O valor `AccessKey (Chave de Acesso)`.
    * **AWS Secret Access Key:** O valor `SecretKey (Chave de Acesso Secreta)`.
    * **Default region name:** `us-west-2`
    * **Default output format:** `json`

#### Tarefa 3: Criando o "Terreno" (O Bucket S3)
Vamos criar o bucket que hospedará nosso site. Lembre-se, o nome deve ser globalmente único.

1.  Execute o comando abaixo, **substituindo `<SEU-NOME-UNICO-BUCKET>`** por um nome único (ex: `cafe-renato-2025`).
    ```bash
    aws s3api create-bucket \
        --bucket <SEU-NOME-UNICO-BUCKET> \
        --region us-west-2 \
        --create-bucket-configuration LocationConstraint=us-west-2
    ```
    > **O "Porquê":** Usamos `s3api` para comandos mais específicos. Como estamos criando o bucket em uma região diferente de `us-east-1`, é necessário especificar o `LocationConstraint` para que o S3 saiba onde criar o bucket fisicamente.

#### Tarefa 4: Criando o "Zelador" (O Usuário IAM)
**Melhor Prática:** Não usamos nossas credenciais de administrador para tarefas do dia a dia. Vamos criar um usuário dedicado apenas para gerenciar o S3.

1.  Crie o usuário:
    ```bash
    aws iam create-user --user-name awsS3user
    ```
2.  Crie um perfil de login para que ele possa acessar o console (opcional, mas parte do lab):
    ```bash
    aws iam create-login-profile --user-name awsS3user --password "Training123!"
    ```
3.  Para anexar a permissão correta, primeiro precisamos encontrar o ARN da política gerenciada `AmazonS3FullAccess`:
    ```bash
    aws iam list-policies --query "Policies[?PolicyName=='AmazonS3FullAccess'].Arn" --output text
    ```
4.  Copie o ARN da saída do comando anterior e use-o para anexar a `política (policy)` ao usuário:
    ```bash
    aws iam attach-user-policy --policy-arn <ARN_DA_POLITICA_S3_AQUI> --user-name awsS3user
    ```

#### Tarefa 5: Ajustando as Permissões do Bucket (Via Console)
Para um site público, precisamos desabilitar o bloqueio de acesso público.

1.  No Console da AWS, navegue até o serviço **S3**.
2.  Encontre e clique no seu bucket.
3.  Vá para a aba **Permissões (Permissions)**.
4.  Em **Bloquear acesso público (Block public access)**, clique em **Editar (Edit)**.
5.  Desmarque a opção **Bloquear todo o acesso público (Block all public access)** e clique em **Salvar alterações (Save changes)**. Confirme a ação.

#### Tarefa 6: Descompactando o Conteúdo do Site
Os arquivos do nosso site já estão na instância. Vamos descompactá-los.
```bash
cd ~/sysops-activity-files
tar xvzf static-website-v2.tar.gz
cd static-website
ls
```
> Você deve ver os arquivos do site, incluindo `index.html`.

#### Tarefa 7: Publicando o Site (Upload para o S3)
Agora, vamos enviar nosso site para a nuvem e torná-lo público.

1.  **Configure o bucket para ser um site**, definindo o documento de índice:
    ```bash
    aws s3 website s3://<SEU-NOME-UNICO-BUCKET>/ --index-document index.html
    ```
2.  **Copie os arquivos e os torne públicos:**
    ```bash
    aws s3 cp ~/sysops-activity-files/static-website/ s3://<SEU-NOME-UNICO-BUCKET>/ --recursive --acl public-read
    ```
    > **O "Porquê":** O `--recursive` copia todos os arquivos e pastas. O `--acl public-read` define a permissão para que o mundo possa ler os arquivos (ver o site).
3.  **Verificação Final:** No console do **S3**, encontre seu bucket, clique na aba **Propriedades (Properties)** e, no final, copie o **Endpoint do site estático**. Cole em um navegador. **Seu site está no ar!**

---

#### Tarefa 8: Automatizando as Atualizações (O Script Mágico)
**A Dor:** Se você mudar um arquivo, precisa digitar aquele comando `aws s3 cp` longo de novo. Vamos automatizar isso.

1.  **Crie o arquivo de script:**
    ```bash
    cd ~
    vi update-website.sh
    ```
2.  Pressione `i` para entrar no modo de inserção e cole as linhas abaixo (substituindo pelo nome do seu bucket):
    ```bash
    #!/bin/bash
    aws s3 sync ~/sysops-activity-files/static-website/ s3://<SEU-NOME-UNICO-BUCKET>/ --acl public-read
    ```
3.  Pressione `Esc`, depois digite `:wq` e pressione `Enter` para salvar e sair.

    > **`!!! tip "Otimização com `sync`"`**
    > Trocamos o `cp` (copiar) pelo `sync` (sincronizar). O `sync` é mais inteligente: ele só faz o upload dos arquivos que **realmente mudaram**, economizando tempo e transferência de dados.
4.  **Torne o script executável:**
    ```bash
    chmod +x update-website.sh
    ```
5.  **Teste a Automação:**
    * Edite o arquivo `index.html` localmente (`vi ~/sysops-activity-files/static-website/index.html`). Mude uma cor ou um texto.
    * Agora, em vez de digitar o comando longo, apenas execute seu script:
      ```bash
      ./update-website.sh
      ```
    * Atualize o site no navegador. Suas alterações estarão lá!

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você não apenas publicou um site estático, mas também criou uma ferramenta de automação (`update-website.sh`) que simplifica drasticamente o processo de atualização. Esta é a essência do SysOps na nuvem: transformar tarefas manuais e repetitivas em processos automatizados e confiáveis.

---

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: O Nascimento do Meu Primeiro Site Automatizado

Sempre que eu pensava em colocar um site no ar, a imagem que vinha à mente era a de um servidor complexo, com um sistema operacional para gerenciar, patches de segurança para aplicar... parecia um exagero para um site simples, como um portfólio.

Hoje, no lab do AWS re/Start, eu descobri que existe um caminho muito mais inteligente e moderno. E o mais legal: aprendi a automatizar todo o processo de atualização.

### A Primeira Descoberta: A Casa Sem Servidor

A primeira grande sacada foi usar o **Amazon S3** para hospedar o site.

* **A Dor:** Usar um servidor inteiro (um EC2) para servir arquivos HTML simples é como alugar um restaurante de 5 estrelas só para vender limonada. É um desperdício de recursos e de dinheiro.
* **A Solução:** O S3 pode servir arquivos estáticos diretamente para a web. É a sua **"barraca de limonada"**: super barata, infinitamente escalável (aguenta milhões de "clientes" sem piscar) e você não precisa gerenciar nenhuma cozinha (servidor).

### A Segunda Descoberta: O "Zelador" Dedicado

Para interagir com o S3 via linha de comando, eu precisava de credenciais. A primeira tentação seria usar minhas chaves de administrador.

* **A Dor:** Usar a "chave mestra do prédio" para uma tarefa simples é um risco de segurança enorme.
* **A Solução:** Criei um **usuário IAM** dedicado, o `awsS3user`. Ele é o **"zelador do site"**. Ele tem uma chave que **só abre a porta do S3** e mais nada. Isso é o Princípio do Menor Privilégio na prática, e me deu uma tranquilidade imensa.

### A Terceira (e Melhor) Descoberta: O Robô de Publicação

A parte mais incrível do lab foi a automação.

* **A Dor:** Fazer o upload de arquivos alterados um por um, ou digitar aquele comando `aws s3 cp ...` longo toda vez, é tedioso e uma receita para o erro.
* **A Solução:** Eu criei um pequeno **"robô de publicação"** (`update-website.sh`).
    * Primeiro, usei o comando `aws s3 cp --recursive` para enviar tudo de uma vez. Já foi um grande avanço.
    * Mas o verdadeiro "momento a-ha!" foi quando o desafio me apresentou ao comando `aws s3 sync`.
* **O Resultado Incrível:** O `sync` é muito mais inteligente que o `cp`. Ele compara o que está na minha máquina com o que está no S3 e faz o upload **apenas dos arquivos que realmente mudaram**.

Agora, para atualizar meu site, eu só preciso rodar um único comando no meu terminal: `./update-website.sh`. O "robô" faz todo o trabalho pesado para mim, de forma rápida e eficiente.

### A Grande Lição

Este laboratório conectou três pilares da nuvem de forma brilhante: **Armazenamento (S3)**, **Segurança (IAM)** e **Automação (CLI)**, tudo para resolver um problema do mundo real.

Ter um script simples, de um comando, para atualizar meu portfólio me deu uma sensação de poder e controle. É um pequeno passo, mas é uma peça real de automação que eu construí. Isso torna a ideia de gerenciar sistemas muito maiores bem menos intimidante.

#AWS #Cloud #S3 #Automation #CLI #DevOps #AWSreStart #CarreiraEmTI #DevOps