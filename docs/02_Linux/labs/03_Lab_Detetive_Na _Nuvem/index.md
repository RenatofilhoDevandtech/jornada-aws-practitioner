# <img src="https://api.iconify.design/mdi/linux.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab 01: A Sala de Máquinas - Conectando via SSH e Usando Man Pages

### O Cenário (A "User Story")

> **Como** um novo administrador de sistemas na nuvem, **EU QUERO** aprender a me conectar de forma segura a um servidor Linux e a encontrar a documentação oficial dos comandos, **PARA QUE** eu possa gerenciar minhas instâncias EC2 e aprender de forma autônoma.

### A Dor que o Lab Resolve

Quando você lança uma instância EC2 Linux, você não recebe uma tela gráfica bonita. Você recebe uma "tela preta com um cursor piscando". Isso pode ser intimidante. Este laboratório resolve duas dores:
1.  **O Medo da Tela Preta:** Mostra o método padrão e seguro para "entrar" e controlar seu servidor.
2.  **A Sobrecarga de Comandos:** O Linux tem milhares de comandos. As `man pages` são sua biblioteca interna, a fonte da verdade para aprender o que cada comando faz.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Conectar-se a uma instância EC2 Linux usando SSH.
* [ ] Entender a finalidade do comando `man`.
* [ ] Navegar e pesquisar dentro de uma `man page`.

### Pré-requisitos
* Uma instância EC2 com o sistema operacional **Amazon Linux** já em execução.
* O **Endereço IP Público** da sua instância.
* O **Par de Chaves** (`.pem` para Mac/Linux ou `.ppk` para Windows) que foi associado à instância no momento do lançamento.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: A Conexão Segura (Acessando a Instância via SSH)

**SSH (Secure Shell)** é o protocolo padrão da indústria para gerenciar servidores remotamente de forma criptografada.
* **Analogia:** Pense no SSH como um **"túnel de acesso seguro e blindado"** e no seu Par de Chaves como a **"chave criptografada única"** que abre a porta da sua sala de máquinas (sua instância).

O processo de conexão varia um pouco dependendo do seu sistema operacional.

!!! tab "macOS / Linux"
    1.  **Abra o Terminal:** Esta é a sua ferramenta de linha de comando nativa.
    2.  **Navegue até a Chave:** Use o comando `cd` para ir até a pasta onde você salvou seu arquivo `.pem`. Geralmente é a pasta `Downloads`.
        ```bash
        cd ~/Downloads
        ```
    3.  **Ajuste as Permissões da Chave (Passo CRUCIAL):** Por segurança, o SSH se recusa a usar uma chave que seja "publicamente visível". Este comando torna sua chave privada legível apenas por você.
        ```bash
        chmod 400 seu-arquivo-de-chave.pem
        ```
        > **`!!! note "Contexto de Segurança"`**
        > `chmod 400` aplica permissões de "somente leitura" apenas para o seu usuário. É uma medida **preventiva** para proteger suas credenciais.
    4.  **Conecte-se:** Use o comando `ssh`. Substitua `seu-arquivo-de-chave.pem` e `<public-ip>` pelos seus valores. O nome de usuário padrão para AMIs Amazon Linux é `ec2-user`.
        ```bash
        ssh -i seu-arquivo-de-chave.pem ec2-user@<public-ip>
        ```
    5.  Na primeira conexão, ele perguntará se você confia no host. Digite `yes` e pressione Enter.

!!! tab "Windows"
    1.  **Baixe as Ferramentas:** Você precisará de duas ferramentas gratuitas:
        * **PuTTY:** O seu cliente SSH. (putty.exe)
        * **PuTTYgen:** A ferramenta para converter a chave. (puttygen.exe)
        Você pode baixá-las no [site oficial do PuTTY](https://www.putty.org/).
    2.  **Converta a Chave:**
        * Abra o **PuTTYgen**.
        * Clique em **Load** e encontre seu arquivo `.pem`. (Você pode precisar mudar o filtro de arquivos para "All Files (*.*)").
        * Após carregar, clique em **Save private key**. Salve-o com o nome `minha-chave.ppk`.
    3.  **Configure a Conexão no PuTTY:**
        * Abra o **PuTTY**.
        * Em **Host Name (or IP address)**, digite `ec2-user@<public-ip>`. Substitua `<public-ip>` pelo IP da sua instância.
        * No menu à esquerda, navegue para **Connection > SSH > Auth > Credentials**.
        * Em **Private key file for authentication**, clique em **Browse...** e selecione o arquivo `minha-chave.ppk` que você acabou de salvar.
    4.  **Conecte-se:** Clique em **Open**. Na primeira vez, ele mostrará um alerta de segurança. Clique em **Accept**.

**Verificação:** Se tudo deu certo, você verá a tela de boas-vindas do Amazon Linux. Você está dentro da sua sala de máquinas!

#### Tarefa 2: A Biblioteca Interna (Explorando as `man` pages)
1.  **O Comando Básico:** Para ler o manual de qualquer comando, basta digitar `man` seguido do nome do comando. Para começar, vamos ler o manual do próprio manual:
    ```bash
    man man
    ```
2.  **Navegação:** Use as **setas para cima e para baixo** para rolar. Pressione a tecla **`q`** para sair.
3.  **Anatomia de uma `man page`:** Observe as seções padrão que te ajudam a entender o comando:
    * **NAME:** O nome do comando e uma descrição de uma linha.
    * **SYNOPSIS:** Mostra a sintaxe do comando e suas opções.
    * **DESCRIPTION:** A explicação detalhada do que o comando faz.
    * **EXAMPLES:** Exemplos práticos de uso.

> **`!!! tip "Dica de Especialista: Como Pesquisar"`**
> Dentro de uma `man page`, você não precisa rolar para sempre. Use a tecla **`/`** para pesquisar!
> 1.  Digite **`/`** seguido da palavra que você quer encontrar (ex: `/size`).
> 2.  Pressione `Enter`. As ocorrências serão destacadas.
> 3.  Pressione a tecla **`n`** (de *next*) para pular para a próxima ocorrência.

**Desafio:** Agora, use o que você aprendeu. Abra o manual do comando `ls` (`man ls`) e pesquise pela opção que ordena os arquivos por tamanho.

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos
* [ ] Se você criou a instância EC2 manualmente para este lab, lembre-se de **terminá-la** para evitar custos.

### <img src="https://api.iconify.design/mdi/comment-quote-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você dominou as duas habilidades mais fundamentais de um administrador Linux: conectar-se de forma segura a um servidor e encontrar ajuda dentro dele. Você agora tem a chave e o manual da sua sala de máquinas, pronto para explorar o vasto mundo da linha de comando.