# <img src="https://api.iconify.design/mdi/account-search-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab [Desafio]: O Detetive do CloudTrail - Investigando uma Violação de Segurança

### O Cenário (A "User Story")

> **Como** um engenheiro de segurança na nuvem, **EU QUERO** usar as ferramentas de auditoria e análise da AWS para investigar uma alteração não autorizada na minha infraestrutura, identificar o responsável e remediar a vulnerabilidade, **PARA QUE** eu possa restaurar a segurança do ambiente e prevenir futuros incidentes.

### A Dor que o Lab Resolve

Quando uma violação de segurança acontece, o caos e a pressão são imensos. A dor que este lab resolve é a **falta de um processo de investigação**. Sem uma trilha de auditoria (CloudTrail) e ferramentas de análise (Athena), é quase impossível responder às perguntas críticas: "O que aconteceu? Como aconteceu? Quem foi? Como evitamos que aconteça de novo?".

### Objetivos de Aprendizado
Ao final deste desafio, você será capaz de:

* [ ] Configurar uma **Trilha (Trail)** do CloudTrail para auditoria.
* [ ] Usar `grep` e a AWS CLI para uma análise inicial de logs.
* [ ] Usar o **Amazon Athena** para executar consultas SQL complexas nos logs do CloudTrail.
* [ ] Identificar a causa raiz de um incidente de segurança e tomar ações de remediação.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: A Investigação

#### Tarefa 1: A "Cena do Crime" Inicial
Nesta etapa, vamos verificar o estado normal da aplicação e fazer uma pequena alteração de segurança controlada.

1.  **Acesse o Site:**
    * No painel do seu laboratório, clique em **Detalhes > Mostrar (Details > Show)**.
    * Copie o valor de `WebServerIP`.
    * Cole em uma nova aba do navegador no formato `http://<WebServerIP>/cafe/`.
    * **O "Porquê":** Esta etapa valida que a aplicação está no ar e funcionando como esperado antes de qualquer incidente. Você verá o site normal da cafeteria.

2.  **Abra uma Brecha (Controlada):**
    * No Console da AWS, navegue até o serviço **EC2**.
    * No menu esquerdo, vá em **Grupos de Segurança (Security Groups)**.
    * Selecione o grupo `WebSecurityGroup`.
    * Vá para a aba **Regras de entrada (Inbound rules)** e clique em **Editar regras de entrada (Edit inbound rules)**.
    * Clique em **Adicionar regra (Add rule)** e configure:
        * **Tipo (Type):** `SSH`.
        * **Origem (Source):** `Meu IP (My IP)`.
    * Clique em **Salvar regras (Save rules)**.
    * **O "Porquê":** Estamos abrindo o acesso administrativo **apenas para nós mesmos**. Esta é a forma segura de permitir o acesso SSH, limitando a origem ao seu endereço IP atual. Precisaremos disso mais tarde para nos conectarmos à instância.

#### Tarefa 2: Ligando as "Câmeras de Segurança" (Criar a Trilha do CloudTrail)
**Analogia:** Antes que o "crime" aconteça, o detetive precisa instalar as câmeras para gravar as evidências.

1.  No Console da AWS, navegue até o serviço **CloudTrail**.
2.  No menu esquerdo, clique em **Trilhas (Trails)**.
3.  Clique em **Criar trilha (Create trail)**.
4.  **Nome da trilha (Trail name):** `monitor`.
5.  Em **Local de armazenamento (Storage location)**, selecione **Criar um novo bucket do S3 (Create new S3 bucket)**.
6.  **Alias do AWS KMS (AWS KMS alias):** Deixe em branco.
7.  Siga clicando em **Próximo (Next)** até o final e clique em **Criar trilha (Create trail)**.
8.  **O Incidente:** Volte para a aba do site do café e **atualize a página** (pode ser necessário usar `Shift + Refresh` para limpar o cache do navegador). **O site foi desfigurado!**
9.  **A Primeira Pista:** Volte para o console do **EC2 > Grupos de Segurança (Security Groups)** e olhe as regras de entrada do `WebSecurityGroup`. Você verá uma nova regra, que você não criou, permitindo SSH da **Internet inteira (`0.0.0.0/0`)**. Alguém abriu uma porta perigosa.

#### Tarefa 3: A Análise Forense com a "Lupa Mágica" (Usando o Athena)

**Analogia:** Em vez de assistir a horas de fitas, o detetive agora vai usar um **"software de análise forense" (o Athena)** para encontrar o suspeito em segundos.

1.  **Crie a "Lente de Análise" (A Tabela do Athena):**
    * Volte para o console do **CloudTrail**.
    * No menu esquerdo, vá em **Histórico de eventos (Event history)**.
    * No topo da página, clique em **Criar tabela do Athena (Create Athena table)**.
    * Em `Local de armazenamento (Storage location)`, selecione o seu bucket de logs que começa com `monitoring...`.
    * Clique em **Criar tabela (Create table)**.
    * **O "Porquê":** Este passo cria uma "tabela virtual" sobre os arquivos de log no S3, permitindo que o Athena os entenda e os consulte com SQL, sem precisar movê-los.

2.  **Inicie a Investigação:**

    * Navegue até o serviço **Amazon Athena**.
    * No painel esquerdo, em **Banco de dados (Database)**, selecione `default`. Você deverá ver sua nova tabela `cloudtrail_logs_monitoring...`.
    * **Configure o Destino dos Resultados:** Se for a primeira vez, o Athena pedirá para configurar um local para salvar os resultados das consultas. Clique em **Configurações (Settings)** ou no link do aviso, clique em **Gerenciar (Manage)** e no campo `Localização do resultado da consulta`, insira `s3://<nome-do-seu-bucket-monitoring>/results/`. Salve.
3.  **Execute as Consultas SQL (A Caça ao Culpado):**

    * Na janela de consulta, cole o seguinte comando SQL (lembre-se de ajustar o nome da tabela se for diferente):
        ```sql
        SELECT 
            useridentity.username, 
            eventtime, 
            eventname, 
            sourceipaddress,
            requestparameters
        FROM "cloudtrail_logs_monitoring####"
        WHERE eventname = 'AuthorizeSecurityGroupIngress'
        ORDER BY eventtime DESC;
        ```
    * Clique em **Executar (Run)**.
    * **A Descoberta:** Analisando o resultado, você encontrará um evento `AuthorizeSecurityGroupIngress` executado por um usuário suspeito (`chaos-user`). Na coluna `requestparameters`, você verá os detalhes da regra maliciosa que foi criada (`"cidrIp": "0.0.0.0/0"`). **Você encontrou a evidência do crime!**

#### Tarefa 4: A Remediação (Limpando a Bagunça e Fortalecendo as Defesas)

1.  **Expulse o Invasor da Instância:**
    * Conecte-se via **SSH** à instância `Cafe Web Server` (usando a regra de `My IP` que você criou).
    * Verifique quem está logado: `who`.
    * Se vir o `chaos-user`, use `sudo userdel -r chaos-user` para deletá-lo. (Se ele estiver ativo, pode ser necessário usar `sudo kill -9 <PID>` no processo dele primeiro).

2.  **Fortaleça o SSH:**
    * Edite o arquivo de configuração do SSH: `sudo vi /etc/ssh/sshd_config`.
    * Certifique-se de que a linha `PasswordAuthentication no` esteja descomentada e a `PasswordAuthentication yes` esteja comentada.
    * Reinicie o serviço: `sudo service sshd restart`.
    * **O "Porquê":** Estamos desabilitando o login por senha, forçando o uso de chaves criptográficas, que é muito mais seguro.

3.  **Corrija o Site:**
    * Navegue até `/var/www/html/cafe/images/`.
    * Restaure a imagem original: `sudo mv Coffee-and-Pastries.backup Coffee-and-Pastries.jpg`.

4.  **Remova o Acesso do Hacker na AWS:**
    * No console do **IAM**, vá em **Usuários (Users)**, selecione o `chaos-user` e **Exclua-o**.

5.  **Corrija o Firewall:**
    * No console do **EC2 > Grupos de Segurança**, edite o `WebSecurityGroup` e remova a regra maliciosa que abre a porta 22 para o mundo.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns, detetive! Você usou as ferramentas da AWS não apenas para construir, mas para **investigar, diagnosticar e remediar** um incidente de segurança. Você viu na prática como os logs do CloudTrail são sua "caixa preta" e como o Athena te dá o poder de analisá-los eficientemente para encontrar a verdade.