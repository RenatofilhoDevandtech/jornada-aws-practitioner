# <img src="https://api.iconify.design/mdi/siren-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Alarme Soou: Guia Prático da Fase de Resposta a Incidentes

As muralhas da prevenção são fortes, e os alarmes da detecção são sensíveis. Mas devemos sempre operar com o princípio de que, um dia, um atacante determinado **vai** conseguir passar.

A fase de **Resposta** não é sobre o "se", mas sobre o "quando". Ter um plano claro, treinado e eficiente para responder a um incidente de segurança é o que diferencia um pequeno susto de uma catástrofe que pode paralisar o negócio.

**Analogia:** Pense no **"Protocolo de Defesa do Castelo Durante um Ataque"**. O sino de alarme da muralha começou a tocar. O caos não é uma opção. Cada guarda sabe exatamente o que fazer, porque eles treinaram para este momento.

---

### <img src="https://api.iconify.design/mdi/clipboard-check-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Regra de Ouro: A Preparação é Tudo

**A Dor que a Preparação Resolve:** O pânico, a desorganização e a tomada de decisões erradas no calor do momento.

**Analogia:** **Você não elabora o plano de evacuação durante o incêndio.** Você o define, treina e simula com antecedência. A preparação é a etapa mais importante de toda a resposta a incidentes.

#### <img src="https://api.iconify.design/mdi/list-box-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> O que um bom plano de preparação inclui?
* **<img src="https://api.iconify.design/mdi/file-document-outline.svg?color=currentColor" width="16" /> Políticas e Processos:** Ter um **Plano de Resposta a Incidentes** escrito. Este documento é o seu manual de batalha. Ele define:
    * Quem são os responsáveis (a "equipe de crise").
    * Como a comunicação flui (quem notifica quem).
    * Quais são os passos técnicos para cada tipo de incidente.
* **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="16" /> Treinamento:** Realizar "simulacros de ataque" (*fire drills*) para que a equipe saiba exatamente como executar o plano.
* **<img src="https://api.iconify.design/mdi/tools.svg?color=currentColor" width="16" /> Ferramentas:** Garantir que suas ferramentas de detecção e resposta (como CloudTrail, GuardDuty e backups) estejam ativas e configuradas **antes** do incidente.

---

### <img src="https://api.iconify.design/mdi/run-fast.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Protocolo de Batalha: As 5 Fases de uma Resposta

Quando um incidente é detectado, a equipe de resposta segue um processo estruturado.

#### 1. <img src="https://api.iconify.design/mdi/radar.svg?color=currentColor" width="18" /> Identificação
* **O que é?** A confirmação de que o alarme (a notificação do **Amazon GuardDuty**, por exemplo) é real e não um alarme falso. Os analistas investigam o alerta para entender a natureza e a gravidade da ameaça.

#### 2. <img src="https://api.iconify.design/mdi/wall.svg?color=currentColor" width="18" /> Contenção
* **O Objetivo:** **ESTANCAR O SANGRAMENTO.** A prioridade máxima é impedir que o ataque se espalhe e cause mais danos.
* **Analogia:** "Fechar o portão do setor oeste e baixar a ponte levadiça para isolar os invasores!"
* **<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> **Ações Imediatas na AWS:**
    * Isolar a instância EC2 comprometida alterando seu **Security Group** para bloquear todo o tráfego.
    * Desabilitar um **usuário IAM** cujas credenciais foram vazadas.
    * Rotacionar imediatamente as **Chaves de Acesso** que possam ter sido expostas.

#### 3. <img src="https://api.iconify.design/mdi/broom.svg?color=currentColor" width="18" /> Erradicação
* **O Objetivo:** Remover completamente a ameaça do seu ambiente.
* **Analogia:** "Expulsar os invasores do pátio e garantir que não deixaram nenhuma armadilha para trás."
* **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> O Superpoder da Nuvem (Infraestrutura Imutável):** No mundo tradicional, você passaria dias tentando "limpar" um servidor infectado. Na nuvem, a melhor prática é tratar a infraestrutura como descartável.
    * **Ação Correta na AWS:** **NÃO TENTE LIMPAR A INSTÂNCIA.** **TERMINE-A**. Depois, lance uma nova instância a partir de uma AMI (Imagem de Máquina) limpa e conhecida. É mais rápido, mais seguro e garante 100% que a ameaça foi eliminada.

#### 4. <img src="https://api.iconify.design/mdi/backup-restore.svg?color=currentColor" width="18" /> Recuperação
* **O Objetivo:** Restaurar os serviços para a operação normal de forma segura.
* **Analogia:** "Consertar o portão danificado e reabrir para os cidadãos de forma ordenada."
* **<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> **Ações na AWS:**
    * Restaurar os dados a partir de um **Snapshot de EBS** ou do **AWS Backup**.
    * Validar que o novo sistema está limpo, com os patches aplicados e funcionando corretamente antes de direcionar o tráfego de produção para ele.

#### 5. <img src="https://api.iconify.design/mdi/magnify-plus-outline.svg?color=currentColor" width="18" /> Lições Aprendidas
* **O Objetivo:** Analisar a causa raiz do incidente e usar esse conhecimento para melhorar a fase de **Prevenção**.
* **Analogia:** A "análise pós-batalha". "Como os invasores passaram pelo portão oeste? Precisamos de mais guardas? A tranca era fraca?".
* **Ação:** Realizar um "post-mortem" sem culpas, focado em fortalecer as defesas para que aquele tipo de ataque não aconteça novamente.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova, você não precisa ser um expert em resposta a incidentes, mas precisa conhecer a lógica e as ferramentas da AWS:
> * A primeira ação ao detectar uma instância comprometida é **contê-la**, e a ferramenta para isso é o **Security Group**.
> * A melhor forma de **recuperar** um sistema é através de **backups**, como os **Snapshots de EBS**.
> * A abordagem de **erradicação** na nuvem prefere **substituir** (terminar e lançar de novo) em vez de reparar.

---

### <img src="https://api.iconify.design/mdi/hospital-building.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Planejando para o Pior: Guia de Continuidade e Recuperação de Desastres

"Não é uma questão de *se* um desastre vai acontecer, mas *quando*." Esta é a mentalidade de um profissional de segurança e infraestrutura. Um desastre pode ser qualquer coisa: um incêndio no data center, um ataque de ransomware, uma falha de hardware crítica ou um erro humano catastrófico.

As empresas que sobrevivem a esses eventos são aquelas que se prepararam com dois manuais essenciais: o BCP e o DRP.

---

### <img src="https://api.iconify.design/mdi/ambulance.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. Continuidade vs. Recuperação (A Diferença Crucial)

Embora parecidos, BCP e DRP têm missões diferentes.

#### Plano de Continuidade de Negócios (BCP)
* **Pergunta que responde:** "Como nós continuamos operando **DURANTE** uma crise?"
* **Analogia:** O **"Protocolo de Atendimento de Emergência"** do hospital. Quando um grande acidente acontece na cidade, o BCP é ativado. Ele dita as regras para operar em modo de crise: "Todas as cirurgias não-urgentes são canceladas; a energia muda para os geradores de backup; focamos apenas nas funções críticas para salvar vidas."
* **Foco:** Processos de negócio, pessoas e operações essenciais.

#### Plano de Recuperação de Desastres (DRP)
* **Pergunta que responde:** "Como nós nos recuperamos **APÓS** a catástrofe?"
* **Analogia:** O **"Plano de Reconstrução do Hospital Pós-Terremoto"**. O hospital principal foi destruído. O DRP é o plano passo a passo para voltar ao normal: "1. Transfira os pacientes para o hospital de campanha. 2. Restaure os sistemas a partir dos backups. 3. Inicie a reconstrução."
* **Foco:** A tecnologia, os sistemas de TI e os dados.

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** O **DRP é um subconjunto do BCP**. O plano de recuperação da TI (DRP) é uma parte crítica do plano geral para manter o negócio funcionando (BCP).

---

### <img src="https://api.iconify.design/mdi/clock-fast.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Linguagem da Recuperação (RTO e RPO)

Todo DRP é definido por duas métricas de negócio cruciais. Elas ditam o quão rápida e completa a recuperação precisa ser.

* **<img src="https://api.iconify.design/mdi/timer-sand.svg?color=currentColor" width="18" /> RTO (Recovery Time Objective - Objetivo de Tempo de Recuperação):**
    * **Pergunta:** "Em **quanto tempo**, no máximo, nosso sistema precisa estar online novamente após o desastre?"
    * **Analogia:** "O cronômetro da emergência." É uma medida de **TEMPO**.
    * **Exemplo:** Um RTO de 2 horas significa que o negócio não pode ficar mais de 2 horas fora do ar.

* **<img src="https://api.iconify.design/mdi/database-clock-outline.svg?color=currentColor" width="18" /> RPO (Recovery Point Objective - Objetivo de Ponto de Recuperação):**
    * **Pergunta:** "Qual a **quantidade máxima de dados** que podemos aceitar perder?"
    * **Analogia:** "A tolerância à perda de memória." É uma medida de **DADOS** (tempo de perda de dados).
    * **Exemplo:** Um RPO de 15 minutos significa que, no pior caso, perderemos os dados gerados nos últimos 15 minutos antes do desastre. Isso dita que precisamos de um backup a cada 15 minutos, no mínimo.

> **<img src="https://api.iconify.design/mdi/cash-multiple.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> O HACK FINANCEIRO:** RTO e RPO definem o **custo** da sua solução de DR. Quanto mais próximos de zero eles forem, **exponencialmente mais cara** será a solução.

---

### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. Estratégias de Recuperação na AWS

A nuvem AWS tornou a recuperação de desastres, antes um luxo para grandes corporações, acessível a todos. Aqui estão as estratégias mais comuns, da mais barata/lenta à mais cara/rápida.

| Estratégia | RTO / RPO | Como Funciona na AWS |
| :--- | :--- | :--- |
| **1. Backup e Restauração** | **Horas a Dias** | Você faz backups regulares dos seus dados (ex: **Snapshots de EBS**, **AWS Backup**) e os armazena em um **Amazon S3** em outra Região. Em caso de desastre, você "restaura" esses backups manualmente na nova Região. |
| **2. Piloto de Chamas (Pilot Light)** | **Dezenas de Minutos a Horas** | Você mantém uma cópia **mínima** da sua infraestrutura (ex: um servidor pequeno) sempre ligada na Região de DR. Os dados são replicados. Em caso de desastre, você "acende a chama": aumenta o tamanho dos servidores e aponta o DNS (**Route 53**) para lá. |
| **3. Espera Quente (Warm Standby)**| **Minutos** | Você mantém uma versão **em escala reduzida, mas totalmente funcional**, da sua infraestrutura sempre rodando na Região de DR. A recuperação é mais rápida, pois os sistemas já estão ligados. |
| **4. Multi-Site (Ativo-Ativo)** | **Segundos ou Zero** | Sua aplicação roda **simultaneamente e com capacidade total** em múltiplas Regiões. O **Amazon Route 53** gerencia o tráfego. Se uma Região falhar, o tráfego é **automaticamente** redirecionado para a outra, sem que o usuário perceba. |

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova, você **precisa** saber a definição de **RTO** (tempo para recuperar) e **RPO** (quantidade de dados perdidos). Eles adoram questões de cenário que pedem para você identificar a estratégia de DR correta (Backup & Restore, Pilot Light, etc.) com base nos requisitos de RTO/RPO de uma empresa.

---

### <img src="https://api.iconify.design/mdi/hospital-building.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Planejando para o Pior: Guia de Continuidade e Recuperação de Desastres na AWS

No último guia, vimos o protocolo de resposta a um incidente de segurança. Agora, vamos ampliar o escopo: o que fazer quando o "incidente" é uma catástrofe que afeta toda a sua operação, como a falha completa de um data center?

É aqui que entram os planos de **Continuidade de Negócios (BCP)** e **Recuperação de Desastres (DRP)**. Eles são o seu manual de sobrevivência corporativa.

---

### <img src="https://api.iconify.design/mdi/clock-fast.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Linha do Tempo Completa da Recuperação

Para planejar a recuperação, precisamos de um vocabulário preciso para o tempo.

* **RTO (Recovery Time Objective - Objetivo de Tempo de Recuperação):**
    * **A Pergunta:** "Em **quanto tempo** o sistema precisa estar de volta ao ar?"
    * **Analogia:** "Em quanto tempo a sala de cirurgia de emergência precisa estar funcionando?" (É uma meta de **TEMPO**).
* **RPO (Recovery Point Objective - Objetivo de Ponto de Recuperação):**
    * **A Pergunta:** "Qual a **quantidade máxima de dados** que podemos perder?"
    * **Analogia:** "Quantos minutos de anotações médicas podemos nos dar ao luxo de perder?" (É uma meta de **DADOS**).
* **WRT (Work Recovery Time - Tempo de Recuperação do Trabalho):**
    * **O que é?** O tempo necessário **após** a restauração do sistema para validar os dados e processos antes de liberar o acesso aos usuários.
    * **Analogia:** "A sala de cirurgia está montada (RTO atingido). Agora, quanto tempo leva para testar os equipamentos e preparar a equipe antes da primeira cirurgia?"
* **MTD (Maximum Tolerable Downtime - Tempo Máximo de Inatividade Tolerável):**
    * **O que é?** O tempo total que o negócio aguenta ficar parado. É a soma: **MTD = RTO + WRT**.

---

### <img src="https://api.iconify.design/mdi/backup-restore.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. As Tecnologias de Recuperação: Backup vs. Replicação

* **Backup (Ex: Snapshots):**
    * **O que é?** Uma "fotografia" dos seus dados em um ponto específico no tempo.
    * **Foco:** Ideal para recuperação de longo prazo, arquivamento e para se proteger contra corrupção de dados (você pode voltar para uma "foto" de ontem, antes do problema). Melhora o **RPO**.
* **Replicação (Ex: Replicação Contínua):**
    * **O que é?** Manter uma cópia "espelhada" e quase em tempo real dos seus dados em outro local.
    * **Foco:** Ideal para recuperação rápida de falhas. Melhora o **RTO**.

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO (Sombreamento de Banco de Dados):** Uma técnica avançada de replicação é o "Database Shadowing". É exatamente isso que serviços como o **Amazon RDS (com Multi-AZ)** fazem para você: eles mantêm uma cópia "sombra" e sincronizada do seu banco de dados em outra Zona de Disponibilidade, pronta para assumir em caso de falha.

---

### <img src="https://api.iconify.design/mdi/chart-line.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Cardápio da Resiliência: Estratégias de DR na AWS

A beleza da nuvem é que você pode escolher o nível de resiliência que seu bolso e seu negócio exigem. Existe uma compensação direta: quanto mais rápido o RTO/RPO, mais caro.

#### Traduzindo os Termos: Cold, Warm e Hot Sites na AWS

| Termo Tradicional | Estratégia de DR na AWS | RTO / RPO | Custo | Analogia (Hospital) |
| :--- | :--- | :---: | :---: | :--- |
| **Local Frio (Cold Site)** | **Backup e Restauração** | **Horas a Dias** | **$** | Um **armazém vazio** em outra cidade. Leva tempo para montar tudo do zero. |
| **Local Morno (Warm Site)**| **Piloto de Chamas (Pilot Light)** ou **Espera Quente (Warm Standby)** | **Minutos a Horas**| **$$** | Um **pequeno ambulatório** que já tem a infraestrutura básica e pode ser expandido rapidamente. |
| **Local Quente (Hot Site)**| **Multi-Site (Ativo-Ativo)** | **Segundos ou Zero**| **$$$$**| Um **hospital-irmão idêntico**, já operando com capacidade total em outra cidade. |

#### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> Como Implementar na AWS:
* **Backup e Restauração:** Use o **AWS Backup** para agendar **Snapshots de EBS** e backups de **RDS**, salvando-os no **Amazon S3** (e **S3 Glacier** para longo prazo, o substituto moderno das "fitas").
* **Piloto de Chamas / Espera Quente:** Mantenha uma infraestrutura mínima rodando em outra Região, com os dados sendo replicados continuamente usando, por exemplo, **RDS Read Replicas** entre regiões.
* **Multi-Site:** Configure sua aplicação para rodar em duas ou mais Regiões simultaneamente, usando o **Amazon Route 53** com políticas de roteamento de failover ou baseadas em latência para distribuir o tráfego.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova, os conceitos mais importantes são:
> 1.  A definição de **RTO (tempo)** e **RPO (dados)**.
> 2.  As **4 estratégias de DR na AWS** (Backup & Restore, Pilot Light, Warm Standby, Multi-Site) e saber qual é a mais barata/lenta e qual é a mais cara/rápida.
> 3.  A diferença entre **Multi-AZ** (que é para **Alta Disponibilidade** dentro de uma Região) e **Multi-Região** (que é para **Recuperação de Desastres**).

É fundamental **testar** seu plano de DRP regularmente. Um plano que nunca foi testado é apenas um documento de boas intenções.

---
### <img src="https://api.iconify.design/mdi/backup-restore.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Rede de Segurança Digital: Guia Prático de Backups na AWS

Quando todas as outras defesas falham, quando um desastre acontece ou um ransomware criptografa seus dados, sua última e mais importante linha de defesa é o seu **backup**. Ter uma estratégia de backup sólida não é apenas uma boa prática; é o que garante a sobrevivência do seu negócio.

Pense nisso como a **estratégia de backup de um fotógrafo profissional**. Ele não apenas salva as fotos em seu computador; ele tem um sistema para garantir que, aconteça o que acontecer — roubo, incêndio, falha de disco — as fotos insubstituíveis de seus clientes estarão seguras.

---

### <img src="https://api.iconify.design/mdi/content-copy.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. As 3 Estratégias de Cópia (Full vs. Incremental vs. Diferencial)

**A Dor que Isso Resolve:** Fazer uma cópia completa de terabytes de dados todos os dias é lento, caro e consome muitos recursos. Por isso, existem estratégias mais inteligentes.

| Tipo de Backup | Como Funciona? (Analogia do Fotógrafo) | Vantagem | Desvantagem |
| :--- | :--- | :--- | :--- |
| **Completo (Full)** | "No domingo, copio **TODAS as 5.000 fotos** do evento." | Restauração simples e rápida (só precisa de um arquivo). | Lento para fazer, ocupa muito espaço. |
| **Incremental** | "Na segunda, copio **apenas as 10 fotos que editei hoje**."<br/>"Na terça, copio **apenas as 15 fotos que editei hoje**." | Backup muito rápido e ocupa pouco espaço. | Restauração complexa e lenta (precisa do backup completo + todos os incrementais em ordem). |
| **Diferencial** | "Na segunda, copio **tudo que mudou desde domingo (as 10 fotos)**."<br/>"Na terça, copio **tudo que mudou desde domingo (as 10 de segunda + as 15 de terça)**." | Restauração mais rápida que o incremental (só precisa do completo + o último diferencial). | Ocupa mais espaço que o incremental. |

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO (O Jeito da AWS):** Serviços modernos como os **Snapshots do Amazon EBS** são inteligentes. Por baixo dos panos, eles são **incrementais** (só copiam os blocos de dados que mudaram desde o último snapshot, economizando tempo e dinheiro), mas para você, eles se apresentam como se fossem um **backup completo**, permitindo uma restauração rápida e simples. Você tem o melhor dos dois mundos!

---

### <img src="https://api.iconify.design/mdi/playlist-check.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Manual de Boas Práticas (Traduzido para a Nuvem)

Vamos pegar as práticas recomendadas tradicionais e ver como a AWS as torna mais fáceis.

* **Prática Tradicional:** Usar armazenamento remoto (*off-site*).
    * **<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> **Na AWS:** Por padrão, um backup no **Amazon S3** já é "remoto" e replicado em múltiplos data centers. Para a máxima proteção contra desastres, configure a **Replicação Entre Regiões (Cross-Region Replication)** para ter uma cópia do seu backup em outra parte do mundo.

* **Prática Tradicional:** Executar backups frequentes.
    * **<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> **Na AWS:** Use o **AWS Backup** para criar planos de backup automatizados que rodam em uma agenda (ex: de hora em hora, diariamente, etc.), sem intervenção manual.

* **Prática Tradicional:** Criptografar os arquivos de backup.
    * **<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> **Na AWS:** Ao criar um backup no **AWS Backup** ou um snapshot, basta marcar uma caixa de seleção para criptografá-lo com chaves gerenciadas pelo **AWS KMS**.

* **Prática Tradicional:** Usar matrizes RAID para proteger contra falha de disco.
    * **<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> **Na AWS:** **Você não precisa se preocupar com isso!** Serviços como **Amazon EBS** e **Amazon S3** já são construídos sobre uma infraestrutura redundante que protege seus dados contra falhas de hardware por baixo dos panos. A AWS gerencia o "RAID" para você.

* **Prática Tradicional:** Usar múltiplas soluções (pilha de backup).
    * **<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> **Na AWS:** Siga a **Regra de Backup 3-2-1**: tenha **3** cópias dos seus dados, em **2** mídias diferentes, com **1** cópia sendo *off-site*.
        1.  Dados em produção no seu volume **EBS**.
        2.  Um snapshot diário no **Amazon S3** (mídia diferente).
        3.  Uma cópia desse snapshot em **outra Região da AWS** (a cópia *off-site*).

---

### <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. A Ferramenta Mestra: AWS Backup

**A Dor que Resolve:** Gerenciar agendas de backup para múltiplos serviços (EC2, EBS, RDS, EFS, DynamoDB) em locais diferentes é complexo.

* **O que é?** O **AWS Backup** é o seu **"gerente de backups centralizado"**.
* **Como Funciona:** A partir de um único painel, você cria "Planos de Backup" que definem:
    * **Com que frequência** o backup será feito (ex: a cada 12 horas).
    * **Por quanto tempo** o backup será retido (ex: reter backups diários por 30 dias).
    * **Para onde** o backup será copiado (ex: copiar para outra Região para DR).
    * **Quais recursos** serão protegidos por este plano (você pode aplicar um plano a todos os recursos com uma tag específica, ex: `Backup: Diário`).

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Saiba a diferença entre backups **Full, Incremental e Differential**.
> 2.  Entenda que **Snapshots de EBS** são a forma principal de fazer backup de instâncias EC2.
> 3.  Conheça o **AWS Backup** como o serviço **centralizado e automatizado** para gerenciar as políticas de backup na AWS.