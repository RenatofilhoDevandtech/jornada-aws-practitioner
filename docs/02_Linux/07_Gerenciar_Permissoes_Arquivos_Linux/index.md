Markdown

# <img src="https://api.iconify.design/mdi/shield-lock-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Permissões no Linux: O Guia Prático para Servidores AWS

No universo da nuvem, a segurança é o pilar número um. E a primeira linha de defesa em qualquer servidor Linux não é um firewall complexo, mas sim um sistema simples e poderoso de permissões de arquivos. Entendê-lo profundamente é a sua principal ferramenta para proteger seus dados.

**A Missão:** Imagine que você acabou de instalar um site (como WordPress ou Magento) em uma instância EC2. Por padrão, ele não funciona direito e está inseguro. Sua missão é usar os comandos de permissão para fazer o site funcionar perfeitamente e, ao mesmo tempo, trancá-lo contra acessos indevidos.

---

### <img src="https://api.iconify.design/mdi/file-eye-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Passo 1: Entendendo o Campo de Batalha com `ls -l`

Antes de mudar qualquer coisa, precisamos de um diagnóstico. O comando `ls -l` é o seu "raio-x", mostrando o dono e as permissões de cada arquivo.

**Cenário Prático:** Você acabou de descompactar os arquivos do seu site na pasta `/var/www/html`. Ao rodar `ls -l`, você vê algo assim:

-rw-r--r--. 1 root root 418 Sep 25 2018 index.php
-rw-r--r--. 1 root root 19935 Jan 1 2020 license.txt
drwxr-xr-x. 9 root root 4096 Jun 8 2021 wp-admin
drwxr-xr-x. 12 root root 4096 Jun 8 2021 wp-content


* **Diagnóstico:** Todos os arquivos e diretórios pertencem ao usuário `root` e ao grupo `root`.
* **A Dor:** O servidor web (Apache ou Nginx) roda com um usuário próprio (ex: `apache` ou `www-data`), que é um usuário comum. Ele não é o `root`. Portanto, quando o WordPress tentar instalar um novo plugin ou fazer upload de uma imagem, ele tentará "gravar" na pasta `wp-content`. Como essa pasta pertence ao `root` e o grupo `root` só tem permissão de leitura (`r-x`), a operação vai falhar com um erro de "Permissão Negada".

---

### <img src="https://api.iconify.design/mdi/account-switch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Passo 2: Entregando as Chaves Corretas com `chown`

A primeira etapa da nossa missão é garantir que o servidor web seja o **dono** dos arquivos que ele precisa gerenciar.

* **O Comando:** `chown` (change owner / mudar dono).
* **Analogia:** "Transferir a Propriedade". Estamos passando a responsabilidade dos arquivos para o funcionário certo (o usuário `apache`).
* **A Sintaxe:**
    * `chown novo_dono arquivo`: Muda só o usuário.
    * `chown :novo_grupo arquivo`: Muda só o grupo.
    * `chown novo_dono:novo_grupo arquivo`: Muda ambos de uma vez (o mais comum).

**Executando a Missão:**
Vamos transferir a propriedade de todos os arquivos e diretórios dentro de `/var/www/html` para o usuário e grupo `apache`.

```bash
# O -R significa "recursivamente", aplicando a mudança a tudo dentro da pasta.
sudo chown -R apache:apache /var/www/html
```
**Verificação:**
Se você rodar ls -l  novamente, verá a mudança:

```bash
drwxr-xr-x. 9 apache apache 4096 Jun 8 2021 wp-admin
drwxr-xr-x. 12 apache apache 4096 Jun 8 2021 wp-content
-rw-r--r--. 1 apache apache 418 Sep 25 2018 index.php
-rw-r--r--. 1 apache apache 19935 Jan 1 2020 license.txt
drwxr-xr-x. 9 apache apache 4096 Jun 8 2021 wp-admin
drwxr-xr-x. 12 apache apache 4096 Jun 8 2021 wp-content
```
**Resultado:** A primeira parte da missão foi um sucesso! O servidor web agora é o dono dos seus próprios arquivos e já consegue fazer uploads e instalar plugins. Mas o site ainda não está totalmente seguro.
---

### <img src="https://api.iconify.design/mdi/key-change.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Passo 3: Trancando as Portas com `chmod` (Princípio do Menor Privilégio)

Agora que o `apache` é o dono, precisamos garantir que os "crachás de acesso" estejam configurados corretamente. A regra de ouro da segurança é o **Princípio do Menor Privilégio**: ninguém deve ter mais acesso do que o estritamente necessário para fazer seu trabalho.

* **A Dor que Resolve:** Evitar que um invasor, caso explore uma falha no site, consiga modificar arquivos críticos do sistema ou executar scripts maliciosos. Um `chmod 777` em toda a pasta do site é como deixar todas as portas do prédio abertas, inclusive a sala do cofre.

#### <img src="https://api.iconify.design/mdi/numeric.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Usando o Método Absoluto (Numérico)

Este é o método mais rápido para aplicar um padrão de segurança. Para um site WordPress, a prática recomendada é:
* **Diretórios (`drwxr-xr-x` ou `755`):** O dono (`apache`) pode fazer tudo. O grupo e os outros podem listar e entrar nos diretórios, mas não criar arquivos.
* **Arquivos (`-rw-r--r--` ou `644`):** O dono (`apache`) pode ler e escrever. O grupo e os outros podem apenas ler os arquivos.

**Executando a Missão:**
Vamos usar o comando `find` em conjunto com o `chmod` para aplicar essas permissões de forma inteligente.

```bash
# Navegue até a pasta raiz do site
cd /var/www/html

# 1. Aplica a permissão 755 em TODOS os diretórios
sudo find . -type d -exec chmod 755 {} \;

# 2. Aplica a permissão 644 em TODOS os arquivos
sudo find . -type f -exec chmod 644 {} \;
```
**Verificação:**
Hack: O comando find . -type d -exec ... é um padrão poderoso que significa: "Encontre todos os diretórios (-type d) a partir daqui (.) e para cada um que encontrar, execute (-exec) o seguinte comando".

### <img src="https://api.iconify.design/mdi/format-letter-case.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Usando o Método Simbólico para Exceções
Há um arquivo especial, o wp-config.php, que contém as senhas do banco de dados. Ele precisa ser ainda mais protegido. Ninguém, exceto o dono, deveria conseguir lê-lo.

**Executando a Missão:**
Vamos remover as permissões de leitura para o grupo e para os outros.

```Bash

# Remove (-) as permissões de leitura (r) para o grupo (g) e outros (o)
sudo chmod go-r wp-config.php
```
**Verificação:**
Se você rodar ls -l wp-config.php, o resultado será -rw-------, que corresponde à permissão numérica 600. Máxima segurança!

### <img src="https://api.iconify.design/mdi/check-decagram-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Missão Cumprida e Práticas Recomendadas

**Ao final da nossa missão:**

A propriedade dos arquivos pertence ao serviço que precisa gerenciá-los (chown).

As permissões estão configuradas para o mínimo necessário, protegendo o sistema (chmod).

Lembre-se sempre:

- Nunca use chmod 777: É um convite para desastres.

- Comece Restritivo: Aplique o menor privilégio primeiro e adicione permissões apenas quando uma funcionalidade quebrar por causa disso.

- Conheça os Caracteres Especiais: Lembre-se que o Linux é "case-sensitive" e caracteres como . e - no início de nomes de arquivos têm funções especiais.

#### <img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação: O exame vai focar em cenários. Se a pergunta for "Como você garante que apenas o dono pode modificar um arquivo, mas o grupo pode apenas ler?", a resposta é chmod 640 nome_do_arquivo. Entender a conversão numérica e a lógica do menor privilégio é essencial.
