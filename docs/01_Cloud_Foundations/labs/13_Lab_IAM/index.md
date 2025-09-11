# <img src="https://api.iconify.design/mdi/account-key-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab 02: O Porteiro - Configurando um Ambiente Seguro com IAM

### O Cenário (A "User Story")

> **Como** o novo administrador da nuvem em uma empresa, **EU QUERO** parar de usar o usuário `root` (a "chave mestra") e criar um sistema de acesso seguro para mim e para minha equipe, **PARA QUE** possamos trabalhar na AWS de forma segura, auditável e seguindo as melhores práticas.

### A Dor que o Lab Resolve

Usar o usuário `root` para tarefas diárias é como andar com a chave mestra de um prédio pendurada no pescoço: é perigoso e desnecessário. Se essa credencial for comprometida, o dano é total e irreversível. Este laboratório resolve essa vulnerabilidade crítica, criando um ambiente de trabalho seguro.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Criar um grupo de administradores no IAM.
* [ ] Criar seu primeiro usuário IAM.
* [ ] Adicionar um usuário a um grupo.
* [ ] Habilitar a Autenticação Multi-Fator (MFA) para um usuário IAM.
* [ ] Fazer login na AWS usando um usuário IAM.

### Pré-requisitos
* Uma conta AWS. Para este lab, você precisará fazer login com seu **usuário `root`**.
* Um smartphone com um aplicativo autenticador instalado (ex: Google Authenticator, Microsoft Authenticator ou Authy).

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Passo 1: Criando o "Departamento de Administradores" (Grupo IAM)
> **(Framework: ITIL/COBIT - Controle de Acesso):** A melhor prática nunca é atribuir permissões diretamente a usuários, mas a grupos. Isso simplifica o gerenciamento e a auditoria.

1.  Faça login no Console da AWS com seu **usuário `root`**.
2.  No menu de serviços, navegue até **IAM**.
3.  No painel de navegação esquerdo, clique em **User groups** (Grupos de usuários).
4.  Clique em **Create group** (Criar grupo).
5.  Em **User group name** (Nome do grupo), digite `Administrators`.
6.  Na seção **Attach permissions policies** (Anexar políticas de permissões), procure por `AdministratorAccess`.
7.  Marque a caixa de seleção ao lado da política **`AdministratorAccess`**.
    > **`!!! note "Contexto"`**
    > Esta é uma "política gerenciada" pela AWS que concede permissão total a todos os serviços e recursos, efetivamente criando um "crachá de administrador".
8.  Role para baixo e clique em **Create group**.

#### Passo 2: Criando seu "Crachá de Funcionário" (Usuário IAM)
1.  No painel de navegação esquerdo, clique em **Users** (Usuários).
2.  Clique em **Add users** (Adicionar usuários).
3.  Em **User name** (Nome do usuário), digite um nome para seu usuário administrativo (ex: `admin-seu-nome`).
4.  Marque a caixa de seleção **Provide user access to the AWS Management Console** (Fornecer ao usuário acesso ao Console de Gerenciamento da AWS).
5.  Selecione a opção **I want to create an IAM user** (Quero criar um usuário do IAM).
6.  Em **Custom password** (Senha personalizada), crie uma senha forte.
7.  **Importante:** Desmarque a opção **Users must create a new password at next sign-in** (Os usuários devem criar uma nova senha no próximo login). Para este lab, vamos manter a senha que definimos.
8.  Clique em **Next** (Avançar).

#### Passo 3: Atribuindo o "Cargo" (Adicionando o Usuário ao Grupo)
1.  Na página **Set permissions** (Definir permissões), selecione **Add user to group** (Adicionar usuário ao grupo).
2.  Marque a caixa de seleção ao lado do grupo `Administrators` que criamos.
3.  Clique em **Next** (Avançar).
4.  Revise as informações e clique em **Create user** (Criar usuário).

#### Passo 4: Habilitando a "Super Fechadura" (MFA)
1.  Na lista de usuários, clique no nome do usuário `admin-seu-nome` que você acabou de criar.
2.  Clique na aba **Security credentials** (Credenciais de segurança).
3.  Na seção **Multi-factor authentication (MFA)**, clique em **Assign MFA device** (Atribuir dispositivo MFA).
4.  **Device name** (Nome do dispositivo): digite um nome, como `MeuCelular`.
5.  Selecione **Authenticator app** e clique em **Next**.
6.  Uma tela com um QR code aparecerá.
    * Abra seu aplicativo autenticador no celular (Google Authenticator, etc.).
    * Escaneie o QR code.
    * O aplicativo irá gerar um código de 6 dígitos. Digite **dois códigos consecutivos** nos campos `MFA code 1` e `MFA code 2`.
7.  Clique em **Add MFA device** (Adicionar dispositivo MFA).

---

### <img src="https://api.iconify.design/mdi/check-all.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Verificação

1.  No canto superior direito do Console da AWS, clique no nome da sua conta e **Sign out** (Sair).
2.  Na página de login, selecione **IAM user** (Usuário do IAM).
3.  O **Account ID** (ID da conta) pode já estar preenchido. Se não, você pode encontrá-lo no canto superior direito do console.
4.  Faça login com o **User name** (`admin-seu-nome`) e a **senha** que você criou.
5.  Você será solicitado a inserir o código MFA do seu aplicativo. Digite o código atual.

Se você conseguiu entrar, a missão foi um sucesso! Você agora está operando na AWS de forma segura, seguindo as melhores práticas da indústria.

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos

Manter usuários e grupos IAM não gera custo, mas é uma boa prática de segurança remover o que não está em uso.

* [ ] Faça login com seu usuário `root`.
* [ ] Navegue até o **IAM**.
* [ ] Em **Users**, selecione o usuário `admin-seu-nome` e delete-o.
* [ ] Em **User groups**, selecione o grupo `Administrators` e delete-o.