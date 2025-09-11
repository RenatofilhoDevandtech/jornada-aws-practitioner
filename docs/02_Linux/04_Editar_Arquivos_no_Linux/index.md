# <img src="https://api.iconify.design/mdi/file-edit-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Arte da Edição: Dominando os Editores de Texto na AWS

No mundo da nuvem, sua casa é a linha de comando de uma instância EC2. E a habilidade mais fundamental para manter essa casa em ordem é saber editar arquivos de configuração, scripts e logs.

Neste guia, vamos além do básico. Vamos explorar os dois editores de texto essenciais, **nano** e **Vim**, através da lente de um profissional de cloud. Você não vai apenas aprender os comandos, vai entender quando usar a "Bicicleta" (nano) para um passeio rápido e quando pilotar o "Avião a Jato" (Vim) para uma missão complexa.

---

### <img src="https://api.iconify.design/mdi/tools.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> As Ferramentas e Seus Casos de Uso

| Ferramenta | Analogia | Filosofia | Quando Usar no Dia a Dia AWS? |
| :--- | :--- | :--- | :--- |
| **GNU nano** | A **Bicicleta** | Simplicidade e Intuitividade | Para edições rápidas e pontuais: alterar uma linha em um arquivo de configuração, corrigir um erro de digitação em um script, adicionar um endereço IP a um arquivo de hosts. |
| **Vim** | O **Avião a Jato** | Poder e Eficiência | Para tarefas complexas: escrever um script de automação do zero, editar múltiplos arquivos, fazer buscas e substituições avançadas em um código ou log. |

---

### <img src="https://api.iconify.design/mdi/road-variant.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Cenários do Mundo Real: Editando Arquivos em uma Instância EC2

Imagine que você é um Analista de Cloud em uma startup. Você acabou de se conectar via SSH a uma instância EC2 que hospeda o site da empresa.

#### Cenário 1: O Ajuste Rápido com `nano` (A Bicicleta)

**A Dor:** Um desenvolvedor te pede para aumentar o limite de tamanho para upload de arquivos no servidor web Nginx, que está bloqueando uploads de imagens maiores que 1MB.

**Por que `nano`?** É uma tarefa cirúrgica. Você precisa abrir um arquivo, encontrar uma linha, mudar um número e salvar. A simplicidade do nano é perfeita para isso, minimizando a chance de erros.

**Passo a Passo Profissional:**

1.  **Acessar o servidor:**
    ```bash
    ssh ec2-user@seu_ip_publico -i sua-chave.pem
    ```

2.  **Abrir o arquivo de configuração com privilégios de administrador:**
    ```bash
    sudo nano /etc/nginx/nginx.conf
    ```

3.  **Encontrar a linha:** Dentro do nano, pressione `Ctrl + W` (procurar) e digite `client_max_body_size`. Pressione `Enter`. O cursor pulará para a linha correta.

4.  **Editar o valor:** Altere a linha de `client_max_body_size 1M;` para `client_max_body_size 10M;`.

5.  **Salvar e Sair:**
    * Pressione `Ctrl + O` (Salvar). O nano confirmará o nome do arquivo, apenas pressione `Enter`.
    * Pressione `Ctrl + X` (Sair).

6.  **Aplicar a mudança:** Para que a alteração tenha efeito, reinicie o serviço do Nginx.
    ```bash
    sudo systemctl restart nginx
    ```
**Resultado:** Em menos de um minuto, você resolveu um problema real de produção de forma segura e eficiente.

#### Cenário 2: Criando um Script com `vim` (O Avião a Jato)

**A Dor:** A equipe precisa de um backup diário dos arquivos do site para um bucket S3. Você precisa criar um script de automação para essa tarefa.

**Por que `vim`?** Escrever um script envolve múltiplas linhas, edições, e talvez copiar e colar trechos de código. A agilidade dos modos e comandos do Vim brilha aqui, tornando o processo muito mais rápido do que no nano.

**Passo a Passo Profissional (com comandos intermediários):**

1.  **Criar o arquivo de script:**
    ```bash
    vim backup_diario.sh
    ```

2.  **Entrar no Modo de Inserção:** Pressione a tecla `i`. O `-- INSERT --` aparecerá no canto inferior esquerdo.

3.  **Escrever o código inicial:**
    ```bash
    #!/bin/bash
    # Script para fazer backup do site para o S3
    
    aws s3 sync /var/www/html/ s3://meu-bucket-de-backup-12345/
    ```

4.  **Copiar e Colar (a mágica do Vim):** Você decide que também quer adicionar um comando que remove logs antigos. Em vez de redigitar, você vai copiar a linha do comando `aws`.
    * Pressione `Esc` para voltar ao **Modo de Comando**.
    * Mova o cursor com as setas até a linha `aws s3 sync...`.
    * Pressione `yy` (yank/copiar a linha).
    * Mova o cursor para a linha de baixo e pressione `p` (paste/colar).

5.  **Editar a linha copiada:** Agora você tem duas linhas `aws s3 sync...`.
    * Vá para a linha duplicada, pressione `i` para entrar no Modo de Inserção novamente.
    * Altere a linha para seu comando de limpeza de logs, por exemplo: `rm -f /var/log/app/antigo.log`.

6.  **Desfazer um erro:** Você percebe que a linha de remoção de logs está errada.
    * Pressione `Esc` para voltar ao Modo de Comando.
    * Pressione `u` (undo/desfazer). A alteração é revertida.

7.  **Salvar e Sair:**
    * Pressione `Esc` para garantir que está no Modo de Comando.
    * Digite `:wq` e pressione `Enter` para salvar e sair.

8.  **Tornar o script executável:** Por padrão, um novo arquivo não tem permissão de execução.
    ```bash
    chmod +x backup_diario.sh
    ```
**Resultado:** Você criou um script funcional de forma muito mais rápida, editando e manipulando linhas com a eficiência de um piloto de caça.

---
### <img src="https://api.iconify.design/mdi/lifebuoy.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Seu Kit de Ferramentas Aprimorado

#### Kit de Sobrevivência do `nano` (A Bicicleta)
* `Ctrl + X`: Sair (pergunta se quer salvar)
* `Ctrl + O`: Salvar
* `Ctrl + W`: Procurar
* `Ctrl + G`: Ajuda
* `Ctrl + K` / `Ctrl + U`: Recortar / Colar linha

#### Kit de Voo Essencial do `vim` (O Avião a Jato)
* **Modos:** `i` para **I**nserir, `Esc` para voltar ao **C**omando.
* **Sair/Salvar:**
  * `:wq` - Salvar e Sair (Write & Quit)
  * `:q!` - Sair sem Salvar (Quit & Force)
* **Edição no Modo de Comando:**
  * `yy` - Copiar linha (Yank)
  * `p` - Colar linha (Paste)
  * `dd` - Deletar linha
  * `u` - Desfazer (Undo)
  * `/palavra` - Procurar por "palavra"

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO LINUX ESSENTIALS:** A prova espera que você conheça a finalidade de ambos os editores. Entenda que **Vim é um editor modal** e **nano é um editor não-modal**. Saber os comandos básicos para salvar e sair de ambos (`:wq` para Vim, `Ctrl+X` para nano) é o mínimo absoluto.

