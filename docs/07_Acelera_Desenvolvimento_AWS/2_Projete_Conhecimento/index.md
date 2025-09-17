# <img src="https://api.iconify.design/mdi/notebook-edit-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Projeto: Criando sua Base de Conhecimento para Solução de Problemas

Bem-vindo ao projeto que será a espinha dorsal da sua jornada no AWS re/Start. Este não é um simples exercício, mas sim a criação de um **ativo de carreira**: sua própria base de conhecimento pessoal e profissional para solucionar problemas na nuvem.

**Analogia:** Pense neste projeto como o **"Diário de Bordo de um Piloto de Caça"**. Após cada missão (cada laboratório, cada erro), um piloto experiente anota tudo: os desafios, as soluções e as lições aprendidas. Com o tempo, este diário se torna seu recurso mais valioso, uma fonte de sabedoria prática que o diferencia dos novatos.

---

### <img src="https://api.iconify.design/mdi/bullseye-arrow.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. Visão Geral e Objetivos

* **Sua Missão:** Documentar cada desafio técnico que você encontrar e resolver durante este curso, seja em laboratórios guiados ou em suas próprias explorações.
* **A Dor que Resolve:** A "curva do esquecimento". Sem documentação, a solução para um problema complexo que você resolveu hoje pode ser esquecida em três semanas. Este projeto transforma suas experiências em conhecimento **permanente e reutilizável**.
* **O Resultado Final:** Ao final do curso, você terá um guia de referência pessoal e detalhado, que poderá levar com você para sua carreira como profissional de nuvem.

---

### <img src="https://api.iconify.design/mdi/file-excel-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Ferramenta: O Modelo da Base de Conhecimento

Você usará um modelo de planilha para organizar suas descobertas. Cada linha na planilha será uma nova "página" no seu diário de bordo.

#### Os Campos do seu "Diário de Bordo":
* **Problema nº:** Um identificador único para cada registro (sua "chave primária").
* **Categoria:** A "seção" do diário onde a entrada pertence. Use as categorias definidas para manter tudo organizado.
* **Descrição do Problema:** Um título de alto nível, como "Falha ao conectar na instância EC2 via SSH".
* **Sintoma ou Problema:** Detalhes precisos! "Recebi a mensagem de erro `Permission denied (publickey)` no terminal."
* **Análise de Causa Raiz (RCA):** A parte do "detetive". "Após investigação, a causa raiz era que eu esqueci de rodar o comando `chmod 400` no meu arquivo `.pem`."
* **Procedimentos de Resolução:** O "manual de instruções" para o seu "eu" do futuro. "1. Navegar até a pasta da chave. 2. Executar `chmod 400 nome_da_chave.pem`. 3. Tentar a conexão SSH novamente."
* **Ferramentas ou Recursos Úteis:** Links para a documentação da AWS, um artigo de blog ou o nome do colega que te ajudou.
* **Comentários:** Qualquer insight extra. "Lembrete: O Linux é case-sensitive, então `Downloads` é diferente de `downloads`."

---

### <img src="https://api.iconify.design/mdi/format-list-bulleted-square.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. As Categorias do Conhecimento

Para manter seu "diário" organizado, cada entrada deve ser classificada em uma das seguintes categorias. Abaixo estão alguns exemplos do que você pode documentar em cada uma.

| Categoria | <img src="https://api.iconify.design/logos/aws.svg" /> Serviços AWS Relacionados | Exemplos de Problemas a Documentar |
| :--- | :--- | :--- |
| **Armazenamento e Dados** | S3, EBS, EFS, RDS, DynamoDB, Redshift | Falha no upload para o S3, aumentar o tamanho de um volume EBS, erro de acesso ao RDS, consulta lenta no DynamoDB. |
| **Segurança e Conformidade** | IAM, Security Groups, Pares de Chaves, Trusted Advisor | Usuário IAM não consegue fazer login, erro de permissão negada, porta bloqueada no Security Group, alerta do Trusted Advisor. |
| **Redes** | VPC, Sub-redes, Route 53, API Gateway | Instância em sub-rede privada sem acesso à internet, erro de DNS no Route 53, problema de acesso a uma página web no EC2. |
| **Automação e Otimização** | CloudFormation, Systems Manager, Auto Scaling | Erro de sintaxe em um template do CloudFormation, falha do Auto Scaling em lançar novas instâncias. |
| **Computação** | EC2, ECS, Lambda | Instância EC2 não inicia, contêiner Docker não roda, função Lambda dando timeout ou erro de permissão. |
| **Monitoramento e Relatórios** | CloudWatch, SNS, SQS, CloudTrail | Alarme do CloudWatch não dispara, dificuldade em encontrar um evento no CloudTrail. |
| **TI Fundamental** | Linux, Python, SQL | Erro de sintaxe em um script Python, comando Linux não encontrado (`command not found`), consulta SQL retorna o resultado errado. |

> **`!!! tip "Dica de Especialista"`**
> Este projeto é o que os profissionais chamam de **"Playbook"** ou **"Runbook"**. Em equipes de DevOps e SRE (Site Reliability Engineering), ter runbooks bem documentados para incidentes comuns é uma prática essencial. Você já está aprendendo uma habilidade de nível sênior desde o primeiro dia!

---

### <img src="https://api.iconify.design/mdi/presentation-play.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 4. A Apresentação Final

Ao final do curso, sua equipe apresentará suas descobertas de uma das categorias.
* **O Objetivo:** Compartilhar o conhecimento adquirido com toda a turma. É uma simulação de como equipes técnicas apresentam suas "lições aprendidas" para o resto da empresa após resolver um grande problema.
* **A Preparação:** Mantenha sua base de conhecimento sempre atualizada. Como você não saberá qual categoria irá apresentar, documente problemas em **todas** elas.

Este projeto é a sua oportunidade de construir um registro tangível do seu crescimento e aprendizado. Aproveite e boa sorte!

--- 

### <img src="https://api.iconify.design/mdi/brain.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Do Diário à Inteligência: Elevando sua Base de Conhecimento a um Nível Profissional

Você já tem o conceito fundamental do seu "Diário de Bordo" (a Base de Conhecimento). Isso já te coloca à frente de muitos. Agora, vamos ver como os profissionais de elite transformam esse diário em uma poderosa ferramenta de equipe e em um sistema de inteligência automatizado.

---

### <img src="https://api.iconify.design/mdi/upgrade.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Upgrade: Da Planilha à Wiki Colaborativa

**A Dor da Planilha:** Uma planilha Excel é ótima para anotações individuais, mas se torna um gargalo para uma equipe. É difícil de pesquisar, não permite colaboração em tempo real, não lida bem com imagens e formatação de código, e não é fácil de linkar.

**A Solução Profissional:** Transforme sua base de conhecimento em uma **Wiki** interna.
* **Analogia:** Em vez de cada piloto ter sua própria caderneta, o esquadrão cria uma **"Biblioteca Digital Central"**.

#### <img src="https://api.iconify.design/mdi/tools.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Ferramentas do Mundo Real:
* **Confluence:** O padrão da indústria para documentação em grandes empresas.
* **Notion:** Uma alternativa moderna e flexível, muito popular em startups.
* **<img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="18" /> Sua Própria Wiki com o MkDocs (O Hack Definitivo):**
    > **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> INSIGHT PODEROSO:** Você **já está construindo** a ferramenta perfeita! Você pode criar uma nova seção de alto nível no seu `mkdocs.yml` chamada `'<img ... /> Base de Conhecimento'`, e dentro dela, criar um arquivo `.md` para cada categoria (`seguranca.md`, `redes.md`, etc.).
    > O resultado será uma base de conhecimento **pesquisável, bonita, fácil de navegar e perfeitamente integrada** ao seu portfólio. É a sua "caderneta" pessoal, mas com o poder de um site profissional.

---

### <img src="https://api.iconify.design/mdi/cloud-sync-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Salto Quântico: Integrando com o Ecossistema AWS

Uma base de conhecimento não precisa ser passiva. Na nuvem, podemos conectá-la aos nossos sistemas de monitoramento para criar um ciclo de melhoria contínua.

**A Dor:** "Recebi um alerta às 3 da manhã. Agora preciso procurar em vários lugares qual é o procedimento para resolver isso."

**A Solução (A Arquitetura da Inteligência Operacional):**
1.  **<img src="https://api.iconify.design/mdi/alert-outline.svg?color=currentColor" width="18" /> O Evento:** Uma instância EC2 para de responder.
2.  **<img src="https://api.iconify.design/logos/aws-cloudwatch.svg?color=currentColor" width="18" /> A Detecção:** Um **Alarme do Amazon CloudWatch** dispara.
3.  **<img src="https://api.iconify.design/logos/aws-sns.svg?color=currentColor" width="18" /> A Notificação:** O alarme envia uma notificação para um canal do **Slack** da equipe de operações.
4.  **<img src="https://api.iconify.design/mdi/link-variant.svg?color=currentColor" width="18" /> A Conexão com o Conhecimento:**
    > **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" /> O HACK:** Na mensagem de alerta enviada para o Slack, uma automação (usando **AWS Chatbot** ou **AWS Lambda**) inclui um **link direto para a página na sua Base de Conhecimento** que documenta o procedimento exato para resolver *aquele* tipo de falha!
    > **Exemplo de Alerta:** `ALERTA CRÍTICO: Falha no Status Check da Instância i-0123456789abcdef. Consulte o playbook de resolução aqui: [link para sua página sobre "Resolver Falhas de Instância"]`
5.  **<img src="https://api.iconify.design/mdi/arrow-u-left-top.svg?color=currentColor" width="18" /> O Ciclo se Fecha:** Após resolver o problema seguindo o guia, a equipe atualiza a página da base de conhecimento com as novas lições aprendidas, tornando o processo ainda mais robusto para a próxima vez.

---

### <img src="https://api.iconify.design/mdi/account-voice.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Dicas Finais de um Especialista

* **Escreva para o "Você" do Futuro às 3 da Manhã:** Sua documentação deve ser clara, concisa e fácil de seguir, mesmo sob pressão e com sono. Assuma que você terá esquecido de tudo. Use checklists e comandos "copiáveis".
* **A Causa Raiz é a Estrela do Show:** Não documente apenas *como* consertar. O aprendizado mais valioso está em entender profundamente **por que** o problema aconteceu em primeiro lugar. Isso é o que te impede de cometê-lo novamente.
* **Transforme Perguntas em Documentação:** Se um colega de equipe te faz uma pergunta, e a resposta não está na base de conhecimento, **adicione-a!** Essa é a forma como uma base de conhecimento cresce e se torna o cérebro da equipe.

Este projeto é, sem dúvida, o ativo de carreira mais importante que você construirá durante este curso. Ele demonstra não apenas seu conhecimento técnico, mas sua maturidade profissional e seu compromisso com a melhoria contínua.

---


### <img src="https://api.iconify.design/mdi/notebook-edit-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Projeto: Exemplos da Base de Conhecimento

Bem-vindo à sua Base de Conhecimento! Este documento é o seu "diário de bordo" como profissional de nuvem, onde cada problema resolvido se transforma em sabedoria para o futuro.

A seguir, apresentamos quatro exemplos clássicos de incidentes e suas soluções, formatados como "arquivos de caso". Use-os como modelo para documentar suas próprias descobertas ao longo dos laboratórios.

---
<br>

### <img src="https://api.iconify.design/mdi/numeric-1-circle-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Caso #001: O Site Desaparecido

* **<img src="https://api.iconify.design/mdi/format-list-bulleted-square.svg?color=currentColor" width="18" /> Categoria:** Redes
* **<img src="https://api.iconify.design/mdi/alert-circle-outline.svg?color=currentColor" width="18" /> Problema:** Aplicativo na instância do Amazon EC2 — problema de conectividade.

#### Investigação (Sintomas)
> O site, que funcionava ontem, agora não pode ser acessado. Testes em diferentes navegadores mostram os seguintes erros:
> * **Chrome:** `ERR_CONNECTION_TIMED_OUT`
> * **Firefox:** `A conexão expirou`
> * **Edge:** `Hmmm... não consigo acessar esta página`

#### Diagnóstico (Análise de Causa Raiz)
> A instância EC2 não estava mais em execução (`running`). Provavelmente foi parada (`stopped`) e, ao ser iniciada novamente, recebeu um novo endereço IP público, tornando a URL antiga inválida.

#### O Plano de Tratamento (Resolução)
1.  Navegue até o painel do **Amazon EC2** no console da AWS.
2.  Verifique a coluna **Instance State** (Estado da instância) para a instância em questão.
3.  Se o estado for `stopped`, selecione a instância e vá em **Actions** (Ações) > **Instance state** (Estado da instância) > **Start instance** (Iniciar instância).
4.  Aguarde até que o estado mude para `running`.
5.  **Crucial:** Após iniciar, copie o **novo** valor do **Public IPv4 address** (Endereço IPv4 público) e use-o para acessar o site.

#### Ferramentas e Pistas Adicionais
* **Ferramenta:** Painel do Amazon EC2.
* **Recurso:** AWS Service Health Dashboard ([status.aws.amazon.com](https://status.aws.amazon.com/)) para verificar se há alguma interrupção geral no serviço da AWS na região de destino.

---
<br>

### <img src="https://api.iconify.design/mdi/numeric-2-circle-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Caso #002: A Porta Trancada

* **<img src="https://api.iconify.design/mdi/format-list-bulleted-square.svg?color=currentColor" width="18" /> Categoria:** Redes
* **<img src="https://api.iconify.design/mdi/alert-circle-outline.svg?color=currentColor" width="18" /> Problema:** Falha ao conectar em uma instância EC2 via SSH.

#### Investigação (Sintomas)
> Ao tentar conectar via SSH com o comando `ssh -i key.pem ec2-user@publicip`, a conexão falha com o erro: `"Erro de rede: A conexão expirou"`. A instância está no estado `running`.

#### Diagnóstico (Análise de Causa Raiz)
> Houve dois problemas combinados:
> 1.  As permissões no arquivo da chave (`key.pem`) no computador local estavam muito abertas.
> 2.  O **Security Group** associado à instância EC2 não permitia tráfego de entrada na porta 22 (SSH) a partir do meu endereço IP.

#### O Plano de Tratamento (Resolução)
1.  **No seu computador local:** Garanta que a chave privada tenha as permissões corretas (somente leitura para o seu usuário).
    ```bash
    chmod 400 sua-chave.pem
    ```
2.  **No Console da AWS:**
    * Vá para o serviço **EC2** > **Security Groups**.
    * Selecione o Security Group associado à sua instância.
    * Clique na aba **Inbound rules** (Regras de entrada) e em **Edit inbound rules**.
    * Clique em **Add rule** e configure:
        * **Type:** `SSH`
        * **Source:** `My IP` (Isso preencherá automaticamente seu endereço IP atual, que é a prática mais segura).
    * Salve as regras.

#### Ferramentas e Pistas Adicionais
* **Recurso:** [Guia de Solução de Problemas de Conexão da AWS](https://aws.amazon.com/premiumsupport/knowledge-center/ec2-linux-ssh-troubleshooting/)
* **Pistas Adicionais:** O nome de usuário (`ec2-user`) está correto para a AMI que estou usando? (Para Ubuntu, seria `ubuntu`).

---
<br>

### <img src="https://api.iconify.design/mdi/numeric-3-circle-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Caso #003: O Armazém Lotado

* **<img src="https://api.iconify.design/mdi/format-list-bulleted-square.svg?color=currentColor" width="18" /> Categoria:** TI Fundamental
* **<img src="https://api.iconify.design/mdi/alert-circle-outline.svg?color=currentColor" width="18" /> Problema:** A aplicação em uma instância EC2 parou de funcionar.

#### Investigação (Sintomas)
> A aplicação parou de responder. Ao conectar via SSH, vemos que os processos estão rodando, mas nenhum novo log é gerado.

#### Diagnóstico (Análise de Causa Raiz)
> A instância ficou **sem espaço em disco**. O volume EBS está 100% cheio, impedindo que a aplicação escreva novos logs ou arquivos temporários.

#### O Plano de Tratamento (Resolução)
1.  **Verifique o espaço em disco:** Conecte-se à instância e execute `df -h` (disk free - human readable).
    ```bash
    df -h
    ```
2.  **Encontre os culpados:** Use o comando `find` para localizar arquivos grandes ou modificados recentemente que possam ser limpos.
    ```bash
    # Encontra arquivos no diretório raiz (/) maiores que 1GB
    sudo find / -size +1G -ls
    ```
3.  **Ação Corretiva:** Remova arquivos de log antigos, caches ou artefatos desnecessários. Para uma solução de longo prazo, considere aumentar o tamanho do volume EBS no console da AWS.

#### Ferramentas e Pistas Adicionais
* **Ferramentas:** Comandos Linux `df`, `du`, e `find`.
* **Pistas Adicionais:** Verifique se há algum processo "fugitivo" que está gerando logs excessivos.

---
<br>

### <img src="https://api.iconify.design/mdi/numeric-4-circle-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Caso #004: O Atendente Ausente

* **<img src="https://api.iconify.design/mdi/format-list-bulleted-square.svg?color=currentColor" width="18" /> Categoria:** TI Fundamental
* **<img src="https://api.iconify.design/mdi/alert-circle-outline.svg?color=currentColor" width="18" /> Problema:** A página web hospedada na instância não está carregando.

#### Investigação (Sintomas)
> O navegador exibe um erro de "Página não encontrada" ou "Não é possível acessar esse site", mesmo que a instância EC2 esteja `running` e o Security Group esteja correto.

#### Diagnóstico (Análise de Causa Raiz)
> O **serviço** do servidor web (ex: Apache `httpd` ou Nginx) não estava em execução na instância. A "casa" (instância) estava de pé, mas o "atendente" (o serviço) não estava trabalhando.

#### O Plano de Tratamento (Resolução)
1.  **Verifique o status do serviço:** Conecte-se à instância e use o `systemctl` para verificar o serviço.
    ```bash
    sudo systemctl status httpd
    ```
2.  **Inicie o serviço (se estiver parado):**
    ```bash
    sudo systemctl start httpd
    ```
3.  **Garanta que ele inicie no boot:** Para evitar que o problema se repita após uma reinicialização.
    ```bash
    sudo systemctl enable httpd
    ```

#### Ferramentas e Pistas Adicionais
* **Pista Principal:** Se o serviço não iniciar, a resposta quase sempre estará nos arquivos de log dele, localizados em `/var/log/httpd/` ou `/var/log/apache2/`.


---
<br>

### <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Arquiteto da Automação: Guia de Operações de Sistema (SysOps) na Nuvem

O papel do "administrador de sistemas" mudou drasticamente com a chegada da nuvem. No passado, o foco era gerenciar servidores individuais. Hoje, o foco é em gerenciar **sistemas inteiros como código**. Isso é o coração do **SysOps (System Operations)** na nuvem.

**Analogia:** Pense na diferença entre um **"artesão construindo uma única casa, tijolo por tijolo"** (o jeito antigo) e um **"engenheiro-chefe de uma construtora de casas pré-fabricadas"** (o jeito SysOps na nuvem).

* **O Artesão:** Cada casa é única, o processo é lento, manual e sujeito a erros.
* **O Engenheiro:** Ele primeiro cria uma **planta baixa digital e perfeita** (o modelo). Uma **fábrica automatizada** lê essa planta e constrói dez casas idênticas, de forma rápida e sem falhas.

---

### <img src="https://api.iconify.design/mdi/recycle-variant.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Foco Central: Infraestrutura Reutilizável

O objetivo principal do SysOps na nuvem é criar **modelos de infraestrutura reutilizáveis**. Em vez de configurar um servidor manualmente, você escreve um "molde" ou uma "receita" que descreve como o servidor, a rede e a segurança devem ser.

Este "molde" passa por um ciclo de vida completo, assim como um software:
1.  **Criação:** Escrever o código do modelo (a "planta baixa").
2.  **Teste:** Usar o modelo para criar um ambiente de teste e validar se tudo funciona.
3.  **Implantação (Deploy):** Usar o modelo para criar o ambiente de produção.
4.  **Monitoramento:** Observar a saúde e a performance do ambiente.
5.  **Manutenção:** Se uma atualização for necessária, você **atualiza o modelo**, não o servidor diretamente.
6.  **Proteção:** A segurança é definida no modelo desde o início.

---

### <img src="https://api.iconify.design/mdi/robot-industrial-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Os 3 Benefícios da Automação na Nuvem

Ao tratar sua infraestrutura como código, você ganha superpoderes.

#### 1. <img src="https://api.iconify.design/mdi-content-copy.svg?color=currentColor" width="18" /> Implantação Repetível
* **A Dor que Resolve:** O famoso "mas funcionava na minha máquina!". Inconsistências entre os ambientes de desenvolvimento, teste e produção são a principal causa de bugs.
* **A Solução:** Ao usar o mesmo "molde" (script ou template) para criar todos os ambientes, você garante que eles sejam **100% idênticos**, eliminando essa classe de problemas.

#### 2. <img src="https://api.iconify.design/mdi/file-document-outline.svg?color=currentColor" width="18" /> Sistemas Autodescritivos
* **A Dor que Resolve:** "Ninguém sabe como este servidor foi configurado; o cara que o montou saiu da empresa há 5 anos."
* **A Solução:** O **código é a documentação**. A "planta baixa" (o template do CloudFormation, por exemplo) é a fonte única e indiscutível da verdade sobre como sua infraestrutura está configurada.

#### 3. <img src="https://api.iconify.design/mdi/shield-check-outline.svg?color=currentColor" width="18" /> Sistemas Seguros e Bem Testados
* **A Dor que Resolve:** A segurança ser uma "etapa final" e muitas vezes esquecida.
* **A Solução:** As regras de segurança (como as configurações de firewall e permissões de IAM) são **definidas no código**. Isso significa que a segurança é parte do design desde o início e é aplicada de forma consistente em toda nova implantação.

---

### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> As Ferramentas do Engenheiro SysOps na AWS

Para transformar esses conceitos em realidade, um profissional de SysOps na AWS usa um conjunto de ferramentas de automação:

* **<img src="https://api.iconify.design/logos/aws-cloudformation.svg?color=currentColor" width="18" /> AWS CloudFormation:**
    * **O que é?** A principal ferramenta para criar as "plantas baixas" da sua infraestrutura (Infraestrutura como Código). Você descreve todos os seus recursos (EC2, VPC, RDS, etc.) em um arquivo de modelo (template), e o CloudFormation constrói tudo para você.

* **<img src="https://api.iconify.design/logos/aws-systems-manager.svg?color=currentColor" width="18" /> AWS Systems Manager:**
    * **O que é?** O "canivete suíço" para **manter e operar** sua frota de instâncias EC2 *depois* de construída.
    * **Para que serve?** Para automatizar tarefas como aplicação de patches de segurança, execução de comandos em múltiplos servidores e manter um estado de configuração consistente.

* **<img src="https://api.iconify.design/logos/aws-codepipeline.svg?color=currentColor" width="18" /> AWS CodePipeline (e todo o CodeSuite):**
    * **O que é?** A "esteira rolante da fábrica" que automatiza o processo de testar e implantar as atualizações na sua "planta baixa" (seu código de infraestrutura).

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova Cloud Practitioner, entenda o conceito de **implantações automatizadas e repetíveis** como um benefício chave da nuvem.
> * Saiba que o **AWS CloudFormation** é o serviço principal para **Infraestrutura como Código**.
> * Saiba que o **AWS Systems Manager** é a ferramenta principal para **automação operacional** em frotas de instâncias EC2.
