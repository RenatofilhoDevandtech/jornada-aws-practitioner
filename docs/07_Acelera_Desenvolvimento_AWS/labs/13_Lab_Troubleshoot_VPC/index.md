# <img src="https://api.iconify.design/mdi/magnify-scan.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Detetive da Rede - Solucionando Problemas na VPC com Flow Logs

### O Cenário (A "User Story")

> **Como** um engenheiro de redes, **EU QUERO** usar os VPC Flow Logs para capturar e analisar o tráfego de rede, **PARA QUE** eu possa diagnosticar problemas de conectividade, identificar tráfego não autorizado e garantir que minhas regras de segurança estão funcionando como esperado.

### A Dor que o Lab Resolve

Quando uma conexão falha na nuvem, pode ser por vários motivos: Security Group, Network ACL, Tabela de Rotas... A dor é a **falta de visibilidade**. Como saber *onde* o tráfego está sendo bloqueado? Os **VPC Flow Logs** são a "câmera de segurança" da sua rede. Eles gravam cada tentativa de conexão, mostrando o que foi `ACCEPT` (Aceito) e o que foi `REJECT` (Rejeitado), te dando as pistas necessárias para resolver o mistério.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Criar um bucket S3 para armazenar logs.
* [ ] Habilitar os VPC Flow Logs para uma VPC.
* [ ] Usar um método de troubleshooting sistemático para corrigir problemas de rede.
* [ ] Baixar e analisar os logs de fluxo para encontrar a causa raiz de uma falha.


---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: A Investigação

#### Tarefa 1: Instalando as "Câmeras de Segurança" (Habilitar os Flow Logs)

**Analogia:** Antes que o "crime" aconteça, o detetive precisa instalar as câmeras para gravar as evidências.

1.  **Conecte-se ao `Host da CLI (CLI Host)`** e configure a AWS CLI com `aws configure`.
2.  **Crie o "Depósito de Gravações" (O Bucket S3):**
    * Substitua `######` por 6 números aleatórios para criar um nome único.
    ```bash
    aws s3api create-bucket --bucket flowlogs-renato-###### --region 'us-west-2' --create-bucket-configuration LocationConstraint='us-west-2'
    ```
3.  **Ligue as "Câmeras" (Crie os Flow Logs):**
    * Primeiro, encontre o ID da sua VPC (substitua os valores se necessário):
    ```bash
    aws ec2 describe-vpcs --filters "Name=tag:Name,Values='VPC1'" --query 'Vpcs[0].VpcId' --output text
    ```
    * Agora, crie o log de fluxo (substitua `<vpc-id>` e o `<nome-do-seu-bucket>`):
    ```bash
    aws ec2 create-flow-logs \
        --resource-type VPC --resource-ids <vpc-id> \
        --traffic-type ALL \
        --log-destination-type s3 \
        --log-destination arn:aws:s3:::<nome-do-seu-bucket>
    ```
    > **O "Porquê":** Estamos dizendo à AWS: "Grave *todo* o tráfego (`ALL`) que passa pela `VPC1` e envie as gravações para este bucket S3."

#### Tarefa 2: A Cena do Crime (Identificando o Problema)
1.  No painel do laboratório, copie o valor de `WebServerIP` e cole em uma nova aba do navegador. **A página não vai carregar.** (`ERR_CONNECTION_TIMED_OUT`).
2.  Tente se conectar à mesma instância via **EC2 Instance Connect**. **A conexão também vai falhar.**
3.  **Diagnóstico Inicial:** Temos uma vítima (`WebServer`) que está viva (sabemos que a instância foi provisionada), mas completamente isolada.

#### Tarefa 3: O Inquérito (Solucionando os Problemas)

**Analogia:** É hora de agir como um detetive. Vamos seguir um método, do mais provável para o menos provável.

##### Desafio #1: O Problema de Acesso Público
* **Pista:** A falha de conexão HTTP (porta 80) sugere um problema de roteamento ou firewall.
* **Investigação (Usando a CLI):**
    1.  **O Servidor está OK?** O `describe-instances` confirma que ele está `running`.
    2.  **A "Fechadura da Casa" (Security Group) está OK?**
        ```bash
        # Substitua pelo ID do SG do WebServer (WebServerSgId nos detalhes do lab)
        aws ec2 describe-security-groups --group-ids <WebServerSgId>
        ```
        > Você notará que o SG **permite** tráfego nas portas 80 e 22. Então, o problema não está aqui.
    3.  **O "Mapa da Rua" (Route Table) está OK?**
        ```bash
        # Substitua pelo ID da sub-rede pública (VPC1PubSubnetID)
        aws ec2 describe-route-tables --filter "Name=association.subnet-id,Values='<VPC1PubSubnetID>'"
        ```
        > **A Descoberta:** Você verá que a tabela de rotas da sub-rede pública **NÃO TEM** uma rota para a internet! Ela só conhece a rota `local`.
* **A Solução:**
    ```bash
    # Substitua pelos IDs da Route Table e do Internet Gateway (nos detalhes do lab)
    aws ec2 create-route \
        --route-table-id <VPC1PubRouteTableId> \
        --gateway-id <VPC1GatewayId> \
        --destination-cidr-block '0.0.0.0/0'
    ```
* **Verificação:** Atualize a página do `WebServerIP` no navegador. **Agora você deve ver a mensagem "Hello From Your Web Server!"**.

##### Desafio #2: O Problema de Acesso Administrativo
* **Pista:** O site funciona, mas a conexão SSH (porta 22) via Instance Connect ainda falha. O Security Group já permite a porta 22. Qual é a outra camada de firewall? **A Network ACL.**
* **Investigação:**
    ```bash
    # Substitua pelo ID da sub-rede pública (VPC1PublicSubnetID)
    aws ec2 describe-network-acls --filter "Name=association.subnet-id,Values='<VPC1PublicSubnetID>'"
    ```
    > **A Descoberta:** Você verá regras explícitas de `Deny` (Negar) na Network ACL que estão bloqueando o tráfego.
* **A Solução:**
    ```bash
    # Substitua pelo ID da sua NACL e o número da regra que você quer deletar
    aws ec2 delete-network-acl-entry --network-acl-id <acl-id> --ingress --rule-number 40
    ```
* **Verificação:** Tente se conectar via **EC2 Instance Connect** novamente. **Agora deve funcionar!**

#### Tarefa 4: A Análise Forense (Analisando os Logs de Fluxo)
Agora que os crimes foram resolvidos, vamos analisar as "fitas da câmera de segurança" para ver as tentativas de invasão.

1.  **Baixe as Evidências:**
    ```bash
    mkdir ~/flowlogs
    cd ~/flowlogs
    aws s3 cp s3://<nome-do-seu-bucket>/ . --recursive
    ```
2.  **Descompacte os Arquivos:** Navegue pela estrutura de pastas que foi criada (`cd AWSLogs/...`) e descompacte os arquivos de log:
    ```bash
    gunzip *.gz
    ```
3.  **Procure por Pistas:** Use o `grep` para filtrar os logs.
    * **Encontre as tentativas de conexão SSH que foram REJEITADAS:**
    ```bash
    # Procura por linhas que contenham a porta 22 E a palavra REJECT
    grep -rn 22 . | grep REJECT
    ```
    > **O Resultado:** Você verá as entradas de log exatas, gravadas no momento em que suas tentativas de conexão SSH falharam, provando que foi a Network ACL que bloqueou o tráfego.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns, detetive! Você usou as ferramentas da AWS não apenas para construir, mas para **diagnosticar e consertar** uma infraestrutura de rede com problemas. Você aprendeu o fluxo de troubleshooting e viu o poder dos VPC Flow Logs para obter visibilidade e encontrar a causa raiz dos problemas.

---

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: Colocando o Chapéu de Sherlock Holmes na Nuvem

A missão de hoje foi diferente. Eu não recebi um terreno vazio para construir; recebi a chave de um "condomínio" (uma VPC) que estava um caos. Nada se conectava. Minha tarefa era ser o detetive, encontrar os problemas e consertar a rede.

Foi um dos laboratórios mais realistas e desafiadores do AWS re/Start até agora, e com certeza um dos que mais me ensinou.

### A Investigação em 3 Atos

#### Ato 1: Instalando as Câmeras de Segurança (VPC Flow Logs)
Antes de entrar na cena do crime, um bom detetive instala suas ferramentas de vigilância.

* **A Dor:** Como eu posso saber o que está acontecendo na minha rede? Quais conexões estão sendo permitidas e quais estão sendo bloqueadas? Sem visibilidade, solucionar problemas é um tiro no escuro.
* **O Que Eu Fiz:** A primeira coisa que fiz foi habilitar os **VPC Flow Logs**.
* **O "Aha!" Moment:**
    * **Analogia:** Foi como instalar **"câmeras de segurança"** em todas as ruas do condomínio. Eu configurei o sistema para gravar cada "carro" (pacote de dados) que tentasse entrar ou sair, e enviar todas as "fitas" para um **"depósito de evidências" seguro (um bucket S3)**. Com as câmeras ligadas, a investigação podia começar.

#### Ato 2: O Mistério da Ilha Isolada

* **A Pista:** O servidor web estava ligado, mas ninguém de fora conseguia acessá-lo. O navegador só mostrava `Connection Timed Out`.
* **A Investigação:** Segui meu checklist de detetive, camada por camada. A "fechadura da casa" (Security Group) parecia ok. O "guarda da rua" (Network ACL) também. Mas quando olhei o "mapa de trânsito" (a Tabela de Rotas)...
* **A Descoberta:** A rua principal do condomínio **não tinha uma placa indicando a saída para a "rodovia" (a internet)**. Faltava a rota para o **Internet Gateway**.
    * **Analogia:** Era uma ilha sem porto. As pessoas podiam andar dentro da ilha, mas ninguém de fora conseguia chegar. A solução foi "construir o porto" (garantir que o Internet Gateway estava anexado) e "colocar a placa de 'Saída'" (adicionar a rota `0.0.0.0/0` na tabela).

#### Ato 3: O Muro Interno

* **A Pista:** O site agora funcionava, mas eu, o administrador, não conseguia entrar pela "porta dos fundos" (SSH).
* **A Investigação:** Eu sabia que o Security Group estava permitindo meu acesso. Então, o culpado só podia ser a outra camada de defesa: o "guarda da rua" (a Network ACL).
* **A Descoberta:** Ao investigar a NACL com a CLI, encontrei uma regra explícita de `Deny` (Negar) que estava bloqueando todo o tráfego. Alguém tinha construído um muro no meio do condomínio! Removi a regra, e o acesso foi liberado.

### A Prova Final: A Análise Forense
A parte mais legal foi voltar ao "depósito de evidências" (o S3), baixar as "fitas" (os logs) e, usando o comando `grep`, encontrar a linha exata que dizia: `... REJECT ...` para a minha tentativa de conexão na porta 22. Ver a evidência do "crime" que eu mesmo tinha acabado de resolver foi incrível.

### A Grande Lição
Este lab me ensinou que **troubleshooting é um método**. Não é sorte, é processo. O fluxo é sempre:

1.  Verifique a **Instância**.
2.  Verifique o **Security Group**.
3.  Verifique a **Network ACL**.
4.  Verifique a **Tabela de Rotas**.

Consertar algo que está quebrado te dá uma compreensão muito mais profunda do que construir algo do zero. Este lab me deu a confiança de que, com um método lógico e as ferramentas certas como os Flow Logs, posso encarar qualquer problema de rede na nuvem.

#AWS #Cloud #Networking #Troubleshooting #Security #VPC #DevOps #AWSreStart