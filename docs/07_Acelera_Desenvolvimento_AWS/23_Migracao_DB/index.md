# <img src="https://api.iconify.design/mdi/database-sync-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Mudança Inteligente: Guia de Migração de Bancos de Dados com DMS e SCT

**A Dor:** Migrar um banco de dados de produção é uma das tarefas mais temidas em TI. O risco de perda de dados e de ter que tirar a aplicação do ar por horas (ou dias) é imenso e pode custar muito caro para o negócio.

**A Solução da AWS:** Um conjunto de ferramentas especializadas que atuam como uma **"empresa de mudança de bibliotecas"** de alta tecnologia, projetada para fazer a transição de forma rápida e segura. As duas principais ferramentas são o **AWS DMS** e a **AWS SCT**.

---

### <img src="https://api.iconify.design/mdi/account-hard-hat.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Equipe de Especialistas (SCT vs. DMS)

Pense na migração como um projeto com dois especialistas: o Arquiteto e o Operador de Logística.

#### <img src="https://api.iconify.design/mdi/floor-plan.svg?color=currentColor" width="20" /> AWS Schema Conversion Tool (SCT) - O Arquiteto
* **O que faz?** Converte o **SCHEMA** do banco de dados.
* **Analogia:** O **"Arquiteto"**. Seu trabalho **NÃO** é mover os livros. É analisar a "planta baixa" da biblioteca antiga (com suas estantes de madeira e sistema de fichas de papel - *schema Oracle*) e criar a **nova planta baixa** para a biblioteca moderna (com estantes de metal e sistema digital - *schema PostgreSQL*). Ele prepara as novas prateleiras vazias.
* **Quando usar?** **APENAS** em migrações **HETEROGÊNEAS**.

#### <img src="https://api.iconify.design/mdi/truck-delivery-outline.svg?color=currentColor" width="20" /> AWS Database Migration Service (DMS) - O Operador de Logística
* **O que faz?** **Move os DADOS**.
* **Analogia:** O **"Operador de Logística"**. Seu trabalho é pegar os livros das prateleiras antigas e colocá-los nas novas prateleiras que o Arquiteto preparou.
* **Quando usar?** Em **TODAS** as migrações, sejam elas homogêneas ou heterogêneas.

---

### <img src="https://api.iconify.design/mdi/compare-horizontal.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. Os Tipos de Mudança

#### Migração Homogênea
* **O que é?** Mover um banco de dados para o **mesmo** motor de banco de dados.
* **Analogia:** "Mudar de um prédio de madeira para *outro* prédio de madeira."
* **Exemplo:** `Oracle on-premises -> Oracle no Amazon RDS`.
* **Ferramentas:** Apenas o **DMS** (o schema não precisa ser convertido).

#### Migração Heterogênea
* **O que é?** Mover um banco de dados para um motor de banco de dados **diferente**.
* **Analogia:** "Mudar do prédio de madeira para o novo prédio de metal."
* **Exemplo:** `Microsoft SQL Server on-premises -> Amazon Aurora (PostgreSQL)`.
* **Ferramentas:** **SCT** primeiro (para converter o schema), **DMS** depois (para mover os dados).

---

### <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. A Arquitetura da Migração

O DMS funciona com três componentes principais:
1.  **Endpoint de Origem (Source Endpoint):** O "endereço" da biblioteca antiga.
2.  **Endpoint de Destino (Target Endpoint):** O "endereço" da nova biblioteca.
3.  **Instância de Replicação (Replication Instance):**
    * **Analogia:** O **"Caminhão de Mudança"**.
    * **O que é?** Uma instância EC2 gerenciada que o DMS usa para executar o trabalho pesado de ler os dados da origem, fazer qualquer conversão necessária e escrevê-los no destino. Você escolhe o "tamanho do caminhão" com base no tamanho da sua "biblioteca".

---

### <img src="https://api.iconify.design/mdi/sync-circle.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 4. A Mágica do Quase Zero Downtime (Replicação Contínua)

**A Dor:** "Como eu movo 1 terabyte de dados sem fechar minha aplicação por 12 horas?"

**A Solução do DMS:** Replicação Contínua de Dados (CDC - Change Data Capture).
* **Analogia:** O processo de mudança da biblioteca acontece em duas fases:
    1.  **Carga Total:** O "Operador de Logística" (DMS) primeiro faz uma **grande viagem com um caminhão gigante** para copiar todos os livros existentes da biblioteca antiga para a nova.
    2.  **Replicação Contínua:** Enquanto ele fazia a primeira viagem, novos livros foram devolvidos e emprestados na biblioteca antiga! Para manter tudo em dia, o Operador deixa um **"assistente"** na biblioteca antiga que anota cada mudança. Ele então faz **viagens contínuas com uma "van pequena"** para levar apenas essas mudanças, mantendo as duas bibliotecas em perfeita sincronia.
* **O Resultado:** Você pode manter sua aplicação funcionando na biblioteca antiga enquanto o DMS trabalha. Quando as duas estiverem sincronizadas, você pode planejar uma janela de manutenção de apenas alguns minutos para "virar a chave" e apontar sua aplicação para a nova biblioteca, com o mínimo de tempo de inatividade.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  **AWS DMS** é o serviço para **MIGRAR DADOS** de um banco de dados para outro.
> 2.  Sua principal vantagem é a capacidade de migrar com **mínimo ou zero tempo de inatividade**.
> 3.  Para migrações **HETEROGÊNEAS** (ex: Oracle para Aurora), você primeiro usa a **AWS SCT** para converter o **SCHEMA**, e depois o **DMS** para mover os **DADOS**.

---

### <img src="https://api.iconify.design/mdi/database-move-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Mapas da Mudança: Guia de Migrações Homogêneas vs. Heterogêneas

Quando um cliente decide migrar seu banco de dados para a AWS, a primeira pergunta que um arquiteto faz é: "Estamos apenas 'mudando de endereço' ou estamos 'modernizando a casa'?".

A resposta a essa pergunta define se a migração será **Homogênea** ou **Heterogênea** e quais ferramentas da "empresa de mudança" (AWS) precisaremos usar.

---

### <img src="https://api.iconify.design/mdi/home-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Mudança Simples (Migração Homogênea)

* **O que é?** Uma migração onde o banco de dados de **origem** e o de **destino** usam o **mesmo** motor (ou motores compatíveis).
* **Analogia:** "Mudar a biblioteca para um **prédio idêntico** do outro lado da rua."
* **Exemplos:**
    * Mover um banco de dados `Oracle` de um servidor local para o `Amazon RDS for Oracle`.
    * Mover um banco de dados `MySQL` de um servidor local para o `Amazon RDS for MySQL`.

#### O Processo de 1 Etapa
Como a "planta baixa" (o schema, os tipos de dados e o código) é a mesma, não precisamos de um "arquiteto" para redesenhar as prateleiras. Precisamos apenas da equipe de logística para mover os livros.

* **<img src="https://api.iconify.design/mdi/truck-delivery-outline.svg?color=currentColor" width="18" /> Ferramenta Chave:** **AWS Database Migration Service (DMS)**. Ele é o especialista em mover os dados de forma rápida e segura, com o mínimo de tempo de inatividade.

<p align="center">
  <img src="https://i.imgur.com/83U7n2b.png" alt="Migração Homogênea" />
</p>

---

### <img src="https://api.iconify.design/mdi/home-lightning-bolt-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Modernização (Migração Heterogênea)

* **O que é?** Uma migração onde o banco de dados de **origem** e o de **destino** usam motores **diferentes**.
* **Analogia:** "Mudar a biblioteca de um **prédio histórico com estantes de madeira** para um **prédio moderno com estantes de metal** e um sistema digital."
* **Exemplos:**
    * Mover de `Microsoft SQL Server` para `Amazon Aurora (PostgreSQL)`.
    * Mover de `Oracle` para `MySQL`.

#### O Processo de 2 Etapas
Como o "formato das estantes" e o "sistema de catalogação" são incompatíveis, a mudança exige um planejamento mais cuidadoso.

1.  **<img src="https://api.iconify.design/mdi/floor-plan.svg?color=currentColor" width="18" /> Etapa 1: Converter o Schema (O Arquiteto)**
    * **Ferramenta Chave:** **AWS Schema Conversion Tool (SCT)**. O "arquiteto" (SCT) analisa o schema antigo e o converte automaticamente para o formato do novo motor de banco de dados. Ele prepara as novas "prateleiras" vazias.

2.  **<img src="https://api.iconify.design/mdi/truck-delivery-outline.svg?color=currentColor" width="18" /> Etapa 2: Migrar os Dados (A Logística)**
    * **Ferramenta Chave:** **AWS Database Migration Service (DMS)**. Com as novas prateleiras prontas, a "equipe de logística" (DMS) entra em ação para mover os "livros" (os dados) para o novo local.

<p align="center">
  <img src="https://i.imgur.com/gK9JdKq.png" alt="Migração Heterogênea" />
</p>

---

### <img src="https://api.iconify.design/mdi/clipboard-check-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Resumo do Arquiteto

| Característica | Migração Homogênea | Migração Heterogênea |
| :--- | :--- | :--- |
| **Motores de BD** | **Iguais** (Oracle -> Oracle) | **Diferentes** (Oracle -> Aurora) |
| **Principal Desafio**| Mover os **Dados** | Converter o **Schema** + Mover os **Dados** |
| **Ferramenta SCT Necessária?**| **Não** | **Sim, é a primeira etapa** |
| **Ferramenta DMS Necessária?**| **Sim** | **Sim, é a segunda etapa** |
| **Principal Benefício de Negócio**| Sair do data center, reduzir custos operacionais. | **Modernização**, sair de licenças caras, adotar cloud-native. |

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** A diferença entre migrações homogêneas e heterogêneas é um conceito-chave. Lembre-se:
> 1.  **Homogênea = Motores Iguais**. Usa apenas o **DMS**.
> 2.  **Heterogênea = Motores Diferentes**. Usa **SCT primeiro** (para o schema) e **DMS depois** (para os dados).
> Esta é uma das perguntas de cenário mais comuns sobre migração.

---

### <img src="https://api.iconify.design/mdi/truck-delivery-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Logística da Mudança: Guia da Arquitetura do AWS DMS e SCT

Já sabemos a diferença entre uma mudança simples (homogênea) e uma modernização (heterogênea). Agora, vamos abrir o capô da nossa "empresa de mudança" para ver as ferramentas e o processo que eles usam.

---

### <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Arquitetura do AWS DMS (A Empresa de Logística)

O AWS Database Migration Service (DMS) é o coração da operação. Ele é composto por três peças principais.

* **<img src="https://api.iconify.design/mdi/map-marker-outline.svg?color=currentColor" width="18" /> Endpoints (Os Endereços):**
    * **Analogia:** Os **"endereços de CEP"** da biblioteca antiga (origem) e da nova (destino).
    * **O que são?** São objetos de configuração que contêm as informações de conexão (endereço do servidor, porta, nome de usuário, senha) para seus bancos de dados de origem e destino.

* **<img src="https://api.iconify.design/mdi/engine-outline.svg?color=currentColor" width="18" /> Instância de Replicação (Replication Instance):**
    * **Analogia:** O **"Caminhão de Mudança"**.
    * **O que é?** Uma instância EC2 gerenciada que o DMS provisiona para executar o trabalho pesado. É o motor que se conecta à origem, lê os dados, os transforma (se necessário) e os escreve no destino. Você escolhe o "tamanho do caminhão" (o tipo da instância) com base no volume da sua migração.

* **<img src="https://api.iconify.design/mdi/clipboard-list-outline.svg?color=currentColor" width="18" /> Tarefa de Migração (Migration Task):**
    * **Analogia:** O **"Plano de Trabalho Detalhado"** para a equipe de mudança.
    * **O que é?** É a configuração que une tudo. Você define a origem, o destino e a instância de replicação, e configura as regras da migração, como quais tabelas mover e como lidar com as mudanças contínuas.

---

### <img src="https://api.iconify.design/mdi/floor-plan.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Ferramenta do Arquiteto (AWS Schema Conversion Tool - SCT)

Lembre-se: o DMS move os "livros" (dados). A **SCT** redesenha as "prateleiras" (o schema).

* **A Dor que Resolve:** Converter manualmente o schema de um banco de dados Oracle para um formato compatível com PostgreSQL é um trabalho para um especialista, que pode levar semanas ou meses.
* **A Solução (SCT):** É uma ferramenta que **automatiza** a conversão do seu schema.

#### O Que a SCT Converte?
* **<img src="https://api.iconify.design/mdi/table.svg?color=currentColor" width="18" /> Schema:** As definições de tabelas, colunas, tipos de dados e chaves.
* **<img src="https://api.iconify.design/mdi/code-braces.svg?color=currentColor" width="18" /> Objetos de Código do Banco de Dados:**
    * **Views:** Consultas salvas.
    * **Stored Procedures e Funções:** Lógica de negócio complexa que vive dentro do banco de dados (ex: PL/SQL no Oracle para T-SQL no SQL Server).

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT DE ESPECIALISTA:** A SCT não é mágica. Para conversões muito complexas, ela pode não conseguir converter 100% do código. Nesses casos, ela gera um **relatório de avaliação detalhado**, apontando exatamente quais trechos de código precisam de intervenção manual do seu desenvolvedor. Isso, por si só, já economiza um tempo imenso de análise.

---

### <img src="https://api.iconify.design/mdi/sync-circle.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Fluxo da Mudança com Mínimo Downtime

Uma tarefa de migração no DMS geralmente segue um fluxo de três fases para garantir que sua aplicação continue funcionando durante a mudança.

1.  **<img src="https://api.iconify.design/mdi/truck.svg?color=currentColor" width="18" /> Carga Total (Full Load):**
    * **Analogia:** A **"primeira grande viagem do caminhão"**, copiando todos os livros existentes.
2.  **<img src="https://api.iconify.design/mdi/clipboard-text-clock-outline.svg?color=currentColor" width="18" /> Aplicação de Alterações em Cache:**
    * **Analogia:** Enquanto o caminhão estava na estrada, alguns livros foram devolvidos. O DMS aplica essas mudanças que ocorreram *durante* a carga total.
3.  **<img src="https://api.iconify.design/mdi-satellite-uplink.svg?color=currentColor" width="18" /> Replicação Contínua (Change Data Capture - CDC):**
    * **Analogia:** A **"van pequena que fica fazendo viagens contínuas"** para levar apenas os novos livros e as atualizações, mantendo as duas bibliotecas em sincronia.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Lembre-se dos 3 componentes do DMS: **Endpoints** (os endereços), **Instância de Replicação** (o motor) e **Tarefa de Migração** (o plano).
> 2.  **SCT** é para converter o **SCHEMA** (a estrutura). **DMS** é para mover os **DADOS**.
> 3.  A combinação de **Carga Total + Replicação Contínua** é o que permite ao DMS realizar migrações com **mínimo ou zero tempo de inatividade**.

---

### <img src="https://api.iconify.design/mdi/engine-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Sala de Máquinas da Migração: Guia da Arquitetura do AWS DMS

Já sabemos que o DMS é a nossa "empresa de mudança" de bancos de dados. Agora, vamos preencher o "contrato de serviço" e entender cada peça da sua arquitetura. Uma migração bem-sucedida depende da configuração correta de quatro componentes essenciais.

---

### <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. Os 4 Componentes Essenciais de uma Migração DMS

#### 1. <img src="https://api.iconify.design/mdi/map-marker-outline.svg?color=currentColor" width="20" /> Endpoints de Origem e Destino (Os Endereços)
* **O que são?** São as informações de conexão para seus bancos de dados.
* **Analogia:** Os **"endereços de CEP"** da biblioteca antiga (origem) e da nova (destino).
* **Como Funciona:** Um endpoint contém tudo que o DMS precisa para se conectar ao banco de dados: o endereço do servidor, a porta, o nome de usuário, a senha e os detalhes do certificado SSL, se necessário.
* **Flexibilidade:** A AWS suporta uma vasta gama de combinações. Você pode ter uma origem on-premises e um destino no Amazon RDS, ou uma origem no EC2 e um destino no Amazon S3, entre muitas outras.

#### 2. <img src="https://api.iconify.design/mdi/truck-delivery-outline.svg?color=currentColor" width="20" /> Instância de Replicação (O Caminhão de Mudança)
* **O que é?** Uma instância EC2 gerenciada que o DMS provisiona para executar o trabalho pesado da migração.
* **Analogia:** O **"Caminhão de Mudança"**.
* **Como Funciona:** É o motor que se conecta aos dois endpoints, lê os dados da origem, os transforma (se necessário) e os escreve no destino.
* **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> Insight de Arquiteto:** O **tamanho** (tipo de instância) que você escolhe para sua Instância de Replicação impacta diretamente a **velocidade** da sua migração. Para mover bibliotecas maiores, você precisa de um caminhão maior e mais potente.

#### 3. <img src="https://api.iconify.design/mdi/clipboard-list-outline.svg?color=currentColor" width="20" /> Tarefa de Migração (O Plano de Trabalho)
* **O que é?** A configuração que une tudo e define a lógica da migração.
* **Analogia:** O **"Plano de Trabalho Detalhado"** para a equipe de mudança.
* **Como Funciona:** Na tarefa, você especifica:
    * O endpoint de origem.
    * O endpoint de destino.
    * A instância de replicação a ser usada.
    * O **tipo de migração**:
        1.  Apenas carga total (`Full Load`).
        2.  Apenas replicação contínua (`CDC - Change Data Capture`).
        3.  Carga total + Replicação Contínua (o mais comum para migrações com mínimo downtime).

---

### <img src="https://api.iconify.design/mdi/shield-check-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Plano de Contingência (Alta Disponibilidade da Migração)

**A Dor que Resolve:** "Estou no meio de uma migração crítica que vai levar 48 horas. O que acontece se o 'caminhão de mudança' (a Instância de Replicação) quebrar no meio do caminho?"

**A Solução do DMS:** **Implantação Multi-AZ para a Instância de Replicação**.

* **Como Funciona:** Ao criar sua Instância de Replicação, você pode marcar uma única caixa de seleção para habilitar o `Multi-AZ`.
* **O Resultado:** O DMS automaticamente provisiona uma **réplica de segurança síncrona** da sua instância em outra Zona de Disponibilidade. Se a instância principal falhar por qualquer motivo, o DMS faz o **failover automático** para a réplica, e sua tarefa de migração continua de onde parou, com o mínimo de interrupção.
* **Analogia:** É como ter **dois caminhões de mudança idênticos** em garagens diferentes. Se o primeiro quebrar, o segundo assume a rota automaticamente.

---

### <img src="https://api.iconify.design/mdi/format-list-numbered.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Fluxo de Trabalho do Arquiteto (Resumo)

O processo de configurar uma migração no console segue esta ordem lógica:
1.  **Crie sua Instância de Replicação:** Escolha o tamanho e se será Multi-AZ.
2.  **Crie o Endpoint de Origem:** Forneça os detalhes de conexão do seu banco de dados antigo.
3.  **Crie o Endpoint de Destino:** Forneça os detalhes de conexão do seu novo banco de dados na AWS.
4.  **Crie e inicie a Tarefa de Migração:** Junte as três peças acima e defina o tipo de migração.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Conheça os **componentes** do DMS: **Endpoints** (os endereços), **Instância de Replicação** (o motor) e **Tarefa de Migração** (o plano).
> 2.  Saiba que a **Instância de Replicação** é uma instância EC2 gerenciada que faz o trabalho.
> 3.  Entenda que a **Instância de Replicação pode ser Multi-AZ** para garantir a **alta disponibilidade** do processo de migração.

