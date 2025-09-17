# <img src="https://api.iconify.design/logos/aws-vpc.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab [Desafio]: O Arquiteto da Fortaleza - Construindo uma VPC Completa

### O Cenário (A "User Story")

> **Como** um arquiteto de nuvem, **EU QUERO** construir uma VPC completa do zero, com sub-redes públicas e privadas, gateways e roteamento correto, **PARA QUE** eu possa hospedar uma aplicação de forma segura, com os servidores de frontend expostos à internet e os servidores de backend protegidos em uma rede isolada.

### A Dor que o Lab Resolve

Usar a VPC Padrão é fácil, mas não é seguro para produção. A dor que este lab resolve é a **falta de isolamento e controle**. Vamos construir uma arquitetura que segue o princípio de **defesa em profundidade**, separando os recursos em camadas de rede distintas e controlando o fluxo de tráfego entre elas.

### Objetivos de Aprendizado
Ao final deste desafio, você terá construído:

* [ ] Uma **VPC** customizada.
* [ ] Uma **Sub-rede Pública** e uma **Sub-rede Privada**.
* [ ] Um **Internet Gateway** e um **NAT Gateway**.
* [ ] **Tabelas de Rotas** para controlar o fluxo de tráfego.
* [ ] Um **Host Bastião** para acesso administrativo seguro.


---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: Construindo a Fortaleza

**Analogia:** Nossa missão é construir um **"condomínio fechado"** completo, com a "rua da portaria" (pública) e a "rua residencial" (privada).

#### Tarefa 1: Cercando o Terreno (Criar a VPC)
1.  No Console da AWS, navegue até o serviço **VPC**.
2.  Clique em **Criar VPC (Create VPC)**.
3.  Selecione **Somente VPC (VPC only)** e configure:
    * **Tag de nome (Name tag):** `Lab-VPC`
    * **Bloco CIDR IPv4 (IPv4 CIDR block):** `10.0.0.0/16`
4.  Clique em **Criar VPC**.
5.  **Ajuste de DNS:** Selecione sua `Lab-VPC`, vá em **Ações (Actions) > Editar configurações da VPC (Edit VPC settings)** e marque a caixa **Habilitar nomes de host DNS (Enable DNS hostnames)**. Salve.

#### Tarefa 2: Desenhando as Ruas (Criar as Sub-redes)
1.  No menu da VPC, vá em **Sub-redes (Subnets)** e clique em **Criar sub-rede (Create subnet)**.
2.  **Crie a Sub-rede Pública:**
    * **ID da VPC:** `Lab-VPC`.
    * **Nome da sub-rede:** `Sub-rede-Publica`.
    * **Zona de Disponibilidade (Availability Zone):** Escolha a primeira da lista (ex: `us-west-2a`).
    * **Bloco CIDR IPv4:** `10.0.0.0/24`.
3.  **Habilite o IP Público Automático:** Selecione a `Sub-rede-Publica`, vá em **Ações > Editar configurações da sub-rede** e marque **Habilitar atribuição automática de endereço IPv4 público**.
4.  **Crie a Sub-rede Privada:**
    * **ID da VPC:** `Lab-VPC`.
    * **Nome da sub-rede:** `Sub-rede-Privada`.
    * **Zona de Disponibilidade:** Escolha a **mesma** da sub-rede pública.
    * **Bloco CIDR IPv4:** `10.0.2.0/23`.

#### Tarefa 3: Construindo os Portões (Gateways)
1.  **Crie o Internet Gateway (A Portaria Principal):**
    * No menu da VPC, vá em **Gateways da Internet (Internet Gateways)**.
    * Clique em **Criar gateway da Internet**, dê o nome de `Lab-IGW` e crie.
    * Com o `Lab-IGW` selecionado, vá em **Ações > Associar a uma VPC (Attach to VPC)** e associe-o à sua `Lab-VPC`.
2.  **Crie o NAT Gateway (A Portaria de Serviços):**
    * No menu da VPC, vá em **Gateways NAT (NAT Gateways)**.
    * Clique em **Criar gateway NAT (Create NAT gateway)**.
    * **Nome:** `Lab-NAT-Gateway`.
    * **Sub-rede:** Escolha a sua `Sub-rede-Publica`.
    * **Tipo de conectividade:** `Público`.
    * Clique em **Alocar IP elástico (Allocate Elastic IP)**.
    * Clique em **Criar um gateway NAT**.

#### Tarefa 4: Desenhando o Mapa de Trânsito (Tabelas de Rotas)
1.  No menu da VPC, vá em **Tabelas de rotas (Route Tables)**.
2.  **Configure a Tabela de Rotas Pública:**
    * Selecione a tabela de rotas principal da sua `Lab-VPC`. Dê a ela o nome de `Tabela-Rotas-Publica`.
    * Vá na aba **Rotas (Routes)** e clique em **Editar rotas (Edit routes)**.
    * Adicione uma rota: `Destino: 0.0.0.0/0`, `Alvo: Internet Gateway > Lab-IGW`. Salve.
    * Vá na aba **Associações de sub-rede (Subnet associations)** e associe esta tabela à sua `Sub-rede-Publica`.
3.  **Configure a Tabela de Rotas Privada:**
    * Clique em **Criar tabela de rotas (Create route table)**.
    * **Nome:** `Tabela-Rotas-Privada`.
    * **VPC:** `Lab-VPC`.
    * Após criar, selecione-a, vá em **Rotas > Editar rotas**.
    * Adicione uma rota: `Destino: 0.0.0.0/0`, `Alvo: Gateway NAT > Lab-NAT-Gateway`. Salve.
    * Vá na aba **Associações de sub-rede** e associe esta tabela à sua `Sub-rede-Privada`.

#### Tarefa 5: Construindo a Torre de Vigia (O Host Bastião)
1.  Vá para o serviço **EC2** e clique em **Lançar instância (Launch instance)**.
2.  **Nome:** `Servidor-Bastiao`.
3.  **AMI:** `Amazon Linux 2023`.
4.  **Tipo de instância:** `t3.micro`.
5.  **Par de chaves:** Prossiga sem um par de chaves.
6.  **Configurações de rede:**
    * **VPC:** `Lab-VPC`.
    * **Sub-rede:** `Sub-rede-Publica`.
    * **IP público automático:** `Habilitar`.
    * **Grupo de segurança:** Crie um novo chamado `SG-Bastiao` que permita **SSH (porta 22)** da origem `Qualquer lugar (Anywhere)`.
7.  Lance a instância.

---

### <img src="https://api.iconify.design/mdi/puzzle-check-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Desafio Opcional: Testando a Sub-rede Privada

1.  **Lance uma Instância Privada:** Siga os mesmos passos para lançar uma instância, mas com estas diferenças:
    * **Nome:** `Instancia-Privada`.
    * **Sub-rede:** `Sub-rede-Privada`.
    * **Grupo de segurança:** Crie um novo chamado `SG-Privado` que permita **SSH (porta 22)** da origem `10.0.0.0/16` (isso permite acesso de dentro da sua VPC).
2.  **Conecte-se ao Bastião:** Use o **EC2 Instance Connect** para se conectar ao `Servidor-Bastiao`.
3.  **Pule para a Instância Privada:**
    * No console do EC2, copie o **Endereço IPv4 privado (Private IPv4 address)** da sua `Instancia-Privada`.
    * No terminal do Bastião, conecte-se a ela: `ssh <IP_PRIVADO_DA_INSTANCIA>`.
4.  **Teste a Conexão de Saída:** Dentro da Instância Privada, execute:
    ```bash
    ping -c 3 amazon.com
    ```
    > **Verificação:** O `ping` deve funcionar! Isso prova que sua instância na sub-rede privada está acessando a internet através do seu **NAT Gateway**.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns, arquiteto! Você construiu uma VPC segura do zero, com camadas de rede distintas, roteamento correto e um ponto de acesso administrativo seguro. Esta é a base para 90% das arquiteturas de aplicação na AWS.

---

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: Da Primeira Cerca ao Castelo Digital

Hoje foi o "exame final" do meu módulo de redes no AWS re/Start. A missão não era seguir uma receita, mas sim encarar uma tela em branco e construir, do zero, uma infraestrutura de rede segura e funcional. Foi o momento em que a teoria se tornou prática.

O desafio era criar um ambiente completo: uma rede privada virtual (VPC), com ruas públicas e privadas, portões para a internet e um sistema de acesso seguro para administrar tudo.

### A Jornada em 3 Atos: Arquiteto, Engenheiro de Trânsito e Segurança

#### Ato 1: O Urbanista (Planejando a Rede)
* **A Dor:** É muito fácil colocar tudo em uma única rede pública, mas isso é como construir um banco com a porta do cofre abrindo direto para a rua. É inseguro e nada profissional.
* **O Que Eu Fiz:** Tive que agir como um **urbanista**.
    * **Analogia:** Recebi um **"terreno vazio"** e precisei planejar tudo. Primeiro, ergui os **"muros do condomínio" (a VPC)**. Depois, desenhei duas "ruas": uma **"rua comercial" na entrada (a Sub-rede Pública)** e uma **"rua residencial" nos fundos (a Sub-rede Privada)**.
* **O "Aha!" Moment:** O poder da segmentação. Ao separar os recursos em sub-redes diferentes, eu criei a primeira e mais importante camada de segurança.

#### Ato 2: O Engenheiro de Trânsito (Configurando as Rotas)
* **A Dor:** As ruas e os portões existem, mas como os "carros" (o tráfego de dados) sabem para onde ir? Como um morador da rua privada consegue receber uma "entrega da internet" (como uma atualização de software)?
* **O Que Eu Fiz:** Vesti o chapéu de **"engenheiro de trânsito"** e configurei as **Tabelas de Rotas (Route Tables)**.
* **O "Aha!" Moment:** A lógica do **NAT Gateway** finalmente "clicou" na prática.
    1.  Para a rua pública, a placa era simples: "Para a internet (`0.0.0.0/0`), use a portaria principal (`Internet Gateway`)".
    2.  Para a rua privada, a placa era a mágica: "Para a internet, vá primeiro para a **portaria de serviços (`NAT Gateway`)**".
* **A Descoberta:** O NAT Gateway é o intermediário genial. Ele permite que meus servidores privados *iniciem* uma conversa com a internet, mas impede que a internet inicie uma conversa com eles. É a segurança em ação.

#### Ato 3: O Segurança (O Host Bastião)
* **A Dor:** Como eu, o administrador, entro na "rua residencial privada" para fazer a manutenção das casas, sem criar uma porta dos fundos vulnerável?
* **O Que Eu Fiz:** Construí uma **"torre de vigia" fortificada (o Host Bastião)** na rua pública.
* **O "Aha!" Moment:**
    * **Analogia:** O Bastião é a **única entrada permitida** para administradores. De lá, eu usei uma **"passagem secreta" (uma conexão SSH privada)** para chegar às casas na rua residencial. Foi a aplicação prática perfeita da defesa em camadas.

### A Grande Lição
O maior aprendizado deste desafio foi a **ordem das operações**. Na nuvem, a arquitetura é construída de fora para dentro: **1º a Rede, 2º a Segurança da Rede, 3º o Servidor, 4º a Aplicação**. Tentar fazer o passo 3 antes do 1 simplesmente não funciona.

Foi desafiador, mas ver a minha própria página web, rodando em um servidor que lancei, dentro de uma rede que eu mesmo projetei do zero, foi incrivelmente gratificante. A sensação de "pingar" um site da internet de dentro de uma instância privada, vendo o tráfego passar por todas as camadas que eu construí, foi a prova de que as peças do quebra-cabeça estão finalmente se encaixando.

#AWS #Cloud #VPC #Networking #Security #DevOps #AWSreStart #HandsOn