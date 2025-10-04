# <img src="https://api.iconify.design/mdi/piggy-bank-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Cofre da Nuvem: Guia de Gerenciamento de Custos na AWS

Um dos maiores benefícios da nuvem é o modelo de pagamento sob demanda (`pay-as-you-go`). Mas, com grande poder, vem a responsabilidade de gerenciar os custos. A boa notícia é que a AWS nos dá uma caixa de ferramentas completa para sermos os "donos" do nosso orçamento na nuvem.

**Analogia:** Pense em gerenciar seus custos na AWS como **gerenciar seu orçamento doméstico com um aplicativo de finanças**.

---

### <img src="https://api.iconify.design/mdi/lightbulb-off-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Regra de Ouro da Economia: Apague as Luzes!

A forma mais simples e eficaz de economizar dinheiro na nuvem é também a mais óbvia: **desligue os recursos que você não está usando**.

**A Dor que Resolve:** A principal causa de desperdício de dinheiro na nuvem é pagar por recursos ociosos.

#### Oportunidades Comuns de Redução de Custos:
* **<img src="https://api.iconify.design/mdi/laptop.svg?color=currentColor" width="18" /> Ambientes de Desenvolvimento e Teste:** Desligue-os automaticamente à noite e nos fins de semana. Um ambiente de dev ligado 24/7 desperdiça quase 70% do seu custo.
* **<img src="https://api.iconify.design/mdi/server-off.svg?color=currentColor" width="18" /> Instâncias Temporárias:** Crie scripts ou use tags para identificar e encerrar instâncias que foram criadas para uma tarefa específica e não são mais necessárias.

---

### <img src="https://api.iconify.design/mdi/toolbox-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Caixa de Ferramentas do FinOps

A AWS oferece um conjunto de ferramentas para te dar total controle e visibilidade sobre seus gastos.

#### <img src="https://api.iconify.design/mdi/finance.svg?color=currentColor" width="20" /> Painel de Faturamento (Billing Dashboard)
* **Analogia:** A **"tela inicial do seu aplicativo do banco"**.
* **Pergunta que Responde:** "Como estão meus gastos este mês? Qual foi o valor da minha última fatura?"
* **Função Principal:** Te dá uma visão geral rápida dos seus custos atuais, do mês anterior e um detalhamento por serviço.

#### <img src="https://api.iconify.design/mdi/chart-bar.svg?color=currentColor" width="20" /> AWS Cost Explorer
* **Analogia:** O **"Relatório de Análise de Gastos"** detalhado.
* **Pergunta que Responde:** "Para onde foi meu dinheiro no último semestre? Qual projeto ou departamento está gastando mais?"
* **Função Principal:** É a sua ferramenta de **análise e visualização**. Com ele, você pode criar gráficos, filtrar por tags, por serviço ou por tipo de conta, e identificar tendências e anomalias nos seus gastos. Ele te ajuda a entender o **passado**.

#### <img src="https://api.iconify.design/mdi/bell-alert-outline.svg?color=currentColor" width="20" /> AWS Budgets
* **Analogia:** O **"Sistema de Orçamento e Alertas"** do aplicativo.
* **Pergunta que Responde:** "Como eu posso ser avisado *antes* de estourar meu orçamento?"
* **Função Principal:** É a sua ferramenta de **controle proativo**. Você define um orçamento (ex: "não quero gastar mais de US$ 500 este mês") e o AWS Budgets te envia um alerta por e-mail ou SNS quando seus gastos **reais ou previstos** atingem um limite (ex: 80% do orçado). Ele te ajuda a controlar o **futuro**.

#### <img src="https://api.iconify.design/logos/aws-cloudwatch.svg?color=currentColor" width="20" /> Alarmes de Faturamento do CloudWatch
* **Analogia:** Um **"alerta de emergência"** mais simples.
* **Pergunta que Responde:** "Me avise imediatamente se a projeção da minha fatura mensal passar de um valor X."
* **Função Principal:** É uma forma simples de criar um alarme sobre o **total estimado da sua fatura**. Enquanto o AWS Budgets é mais flexível (pode orçar por tag, por uso, etc.), o alarme de faturamento do CloudWatch é uma ótima rede de segurança geral.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** A diferença entre estas ferramentas é um tópico **MUITO IMPORTANTE** para a prova.
> 1.  **Cost Explorer:** Para **VISUALIZAR e ANALISAR** os custos.
> 2.  **AWS Budgets:** Para **DEFINIR ORÇAMENTOS** e receber **ALERTAS** quando os limites são ultrapassados.
> 3.  Lembre-se da prática mais básica de otimização de custos: **desligar recursos ociosos**.

---

### <img src="https://api.iconify.design/mdi/finance.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Extrato Detalhado: Guia Prático das Ferramentas de Custo da AWS

A fatura da AWS não precisa ser uma caixa preta. A AWS nos dá um conjunto completo de ferramentas para transformar dados brutos de faturamento em inteligência de negócio, permitindo que você entenda, controle e otimize seus gastos na nuvem.

**Analogia:** Pense nestas ferramentas como os diferentes módulos do seu **"aplicativo de finanças pessoais"**.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Ciclo de Gerenciamento de Custos

#### <img src="https://api.iconify.design/mdi/view-dashboard-outline.svg?color=currentColor" width="20" /> O Resumo Diário (Painel de Faturamento - Billing Dashboard)
* **Analogia:** A **"Tela Principal (Home Screen)"** do seu app.
* **Pergunta que Responde:** "Como estão meus gastos este mês? Quanto gastei no mês passado e qual é a previsão para este mês?"
* **Função Principal:** Te dar uma visão geral e rápida da saúde financeira da sua conta, incluindo um gráfico dos serviços que mais consomem recursos.

#### <img src="https://api.iconify.design/mdi/file-document-outline.svg?color=currentColor" width="20" /> O Histórico Mensal (Página de Faturas - Bills)
* **Analogia:** A **"Seção de Faturas do Cartão de Crédito"**.
* **Pergunta que Responde:** "Onde eu posso ver e baixar minhas faturas fechadas dos meses anteriores?"
* **Função Principal:** É o seu arquivo histórico oficial. Fornece uma lista de todas as suas faturas mensais para fins contábeis.

#### <img src="https://api.iconify.design/mdi/chart-bar.svg?color=currentColor" width="20" /> A Investigação Profunda (AWS Cost Explorer)
* **Analogia:** O **"Módulo de Relatórios e Gráficos"** do app.
* **Pergunta que Responde:** "Por que meus custos com o EC2 aumentaram 30% nos últimos 3 meses? Qual dos meus projetos (tag `Projeto:X`) está gastando mais com o S3?"
* **Função Principal:** É a sua ferramenta de **análise e investigação**. Permite que você crie relatórios e gráficos customizados, filtre por serviço, por tag, por tipo de conta, etc., para identificar tendências e entender os detalhes dos seus gastos.

#### <img src="https://api.iconify.design/mdi/bell-alert-outline.svg?color=currentColor" width="20" /> O Controle Proativo (AWS Budgets)
* **Analogia:** O **"Módulo de Planejamento e Alertas"** do app.
* **Pergunta que Responde:** "Como eu posso ser avisado *antes* que meu time de desenvolvimento estoure o orçamento de 1000 dólares para o mês?"
* **Função Principal:** É a sua ferramenta de **controle do futuro**. Você define orçamentos personalizados (de custo ou de uso) e o AWS Budgets te envia um alerta quando seus gastos **reais ou previstos** atingem um limite.

#### <img src="https://api.iconify.design/mdi/file-table-box-outline.svg?color=currentColor" width="20" /> Os Dados Brutos (AWS Cost and Usage Report - CUR)
* **Analogia:** A opção de **"Exportar TODAS as suas transações para um arquivo CSV"**.
* **A Dor que Resolve:** "Os relatórios do Cost Explorer são bons, mas eu preciso cruzar os dados de custo com meus próprios dados de negócio em uma ferramenta de BI como o Tableau ou o Amazon QuickSight."
* **Função Principal:** O CUR é a fonte de dados de custo e uso **mais detalhada e granular** que a AWS oferece. Ele gera um relatório massivo (em formato CSV ou Parquet) e o entrega em um bucket S3, pronto para ser ingerido por sistemas de análise de dados.

#### <img src="https://api.iconify.design/logos/aws-cloudwatch.svg?color=currentColor" width="20" /> O Alarme de Emergência (Alarmes de Faturamento do CloudWatch)
* **Analogia:** Um **"Alerta de Saldo Baixo"** simples na sua conta.
* **Pergunta que Responde:** "Me avise imediatamente se a projeção total da minha fatura mensal passar de um valor X."
* **Função Principal:** É uma forma simples e direta de criar um alarme de segurança sobre o **total estimado da sua fatura**.
> **`!!! tip "Insight de Especialista"`**
> Lembre-se que as métricas de faturamento do CloudWatch são sempre armazenadas na região `us-east-1` (Norte da Virgínia), independentemente de onde seus recursos estão.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** A diferença entre estas ferramentas é um tópico **MUITO IMPORTANTE** para a prova.
> 1.  **Cost Explorer:** Para **VISUALIZAR e ANALISAR** os custos (passado).
> 2.  **AWS Budgets:** Para **DEFINIR ORÇAMENTOS** e receber **ALERTAS** (futuro).
> 3.  **Cost and Usage Report (CUR):** A fonte de dados **mais detalhada**, entregue em um **bucket S3**.
> 4.  **Painel de Faturamento (Billing Dashboard):** A visão **geral e simplificada**.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Playbook da Economia: Guia de Otimização de Custos na AWS

Na nuvem, assim como na Fórmula 1, a vitória não é apenas sobre ter o motor mais potente, mas sobre ser o mais **eficiente**. Cada grama de peso, cada gota de combustível e cada dólar contam. Este guia é o seu "playbook" com as três jogadas principais para otimizar seus custos e garantir que seu investimento na AWS tenha o máximo retorno.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Jogada #1: Escolha o Motor Certo (Dimensionamento e Serviços Corretos)

**Analogia:** "Escolhendo o motor certo para a pista certa."

#### 1. <img src="https://api.iconify.design/mdi/ruler-square.svg?color=currentColor" width="18" /> Dimensione Corretamente (`Right-Sizing`)
* **A Dor:** Usar uma instância EC2 `m5.2xlarge` para um blog com 10 visitas por dia.
* **A Solução:** Escolha o **tipo e o modelo de compra** corretos para sua carga de trabalho.
    * **Instâncias T2/T3:** Para cargas de trabalho que ficam a maior parte do tempo ociosas, mas precisam de picos de performance (ex: ambientes de desenvolvimento).
    * **Instâncias Reservadas / Savings Plans:** Para cargas de trabalho estáveis e previsíveis (ex: seu servidor de produção). Comprometer-se por 1 ou 3 anos pode te dar até 72% de desconto.
    * **Instâncias Spot:** Para cargas de trabalho que podem ser interrompidas (ex: processamento em lote). Oferece os maiores descontos.

#### 2. <img src="https://api.iconify.design/logos/aws-lambda.svg?color=currentColor" width="18" /> Use o Motor Certo para a Tarefa (Serverless)
* **A Dor:** Manter um servidor EC2 ligado 24/7 para executar uma tarefa que só roda por 5 minutos toda noite.
* **A Solução:** Use o **AWS Lambda**.
* **Analogia:** Para uma tarefa rápida no pit stop, você não deixa um motor de corrida ligado. Você usa uma **"ferramenta pneumática de impacto"** que só consome energia no exato segundo em que é usada.

#### 3. <img src="https://api.iconify.design/logos/aws-rds.svg?color=currentColor" width="18" /> Deixe a AWS Gerenciar (Serviços Gerenciados)
* **A Dor:** O "custo oculto" de pagar um engenheiro caro para passar horas aplicando patches, fazendo backups e gerenciando a alta disponibilidade de um banco de dados no EC2.
* **A Solução:** Use serviços gerenciados como **Amazon RDS** e **Amazon S3**. Eles reduzem o **Custo Total de Propriedade (TCO)** ao eliminar a carga operacional.

---

### <img src="https://api.iconify.design/mdi/lightbulb-off-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Jogada #2: Jogue Apenas Quando Necessário (Eliminando o Desperdício)

**Analogia:** "Desligando o túnel de vento durante a noite."

#### 1. <img src="https://api.iconify.design/mdi/magnify-scan.svg?color=currentColor" width="18" /> Encontre os Desperdícios
* **Como?** Use as ferramentas que já conhecemos:
    * **Amazon CloudWatch:** Crie um gráfico de `CPUUtilization` para sua frota. Instâncias que ficam consistentemente abaixo de 5% de uso são "zumbis" de custo.
    * **AWS Cost Explorer:** Use as **tags** para filtrar os custos por projeto e identificar quais iniciativas estão gastando mais do que o esperado.

#### 2. <img src="https://api.iconify.design/mdi/robot-industrial-outline.svg?color=currentColor" width="18" /> Automatize a Limpeza (O Padrão "Stopinator")
* **A Dor:** Desenvolvedores sempre esquecem de desligar suas instâncias de teste no final do dia.
* **A Solução:** Crie um **"Stopinator"**. É um nome genérico para um script que desliga recursos com base em uma programação ou em tags.
* **A Implementação Moderna (Serverless):**
    1.  Crie uma função **AWS Lambda** com o código para procurar e desligar instâncias com a tag `Ambiente:Dev`.
    2.  Use o **Amazon EventBridge (CloudWatch Events)** para criar uma regra agendada que aciona essa função **todos os dias às 18:00**.

---

### <img src="https://api.iconify.design/logos/aws-trusted-advisor.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Jogada #3: Ouça o Treinador (Usando o AWS Trusted Advisor)

**A Dor:** "Eu não tenho tempo para inspecionar manualmente toda a minha conta em busca de melhores práticas."

**A Solução:** O **AWS Trusted Advisor** faz isso por você.
* **Analogia:** É o **"consultor de eficiência e segurança da FIA"**. Ele visita sua "garagem", analisa seus dados e te entrega um relatório.
* **As 5 Categorias de Recomendações:**
    1.  **Otimização de Custos:** (Ex: "Você tem 3 volumes EBS não anexados").
    2.  **Performance:** (Ex: "Seu limite de serviço para VPCs está quase no máximo").
    3.  **Segurança:** (Ex: "Seu bucket S3 tem acesso público irrestrito").
    4.  **Tolerância a Falhas:** (Ex: "Seu backup do RDS não está habilitado").
    5.  **Limites de Serviço:** (Um resumo dos seus limites de uso).

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  A prática mais fácil e impactante é **desligar recursos ociosos**.
> 2.  O **AWS Trusted Advisor** é a sua principal ferramenta para receber **recomendações automatizadas** de otimização de custos.
> 3.  Conheça os principais modelos de preço do EC2: **Sob Demanda, Instâncias Reservadas, Savings Plans e Spot**.

---

### <img src="https://api.iconify.design/mdi/face-agent.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Equipe de Pit Stop da Nuvem: Guia Prático dos Planos de Suporte da AWS

Mesmo a arquitetura mais bem projetada pode enfrentar problemas. Quando sua aplicação de missão crítica está fora do ar às 3 da manhã, a velocidade e a qualidade do suporte que você recebe podem definir o sucesso ou o fracasso do seu negócio.

O **AWS Support** é a sua "equipe de pit stop", uma combinação de ferramentas, tecnologia e especialistas humanos projetada para te ajudar a operar de forma segura, otimizada e inovadora.

**Analogia:** Pense na AWS como a **"fabricante do seu carro de F1"**. Os planos de suporte são os diferentes níveis de "contrato de manutenção e engenharia de corrida" que você pode ter.

---

### <img src="https://api.iconify.design/mdi/format-list-bulleted-square.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Cardápio de Suporte (Comparando os 4 Planos)

A prova Cloud Practitioner **adora** este tópico. Entender a diferença entre os planos é fundamental.

| Recurso | Basic (Grátis) | Developer | Business | Enterprise |
| :--- | :---: | :---: | :---: | :---: |
| **Analogia**| O **"Manual do Proprietário"**| A **"Linha de E-mail com um Engenheiro"**| A **"Linha Direta 24/7 com a Equipe de Pit Stop"**| O **"Engenheiro Chefe Dedicado à sua Equipe"** |
| **Caso de Uso**| Pessoal, experimentando | Desenvolvimento/Teste | **Cargas de Trabalho de Produção** | **Cargas de Trabalho de Missão Crítica** |
| **Suporte Técnico**| Apenas faturamento e conta | E-mail (horário comercial) | **E-mail, Chat, Telefone 24/7** | E-mail, Chat, Telefone 24/7 |
| **Tempo de Resposta (Produção Fora do Ar)** | - | - | **< 1 hora** | **< 1 hora** |
| **Tempo de Resposta (Crítico p/ Negócio Fora do Ar)**| - | - | - | **< 15 minutos** |
| **Trusted Advisor**| 7 Verificações Core | 7 Verificações Core | **Todas as Verificações** | **Todas as Verificações** |
| **Gerente Técnico de Contas (TAM)**| Não | Não | Não | **SIM (Dedicado)** |

---

### <img src="https://api.iconify.design/mdi/account-star-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Valor Agregado (Os Especialistas Dedicados)

Os planos mais altos oferecem mais do que apenas suporte reativo; eles te dão parceiros estratégicos.

#### <img src="https://api.iconify.design/mdi/account-tie.svg?color=currentColor" width="20" /> Gerente Técnico de Contas (TAM) - Apenas Enterprise
* **Analogia:** O seu **"Engenheiro Chefe Dedicado"**.
* **O que faz?** Um TAM é um especialista da AWS que se torna seu principal ponto de contato. Ele aprende sobre sua arquitetura e seus objetivos de negócio, te dá orientação proativa, te ajuda a planejar eventos e atua como seu defensor dentro da AWS.

#### <img src="https://api.iconify.design/mdi/concierge.svg?color=currentColor" width="20" /> AWS Support Concierge - Business e Enterprise
* **Analogia:** O **"Assistente Pessoal da Equipe"**.
* **O que faz?** São especialistas em **faturamento e gerenciamento de contas**. Se você tem uma dúvida sobre sua fatura ou precisa de ajuda com a administração da sua conta, eles são as pessoas certas para contatar, liberando seus engenheiros para focarem em tarefas técnicas.

#### <img src="https://api.iconify.design/mdi/calendar-star.svg?color=currentColor" width="20" /> AWS Infrastructure Event Management (IEM) - Business e Enterprise
> **`!!! tip "Insight de Especialista"`**
> Este é um benefício incrível. Se você vai lançar um novo produto ou espera um pico massivo na Black Friday, você avisa a AWS com antecedência. Eles alocam engenheiros de suporte para ficarem de prontidão, monitorando seu evento **junto com você**, prontos para agir. É um seguro para seus eventos mais importantes.

---

### <img src="https://api.iconify.design/mdi/help-circle-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Escopo do Jogo (O que o Suporte Cobre?)

É importante saber o que pedir para o suporte.

* **Suporte PODE te ajudar com:**
    * Perguntas do tipo "como eu faço X na AWS?".
    * Solução de problemas com serviços da AWS (ex: "Meu ELB não está passando nas health checks").
    * Problemas com o console, CLI ou APIs da AWS.

* **Suporte NÃO PODE te ajudar com:**
    * **Escrever ou depurar o *seu* código de aplicação.**
    * **Administrar o *seu* sistema operacional** (ex: "Como eu configuro o Apache?").

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Os **Planos de Suporte** são um dos tópicos mais detalhados e frequentemente testados na prova. **MEMORIZE a tabela de comparação.** Foque em:
> 1.  **Business:** Acesso 24/7 e resposta em **< 1 hora** para produção fora do ar.
> 2.  **Enterprise:** Resposta em **< 15 minutos** para sistemas críticos e um **TAM dedicado**.
> 3.  **Todos os planos pagos** dão acesso a **todas as verificações do Trusted Advisor**.

---

### <img src="https://api.iconify.design/mdi/face-agent.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Contrato de Performance: Guia de Preços e SLAs dos Planos de Suporte AWS

A pergunta que define a escolha de um plano de suporte é simples: **"Quanto custa para o meu negócio ficar parado por uma hora? E por 15 minutos?"**. A resposta a essa pergunta determina se você precisa de um "manual do proprietário" ou de um "engenheiro chefe dedicado" 24/7.

Vamos analisar em detalhe o que cada plano oferece.

---

### <img src="https://api.iconify.design/mdi/format-list-bulleted-square.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. Decifrando o Contrato (Os 4 Planos em Detalhe)

#### <img src="https://api.iconify.design/mdi/account-outline.svg?color=currentColor" width="20" /> Plano Basic (O Manual do Proprietário)
* **Para Quem?** Todos os clientes da AWS. É ideal para quem está experimentando ou aprendendo.
* **Custo:** **Gratuito**.
* **O que você recebe?** Acesso à documentação, fóruns da comunidade e as 7 verificações principais do Trusted Advisor. Suporte apenas para questões de faturamento e conta.
* **SLA de Suporte Técnico:** Não há.

#### <img src="https://api.iconify.design/mdi/account-wrench-outline.svg?color=currentColor" width="20" /> Plano Developer (A Linha de E-mail com um Engenheiro)
* **Para Quem?** Desenvolvedores e equipes em ambientes de **teste e desenvolvimento**.
* **Custo:** A partir de **US$ 29/mês** (ou 3% do uso da AWS).
* **O que você recebe?** Acesso por e-mail a engenheiros de suporte durante o horário comercial.
* **SLA de Suporte Técnico:** Resposta em **< 12 horas** para sistemas com deficiência.

#### <img src="https://api.iconify.design/mdi/briefcase-account-outline.svg?color=currentColor" width="20" /> Plano Business (A Equipe de Pit Stop 24/7)
* **Para Quem?** Empresas com **cargas de trabalho de produção** na AWS.
* **Custo:** A partir de **US$ 100/mês** (com uma escala percentual sobre o uso).
* **O que você recebe?** Acesso 24/7 por e-mail, chat e telefone a engenheiros de suporte. Acesso a **todas as verificações do Trusted Advisor**.
* **SLA de Suporte Técnico:**
    * Sistema de produção fora do ar: **< 1 hora**.
    * Sistema de produção com deficiência: **< 4 horas**.

#### <img src="https://api.iconify.design/mdi/account-tie-voice.svg?color=currentColor" width="20" /> Plano Enterprise (O Engenheiro Chefe Dedicado)
* **Para Quem?** Grandes empresas com **cargas de trabalho de missão crítica**.
* **Custo:** A partir de **US$ 15.000/mês**.
* **O que você recebe?** Tudo do plano Business, mais um **Gerente Técnico de Contas (TAM)** dedicado, revisões de arquitetura proativas e o programa Infrastructure Event Management (IEM).
* **SLA de Suporte Técnico:**
    * Sistema crítico para o negócio fora do ar: **< 15 minutos**.

---

### <img src="https://api.iconify.design/logos/aws-trusted-advisor.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Consultor Robô (Recap do AWS Trusted Advisor)

* **O que é?** Seu consultor automatizado que te dá recomendações para seguir as melhores práticas.
* **A Dor que Resolve:** A dificuldade de inspecionar manualmente toda a sua conta em busca de oportunidades de otimização e falhas de segurança.
> **`!!! tip "O Link com o Suporte"`**
> Lembre-se: para desbloquear o poder **total** do Trusted Advisor (todas as verificações nas 5 categorias), você precisa de um plano de suporte **Business** ou superior.

---

### <img src="https://api.iconify.design/mdi/book-open-page-variant-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. A Biblioteca do Arquiteto (Whitepapers)

* **O que são?** Documentos técnicos profundos, guias de melhores práticas e arquiteturas de referência, escritos pelos próprios arquitetos e especialistas da AWS.
* **A Dor que Resolve:** "Onde eu encontro a fonte de conhecimento oficial e mais aprofundada sobre como construir uma arquitetura X ou seguir as melhores práticas de segurança Y?"
* **O Resultado:** Os whitepapers são uma fonte de conhecimento inestimável e **gratuita** para qualquer pessoa que queira aprofundar seus conhecimentos em tópicos específicos.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Os **Planos de Suporte** são um dos tópicos mais detalhados e frequentemente testados na prova. **MEMORIZE os tempos de resposta para os casos críticos**.
> 1.  **Business** -> Produção Fora do Ar -> **< 1 hora**.
> 2.  **Enterprise** -> Crítico p/ Negócio Fora do Ar -> **< 15 minutos**.
> 3.  **Enterprise** é o único plano que oferece um **Gerente Técnico de Contas (TAM)**.