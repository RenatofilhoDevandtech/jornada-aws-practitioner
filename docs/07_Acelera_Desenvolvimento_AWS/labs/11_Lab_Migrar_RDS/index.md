# <img src="https://api.iconify.design/logos/aws-rds.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: A Modernização do Café - Migrando para o Amazon RDS

### O Cenário (A "User Story")

> **Como** o engenheiro de nuvem da Cafeteria, **EU QUERO** migrar o banco de dados da aplicação de um servidor local para uma instância do Amazon RDS, **PARA QUE** eu possa aumentar a performance, a resiliência e a segurança da aplicação, além de reduzir a carga de trabalho operacional da minha equipe.

### A Dor que o Lab Resolve

Rodar uma aplicação e seu banco de dados na mesma instância EC2 é simples para começar, mas é uma arquitetura frágil e que não escala.
1.  **Conflito de Recursos:** O servidor web e o banco de dados competem pela mesma CPU e memória, causando lentidão.
2.  **Risco de Segurança:** O banco de dados fica em uma sub-rede pública, exposto a um risco maior.
3.  **Carga Operacional:** Sua equipe é responsável por tudo: backups, patching, failover, etc.

Este laboratório resolve essas dores **desacoplando** o banco de dados da aplicação, movendo-o para um serviço totalmente gerenciado.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Criar a infraestrutura de rede (sub-redes, security group) para um banco de dados.
* [ ] Lançar uma instância de banco de dados MariaDB no Amazon RDS usando a AWS CLI.
* [ ] Migrar o schema e os dados de um banco MySQL/MariaDB para o RDS.
* [ ] Reconfigurar uma aplicação para usar o novo endpoint do RDS.
* [ ] Monitorar a performance do banco de dados com o Amazon CloudWatch.


---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Gerando Dados de Teste
**Analogia:** Antes de nos mudarmos para a "cozinha nova", vamos fazer alguns pedidos na "cozinha antiga" para termos dados para migrar.

1.  No painel do seu laboratório, clique em **Detalhes > Mostrar (Details > Show)**.
2.  Copie o valor de `CafeInstanceURL` e cole em uma nova aba do navegador.
3.  No site do café, vá em **Menu** e faça pelo menos dois pedidos diferentes.
4.  Vá para a página **Histórico de Pedidos (Order History)** e anote quantos pedidos você fez.

#### Tarefa 2: Construindo a "Cozinha Nova" (Criando a Instância RDS via CLI)

**Analogia:** Agora, vamos construir nossa cozinha de banco de dados profissional, com segurança e rede adequadas.

1.  **Conecte-se ao `Host da CLI (CLI Host)`** usando o EC2 Instance Connect e configure a AWS CLI com `aws configure`, usando as credenciais do seu laboratório.
2.  **Crie a "Fechadura" do Banco de Dados (Security Group):**
    * Substitua `<ID_DA_SUA_VPC>` pelo valor `CafeVpcID` do painel de detalhes.
    ```bash
    aws ec2 create-security-group \
        --group-name CafeDatabaseSG \
        --description "Security group para o banco de dados do Cafe" \
        --vpc-id <ID_DA_SUA_VPC>
    ```
    * Anote o `GroupId` da saída.
    * Agora, autorize a entrada. Substitua os IDs e execute:
    ```bash
    aws ec2 authorize-security-group-ingress \
        --group-id <ID_DO_SEU_NOVO_SG> \
        --protocol tcp --port 3306 \
        --source-group <ID_DO_CAFE_SECURITY_GROUP>
    ```
    > **O "Porquê":** Esta é a melhor prática. Estamos dizendo: "Permita conexões na porta do MySQL (3306) **APENAS** de instâncias que fazem parte do `CafeSecurityGroup` (nosso servidor web)."
3.  **Crie as "Ruas Privadas" (Sub-redes):**
    * O RDS precisa de um **Grupo de Sub-redes (DB Subnet Group)** com pelo menos duas sub-redes privadas em AZs diferentes para alta disponibilidade.
    * Crie as duas sub-redes (substitua os valores de VPC e AZ):
    ```bash
    # Sub-rede Privada 1
    aws ec2 create-subnet \
        --vpc-id <ID_DA_SUA_VPC> \
        --cidr-block 10.200.2.0/23 \
        --availability-zone <AZ_DA_SUA_INSTANCIA_CAFE>
    # (Anote o SubnetId da saída)

    # Sub-rede Privada 2
    aws ec2 create-subnet \
        --vpc-id <ID_DA_SUA_VPC> \
        --cidr-block 10.200.10.0/23 \
        --availability-zone <UMA_AZ_DIFERENTE>
    # (Anote o SubnetId da saída)
    ```
4.  **Crie o Grupo de Sub-redes:**
    ```bash
    aws rds create-db-subnet-group \
        --db-subnet-group-name "CafeDB-Subnet-Group" \
        --db-subnet-group-description "Grupo de sub-redes para o BD do Cafe" \
        --subnet-ids <ID_SUBNET_1> <ID_SUBNET_2>
    ```
5.  **Crie a Instância do Banco de Dados:**
    * Chegou a hora de lançar nosso banco MariaDB gerenciado! Substitua os valores e execute:
    ```bash
    aws rds create-db-instance \
        --db-instance-identifier CafeDBInstance \
        --engine mariadb \
        --db-instance-class db.t3.micro \
        --allocated-storage 20 \
        --db-subnet-group-name "CafeDB-Subnet-Group" \
        --vpc-security-group-ids <ID_DO_SEU_NOVO_SG> \
        --no-publicly-accessible \
        --master-username root --master-user-password 'Re:Start!9'
    ```
6.  **Monitore a Criação:** O banco de dados pode levar até 10 minutos para ser criado. Verifique o status com o comando abaixo até que o `DBInstanceStatus` mude para **`available`**.
    ```bash
    aws rds describe-db-instances --db-instance-identifier CafeDBInstance --query "DBInstances[*].DBInstanceStatus"
    ```
    * Quando estiver `available`, pegue o "endereço" do seu novo banco de dados:
    ```bash
    aws rds describe-db-instances --db-instance-identifier CafeDBInstance --query "DBInstances[*].Endpoint.Address"
    ```
    * **Anote este endereço do Endpoint**. Ele é a informação mais importante.

#### Tarefa 3: A Mudança (Migrando os Dados)
**Analogia:** Agora que a cozinha nova está pronta, vamos usar uma "transportadora" (`mysqldump`) para mover todos os ingredientes.

1.  Conecte-se à instância **`CafeInstance`** (o servidor web original) via EC2 Instance Connect.
2.  **Faça o "dump" (backup) do banco de dados local:**
    ```bash
    mysqldump --user=root --password='Re:Start!9' \
    --databases cafe_db --add-drop-database > cafedb-backup.sql
    ```
3.  **Restaure o backup no novo banco RDS:** (Substitua `<SEU_ENDPOINT_RDS>` pelo endereço que você anotou).
    ```bash
    mysql --user=root --password='Re:Start!9' \
    --host=<SEU_ENDPOINT_RDS> \
    < cafedb-backup.sql
    ```
4.  **Verifique a Migração:** Conecte-se ao RDS e veja se os dados estão lá.
    ```bash
    # Conecta ao RDS
    mysql --user=root --password='Re:Start!9' --host=<SEU_ENDPOINT_RDS> cafe_db

    # Dentro do MySQL, execute a query:
    select * from product;
    exit;
    ```
    > Você deve ver a lista de produtos da cafeteria.

#### Tarefa 4 e 5: Virando a Chave e Monitorando
**Analogia:** Com a cozinha nova abastecida, vamos atualizar o "endereço de entrega" dos pedidos e monitorar o funcionamento.

1.  Vá para o **AWS Systems Manager > Parameter Store**.
2.  Encontre e edite o parâmetro `/cafe/dbUrl`.
3.  No campo **Valor (Value)**, apague o valor antigo e cole o **endereço do Endpoint do seu RDS**. Salve as alterações.
4.  **Verificação:**
    * Atualize a página do site do café no seu navegador. Ele deve continuar funcionando perfeitamente.
    * Vá para a página **Histórico de Pedidos** e confirme que o número de pedidos é o mesmo que você anotou no início. A aplicação agora está usando o RDS!
5.  **Monitoramento:**
    * Vá para o console do **Amazon RDS**, selecione sua `CafeDBInstance` e clique na aba **Monitoramento (Monitoring)**.
    * Observe as métricas do **CloudWatch**, como `CPUUtilization` e `DatabaseConnections`, para ver a saúde do seu novo banco de dados gerenciado.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você executou uma migração de banco de dados do mundo real. Você desacoplou a camada de dados da camada de aplicação, moveu-a para um serviço gerenciado, seguro e resiliente (RDS), e reconfigurou a aplicação para usar o novo banco, tudo com o mínimo de impacto. Esta é uma das tarefas mais valiosas que um engenheiro de nuvem pode realizar.

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: A Cirurgia de Coração Aberto da Minha Aplicação

Hoje foi dia de cirurgia. No laboratório do AWS re/Start, minha missão era pegar uma aplicação que funcionava, mas que tinha um problema de nascença, e realizar um "transplante de coração". Foi um dos desafios mais realistas e gratificantes até agora.

### O Diagnóstico (O Problema)

A aplicação da cafeteria tinha o "coração" (o banco de dados) e o "cérebro" (o servidor web) vivendo no mesmo corpo (a mesma instância EC2).
* **A Dor:** Isso é um problema sério em qualquer arquitetura. Causa conflito de recursos (o site fica lento quando o banco de dados trabalha muito), aumenta o risco de segurança (o banco fica exposto na mesma rede que o site) e dificulta a escalabilidade.
* **O Tratamento:** A cirurgia consistia em **desacoplar** as camadas. Mover o coração para um corpo novo, mais forte e seguro: o **Amazon RDS**.

### A Sala de Cirurgia (Preparando o Ambiente RDS)
Antes da cirurgia, precisei preparar a "sala de operação" estéril. Isso significou usar a AWS CLI para construir a nova casa do banco de dados do zero.
* **O "Aha!" Moment:** Foi incrível ver como as peças de rede se encaixam para criar um ambiente seguro.
    * **Analogia:** Primeiro, construí as **"paredes seguras" (o Security Group do banco de dados)**, com uma regra clara: "Apenas o cérebro (o servidor web) tem permissão para falar com o coração".
    * Depois, desenhei as **"ruas de acesso privadas" (as Sub-redes Privadas)** em "bairros" (Zonas de Disponibilidade) diferentes, garantindo que o coração ficasse protegido da internet.

### O Transplante (A Migração dos Dados)
Com a sala pronta, chegou a hora da parte delicada.
* **A Dor:** Como mover todos os "dados vitais" do coração antigo para o novo sem corromper nada?
* **O Que Eu Fiz:** Usei uma ferramenta padrão do MySQL chamada `mysqldump`.
* **O "Aha!" Moment:**
    * **Analogia:** Foi como usar uma máquina para fazer uma **"cópia exata"** de todo o "sangue" (os dados) do coração antigo. Depois, me conectei ao "coração novo" (o endpoint do RDS) e fiz a **"transfusão"**, restaurando o backup. Ver os dados dos pedidos que eu mesmo criei aparecerem no novo banco foi a confirmação de que a cirurgia estava no caminho certo.

### A Conexão Final (Virando a Chave)
* **A Dor:** Como "dizer" para a aplicação começar a usar o novo coração, sem precisar reescrever o código?
* **O Que Eu Fiz:** A aplicação foi construída de forma inteligente. O "endereço" do banco de dados estava guardado no **Parameter Store**.
* **O "Aha!" Moment:**
    * **Analogia:** Em vez de ter o "endereço do coração" escrito em seu DNA (hard-coded), o "cérebro" perguntava para a **"central de informações" (o Parameter Store)**. Minha única tarefa foi ir até a central e atualizar o endereço para o do novo coração.
* **O Resultado:** Atualizei a página do site e... tudo funcionava perfeitamente. A aplicação nem percebeu que passou por um transplante de coração.

### A Grande Lição
O lab de hoje me ensinou o poder do **desacoplamento** e dos **serviços gerenciados**. Separar a camada de dados da camada de aplicação não é apenas uma boa prática, é o que permite construir sistemas que são, ao mesmo tempo, seguros, escaláveis e fáceis de manter.

Realizar essa "cirurgia" de ponta a ponta me deu uma confiança enorme. Sinto que agora eu não só sei o que é o RDS, mas entendo *por que* ele é tão fundamental para construir aplicações robustas na AWS.

#AWS #Cloud #RDS #DatabaseMigration #DevOps #SysOps #AWSreStart