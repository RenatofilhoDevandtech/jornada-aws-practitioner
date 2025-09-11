# <img src="https://api.iconify.design/mdi/console-line.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Aprendendo a Falar "Shell": O Guia Prático de Comandos

Bem-vindo à linha de comando (CLI). Pense nela como aprender um novo idioma. Você não precisa saber todas as palavras do dicionário para ser fluente; você só precisa dominar as frases mais comuns e ter o dicionário por perto para consulta. Este guia é o seu dicionário de bolso e livro de frases.

---

### <img src="https://api.iconify.design/mdi/syllabary-katakana.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Gramática do Shell: Entendendo a Sintaxe

Quase todo comando no Linux segue a lógica: `comando -opção(ões) argumento(s)`

* **Comando:** O verbo, a ação (ex: `cp` - copiar).
* **Opção:** O adjetivo, como fazer a ação (ex: `-r` - recursivamente).
* **Argumento:** O substantivo, o alvo da ação (ex: `arquivo.txt`).

---

### <img src="https://api.iconify.design/mdi/heart-pulse.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Kit de Sobrevivência: Os 10 Comandos que Você Usará 90% do Tempo

Se você só puder memorizar alguns comandos, que sejam estes.

| Comando | O que faz? (A Dor que Resolve) | Exemplo de Uso |
| :--- | :--- | :--- |
| **`ls`** | **L**i**s**ta o conteúdo de um diretório. (Abre a gaveta para ver o que tem dentro). | `ls -lah` |
| **`cd`** | **C**hange **D**irectory. (Anda de uma sala para outra). | `cd /var/log` |
| **`pwd`** | **P**rint **W**orking **D**irectory. (Pergunta "Onde estou agora?"). | `pwd` |
| **`cat`** | Mostra o conteúdo de um arquivo na tela. (Abre um livro e lê o texto). | `cat arquivo.txt` |
| **`rm`** | **R**e**m**ove (apaga) um arquivo ou diretório. (**CUIDADO!** Não tem lixeira). | `rm arquivo_temporario.txt` |
| **`cp`** | **C**o**p**ia um arquivo ou diretório. | `cp relatorio.docx relatorio_backup.docx`|
| **`mv`** | **M**o**v**e ou renomeia um arquivo ou diretório. | `mv foto.jpg /home/usuario/Imagens/` |
| **`sudo`** | **S**uper**u**ser **Do**. (Pede a chave do "gerente" para executar um comando com privilégios de administrador). | `sudo apt update` |
| **`man`** | **Man**ual. (Abre o manual de instruções de qualquer comando). | `man ls` |
| **`clear`**| Limpa a tela do terminal. (Organiza sua mesa de trabalho). | `clear` |

---

### <img src="https://api.iconify.design/mdi/book-plus-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Gerenciando seu Inventário: Pacotes e Programas

Todo servidor precisa instalar e atualizar softwares. O comando que você usa depende da "família" da sua distro Linux. No ambiente AWS, você usará `yum` (ou `dnf`) para Amazon Linux e `apt` para Ubuntu.

!!! tab "Família Red Hat (Amazon Linux, RHEL, CentOS)"
    O comando principal é `yum` (ou o mais moderno `dnf`).

    * `sudo yum install httpd`: Instala o servidor web Apache.
    * `sudo yum update`: Atualiza todos os pacotes do sistema.
    * `sudo yum remove httpd`: Remove o servidor web Apache.
    * `yum search httpd`: Procura por pacotes relacionados ao Apache.
    * `yum list installed`: Lista todos os pacotes já instalados.
    * `sudo yum clean all`: Limpa os arquivos de cache para economizar espaço.

!!! tab "Família Debian (Ubuntu, Debian)"
    O comando principal é `apt`.

    * `sudo apt update`: **(Passo 1 obrigatório!)** Atualiza a lista de pacotes disponíveis.
    * `sudo apt upgrade`: **(Passo 2)** Atualiza os pacotes instalados para suas novas versões.
    * `sudo apt install apache2`: Instala o servidor web Apache.
    * `sudo apt remove apache2`: Remove o servidor web Apache.
    * `sudo apt autoremove`: Remove pacotes que foram instalados como dependência e não são mais necessários.
    * `sudo apt autoclean`: Limpa pacotes antigos do cache.

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** A principal dor que esses comandos resolvem é o **gerenciamento de dependências**. Se o programa "A" precisa do programa "B" para funcionar, ao instalar "A", o `apt` ou `yum` automaticamente instala "B" para você.

---

### <img src="https://api.iconify.design/mdi/stethoscope.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Diagnosticando o Paciente: Comandos de Sistema e Hardware

Esses comandos são o "check-up" do seu servidor.

* **`df -h`**: Mostra o espaço em **d**isco **l**ivre (disk free) de forma **h**umana (GB, MB).
    * **Dor que Resolve:** "Meu disco (volume EBS) está cheio?"
* **`free -h`**: Mostra a memória **RAM** livre e usada de forma **h**umana.
    * **Dor que Resolve:** "Meu servidor está lento por falta de memória?"
* **`uname -a`**: Mostra informações detalhadas sobre o Kernel do Linux.
* **`lspci` / `lsusb`**: Listam os dispositivos conectados nos barramentos PCI e USB.
* **`cat /proc/cpuinfo` e `cat /proc/meminfo`**: Uma forma alternativa e mais detalhada de ver informações da CPU e Memória.

---

### <img src="https://api.iconify.design/mdi/electric-switch.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Controlando a Central Elétrica: Processos e Serviços

* **`systemctl status httpd`**: Mostra o **status** de um serviço (ex: o servidor web Apache). Está rodando? Deu erro?
* **`sudo systemctl start httpd`**: **Inicia** um serviço.
* **`sudo systemctl stop httpd`**: **Para** um serviço.
* **`sudo systemctl restart httpd`**: **Reinicia** um serviço.
* **`sudo systemctl enable httpd`**: **Habilita** um serviço para iniciar automaticamente com o boot do servidor.
* **`sudo systemctl disable httpd`**: **Desabilita** um serviço de iniciar no boot.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação:** O `systemd` (e o comando `systemctl`) é o padrão moderno para gerenciar serviços no Linux. Entender o ciclo `start`, `stop`, `restart`, `status`, `enable`, `disable` é fundamental.

---

### <img src="https://api.iconify.design/mdi/file-find-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Mestre dos Arquivos: Ferramentas de Texto e Busca

* **`grep "palavra" arquivo.txt`**: O **"Ctrl+F com superpoderes"**. Procura por uma palavra ou padrão dentro de arquivos.
    * **Dor que Resolve:** "Preciso encontrar a linha exata que contém a palavra 'ERROR' em um arquivo de log de 10GB."
* **`tail -n 20 /var/log/messages`**: Mostra as últimas 20 linhas de um arquivo.
    * **Hack:** `tail -f /var/log/messages`: O `-f` (follow) mostra o final do arquivo **e continua exibindo novas linhas em tempo real**. É a ferramenta essencial para monitorar logs.
* **`touch`**: Além de criar arquivos vazios, pode ser usado para atualizar a data de modificação.

---

### <img src="https://api.iconify.design/mdi/account-key-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Porteiro e o Carteiro: Usuários e Permissões

* **`adduser novousuario`**: Cria um novo usuário de forma interativa.
* **`passwd novousuario`**: Altera a senha de um usuário.
* **`userdel -r novousuario`**: Remove um usuário e seu diretório home.
* **`addgroup novogrupo`** e **`groupdel novogrupo`**: Adicionam e removem grupos.

---

### <img src="https://api.iconify.design/mdi/wan.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conectando-se ao Mundo: Comandos de Rede

* **`ping google.com`**: Testa a conectividade com um destino.
* **`ifconfig` ou `ip addr`**: Mostra a configuração de rede, incluindo o seu endereço IP.
* **`netstat -tulpn`**: Mostra as portas de rede que estão "escutando" por conexões.
    * **Dor que Resolve:** "Meu servidor web está realmente rodando na porta 80?"
* **`ssh usuario@ip_do_servidor`**: O comando para **acesso remoto seguro**. É como você vai se conectar à sua instância EC2.

---

### <img src="https://api.iconify.design/mdi/archive-arrow-down-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Fazendo as Malas: Compactação de Arquivos

* **Comando:** `tar`
* **Dor que Resolve:** A necessidade de juntar múltiplos arquivos e pastas em um único pacote para backup ou transferência.
* **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="16" /> Hack para lembrar as opções:**
    * Para **C**riar um arquivo: `tar -c**z**f arquivo.tar.gz /pasta/` (**C**reate **Z**ipped **F**ile)
    * Para **E**xtrair um arquivo: `tar -x**v**f arquivo.tar.gz` (**E**xtract **V**erbosely from **F**ile)

---

### <img src="https://api.iconify.design/logos/aws-ec2.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Contexto AWS: Por que Tudo Isso Importa no EC2?

No dia a dia com a AWS, você usará esses comandos constantemente. Imagine que você acabou de criar uma instância EC2 com Amazon Linux:

1.  A primeira coisa que você faz é se conectar a ela com **`ssh ec2-user@ip_publico`**.
2.  Você se torna o superusuário com **`sudo su`** para ter privilégios.
3.  Você atualiza o sistema com **`sudo yum update -y`**.
4.  Você instala um servidor web com **`sudo yum install -y httpd`**.
5.  Você inicia o servidor e o habilita no boot com **`sudo systemctl start httpd`** e **`sudo systemctl enable httpd`**.
6.  Você navega até a pasta do site com **`cd /var/www/html`**.
7.  Você cria uma página de teste com **`echo "<h1>Olá, Mundo da AWS!</h1>" > index.html`**.
8.  Se algo der errado, você verifica os logs com **`tail -f /var/log/httpd/error_log`**.

Esses comandos não são apenas teoria; são os tijolos com os quais você constrói e gerencia suas soluções na nuvem todos os dias.

---