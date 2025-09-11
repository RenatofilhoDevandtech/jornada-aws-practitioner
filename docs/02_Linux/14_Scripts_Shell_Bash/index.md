# <img src="https://api.iconify.design/mdi/script-text-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Livro de Receitas do Mestre: Guia Definitivo de Scripts em Shell Bash

Até agora, agimos como um Chef dando ordens uma a uma na cozinha. Mas e se pudéssemos escrever a **receita completa** uma única vez e entregar para um robô executá-la perfeitamente sempre que precisarmos? Isso é o **Scripting em Shell Bash**.

Um script é a sua ferramenta máxima de **automação**. É como você transforma tarefas repetitivas e complexas em um único comando, economizando tempo e eliminando erros humanos. Este guia é o seu curso de culinária para escrever essas receitas.

---

### <img src="https://api.iconify.design/mdi/file-code-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Estrutura de uma Receita (Script)

Todo bom script tem uma estrutura básica.

#### <img src="https://api.iconify.design/mdi/exclamation-thick.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> 1. O "Shebang": `#!/bin/bash`
Esta **deve** ser sempre a primeira linha do seu script.
* **Analogia:** "Esta receita segue as regras da Culinária Francesa (`bash`)".
* **O que faz?** Diz ao sistema operacional qual intérprete (shell) deve ser usado para ler e executar os comandos da sua receita.

#### <img src="https://api.iconify.design/mdi/check-decagram-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> 2. A Permissão de Execução: `chmod +x`
Um arquivo de texto não pode ser executado por padrão. Você precisa dar a ele essa permissão.
* **Analogia:** Dar a "autorização sanitária" para que a receita possa ser executada.
* **O Comando:** `chmod +x nome_do_script.sh`

#### <img src="https://api.iconify.design/mdi/play-box-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> 3. A Execução: O Segredo do `./`
Para executar um script, você não pode simplesmente digitar seu nome. Você precisa dizer ao shell para procurar "aqui neste diretório".
* **O Comando:** `./nome_do_script.sh`
* **A Dor que Resolve:** Evita conflitos de segurança. O Linux, por padrão, não procura por programas no diretório atual por motivos de segurança (para evitar que um script malicioso chamado `ls` seja executado em vez do comando real). O `./` diz explicitamente: "execute o script que está **aqui**".

---

### <img src="https://api.iconify.design/mdi/variable-box.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Tornando as Receitas Dinâmicas (Entradas do Script)

Uma receita que faz sempre a mesma coisa é útil, mas uma que se adapta aos ingredientes que você fornece é muito mais poderosa.

#### <img src="https://api.iconify.design/mdi/numeric-1-box-multiple-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Argumentos (`$1`, `$2`...)
* **Analogia:** Os "campos em branco" na receita: `Faça uma pizza para [NOME_DO_CLIENTE] com [QUANTIDADE] fatias`.
* **Como Funciona:** O shell armazena os valores que você passa após o nome do script nas variáveis `$1` (primeiro argumento), `$2` (segundo), e assim por diante.
* **Exemplo:** `cria_backup.sh /var/www/html backup_site.tar.gz`
    * Dentro do script, `$1` será `/var/www/html` e `$2` será `backup_site.tar.gz`.

#### <img src="https://api.iconify.design/mdi/keyboard-return.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Lendo a Entrada do Usuário (`read`)
* **Analogia:** "Perguntar ao cliente qual o sabor da pizza".
* **A Dor que Resolve:** Criar scripts interativos que pedem informações ao usuário durante a execução.
* **Exemplo:**
    ```bash
    #!/bin/bash
    echo "Olá! Qual é o seu nome?"
    read NOME_DO_USUARIO
    echo "Prazer em te conhecer, $NOME_DO_USUARIO!"
    ```

#### <img src="https://api.iconify.design/mdi/arrow-decision-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Substituição de Comando (`$(...)`)
* **Analogia:** "Use o resultado de uma receita como ingrediente para outra".
* **A Dor que Resolve:** Usar a saída de um comando como parte de outro comando ou variável.
* **Exemplo:** Criar um nome de arquivo de log com a data e hora exatas.
    ```bash
    #!/bin/bash
    
    # Executa o comando 'date' e guarda o resultado na variável
    DATA_ATUAL=$(date +"%Y-%m-%d_%H-%M-%S")
    
    echo "Iniciando processo de backup às $DATA_ATUAL..."
    touch "log_backup_$DATA_ATUAL.txt"
    ```
> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** A sintaxe `$(comando)` é a forma moderna e preferida. A forma antiga, com crases (``comando``), também funciona, mas é menos legível e mais difícil de aninhar.

---

### <img src="https://api.iconify.design/mdi/call-split.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Adicionando Inteligência à Receita (`if`, `else`)

Scripts realmente úteis tomam decisões.

* **Analogia:** "**SE** o forno estiver pré-aquecido, **ENTÃO** coloque a pizza, **SENÃO**, espere 5 minutos."
* **A Dor que Resolve:** A necessidade de tratar erros e diferentes cenários.
* **<img src="https://api.iconify.design/logos/aws-ec2.svg?color=currentColor" width="18" /> Cenário Prático na AWS:** Um script que verifica se um diretório de backup existe antes de tentar usá-lo.
    ```bash
    #!/bin/bash
    
    DIRETORIO_BACKUP="/mnt/backups"
    
    if [ -d "$DIRETORIO_BACKUP" ]; then
      echo "Diretório encontrado. Iniciando backup..."
      # ... (comandos de backup aqui) ...
    else
      echo "ERRO: O diretório $DIRETORIO_BACKUP não existe! Criando agora..."
      mkdir "$DIRETORIO_BACKUP"
    fi
    ```

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Checklist do Chef Profissional (Boas Práticas)

1.  **<img src="https://api.iconify.design/mdi/comment-text-outline.svg?color=currentColor" width="16" /> Comente seu Código:** Scripts são lidos por você no futuro e por outras pessoas. Use `#` para explicar o que as partes complexas fazem.
2.  **<img src="https://api.iconify.design/mdi/variable-box.svg?color=currentColor" width="16" /> Use Variáveis:** Não repita caminhos de arquivos ou nomes de servidores. Coloque-os em variáveis no topo do script para facilitar a manutenção.
3.  **<img src="https://api.iconify.design/mdi/security.svg?color=currentColor" width="16" /> Segurança Primeiro:** Verifique as permissões. Seu script precisa mesmo rodar como `root`? Siga o princípio do menor privilégio.
4.  **<img src="https://api.iconify.design/mdi/test-tube.svg?color=currentColor" width="16" /> Teste! Teste! Teste!** Sempre teste seus scripts em um ambiente de desenvolvimento antes de rodá-los em produção. Um script com um comando `rm` errado pode causar um desastre.

> **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação Linux Essentials:** O exame focará em entender a estrutura básica de um script (`#!/bin/bash`), como torná-lo executável (`chmod`), como executá-lo (`./`) e como ele usa variáveis e parâmetros como `$1`.