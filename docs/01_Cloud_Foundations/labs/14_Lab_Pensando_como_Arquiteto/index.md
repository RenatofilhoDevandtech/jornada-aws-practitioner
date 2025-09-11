# <img src="https://api.iconify.design/mdi/calculator-variant-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab 01: O Arquiteto Financeiro - Orçando um Projeto com o AWS Pricing Calculator

### O Cenário (A "User Story" do Cliente)

> **Como** o fundador de uma nova startup de e-commerce, **EU QUERO** uma estimativa de custo mensal para hospedar minha loja virtual na AWS, **PARA QUE** eu possa validar a viabilidade financeira do meu projeto e apresentá-lo a investidores.

### A Dor que o Lab Resolve

Um cliente nunca aprovará um projeto sem saber o custo. A "dor" aqui é a **incerteza financeira**. Um arquiteto de nuvem de sucesso não apenas projeta a melhor solução técnica, mas também a solução mais **custo-efetiva**. O AWS Pricing Calculator é a sua principal ferramenta para traduzir uma arquitetura em um orçamento claro e defender suas decisões.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Navegar na interface do AWS Pricing Calculator.
* [ ] Modelar uma arquitetura web de 3 camadas (Balanceador de Carga, Servidores Web, Banco de Dados).
* [ ] Comparar o impacto financeiro de diferentes modelos de preços (Sob Demanda vs. Savings Plans).
* [ ] Gerar e compartilhar uma estimativa de custos profissional.

### Pré-requisitos
* Um navegador web.
> **`!!! note "Nenhuma Conta AWS é Necessária!"`**
> Este laboratório é 100% focado em planejamento e não cria nenhum recurso real. É uma ferramenta gratuita e aberta a todos, perfeita para praticar sem medo de custos.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: Orçando a Loja Virtual

A arquitetura que vamos orçar é um pilar da nuvem: uma aplicação web resiliente e escalável.

#### Passo 1: Acessando a Ferramenta e Configurando o Grupo
1.  Acesse o AWS Pricing Calculator: **[https://calculator.aws/](https://calculator.aws/)**
2.  Clique em **Create estimate** (Criar estimativa).
3.  Por padrão, você está em um grupo chamado "My estimate". Vamos renomeá-lo. Clique no ícone de lápis ao lado do nome e renomeie para `Arquitetura-Loja-Virtual`. Isso ajuda a organizar estimativas complexas.

#### Passo 2: Adicionando os Servidores da Aplicação (Amazon EC2)
1.  Na barra de busca, digite `EC2` e clique em **Configure** no serviço **Amazon EC2**.
2.  Vamos preencher a "ficha técnica" dos nossos servidores:
    * **Region** (Região): Selecione `South America (Sao Paulo)`.
    * **EC2 instance specifications** (Especificações da instância):
        * **Operating system**: `Linux`.
        * **Search for instance type** (Buscar tipo): `t3.micro`.
        * **Number of instances** (Número de instâncias): `2`. (Para alta disponibilidade).
    * **Pricing strategy** (Estratégia de preços): Deixe em **On-Demand** por enquanto.
3.  Role para baixo até **Amazon Elastic Block Store (EBS)**.
    * **Storage amount** (Quantidade de armazenamento): Digite `30` GB.
4.  Clique em **Add to my estimate** (Adicionar à minha estimativa).

#### Passo 3: Adicionando o Balanceador de Carga (ELB)
1.  Na tela principal da estimativa, clique em **Add service** (Adicionar serviço).
2.  Procure por `Elastic Load Balancing` e clique em **Configure**.
3.  Selecione **Application Load Balancer**.
4.  Role para baixo até **Data processing** (Processamento de dados). Para uma loja pequena/média, vamos estimar `100` GB de tráfego processado por mês.
5.  Clique em **Add to my estimate**.

#### Passo 4: Adicionando o Banco de Dados (Amazon RDS)
1.  Clique em **Add service** novamente.
2.  Procure por `Amazon RDS for MySQL` e clique em **Configure**.
3.  Preencha as informações:
    * **Region**: `South America (Sao Paulo)`.
    * **Deployment option** (Opção de implantação): Selecione **Multi-AZ deployment**.
        > **(ITIL - Disponibilidade):** Por que Multi-AZ? Para um e-commerce, a disponibilidade é crítica. Esta opção cria uma réplica de segurança do banco de dados em outra Zona de Disponibilidade, garantindo que a loja não saia do ar se houver uma falha.
    * **DB instance** (Instância de BD): Selecione uma da família `db.t3`, por exemplo, `db.t3.micro`.
    * **Storage amount** (Quantidade de armazenamento): Digite `20` GB.
4.  Clique em **Add to my estimate**.

---

### <img src="https://api.iconify.design/mdi/chart-line.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Análise do Arquiteto

Agora, na sua tela de estimativa, você tem o poder.

* **Analise o Custo Total:** Veja o custo mensal estimado. É viável para o cliente?
* **Otimize com Savings Plans:** Volte na configuração do **EC2** e do **RDS** e mude a estratégia de preços para **1 Year No Upfront Savings Plan**. Observe a queda no custo mensal.
    > **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> Insight para o Cliente:** "Podemos começar com o modelo Sob Demanda para ter flexibilidade. Assim que validarmos o tráfego nos primeiros meses, podemos migrar para um Savings Plan e reduzir nossos custos em até 40%, sem nenhum pagamento inicial."

* **Compartilhe a Estimativa:** No topo da página, clique em **Actions** (Ações) > **Save and share**. Isso gera um link público que você pode enviar para seu cliente ou equipe.

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos
* [x] **Não há nada para limpar!** Você acaba de projetar e orçar uma arquitetura completa sem gastar um único centavo.

### <img src="https://api.iconify.design/mdi/comment-quote-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você agiu como um verdadeiro Arquiteto de Nuvem. Você pegou um requisito de negócio, projetou uma solução técnica resiliente e, o mais importante, traduziu essa solução em um orçamento claro e otimizado.

Agora que sabemos planejar, no próximo laboratório, vamos começar a construir.