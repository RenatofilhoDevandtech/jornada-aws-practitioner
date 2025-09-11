# <img src="https://api.iconify.design/mdi/calculator-variant-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab 01: O Planejador - Estimando Custos com o AWS Pricing Calculator

### O Cenário (A "User Story")

> **Como** o fundador de uma nova startup, **EU QUERO** estimar o custo mensal de hospedar minha aplicação web na AWS, **PARA QUE** eu possa criar um orçamento, apresentar aos meus investidores e tomar uma decisão financeira informada.

### A Dor que o Lab Resolve

No mundo tradicional, o custo da infraestrutura é um grande investimento inicial (CapEx). Na nuvem, é um custo operacional mensal (OpEx), mas pode ser difícil de prever. O AWS Pricing Calculator é a ferramenta oficial e gratuita que transforma a incerteza em uma estimativa clara, permitindo que você planeje seus gastos sem surpresas.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Navegar na interface do AWS Pricing Calculator.
* [ ] Adicionar e configurar serviços (EC2, EBS, ELB) a uma estimativa.
* [ ] Comparar diferentes modelos de preços (On-Demand vs. Savings Plans).
* [ ] Gerar um relatório final de custo estimado.

### Pré-requisitos
* Um navegador web.
> **`!!! note "Nenhuma Conta AWS é Necessária!"`**
> A melhor parte deste laboratório é que ele é 100% gratuito e não exige que você tenha uma conta na AWS. É uma ferramenta de planejamento aberta a todos.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

Nossa missão é orçar uma arquitetura web básica, mas realista e resiliente: dois pequenos servidores web atrás de um balanceador de carga.

#### Passo 1: Acessando a Ferramenta
1.  Abra seu navegador e acesse o AWS Pricing Calculator: **[https://calculator.aws/](https://calculator.aws/)**
2.  Clique em **Create estimate** (Criar estimativa).

#### Passo 2: Configurando os Servidores Web (Amazon EC2)
1.  Na barra de busca, digite `EC2` e clique em **Configure** no serviço **Amazon EC2**.
2.  Uma nova página de configuração se abrirá. Vamos preenchê-la:
    * **Region** (Região): Na lista, procure e selecione `South America (Sao Paulo)`.
    * Na seção **EC2 instance specifications** (Especificações da instância EC2):
        * **Tenancy**: Mantenha `Shared` (Compartilhado).
        * **Operating system**: Mantenha `Linux`.
        * **Workload**: Mantenha `Constant usage` (Uso constante).
        * **Search for instance type** (Buscar tipo de instância): Digite `t3.micro` e selecione-o.
        * **Number of instances** (Número de instâncias): Digite `2`.

3.  Agora, a mágica da otimização de custos:
    * Role para baixo até a seção **Pricing strategy** (Estratégia de preços).
    * Você verá o custo mensal para o modelo **On-Demand** (Sob Demanda).
    * Agora, selecione **Savings Plans**. Escolha `1 year` (1 ano) e `No upfront` (Sem pagamento inicial).
    > **`!!! tip "Dica de Especialista"`**
    > Observe a economia! O Savings Plan oferece um desconto significativo em troca de um compromisso de uso, mesmo sem pagamento adiantado. Esta é uma das principais formas de otimizar custos na AWS.

#### Passo 3: Configurando o Armazenamento (Amazon EBS)
1.  Na mesma página de configuração do EC2, role para baixo até a seção **Amazon Elastic Block Store (EBS)**.
2.  Cada instância EC2 precisa de um "HD". A configuração já vem com um volume padrão. Vamos ajustar:
    * **Storage type** (Tipo de armazenamento): Mantenha `General Purpose SSD (gp3)`.
    * **Amount of storage (GB per month)** (Quantidade de armazenamento): Digite `30`.
3.  Clique em **Add to my estimate** (Adicionar à minha estimativa) no final da página.

#### Passo 4: Configurando o Balanceador de Carga (ELB)
1.  Agora você está de volta à tela principal da sua estimativa. Clique em **Add service** (Adicionar serviço).
2.  Procure por `Elastic Load Balancing` e clique em **Configure**.
3.  Selecione **Application Load Balancer**.
4.  Role para baixo até a seção **Data processing** (Processamento de dados) e estime o tráfego que seu site receberá. Para nosso exemplo, insira `100` GB.
5.  Clique em **Add to my estimate**.

---

### <img src="https://api.iconify.design/mdi/check-all.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Verificação

Na página da sua estimativa, você agora vê um resumo completo. Ele mostra o custo inicial, o custo mensal e o custo total em 12 meses. Você pode ver o detalhamento de cada serviço e comparar os custos entre os modelos de pagamento.

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos

A melhor parte deste laboratório:
* [x] **Não há nada para limpar!**
> Como o AWS Pricing Calculator é uma ferramenta de planejamento, ele não cria nenhum recurso real na sua conta e, portanto, **não gera nenhum custo**.

---

### <img src="https://api.iconify.design/mdi/comment-quote-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão

Parabéns! Você acaba de realizar uma das tarefas mais importantes de um arquiteto de nuvem: traduzir uma ideia de arquitetura em uma estimativa de custo concreta. Você aprendeu a navegar na ferramenta, a configurar serviços e a comparar modelos de preços.

Agora que planejamos e orçamos nosso primeiro projeto, o próximo passo é construí-lo de verdade!