# <img src="https://api.iconify.design/mdi/finance.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Dono da Nuvem: Guia de Gerenciamento de Custos e Governança na AWS

A nuvem oferece um poder incrível, mas "com grandes poderes, vêm grandes faturas". A habilidade de um arquiteto ou administrador de nuvem moderno não é apenas construir, mas construir de forma **eficiente e com responsabilidade fiscal**.

Este guia é o seu manual para se tornar o "dono" da sua nuvem, dominando as ferramentas que te dão visibilidade, controle e otimização sobre seus gastos.

**Analogia:** Pense em gerenciar as **finanças de uma grande corporação com múltiplas filiais (contas AWS)**.

---

### <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Jornada da Maturidade Financeira na Nuvem

Gerenciar custos na nuvem é uma jornada em 5 passos.

#### Passo 1: Organize a Casa (AWS Organizations)

* **A Dor:** Cada "filial" (conta AWS para Dev, Produção, etc.) tem sua própria fatura. É um caos para o "CFO" (você) consolidar os custos e aplicar políticas corporativas.
* **A Solução:** O **AWS Organizations** permite que você agrupe múltiplas contas AWS sob uma única "holding corporativa".
* **Benefícios Chave:**
    * **Faturamento Consolidado (`Consolidated Billing`):** Uma única fatura para todas as contas.
    * **Descontos por Volume:** Os gastos de todas as contas são somados, o que te ajuda a alcançar descontos por volume mais rapidamente.
    * **Governança Centralizada:** Você pode aplicar "leis corporativas" (Service Control Policies - SCPs) a todas as filiais.

#### Passo 2: Etiquete Tudo (Marcação - Tagging)

* **A Dor:** "A fatura da 'filial de Vendas' veio altíssima. Mas foi o 'Projeto Alpha' ou o 'Projeto Beta' que gastou mais?"
* **A Solução:** A **Marcação (`Tagging`)**. Tags são etiquetas (pares de chave-valor, ex: `Projeto:Alpha`) que você anexa aos seus recursos.
* **O Resultado:** As tags são a base da alocação de custos. Elas permitem que você filtre e agrupe seus gastos por projeto, centro de custo, departamento, etc.

#### Passo 3: Analise os Gastos (Ferramentas de Custo)

* **A Dor:** "Eu tenho os dados etiquetados, mas eles estão em uma planilha gigante. Como eu transformo isso em insights?"
* **A Solução:** O **AWS Cost Explorer**.
* **Analogia:** É o **"software de Business Intelligence (BI) do CFO"**. Ele pega os dados brutos e os transforma em gráficos e relatórios interativos, permitindo que você visualize tendências, preveja gastos futuros e identifique anomalias.

#### Passo 4: Peça Conselho ao Robô (AWS Trusted Advisor)

* **A Dor:** "Eu sei onde estou gastando, mas como eu sei *onde* posso economizar?"
* **A Solução:** O **AWS Trusted Advisor**.
* **Analogia:** É o seu **"consultor de eficiência automatizado"**. Ele escaneia seu ambiente e te dá um relatório com recomendações em cinco categorias:

1.  **Otimização de Custos:** "Você tem 5 instâncias EC2 ociosas."
2.  **Performance:** "Seu volume EBS está sobrecarregado."
3.  **Segurança:** "Seu Security Group está permitindo acesso irrestrito."
4.  **Tolerância a Falhas:** "Você não tem backups habilitados no seu RDS."
5.  **Limites de Serviço:** "Você está perto de atingir seu limite de VPCs."

#### Passo 5: Peça Ajuda a um Humano (AWS Support)

* **A Dor:** "Meu sistema de produção está fora do ar às 3 da manhã!" ou "O Trusted Advisor me disse para comprar Savings Plans, mas eu não sei como."
* **A Solução:** Os **Planos do AWS Support**.
* **Analogia:** A **"linha direta com os engenheiros especialistas"**. Quando a automação não é suficiente, você precisa de um humano. A AWS oferece diferentes níveis de suporte, desde o gratuito até o `Enterprise`, com tempos de resposta de minutos para casos críticos.

---

### <img src="https://api.iconify.design/mdi/notebook-edit-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Lembrete do Projeto: Base de Conhecimento
> **`!!! tip "Registre suas Descobertas"`**
> Ao estudar estas ferramentas, documente seus aprendizados. Exemplo: "Descobri que, para criar um alarme de faturamento, primeiro preciso habilitar os alertas nas preferências de faturamento. Anotado na categoria `TI fundamental`."

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Este módulo é **extremamente importante** para a prova.
> 1.  **AWS Organizations:** Para gerenciar **múltiplas contas** e obter **faturamento consolidado**.
> 2.  **Tagging:** A principal ferramenta para **alocação de custos**.
> 3.  **AWS Cost Explorer:** A ferramenta para **visualizar e analisar** seus custos.
> 4.  **AWS Trusted Advisor:** Te dá **recomendações** em 5 categorias, incluindo **otimização de custos**.
> 5.  **AWS Support Plans:** Conheça os principais níveis (`Basic`, `Developer`, `Business`, `Enterprise`).

---
### <img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Guia Definitivo para a Prova: Dominando Custos, Governança e Suporte

---

### <img src="https://api.iconify.design/logos/aws-organizations.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. AWS Organizations

**Fatos-Chave para a Prova:**

* **O que é?** Um serviço que te ajuda a gerenciar e governar centralmente múltiplas contas AWS.
* **Principal Benefício de Faturamento:** Habilita o **Faturamento Consolidado (Consolidated Billing)**. Você recebe uma única fatura para todas as contas e pode se beneficiar de descontos por volume somado.
* **Estrutura:** Você tem uma **Conta de Gerenciamento (Management Account)**, que é a "matriz", e as **Contas Membro (Member Accounts)**, que são as "filiais".
* **Governança com SCPs:** Você pode usar **Políticas de Controle de Serviço (Service Control Policies - SCPs)**.

> **`!!! tip "Ponto Crítico para a Prova"`**
> As SCPs **NÃO** concedem permissões. Elas funcionam como um "filtro" ou um "guard rail". Elas definem as **permissões máximas** para uma conta. Se uma SCP nega o acesso ao Amazon SageMaker, ninguém naquela conta poderá usar o SageMaker, nem mesmo o administrador (usuário root) da conta.

---

### <img src="https://api.iconify.design/mdi/finance.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. Faturamento e Ferramentas de Custo

**Fatos-Chave para a Prova:**

* **Marcação (Tagging):** É a **base** para a alocação de custos. Tags são etiquetas (chave-valor) que você anexa aos seus recursos (EC2, S3, etc.).
* **AWS Cost Explorer:** A ferramenta para **visualizar, entender e analisar** seus custos e uso da AWS ao longo do tempo. É o seu "software de BI" para finanças na nuvem. Ele usa as tags para filtrar os custos por projeto, departamento, etc.
* **AWS Budgets:** A ferramenta para **criar alertas**. Você define um orçamento (ex: US$ 500 para o mês) e o AWS Budgets te notifica por e-mail ou SNS quando seus custos ou uso **excedem (ou estão prestes a exceder)** esse valor.

> **Diferença Chave:** **Cost Explorer** é para **ANALISAR** o passado. **Budgets** é para **CONTROLAR** o futuro.

---

### <img src="https://api.iconify.design/logos/aws-trusted-advisor.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. AWS Trusted Advisor

**Fatos-Chave para a Prova:**

* **O que é?** Seu **consultor automatizado** que inspeciona seu ambiente AWS e te dá recomendações para seguir as melhores práticas.
* **As 5 Categorias (MEMORIZE ISTO):**
    1.  **<img src="https://api.iconify.design/mdi/cash-multiple.svg?color=currentColor" width="16" /> Otimização de Custos:** (Ex: "Você tem instâncias EC2 ociosas").
    2.  **<img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="16" /> Performance:** (Ex: "A utilização da sua CPU está muito alta").
    3.  **<img src="https://api.iconify.design/mdi/lock-outline.svg?color=currentColor" width="16" /> Segurança:** (Ex: "Seu Security Group permite acesso irrestrito à porta 22").
    4.  **<img src="https://api.iconify.design/mdi/shield-check-outline.svg?color=currentColor" width="16" /> Tolerância a Falhas:** (Ex: "Você não tem backups habilitados no seu RDS").
    5.  **<img src="https://api.iconify.design/mdi/format-list-checks.svg?color=currentColor" width="16" /> Limites de Serviço:** (Ex: "Você está perto de atingir seu limite de VPCs").
* **Nível de Acesso:** No plano de suporte `Basic` (gratuito), você tem acesso a algumas verificações de Segurança e a todas as de Limites de Serviço. Para obter **todas as verificações**, você precisa de um plano de suporte pago (`Business` ou `Enterprise`).

---

### <img src="https://api.iconify.design/mdi/face-agent.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 4. Planos de Suporte da AWS (Tópico Crítico para a Prova)

| Recurso | Basic (Grátis) | Developer | Business | Enterprise |
| :--- | :---: | :---: | :---: | :---: |
| **Caso de Uso**| Pessoal, experimentando | Desenvolvimento/Teste | **Cargas de Trabalho de Produção** | **Cargas de Trabalho de Missão Crítica** |
| **Suporte Técnico** | Apenas faturamento e conta | E-mail (<24h / <12h) | E-mail, Chat, Telefone 24/7 | E-mail, Chat, Telefone 24/7 |
| **Tempo de Resposta (Produção Fora do Ar)** | - | - | **< 1 hora** | **< 1 hora** |
| **Tempo de Resposta (Crítico p/ Negócio Fora do Ar)**| - | - | - | **< 15 minutos** |
| **Acesso a Arquitetos**| Não | Apenas orientação geral | Orientação para seu caso de uso | **Revisões de Arquitetura Consultivas** |
| **Trusted Advisor**| 7 Verificações Core | 7 Verificações Core | **Todas as Verificações** | **Todas as Verificações** |
| **Gerente Técnico de Contas (TAM)**| Não | Não | Não | **SIM (Dedicado)** |