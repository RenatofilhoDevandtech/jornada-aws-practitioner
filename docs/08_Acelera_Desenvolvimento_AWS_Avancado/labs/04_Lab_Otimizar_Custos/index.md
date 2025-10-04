# <img src="https://api.iconify.design/mdi/cash-sync.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: A Dieta da Nuvem - Otimizando Recursos para Reduzir Custos

### O Cenário (A "User Story")

> **Como** um arquiteto de nuvem consciente dos custos, **EU QUERO** analisar uma arquitetura existente, identificar recursos superdimensionados ou desnecessários e redimensioná-los, **PARA QUE** eu possa reduzir a fatura mensal da AWS sem impactar a performance da aplicação.

### A Dor que o Lab Resolve

É muito comum, após uma migração para a nuvem, que os recursos sejam superdimensionados "só por segurança". A dor que este lab resolve é o **desperdício de dinheiro com recursos ociosos**. Vamos aprender a "aparar as gorduras" de uma arquitetura, um processo contínuo de otimização de custos.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Analisar uma arquitetura e identificar oportunidades de otimização.
* [ ] Desinstalar software desnecessário de uma instância EC2.
* [ ] Redimensionar (`right-size`) uma instância EC2 para um tipo menor usando a AWS CLI.
* [ ] Usar a **Calculadora de Preços da AWS (AWS Pricing Calculator)** para estimar e comparar os custos antes e depois da otimização.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: A Otimização

#### Tarefa 1: O Diagnóstico e a "Cirurgia"

**Analogia:** Nossa aplicação é um paciente que passou por um "transplante de coração" (a migração para o RDS). Agora, o coração antigo ainda está lá, desativado, e o paciente está usando uma "maca" maior do que o necessário. Vamos fazer a cirurgia de remoção e dar alta para um "quarto" menor.

1.  **Gere Dados de Teste:**
    * No painel do seu laboratório, clique em **Detalhes > Mostrar (Details > Show)**.
    * Copie o valor de `CafeInstanceURL` e cole em uma nova aba do navegador.
    * No site do café, vá em **Menu** e faça alguns pedidos para garantir que temos dados no banco de dados do RDS.

2.  **Conecte-se à Instância `CafeInstance`:**
    * No console do **EC2**, encontre a instância `CafeInstance`.
    * Use o método de sua preferência (SSH ou EC2 Instance Connect) para se conectar a ela.
    > **O "Porquê":** A otimização começa dentro do servidor. Precisamos remover o software antigo.

3.  **Remova o Banco de Dados Antigo:**
    * No terminal da `CafeInstance`, pare e remova o serviço MariaDB local, que não é mais usado.
    ```bash
    # Parar o serviço do banco de dados local
    sudo systemctl stop mariadb

    # Desinstalar o pacote do servidor de banco de dados
    sudo yum -y remove mariadb-server
    ```
    > **O "Porquê":** Esta ação libera espaço em disco e recursos de CPU/memória na instância, justificando o redimensionamento que faremos a seguir.

4.  **Conecte-se ao `Host da CLI (CLI Host)`:**
    * Abra uma **segunda janela de terminal** e conecte-se à instância `CLI Host`.
    * Configure a AWS CLI com `aws configure` e as credenciais do laboratório.
    > **O "Porquê":** Faremos as ações de infraestrutura (parar/modificar/iniciar a outra instância) a partir deste host de comando, simulando uma automação centralizada.

5.  **Redimensione a Instância (`Right-Sizing`):**
    * **Encontre o ID da instância** a ser modificada:
    ```bash
    aws ec2 describe-instances --filters "Name=tag:Name,Values=CafeInstance" --query "Reservations[0].Instances[0].InstanceId" --output text
    ```
    * Anote o `InstanceId`.
    * **Pare a instância:**
    ```bash
    aws ec2 stop-instances --instance-ids <ID_DA_SUA_CAFEINSTANCE>
    ```
    * **Modifique o tipo de instância** (a "cirurgia" de redimensionamento):
    ```bash
    aws ec2 modify-instance-attribute --instance-id <ID_DA_SUA_CAFEINSTANCE> --instance-type "{\"Value\": \"t3.micro\"}"
    ```
    * **Inicie a instância novamente:**
    ```bash
    aws ec2 start-instances --instance-ids <ID_DA_SUA_CAFEINSTANCE>
    ```
6.  **Verificação:**
    * Aguarde a instância estar no estado `running`.
    * Pegue o **novo** endereço IP público dela:
    ```bash
    aws ec2 describe-instances --instance-ids <ID_DA_SUA_CAFEINSTANCE> --query "Reservations[0].Instances[0].PublicIpAddress" --output text
    ```
    * Acesse `http://<NOVO_IP_PUBLICO>/cafe` no navegador. O site deve funcionar perfeitamente, agora rodando em uma máquina menor e mais barata.

#### Tarefa 2: Quantificando a Economia (Usando a Calculadora de Preços)

**Analogia:** Agora que otimizamos, vamos usar a "planilha de orçamento" da AWS para mostrar ao "CFO" (seu chefe) exatamente quanto dinheiro economizamos.

1.  **Acesse a Calculadora de Preços da AWS:** [calculator.aws](https://calculator.aws)
2.  Clique em **Criar estimativa (Create estimate)**.

##### Estimativa 1: O Custo ANTES da Otimização
1.  Adicione o serviço **Amazon EC2**:
    * **Região (Region):** A mesma do seu laboratório.
    * **Tipo de instância (Instance type):** `t3.small`.
    * **Estratégia de preços (Pricing strategy):** `Sob demanda (On-Demand)`.
    * **Armazenamento EBS (EBS storage):** `gp2`, **40 GB**.
    * Clique em **Adicionar à minha estimativa (Add to my estimate)**.
2.  Adicione o serviço **Amazon RDS for MariaDB**:
    * **Região:** A mesma.
    * **Tipo de instância:** `db.t3.micro`.
    * **Modelo de preço:** `Sob demanda (On-Demand)`.
    * **Armazenamento (Storage):** `gp2`, **20 GB**.
    * Clique em **Adicionar à minha estimativa**.
3.  **Anote o Custo Mensal Total** da sua estimativa.

##### Estimativa 2: O Custo DEPOIS da Otimização
1.  Na sua estimativa, clique em **Editar (Edit)** no serviço Amazon EC2.
2.  Altere o **Tipo de instância** para `t3.micro`.
3.  Altere a **Quantidade de armazenamento (Storage amount)** do EBS para **20 GB**.
4.  Clique em **Salvar (Save)**.
5.  **Anote o Novo Custo Mensal Total**.

##### O Resultado
Compare os dois totais. Você verá uma economia de custos mensal significativa, simplesmente por remover um software desnecessário e escolher um "motor" do tamanho certo para a carga de trabalho.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você atuou como um verdadeiro especialista em FinOps. Você analisou uma arquitetura, identificou desperdícios, executou as mudanças técnicas para otimizar os recursos e, o mais importante, usou a Calculadora de Preços para **quantificar o valor de negócio** da sua otimização. Esta é uma habilidade essencial que demonstra não apenas conhecimento técnico, mas também visão de negócio.