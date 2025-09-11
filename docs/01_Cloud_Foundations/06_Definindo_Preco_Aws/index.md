# Manual Definitivo de Custos na AWS: Do Planejamento à Otimização

A pergunta número um de quem começa na nuvem é: **"Quanto isso vai me custar?"**. O medo de uma fatura inesperada pode paralisar a inovação. Este guia foi criado para destruir esse medo.

Aqui, você não vai apenas aprender a teoria. Você vai aprender a **pensar financeiramente na nuvem**. Vamos te mostrar quais serviços são gratuitos, quais exigem mais atenção, e o mais importante: vamos te ensinar, passo a passo, a **calcular o custo do seu próprio projeto**.

Este é o seu kit de ferramentas completo para se tornar um mestre das finanças na AWS.

---

### Parte 1: O Arsenal Gratuito (O que você PODE e DEVE usar sem custo)

A AWS quer que você experimente. Por isso, o **Nível Gratuito (Free Tier)** é extremamente generoso, mas é crucial entender como ele funciona.

#### 🎁 **O Nível Gratuito de 12 Meses (Para Contas Novas)**
Durante seu primeiro ano, você tem uma "cota" mensal gratuita dos serviços mais importantes. É o seu playground para aprender.
* **Amazon EC2:** 750 horas por mês de uma instância pequena (t2.micro ou t3.micro). O suficiente para rodar um servidor 24/7 o mês inteiro.
* **Amazon S3:** 5 GB de armazenamento padrão. Perfeito para guardar arquivos de um site ou backups iniciais.
* **Amazon RDS:** 750 horas por mês de um banco de dados pequeno.
* **E muito mais...**

#### ✅ **Os Serviços "Sempre Gratuitos" (Always Free)**
Alguns serviços têm uma cota gratuita que **nunca expira**, mesmo depois do primeiro ano.
* **AWS Lambda:** 1 milhão de execuções por mês.
* **Amazon DynamoDB:** 25 GB de armazenamento.
* **Amazon S3 Glacier:** 10 GB de recuperação de dados por mês.
* **AWS IAM:** O serviço de identidade e permissões é totalmente gratuito.
* **AWS Budgets:** As primeiras duas "armadilhas de orçamento" são gratuitas.

#### 🏗️ **Os Orquestradores Gratuitos (O "Mito")**
Lembre-se do nosso hack: serviços como **Auto Scaling, CloudFormation, Elastic Beanstalk e VPC** são gratuitos. A "planta da casa" não custa nada, mas os "tijolos" (os recursos EC2 e RDS que eles criam) são pagos.

> **✨ INSIGHT PODEROSO:** A estratégia mais inteligente é construir suas primeiras aplicações usando o máximo de serviços "Sempre Gratuitos" e mantendo seus recursos de EC2 e RDS dentro dos limites do Free Tier de 12 meses. É totalmente possível rodar um projeto real por quase zero centavos no primeiro ano.

---

### Parte 2: Decifrando os "Vilões" do Custo (O que Ficar de Olho)

Não existem serviços "caros", mas sim serviços que, se mal configurados ou usados em grande escala, podem elevar sua fatura. Fique atento a:

1.  **🏎️ Computação de Alta Performance:** Instâncias EC2 com muita CPU, GPU ou memória (ex: para machine learning, renderização de vídeo) são como carros de Fórmula 1: incrivelmente potentes e com um custo por hora proporcional.
2.  **🌐 Transferência de Dados Massiva PARA FORA:** Como vimos, transferir grandes volumes de dados (vídeos, backups) da AWS para a internet é um dos custos que mais crescem com a escala.
3.  **🗄️ Bancos de Dados Gerenciados de Grande Porte:** Um **Amazon RDS** configurado em **Multi-AZ** (com uma cópia de segurança em outra localidade para alta disponibilidade) custa o dobro de uma instância normal, pois você está, de fato, usando o dobro de infraestrutura.
4.  **⚡ Performance Provisionada:** Em serviços como **DynamoDB** ou discos **EBS io2**, você pode pagar por uma garantia de performance (IOPS). É como alugar uma pista de corrida exclusiva: custa mais, mas você tem a garantia de velocidade máxima.

> **✨ HACK DE OTIMIZAÇÃO:** A regra de ouro é: **comece pequeno**. Use a menor instância EC2/RDS que atenda sua necessidade. É muito mais fácil (e barato) aumentar o tamanho depois (escalar verticalmente) do que começar grande e pagar por recursos ociosos.

---

### Parte 3: Mão na Massa - Calculando seu Primeiro Projeto

Chega de teoria. Vamos calcular o custo de um projeto real: **um blog popular em WordPress**.

**Nossa arquitetura (nossas peças de LEGO):**
* Um servidor para rodar o WordPress (**Amazon EC2**).
* Um banco de dados para guardar os posts e comentários (**Amazon RDS**).
* Um lugar para guardar as imagens e mídias (**Amazon S3**).
* Um volume de visitantes que gera tráfego (**Transferência de Dados**).

#### **Passo a Passo com a AWS Pricing Calculator:**

1.  **Acesse a Ferramenta:** Pesquise por "AWS Pricing Calculator" e clique em **"Create estimate"**.

2.  **Adicionar o Servidor (EC2):**
    * Procure por **"Amazon EC2"** e clique em **"Configure"**.
    * **Região:** Escolha a mais próxima de você (ex: `South America (Sao Paulo)`).
    * **Instância EC2:** Em "Find instance", procure por `t3.micro`. Essa é uma ótima instância para começar e está no Free Tier.
    * **Estratégia de preços:** Deixe em `On-Demand` (Sob Demanda).
    * **Uso:** Coloque `730` horas por mês (para rodar 24/7).
    * Clique em **"Save and add service"**.

3.  **Adicionar o Banco de Dados (RDS):**
    * Clique em **"Add service"**, procure por **"Amazon RDS for MySQL"** e clique em **"Configure"**.
    * **Região:** Escolha a mesma de antes (São Paulo).
    * **Implantação:** Escolha `Single-AZ` (para começar, não precisamos de alta disponibilidade).
    * **Instância de BD:** Procure por `db.t3.micro`. Também está no Free Tier.
    * **Armazenamento:** Deixe o padrão de `20` GB.
    * Clique em **"Save and add service"**.

4.  **Adicionar o Armazenamento de Mídia (S3):**
    * Clique em **"Add service"**, procure por **"Amazon S3"** e clique em **"Configure"**.
    * **Região:** A mesma de antes.
    * **Tipo de Armazenamento:** Deixe em `S3 Standard`.
    * **Armazenamento (GB):** Vamos estimar `10` GB para nossas imagens e vídeos.
    * Clique em **"Save and add service"**.

5.  **Analisar o Resultado:**
    * A calculadora irá te mostrar uma estimativa mensal. Você verá os custos de cada serviço.
    * **O MAIS IMPORTANTE:** Role para baixo e veja a seção **"Cálculos do nível gratuito"**. A calculadora automaticamente aplica os descontos do Free Tier de 12 meses!

**Resultado (Exemplo):** A sua estimativa total pode ser de `$25.00 USD`, mas após os descontos do Free Tier, o custo final para o primeiro ano será de **`$0.00 USD`** ou muito próximo disso, dependendo do tráfego.

> **✨ INSIGHT PODEROSO:** A calculadora não é só para saber o custo. É uma ferramenta de **aprendizado**. Brinque com ela! Mude o tipo de instância EC2 de `t3.micro` para uma `m5.large` e veja o preço explodir. Mude a implantação do RDS para `Multi-AZ` e veja o custo dobrar. É a forma mais segura de entender o impacto de cada decisão de arquitetura no seu bolso.

---

### Conclusão: Você no Controle

Entender os custos na AWS é uma jornada de aprendizado contínuo, mas não precisa ser um mistério. Com a mentalidade certa e as ferramentas corretas, você deixa de ser um passageiro com medo da fatura e se torna o piloto, otimizando a rota para chegar ao seu destino da forma mais eficiente e barata possível.