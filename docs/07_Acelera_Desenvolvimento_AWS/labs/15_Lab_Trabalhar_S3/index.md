# <img src="https://api.iconify.design/logos/aws-s3.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab [Desafio]: Meu Primeiro "Guarda-Volumes" na Nuvem com Amazon S3

### O Cenário (A "User Story")

> **Como** um desenvolvedor, **EU QUERO** criar um repositório seguro para meus arquivos (um bucket S3), fazer o upload de uma imagem e torná-la acessível publicamente através de uma URL, **PARA QUE** eu possa compartilhar ativos de mídia do meu site ou aplicação.

### A Dor que o Lab Resolve

1.  **Armazenamento Inseguro:** Simplesmente jogar arquivos em um servidor os deixa vulneráveis. O S3 oferece um local seguro por padrão.
2.  **Acesso Complexo:** Compartilhar um arquivo de um servidor tradicional pode ser complicado. O S3 torna trivial gerar uma URL pública e segura para um objeto.

Este desafio te ensina o fluxo de trabalho fundamental para armazenar e compartilhar arquivos na nuvem.

### Objetivos de Aprendizado
Ao final deste desafio, você será capaz de:
* [ ] Criar um bucket S3 usando o Console da AWS.
* [ ] Fazer o upload de um objeto para o bucket.
* [ ] Entender e modificar as permissões de acesso público de um bucket e de um objeto.
* [ ] Acessar um objeto do S3 através da sua URL pública.
* [ ] Usar a AWS CLI para listar o conteúdo de um bucket.

### Duração
* Aproximadamente 45 minutos.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Plano de Ação do Arquiteto

#### Tarefa 1: Criando o "Guarda-Volumes" (O Bucket S3)

**Analogia:** Primeiro, vamos alugar nosso "armário" no guarda-volumes infinito da AWS.

1.  No Console da AWS, navegue até o serviço **S3**.
2.  Clique em **Criar bucket (Create bucket)**.
3.  **Configuração:**
    * **Nome do bucket (Bucket name):** Insira um nome **globalmente único**. (ex: `desafio-s3-renato-` seguido de números aleatórios).
    * **Região da AWS (AWS Region):** Mantenha a região padrão do seu laboratório.
    * **Configurações de acesso público (Public access settings):** Por padrão, a opção **Bloquear todo o acesso público (Block all public access)** vem marcada. **Mantenha-a assim por enquanto.** Vamos aprender a liberá-la de forma controlada.
4.  Clique em **Criar bucket**.

#### Tarefa 2: Colocando a "Caixa" no Armário (Upload de um Objeto)
1.  Na lista de buckets, clique no nome do bucket que você acabou de criar.
2.  Clique em **Carregar (Upload)**.
3.  Clique em **Adicionar arquivos (Add files)**. Selecione qualquer imagem simples do seu computador.
4.  Deixe todas as outras opções como padrão e clique em **Carregar (Upload)**.
5.  **Verificação:** Após o upload, clique no nome do objeto (sua imagem). Na página de detalhes, procure pelo **URL do objeto (Object URL)** e copie-o. Tente abri-lo em uma nova aba do navegador.
    > **O Resultado Esperado:** Você verá uma mensagem de erro em XML dizendo **`Access Denied`**. Isso é perfeito! Mostra que, por padrão, o S3 é **privado e seguro**.

#### Tarefa 3: Entregando a "Chave" (Tornando o Objeto Público)
**Analogia:** Agora, vamos dar a "chave" da nossa "caixa" (objeto) para o público, sem abrir o "armário" (bucket) inteiro.

1.  **Primeiro, libere o bloqueio no nível do Bucket:**
    * Volte para a página principal do seu bucket.
    * Vá para a aba **Permissões (Permissions)**.
    * Em **Bloquear acesso público (Block public access)**, clique em **Editar (Edit)**.
    * Desmarque a opção **Bloquear todo o acesso público (Block all public access)**.
    * Clique em **Salvar alterações (Save changes)** e confirme a ação.
2.  **Agora, torne o Objeto público:**
    * Volte para a lista de objetos dentro do seu bucket e selecione sua imagem.
    * Vá no menu **Ações (Actions) > Tornar público via ACL (Make public using ACL)**.
    * Confirme clicando em **Tornar público (Make public)**.
3.  **Verificação Final:** Tente abrir a **URL do objeto** no seu navegador novamente. **Agora, sua imagem deve aparecer!**

#### Tarefa 4: O Inventário via CLI
Vamos usar a linha de comando para verificar o conteúdo do nosso "armário".

1.  **Conecte-se ao `Host da CLI (CLI Host)`** usando o EC2 Instance Connect.
2.  **Configure a AWS CLI** com o comando `aws configure`, usando as credenciais do seu laboratório.
3.  **Execute o comando de listagem:**
    ```bash
    # Primeiro, liste todos os seus "armários" (buckets)
    aws s3 ls

    # Agora, liste o conteúdo do seu bucket específico (substitua pelo nome do seu bucket)
    aws s3 ls s3://<NOME_DO_SEU_BUCKET_S3>
    ```
    > **Verificação:** A saída do comando deve mostrar o nome do arquivo de imagem que você fez o upload.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você completou um dos fluxos de trabalho mais fundamentais da AWS. Você aprendeu a:
* Criar um repositório seguro no S3.
* Entender que o S3 é **privado por padrão**.
* Controlar o acesso público em dois níveis: no bucket e no objeto.
* Usar tanto o console quanto a CLI para interagir com seus dados.

Esta habilidade é a base para hospedar sites estáticos, gerenciar backups, criar data lakes e muito mais.

---

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: O Segredo da Segurança do S3

O desafio de hoje no AWS re/Start parecia simples: criar um "guarda-volumes" no Amazon S3, colocar uma imagem dentro e torná-la visível na internet. Parece fácil, certo? Mas a verdadeira lição não estava no "o quê", mas no "como".

### A Jornada em 2 Atos: O Cofre e as Duas Chaves

#### Ato 1: O Cofre Trancado (A Descoberta do "Privado por Padrão")
* **A Missão:** Criei meu bucket, fiz o upload da minha imagem, cliquei na URL do objeto e... `Access Denied`. Acesso Negado. Minha primeira reação foi: "O que eu fiz de errado?".
* **O "Aha!" Moment:** Depois de um minuto, a ficha caiu. Eu não fiz nada de errado. Na verdade, a AWS fez tudo **certo**.
    * **Analogia:** O S3 não é uma "pasta pública" na internet. Ele é um **"cofre de banco"**. Quando você coloca algo lá dentro, a configuração padrão é de **segurança máxima**. Nada entra e nada sai, a menos que você, o dono, dê uma permissão explícita.
* **A Lição:** Aquele `Access Denied` não foi um bug. Foi o **AWS Well-Architected Framework** em ação, me protegendo de mim mesmo e de expor dados acidentalmente. A segurança na AWS não é algo que você adiciona depois; ela vem "trancada de fábrica".

#### Ato 2: O Sistema de Duas Chaves (As Camadas de Permissão)
* **A Dor:** "Ok, entendi que é um cofre. Mas como eu abro a porta só um pouquinho, para que as pessoas possam ver esta única foto, sem deixar o cofre inteiro aberto?"
* **O Que Eu Fiz:** Descobri que o S3 tem um sistema de segurança de duas camadas, como um cofre que precisa de duas chaves para abrir.
* **O "Aha!" Moment:**
    * **Analogia:**
        1.  **Desativar o "Alarme Principal" do Prédio:** Primeiro, eu tive que ir nas configurações do **Bucket** e desligar a opção `Bloquear todo o acesso público`. Isso foi como dizer à segurança central do prédio: "Ok, estou ciente. Eu pretendo permitir alguma visitação controlada."
        2.  **Destrancar a Gaveta Específica:** Depois, eu tive que ir no **Objeto** (a imagem) e, usando uma ACL, "Torná-lo público". Isso foi como colocar um adesivo verde de "visitação permitida" em uma única gaveta dentro do cofre.
* **A Lição:** Esse processo de duas etapas é genial. Ele te força a ser **intencional** sobre o que você está tornando público, prevenindo erros catastróficos.

### A Grande Lição
O lab de hoje me ensinou a lição mais importante sobre a filosofia de segurança da AWS: **ela é segura por padrão**. Nosso trabalho como arquitetos não é apenas construir, mas entender os controles e tomar decisões conscientes para abrir o acesso apenas quando, e somente quando, for absolutamente necessário.

O que parecia um lab simples de upload de arquivos se tornou uma aula profunda sobre o **Princípio do Menor Privilégio**. É uma daquelas lições que eu sei que vou levar para todos os projetos da minha carreira.

#AWS #Cloud #S3 #Security #DevOps #AWSreStart #CloudPractitioner

