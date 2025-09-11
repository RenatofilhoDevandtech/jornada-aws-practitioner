# <img src="https://api.iconify.design/mdi/script-text-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Livro de Receitas do Mestre: Introdução a Scripts e Variáveis

Até agora, aprendemos a dar ordens diretas ao nosso "Maître" (o Shell). Fomos da gramática básica a comandos avançados. Agora, vamos aprender a escrever um **"Livro de Receitas"** completo, para que o nosso "Robô de Cozinha" (o sistema) possa executar tarefas complexas de forma automática. Isso é o **Scripting**.

Mas antes de escrever a receita, precisamos entender dois conceitos fundamentais: como guardar os ingredientes (**Variáveis**) e como criar apelidos para nossas técnicas culinárias (**Aliases**).

---

### <img src="https://api.iconify.design/mdi/package-variant-closed.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> As Gavetas de Memória (Variáveis)

Uma variável é simplesmente um nome que você dá a um pedaço de informação para poder usá-lo mais tarde.

* **Analogia:** Pense em variáveis como **"gavetas etiquetadas"** na sua cozinha. Em vez de deixar o sal espalhado, você o coloca em uma gaveta com a etiqueta `SAL`.
* **A Dor que Resolve:** Evitar a repetição. Se você precisa usar o mesmo endereço de e-mail 10 vezes em um script, é melhor guardá-lo em uma variável. Se o e-mail mudar, você só precisa alterá-lo em um único lugar.

#### <img src="https://api.iconify.design/mdi/label-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Como Criar e Usar Variáveis

1.  **Para criar (guardar na gaveta):** `NOME_DA_GAVETA="Conteúdo"`
    ```bash
    EMAIL_ADMIN="admin@meuservidor.com"
    ```
    > **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK DE MESTRE:** A regra de ouro do Bash: **NÃO PODE HAVER ESPAÇOS** antes ou depois do sinal de igual (`=`). `VAR = "valor"` dará erro!

2.  **Para usar (abrir a gaveta):** Use o cifrão `$` na frente do nome.
    ```bash
    echo "Enviando relatório para: $EMAIL_ADMIN"
    ```

#### <img src="https://api.iconify.design/mdi/earth.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Variáveis de Ambiente: As Gavetas que Já Vêm com a Cozinha
Seu ambiente Shell já vem com algumas "gavetas" pré-definidas e super importantes. Elas são, por convenção, escritas em MAIÚSCULAS.

* `$HOME`: O caminho para o seu diretório home (sua "sala de estudos pessoal").
* `$USER`: O seu nome de usuário.
* `$PATH`: Uma lista de "caixas de ferramentas" (diretórios) onde o shell procura por comandos.
* **Comando para ver todas:** `env` ou `printenv`
    * Este comando lista todas as variáveis de ambiente ativas na sua sessão.

---

### <img src="https://api.iconify.design/mdi/flash-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Os Atalhos do Chef (Aliases)

Um alias é um "apelido" que você cria para um comando ou uma sequência de comandos que você usa com frequência.

* **Analogia:** Em vez de dizer "Por favor, me traga a Faca do Chef de Aço Damasco com Cabo de Madeira de Nogueira", você simplesmente diz **"Faca Chef"**. É um atalho.
* **A Dor que Resolve:** Digitar comandos longos e repetitivos. `ls -lah`, `sudo systemctl restart httpd`, etc.

#### <img src="https://api.iconify.design/mdi/playlist-edit.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Como Criar um Alias e Torná-lo Permanente

1.  **Criar um alias temporário (só para a sessão atual):**
    ```bash
    alias ll='ls -lah'
    ```
    Agora, sempre que você digitar `ll`, o shell executará `ls -lah`.

2.  **Torná-lo Permanente (O Segredo):** Para que seus apelidos sobrevivam a um reboot, você precisa escrevê-los no seu "caderno de anotações pessoal", o arquivo `~/.bashrc`.
    * **Analogia:** O `~/.bashrc` é um arquivo de configuração que é lido e executado toda vez que você inicia uma nova sessão no terminal.

* **<img src="https://api.iconify.design/logos/aws-ec2.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Cenário Prático na AWS:** Vamos criar um alias `atualizar` para rodar os comandos de atualização do sistema em uma instância Amazon Linux.
    1.  **Abra o arquivo de configuração com o nano:**
        ```bash
        nano ~/.bashrc
        ```
    2.  **Vá até o final do arquivo** e adicione a seguinte linha:
        ```bash
        # Meu alias para atualizar o sistema
        alias atualizar='sudo yum update -y'
        ```
    3.  **Salve e saia** (`Ctrl+O`, `Enter`, `Ctrl+X`).
    4.  **"Recarregue" a configuração** para que o alias funcione imediatamente:
        ```bash
        source ~/.bashrc
        ```
    Agora, basta digitar `atualizar` para que o sistema seja completamente atualizado.

> **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação:** Entender o propósito do arquivo `~/.bashrc` (personalização do ambiente do usuário) e o conceito de variáveis de ambiente como `$PATH` e `$HOME` são tópicos importantes para a certificação Linux Essentials.

---

### <img src="https://api.iconify.design/mdi/file-code-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Escrevendo sua Primeira Receita (Script)

Um script shell é simplesmente um arquivo de texto contendo uma sequência de comandos que o shell executa na ordem em que aparecem.

#### <img src="https://api.iconify.design/mdi/exclamation-thick.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> O Ingrediente Secreto: O "Shebang"
Todo bom script começa com uma linha mágica chamada **Shebang**: `#!/bin/bash`.

* **Analogia:** É a primeira linha de qualquer receita, que diz: **"Esta receita deve ser preparada usando as técnicas da Culinária Francesa (`bash`)"**.
* **O que faz?** Ele diz ao sistema operacional para usar o programa `bash` para interpretar os comandos deste arquivo. Sem ele, o sistema pode não saber como executar seu script.

#### <img src="https://api.iconify.design/mdi/check-decagram-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> A Permissão de Execução
Por padrão, um novo arquivo de texto não tem permissão para ser executado. Você precisa "ativá-lo".

* **Analogia:** É dar a **"autorização sanitária"** para que a receita possa ser executada na cozinha.
* **O Comando:** `chmod +x nome_do_script.sh`

**<img src="https://api.iconify.design/logos/aws-ec2.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Cenário Prático na AWS:** Vamos criar nosso primeiro script.

1.  **Crie o arquivo:** `nano ola_mundo.sh`
2.  **Escreva a receita (o código):**
    ```bash
    #!/bin/bash
    
    # Este é um comentário. Ele é ignorado pelo shell.
    echo "Olá, Mundo! Meu primeiro script está rodando em uma instância EC2."
    ```
3.  **Salve e saia** (`Ctrl+O`, `Enter`, `Ctrl+X`).
4.  **Dê a permissão de execução:**
    ```bash
    chmod +x ola_mundo.sh
    ```
5.  **Execute a receita:** Para executar um script que está no diretório atual, você precisa usar `./` na frente.
    ```bash
    ./ola_mundo.sh
    ```

---

### <img src="https://api.iconify.design/mdi/variable-box.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Tornando as Receitas Dinâmicas

E se quisermos que nossa receita funcione para diferentes "clientes" ou "quantidades"? Usamos **parâmetros posicionais**.

* **Analogia:** São os **"campos em branco"** na sua receita, como `[NOME DO CLIENTE]` ou `[QUANTIDADE]`.
* **Como funciona?** O shell automaticamente armazena os argumentos que você passa para um script em variáveis especiais:
    * `$1`: O primeiro argumento.
    * `$2`: O segundo argumento, e assim por diante.
    * `$0`: O nome do próprio script.
* **Exemplo:** Vamos criar um script `saudacao.sh`:
    ```bash
    #!/bin/bash
    
    # Script que cumprimenta o nome passado como primeiro argumento.
    echo "Olá, $1! Bem-vindo ao servidor."
    ```
* **Como executar:**
    ```bash
    # O script vai imprimir "Olá, Maria! Bem-vindo ao servidor."
    ./saudacao.sh Maria
    ```

---

### <img src="https://api.iconify.design/mdi/call-split.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Adicionando Inteligência à Receita (`if/else`)

A verdadeira automação vem da capacidade de tomar decisões.

* **Analogia:** "**SE** o cliente pediu queijo extra, **ENTÃO** adicione mais mussarela, **SENÃO**, siga a receita padrão."
* **Estrutura básica:** `if [ condição ]; then ... else ... fi`
* **<img src="https://api.iconify.design/logos/aws-ec2.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Cenário Prático:** Vamos melhorar nosso script de saudação para que ele verifique se um nome foi realmente fornecido.
    ```bash
    #!/bin/bash
    
    if [ -z "$1" ]; then
      echo "Erro: Por favor, forneça um nome como argumento."
    else
      echo "Olá, $1! Bem-vindo ao servidor."
    fi
    ```
    > **Hack:** `if [ -z "$1" ]` é uma forma comum de testar se o primeiro argumento está **z**ero ou vazio.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Receita de Mestre: Script de Backup no EC2

Vamos juntar tudo: variáveis, comandos e lógica.
**A Dor:** "Preciso de uma forma simples de fazer o backup do meu site e enviá-lo para um bucket S3, e quero que o nome do arquivo de backup inclua a data de hoje."

```bash
#!/bin/bash

# --- Parte 1: Variáveis (Nossos Ingredientes) ---
# Usar variáveis torna o script fácil de modificar no futuro.
BUCKET_S3="meu-bucket-de-backup-12345"
PASTA_SITE="/var/www/html"
DATA_ATUAL=$(date +"%Y-%m-%d") # <-- Substituição de Comando!

# --- Parte 2: Lógica do Script (Passos da Receita) ---
echo "Iniciando o backup do site..."
tar -czf /tmp/backup-site-$DATA_ATUAL.tar.gz -C $PASTA_SITE .

echo "Enviando para o S3..."
aws s3 cp /tmp/backup-site-$DATA_ATUAL.tar.gz s3://$BUCKET_S3/

echo "Limpando arquivos temporários..."
rm /tmp/backup-site-$DATA_ATUAL.tar.gz

echo "Backup concluído com sucesso!"--- 

```
#### <img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO (Substituição de Comando): A linha DATA_ATUAL=$(...) é um conceito-chave. Ela diz ao shell: "Execute o comando date e guarde o resultado dele na gaveta DATA_ATUAL". Isso permite que seus scripts capturem informações dinâmicas do sistema.

---