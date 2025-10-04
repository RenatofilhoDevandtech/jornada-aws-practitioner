# <img src="https://api.iconify.design/logos/aws-cloudwatch.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: Os Olhos e Ouvidos da Nuvem - Monitorando Aplicações e Infraestrutura

### O Cenário (A "User Story")

> **Como** um engenheiro de operações (SysOps), **EU QUERO** instalar um sistema de monitoramento completo em meus servidores, **PARA QUE** eu possa coletar logs, medir a performance do sistema (como uso de memória), ser alertado sobre problemas e garantir que minha infraestrutura esteja em conformidade com as regras da empresa.

### A Dor que o Lab Resolve

1.  **A Cegueira:** Por padrão, a AWS não te dá métricas de dentro do servidor, como uso de memória ou espaço em disco. Sem isso, você está "voando às cegas".
2.  **Caça aos Logs:** Procurar por erros em arquivos de log, conectando-se a múltiplos servidores, é lento e ineficiente.
3.  **Reação Lenta:** Descobrir um problema horas depois que ele aconteceu é tarde demais. Você precisa de alertas em tempo real.
4.  **Desvio de Configuração:** Como garantir que todos os seus recursos sigam as regras de segurança e governança da empresa?

Este laboratório mostra como o ecossistema de monitoramento da AWS resolve todas essas dores.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Instalar o **Agente do CloudWatch** usando o AWS Systems Manager.
* [ ] Centralizar e monitorar **Logs de Aplicação** com o CloudWatch Logs.
* [ ] Criar **Filtros de Métrica** e **Alarmes** a partir dos logs.
* [ ] Coletar **Métricas do Sistema** (memória, disco) com o Agente.
* [ ] Criar **Notificações em Tempo Real** com o Amazon EventBridge.
* [ ] Acompanhar a **conformidade da infraestrutura** com o AWS Config.


---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Instalando os "Sensores Avançados" (O Agente do CloudWatch)

**Analogia:** O monitoramento padrão do EC2 te dá a "temperatura do motor". O **Agente do CloudWatch** é o "pacote de telemetria completo" que você instala para ver a pressão do óleo (memória), o nível do combustível (espaço em disco) e ouvir o que a aplicação está "falando" (os logs).

1.  **Instale o Agente via Systems Manager:**
    * No Console da AWS, navegue até o serviço **Systems Manager**.
    * No menu esquerdo, selecione `Executar comando (Run Command)`.
    * Clique em `Executar um comando (Run a command)`.
    * Selecione o documento `AWS-ConfigureAWSPackage`.
    * Em `Parâmetros de comando (Command parameters)`:
        * **Ação (Action):** `Instalar (Install)`.
        * **Nome (Name):** `AmazonCloudWatchAgent`.
        * **Versão (Version):** `latest`.
    * Em `Destinos (Targets)`, selecione `Escolher instâncias manualmente (Choose instances manually)` e marque a instância `Web Server`.
    * Clique em `Executar (Run)` e aguarde o status `Com êxito (Success)`.
2.  **Crie o Arquivo de Configuração do Agente:**
    * No menu do Systems Manager, vá para `Armazenamento de parâmetros (Parameter Store)`.
    * Clique em `Criar parâmetro (Create parameter)`.
    * **Nome (Name):** `Monitor-Web-Server`.
    * **Valor (Value):** Cole o seguinte bloco de código JSON no campo `Valor (Value)`:
    ```json
    {
        "logs": {
            "logs_collected": {
                "files": {
                    "collect_list": [
                        {
                            "log_group_name": "HttpAccessLog",
                            "file_path": "/var/log/httpd/access_log",
                            "log_stream_name": "{instance_id}",
                            "timestamp_format": "%b %d %H:%M:%S"
                        },
                        {
                            "log_group_name": "HttpErrorLog",
                            "file_path": "/var/log/httpd/error_log",
                            "log_stream_name": "{instance_id}",
                            "timestamp_format": "%b %d %H:%M:%S"
                        }
                    ]
                }
            }
        },
        "metrics": {
            "metrics_collected": {
                "cpu": {
                    "measurement": [ "cpu_usage_idle", "cpu_usage_iowait", "cpu_usage_user", "cpu_usage_system" ],
                    "metrics_collection_interval": 10,
                    "totalcpu": false
                },
                "disk": {
                    "measurement": [ "used_percent", "inodes_free" ],
                    "metrics_collection_interval": 10,
                    "resources": [ "*" ]
                },
                "diskio": {
                    "measurement": [ "io_time" ],
                    "metrics_collection_interval": 10,
                    "resources": [ "*" ]
                },
                "mem": {
                    "measurement": [ "mem_used_percent" ],
                    "metrics_collection_interval": 10
                },
                "swap": {
                    "measurement": [ "swap_used_percent" ],
                    "metrics_collection_interval": 10
                }
            }
        }
    }
    ```
     > **O "Porquê" deste JSON:** Este arquivo é a "programação" do nosso sensor. Ele diz ao agente: "1. Escute os arquivos de log de acesso e de erro do Apache. 2. A cada 10 segundos, colete as métricas de CPU, disco, I/O de disco e memória."
    * Clique em `Criar parâmetro`.
3.  **Inicie o Agente com a Nova Configuração:**
    * Volte para o `Run Command`.
    * Desta vez, procure e selecione o documento `AmazonCloudWatch-ManageAgent`.
    * Em `Parâmetros de comando`:
        * **Ação (Action):** `configurar (configure)`.
        * **Origem da configuração (Optional configuration source):** `ssm`.
        * **Local da configuração (Optional configuration location):** `Monitor-Web-Server` (o nome do parâmetro que criamos).
    * Selecione a instância `Web Server` como alvo e clique em `Executar (Run)`.

#### Tarefa 2: Os "Ouvidos" da Nuvem (Monitorar Logs da Aplicação)

**Analogia:** Agora que os "microfones" (o Agente) estão instalados e configurados, vamos para a "sala de controle de áudio" (**CloudWatch Logs**) ouvir o que está acontecendo.

1.  **Gere Tráfego e Erros:**
    * Nos detalhes do seu laboratório, copie o valor de `WebServerIP`.
    * Acesse `http://<WebServerIP>` no seu navegador. Você verá a página de teste.
    * Agora, gere um erro acessando uma página que não existe: `http://<WebServerIP>/start`.
2.  **Analise os Logs:**
    * Vá para o serviço **CloudWatch**.
    * No menu esquerdo, selecione `Grupos de logs (Log Groups)`.
    * Você verá dois novos grupos: `HttpAccessLog` e `HttpErrorLog`.
    * Clique em `HttpAccessLog` e, em seguida, no `Fluxo de logs (Log Stream)` que aparecer. Você verá a gravação de todas as visitas ao seu site, incluindo a sua tentativa de acessar `/start`, que resultou em um status `404`.
3.  **Crie um Filtro de Métrica (O "Detector de Palavras-Chave"):**
    * Selecione o grupo de logs `HttpAccessLog`.
    * Em **Ações (Actions)**, selecione `Criar filtro de métrica (Create metric filter)`.
    * **Padrão de filtro (Filter pattern):** `[ip, id, user, timestamp, request, status_code=404, size]`
        > **O "Porquê":** Estamos ensinando o CloudWatch a ler o formato do log do Apache e a "prestar atenção" apenas nas linhas onde o código de status é `404`.
    * Teste o padrão e clique em **Próximo (Next)**.
    * **Nome do filtro:** `404Errors`.
    * **Namespace da métrica:** `LogMetrics`.
    * **Nome da métrica:** `404Errors`.
    * **Valor da métrica:** `1` (conte "1" para cada ocorrência).
    * Clique em **Criar filtro de métrica**.
4.  **Crie um Alarme a partir do Filtro:**
    * Na tela do filtro que você acabou de criar, clique em **Criar alarme (Create alarm)**.
    * **Condições (Conditions):** Configure para disparar `Sempre que 404Errors for... Maior que/igual a (Greater/Equal)` `5`, em um período de `1 Minuto`.
    * **Notificação (Notification):** Crie um **novo tópico do SNS**, dê um nome e insira seu e-mail.
    * Dê um nome ao alarme (`Alarme-Erros-404`) e finalize a criação.
    * **Ação Crítica:** Não se esqueça de **confirmar a inscrição** no e-mail que você receberá do SNS.
5.  **Teste o Alarme:** Volte para o seu site e tente acessar páginas que não existem pelo menos 5 vezes. Em poucos minutos, o alarme no CloudWatch ficará vermelho (`Em alarme (In alarm)`) e você receberá um e-mail de alerta!

#### Tarefa 3: Os "Sensores" em Ação (Monitorar Métricas da Instância)
1.  No console do **CloudWatch**, vá em **Todas as métricas (All metrics)**.
2.  Você verá um novo `Namespace` customizado chamado **CWAgent**.
3.  Clique nele. Você pode agora explorar e criar gráficos para as métricas que o Agente está coletando, como `mem_used_percent` (uso de memória) e `used_percent` (uso de disco), que não estão disponíveis por padrão.

#### Tarefa 4: Os "Reflexos" do Sistema (Notificações em Tempo Real)

**Analogia:** Vamos configurar o "sistema nervoso central do prédio" (**Amazon EventBridge**) para reagir a eventos específicos.

1.  No console do **CloudWatch**, vá em **Eventos (Events) > Regras (Rules)**.
2.  Clique em **Criar regra (Create rule)**.
3.  **Origem do evento (Event Source):**
    * **Nome do serviço:** `EC2`.
    * **Tipo de evento:** `Notificação de alteração do estado da instância do EC2 (EC2 Instance State-change Notification)`.
    * Selecione `Estado(s) específico(s)` e escolha `interrompido (stopped)` e `encerrado (terminated)`.
4.  **Destinos (Targets):**
    * Selecione `Tópico do SNS (SNS topic)`.
    * Escolha o tópico `Default_CloudWatch_Alarms_Topic` (ou o que você criou).
5.  Dê um nome à regra (ex: `Notificar-Parada-Instancia`) e crie.
6.  **Teste:** Vá para o console do **EC2**, selecione sua instância `Web Server` e **Interrompa-a (`Stop instance`)**. Em alguns instantes, você receberá um e-mail com os detalhes do evento.

#### Tarefa 5: O "Auditor Robô" (Monitorar a Conformidade com AWS Config)
1.  Vá para o serviço **AWS Config**.
2.  Siga o assistente de configuração inicial, se necessário.
3.  Vá em **Regras (Rules) > Adicionar regra (Add rule)**.
4.  Procure pela regra gerenciada `required-tags`.
    * Configure-a para verificar se todos os recursos têm uma `tag` com a `Chave (Key)` `project`.
5.  Adicione uma segunda regra, procurando por `ec2-volume-inuse-check`.
    * Esta regra verifica por volumes EBS que não estão anexados a nenhuma instância (um desperdício de dinheiro).
6.  Aguarde alguns minutos para o Config avaliar seus recursos.
7.  **Verificação:** Clique em cada regra para ver os recursos que estão **Em conformidade (Compliant)** e os que estão **Não conformes (Noncompliant)**.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você acaba de construir um sistema de observabilidade completo. Você instalou sensores, centralizou logs, criou alertas inteligentes, monitorou a performance e auditou a conformidade, usando o mesmo conjunto de ferramentas que os profissionais de nuvem usam todos os dias para manter seus ambientes saudáveis e seguros.

