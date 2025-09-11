# <img src="https://api.iconify.design/logos/aws-s3.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab 02: Hospedando um Site Estático Serverless com Amazon S3

### O Cenário (A "User Story")

> **Como** um fotógrafo profissional, **EU QUERO** publicar meu portfólio online em um site estático (HTML, CSS, imagens), **PARA QUE** eu possa divulgar meu trabalho para o mundo de forma barata, confiável e sem me preocupar com o gerenciamento de servidores.

### A Dor que o Lab Resolve

Hospedar um site simples em um servidor tradicional (como fizemos com o EC2 no lab anterior) funciona, mas tem desvantagens para um site estático:

* **Custo:** Você paga pelo servidor 24/7, mesmo que ninguém o acesse.
* **Gerenciamento:** Você é responsável por patches de segurança, atualizações do SO, etc.
* **Escalabilidade:** Se seu site viralizar, o servidor pode não aguentar o tráfego e sair do ar.

Este laboratório mostra como o Amazon S3 resolve todas essas dores.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Criar um bucket S3.
* [ ] Fazer o upload de arquivos para um bucket.
* [ ] Habilitar a funcionalidade de hospedagem de site estático.
* [ ] Criar uma política de bucket para permitir o acesso público.
* [ ] Acessar seu site através de uma URL pública.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Passo 1: Preparando seus Arquivos
Antes de ir para a AWS, vamos criar os arquivos do nosso site. Crie dois arquivos simples no seu computador.

1.  **`index.html`**
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Meu Portfólio Incrível</title>
        <style>
            body { font-family: sans-serif; background-color: #232F3E; color: white; text-align: center; margin-top: 100px; }
            h1 { color: #FF9900; }
        </style>
    </head>
    <body>
        <h1>Bem-vindo ao Meu Site na Nuvem!</h1>
        <p>Este site está sendo hospedado de forma serverless no Amazon S3.</p>
    </body>
    </html>
    ```

2.  **`error.html`** (para páginas não encontradas)
    ```html
    <!DOCTYPE html>
    <html>
    <head>
        <title>Página Não Encontrada</title>
        <style>
            body { font-family: sans-serif; background-color: #232F3E; color: white; text-align: center; margin-top: 100px; }
            h1 { color: #D43F3A; }
        </style>
    </head>
    <body>
        <h1>Oops! Erro 404</h1>
        <p>A página que você procurou não foi encontrada.</p>
    </body>
    </html>
    ```

#### Passo 2: Criar o "Armazém" (O Bucket S3)
1.  No Console da AWS, navegue até o serviço **S3**.
2.  Clique em **Create bucket** (Criar bucket).
3.  **Bucket name** (Nome do bucket): Escolha um nome **globalmente único**. Ninguém mais no mundo pode ter um bucket com o mesmo nome. Ex: `meu-portfolio-incrivel-com-seu-nome-e-numeros`.
4.  **AWS Region** (Região da AWS): Escolha a região mais próxima de você, por exemplo, `sa-east-1` (São Paulo).
5.  **Block Public Access settings** (Configurações de bloqueio de acesso público): **Mantenha a caixa `Block all public access` marcada por enquanto.** Vamos liberar o acesso de forma controlada mais tarde.
    > **(COBIT - Governança):** Esta é a configuração padrão segura ("secure by default"). A AWS te força a tomar ações deliberadas para tornar algo público, o que é uma excelente prática de governança.
6.  Deixe as outras opções como padrão e clique em **Create bucket**.

#### Passo 3: Enviar os "Produtos" (Fazer Upload dos Arquivos)
1.  Clique no nome do bucket que você acabou de criar.
2.  Clique no botão **Upload**.
3.  Clique em **Add files** (Adicionar arquivos) e selecione os dois arquivos (`index.html` e `error.html`) que você criou.
4.  Clique em **Upload** no final da página.

#### Passo 4: Ativar o "Modo Vitrine" (Habilitar a Hospedagem de Site Estático)
1.  Com seu bucket selecionado, clique na aba **Properties** (Propriedades).
2.  Role até o final da página e, na seção **Static website hosting**, clique em **Edit** (Editar).
3.  Selecione **Enable** (Habilitar).
4.  Em **Index document** (Documento de índice), digite `index.html`.
5.  Em **Error document** (Documento de erro), digite `error.html`.
6.  Clique em **Save changes** (Salvar alterações).

Ao final, role novamente até a seção **Static website hosting**. Você verá uma nova informação: a **URL do seu site** (`Bucket website endpoint`). **Copie essa URL**, mas não a acesse ainda.

#### Passo 5: Criar a "Política de Acesso Público" (A Bucket Policy)
Se você tentar acessar a URL agora, receberá um erro `403 Forbidden`. Isso acontece porque, por padrão, ninguém no mundo pode ler os objetos no seu bucket. Precisamos criar uma política para permitir isso.

1.  Clique na aba **Permissions** (Permissões).
2.  Na seção **Bucket policy**, clique em **Edit** (Editar).
3.  No editor de política, cole o seguinte código JSON.
    > **`!!! warning "Atenção"`**
    > **Substitua `SEU-NOME-DE-BUCKET-AQUI` pelo nome exato do seu bucket!**
    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": "arn:aws:s3:::SEU-NOME-DE-BUCKET-AQUI/*"
            }
        ]
    }
    ```
    > **O que esta política diz?**
    > * `Effect: "Allow"`: Estamos permitindo uma ação.
    > * `Principal: "*"`: Para **qualquer pessoa** na internet.
    > * `Action: "s3:GetObject"`: A ação permitida é **ler/baixar objetos**.
    > * `Resource: ...`: Esta regra se aplica a **todos os objetos (`/*`)** dentro do seu bucket.
4.  Clique em **Save changes**.

#### Passo 6: Desativar o "Bloqueio de Acesso Público"
Agora que temos uma política explícita, podemos desativar o bloqueio geral.
1.  Ainda na aba **Permissions**, na seção **Block public access**, clique em **Edit**.
2.  Desmarque a caixa **Block *all* public access**.
3.  Clique em **Save changes** e confirme a alteração digitando `confirm` na caixa de diálogo.

---

### <img src="https://api.iconify.design/mdi/web-check.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Verificação
Agora sim! Pegue a URL do site que você copiou no Passo 4, cole em uma nova aba do navegador e pressione Enter. Seu site deve carregar perfeitamente!

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos (Passo OBRIGATÓRIO!)

1.  [ ] Na aba **Permissions** do seu bucket, delete a **Bucket Policy** e ative o **Block all public access** novamente.
2.  [ ] Vá para a aba **Objects** (Objetos), selecione todos os arquivos e clique em **Delete**. Siga as instruções para esvaziar o bucket.
3.  [ ] Volte para a lista de buckets e **Delete** o seu bucket.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" /> HACK PARA CERTIFICAÇÃO:** Para a prova, lembre-se:
> * **Amazon S3** pode ser usado para **hospedagem de sites estáticos**.
> * Para tornar um site público, você precisa de duas ações: **habilitar a hospedagem estática** E criar uma **política de bucket** que permita a ação `s3:GetObject` para o `Principal` `*`.
