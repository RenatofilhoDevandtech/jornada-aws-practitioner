# <img src="https://api.iconify.design/mdi/file-chart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Diário de Bordo do Servidor: Dominando a Análise de Logs

Todo sistema Linux é como um navio em alto mar, e você é o Capitão. Como saber se os motores estão funcionando bem, se a tripulação está seguindo as ordens ou se uma tempestade se aproxima? Você consulta o **Diário de Bordo**: os **arquivos de log**.

Os logs são o registro cronológico de tudo que acontece no seu servidor. Aprender a lê-los e interpretá-los é a sua ferramenta mais poderosa para diagnosticar problemas, monitorar a segurança e entender a saúde da sua instância EC2.

---

### <img src="https://api.iconify.design/mdi/bookshelf.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Estante do Capitão: Onde Encontrar os Logs

Quase todos os "diários de bordo" do seu sistema são guardados em um único lugar, o diretório `/var/log`.

**Por que `/var`?** Porque é o diretório para arquivos de conteúdo **var**iável, e os logs crescem e mudam constantemente.

#### <img src="https://api.iconify.design/mdi/book-open-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Os Diários Mais Importantes

| Arquivo de Log | O que ele Conta? (A História) |
| :--- | :--- |
| **/var/log/syslog** (Debian/Ubuntu) ou **/var/log/messages** (Red Hat/Amazon Linux) | O **Diário Principal**. Um registro geral de quase tudo que acontece no sistema. |
| **/var/log/auth.log** (Debian/Ubuntu) ou **/var/log/secure** (Red Hat/Amazon Linux) | O **Livro de Portaria**. Registra todas as tentativas de login (bem-sucedidas e falhas) e o uso do `sudo`. |
| **/var/log/boot.log** | A **Narrativa da Partida**. Registra as mensagens do processo de inicialização do sistema. |
| **/var/log/kern.log** | O **Diário da Sala de Máquinas**. Contém mensagens diretas do "Chef" (Kernel). |
| **/var/log/httpd/** ou **/var/log/apache2/** ou **/var/log/nginx/** | O **Diário da Cozinha (Servidor Web)**. Cada servidor web tem sua própria pasta com logs de acesso e de erros. |

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** A prova adora perguntar onde encontrar logs de autenticação. Lembre-se da diferença: **`auth.log`** é para a família **Debian/Ubuntu**. **`secure`** é para a família **Red Hat/Amazon Linux**.

---

### <img src="https://api.iconify.design/mdi/alert-decagram-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Linguagem do Diário: Entendendo os Níveis de Log

As mensagens de log não são todas iguais; elas têm um nível de severidade.

**Analogia:** Pense nos níveis de alerta do Capitão.

| Nível | Nome | O que Significa? (Linguagem do Capitão) |
| :---: | :--- | :--- |
| **7** | `DEBUG` | "Anotando a temperatura exata de cada parafuso do motor." (Informação ultra-detalhada para desenvolvedores). |
| **6** | `INFO` | "Céu azul, mar calmo, velocidade de 15 nós." (Eventos normais e informativos). |
| **5** | `NOTICE` | "Navio avistado no horizonte." (Evento normal, mas que vale a pena notar). |
| **4** | `WARN` | "Nuvens de tempestade se formando a bombordo." (Um aviso; algo pode dar errado se nada for feito). |
| **3** | `ERROR` | "Problema detectado no motor 3!" (Um erro não-crítico que precisa de atenção). |
| **2** | `CRITICAL`| "Vazamento no casco!" (Um erro crítico; o sistema pode parar de funcionar). |
| **1** | `ALERT` | "Fogo na sala de máquinas!" (Uma ação imediata é necessária). |
| **0** | `EMERGENCY`| **"ABANDONAR O NAVIO!"** (O sistema está inutilizável). |

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** Quando você configura um nível de log (ex: `WARN`), o sistema registrará mensagens daquele nível **e de todos os níveis mais graves**. Ou seja, ao definir `WARN` (nível 4), você também verá logs de `ERROR`, `CRITICAL`, `ALERT` e `EMERGENCY`.

---

### <img src="https://api.iconify.design/mdi/magnify.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> As Ferramentas de Leitura do Capitão

Ler um arquivo de log de 2GB com `cat` é impossível. Um profissional usa as ferramentas certas.

* **`less`**: A sua **lupa de leitura**. Abre o arquivo e permite navegar para cima e para baixo.
* **`tail -f`: O Monitor em Tempo Real**
    * **Analogia:** "Observar o marinheiro escrevendo no diário em tempo real."
    * **A Dor que Resolve:** "Acabei de reiniciar meu servidor web. Quero ver as mensagens de erro aparecerem ao vivo enquanto testo o site."
    * **Exemplo:** `tail -f /var/log/nginx/error.log`
* **`grep`: A Lente de Aumento Mágica**
    * **Analogia:** Permite encontrar instantaneamente todas as menções à palavra "iceberg" em 20 anos de diários.
    * **A Dor que Resolve:** "Um usuário específico (jdoe) teve uma falha de login. Preciso encontrar todas as atividades dele no log de segurança."
    * **<img src="https://api.iconify.design/logos/aws-ec2.svg?color=currentColor" width="18" /> Exemplo Prático na AWS:** `sudo cat /var/log/secure | grep "jdoe"`

---

### <img src="https://api.iconify.design/mdi/archive-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Arquivando os Diários Antigos: Rotação de Logs

**A Dor:** Arquivos de log podem crescer para sempre, até encher seu disco (volume EBS) e travar seu servidor.

**A Solução:** A **Rotação de Logs** (`logrotate`), um processo automatizado que age como o "arquivista" do navio.
* **O que faz?** Periodicamente (diária, semanal ou mensalmente), o `logrotate`:
    1.  Pega o diário atual (ex: `access.log`).
    2.  Renomeia para `access.log.1`.
    3.  Cria um novo `access.log` vazio.
    4.  Opcionalmente, comprime os diários antigos (`access.log.1.gz`).
    5.  Apaga os diários mais antigos (ex: mantém apenas os últimos 7).

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** A rotação de logs é essencial para a saúde de qualquer servidor de produção. É uma das primeiras coisas que um administrador experiente configura.

---

### <img src="https://api.iconify.design/logos/aws-cloudwatch.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Visão da Sede: Amazon CloudWatch Logs

As ferramentas Linux são ótimas para investigar um único "navio". Mas e se você tem uma frota de 50 "navios" (instâncias EC2)?

**A Dor que Resolve:** A necessidade de **centralizar e analisar** os logs de toda a sua infraestrutura em um único lugar.

* **Analogia:** O CloudWatch Logs é o **"Sistema de Telemetria da Sede da Companhia de Navegação"**.
* **Como Funciona:** Você instala um pequeno "agente" na sua instância EC2, e ele envia todos os seus "diários de bordo" (`/var/log/secure`, etc.) em tempo real para o serviço CloudWatch Logs.
* **Superpoderes:**
    * **Busca Centralizada:** Procure pela palavra "ERROR" em todos os seus 50 servidores de uma vez.
    * **Alarmes:** Crie uma regra: "Se a palavra 'FATAL' aparecer mais de 10 vezes em 5 minutos em qualquer um dos meus servidores, me envie um SMS!".
    * **Retenção de Longo Prazo:** Guarde seus logs por anos de forma segura e barata.