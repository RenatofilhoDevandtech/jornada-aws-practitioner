# <img src="https://api.iconify.design/logos/aws-elb.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Maestro do Tráfego: Guia Definitivo do Elastic Load Balancing (ELB)

Sua aplicação está rodando em uma frota de instâncias EC2. Mas como os clientes chegam até elas? E como você distribui os milhões de pedidos que chegam durante um pico de tráfego?

A resposta é o **Elastic Load Balancing (ELB)**.

* **O que é?** Um serviço que distribui automaticamente o tráfego de entrada entre múltiplos destinos (como instâncias EC2, contêineres e funções Lambda) em uma ou mais Zonas de Disponibilidade.
* **Analogia:** Pense no ELB como o **"Maestro de Trânsito Inteligente"** na entrada de uma **praça de alimentação movimentada**.
    * **Os Clientes:** São as requisições de rede.
    * **Os Restaurantes:** São suas instâncias EC2.
* **A Dor que o ELB Resolve:**
    1.  **Ponto Único de Falha:** Sem um ELB, se seu único servidor falhar, sua aplicação inteira sai do ar.
    2.  **Sobrecarga:** Sem um ELB, todo o tráfego vai para um único servidor, que pode ficar sobrecarregado e lento.

O "Maestro" (ELB) fica na entrada, verifica quais "restaurantes" (instâncias) estão abertos e com menos fila (`Health Checks`), e direciona cada cliente para o melhor destino, garantindo que ninguém espere demais e que o serviço nunca pare.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Os 3 Tipos de Maestro (Tipos de Load Balancer)

A AWS oferece diferentes tipos de "maestros", cada um especialista em um tipo de tráfego.

#### 1. <img src="https://api.iconify.design/mdi/web.svg?color=currentColor" width="20" /> Application Load Balancer (ALB)
* **Especialidade:** Tráfego **HTTP e HTTPS**. Atua na **Camada 7 (Aplicação)**.
* **Analogia:** O **"Maestro Gourmet"**. Ele é inteligente e entende o *conteúdo* do pedido.
* **Superpoder:** **Roteamento Avançado.** Ele pode olhar para a URL e decidir para onde enviar o tráfego. Por exemplo:
    * Se o pedido for para `/imagens/*`, ele envia para o grupo de servidores de imagem.
    * Se for para `/api/pagamentos/*`, ele envia para os servidores de pagamento.
* **Quando Usar?** É a escolha padrão para qualquer aplicação web moderna, microsserviços e contêineres.

#### 2. <img src="https://api.iconify.design/mdi/network-outline.svg?color=currentColor" width="20" /> Network Load Balancer (NLB)
* **Especialidade:** Tráfego **TCP e UDP**. Atua na **Camada 4 (Transporte)**.
* **Analogia:** O **"Maestro de Entregas Expressas"**. Ele não olha o conteúdo do pacote; ele só se importa com o endereço de destino (IP e porta) e em entregar o mais rápido possível.
* **Superpoder:** **Performance Extrema e IP Estático.** Ele é projetado para lidar com milhões de requisições por segundo com latência ultrabaixa. Ele também pode ter um endereço IP estático, o que é essencial para alguns casos de uso.
* **Quando Usar?** Para aplicações que precisam de altíssima performance e baixa latência, como games online, streaming de vídeo e cargas de trabalho TCP/UDP de alto volume.

#### 3. <img src="https://api.iconify.design/mdi/gate.svg?color=currentColor" width="20" /> Gateway Load Balancer (GWLB)
* **Especialidade:** Tráfego de **inspeção de segurança**. Atua na **Camada 3 (Rede)**.
* **Analogia:** O **"Maestro da Alfândega e Segurança"**.
* **Superpoder:** Permite que você insira uma "frota de aparelhos de segurança virtuais" (como firewalls de terceiros da Fortinet ou Palo Alto) de forma transparente no caminho do seu tráfego de rede para inspeção.
* **Quando Usar?** Um caso de uso mais avançado, para empresas com requisitos de segurança e conformidade rigorosos que precisam inspecionar todo o tráfego de rede com ferramentas de terceiros.

> **`!!! warning "Nota Histórica"`**
> Você pode ver menções ao **Classic Load Balancer**. Ele foi a primeira geração e hoje é considerado legado. Para qualquer nova aplicação, você deve sempre escolher entre o Application Load Balancer e o Network Load Balancer.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO

A diferença entre os tipos de ELB é um tópico **muito comum** na prova Cloud Practitioner.

| Tipo | Camada OSI | Protocolos | Caso de Uso Principal |
| :--- | :---: | :--- | :--- |
| **Application (ALB)**| **7 (Aplicação)** | **HTTP, HTTPS** | Aplicações Web, Microsserviços (roteamento por conteúdo) |
| **Network (NLB)** | **4 (Transporte)**| **TCP, UDP, TLS** | Altíssima Performance, Games, IP Estático |
| **Gateway (GWLB)** | **3 (Rede)** | IP | Inserir firewalls de terceiros para inspeção de tráfego |

> **Lembre-se:** O propósito geral do **Elastic Load Balancing** é fornecer **alta disponibilidade** e **escalabilidade** para suas aplicações, distribuindo o tráfego entre múltiplos destinos saudáveis.

---

### <img src="https://api.iconify.design/logos/aws-elb.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Maestro Inteligente: Guia dos Recursos do Elastic Load Balancing

Já sabemos que o ELB distribui o tráfego. Mas como ele faz isso de forma inteligente e segura? E quais outros "superpoderes" ele oferece que vão muito além de simplesmente encaminhar requisições?

Este guia é um olhar "sob o capô" do ELB, mostrando as ferramentas que o tornam o pilar de qualquer arquitetura de alta disponibilidade na AWS.

**Analogia:** Pense no ELB como o **"Maestro de Trânsito Inteligente"** na entrada de uma **praça de alimentação movimentada**.

---

### <img src="https://api.iconify.design/mdi/toolbox-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Cinto de Utilidades do Maestro (Recursos Chave do ELB)

O ELB não é apenas um "sinaleiro". É um serviço gerenciado com um conjunto de recursos poderosos.

#### <img src="https://api.iconify.design/mdi/heart-pulse.svg?color=currentColor" width="20" /> Verificações de Integridade (Health Checks)
* **A Dor que Resolve:** "O que acontece se uma das minhas instâncias EC2 travar ou o serviço da minha aplicação parar de responder? Eu não quero que meus clientes sejam enviados para um servidor quebrado."
* **Como Funciona:** O ELB atua como um "enfermeiro", verificando constantemente a saúde de cada um dos seus servidores de destino (`targets`). Ele envia um "ping" ou uma requisição HTTP para cada um em intervalos regulares.
* **Analogia:** Antes de enviar um cliente, o Maestro **"liga para o interfone do restaurante"** e pergunta: "Vocês estão abertos e prontos para receber pedidos?". Se o restaurante não atender, o Maestro o marca como "fechado" e para de enviar clientes para lá.
* **O Resultado:** Uma arquitetura que se **auto-corrige**. O ELB automaticamente para de usar alvos doentes e volta a usá-los assim que eles se recuperam.

#### <img src="https://api.iconify.design/mdi/lock-outline.svg?color=currentColor" width="20" /> Recursos de Segurança
* **A Dor que Resolve:** "Como eu protejo minha frota de servidores e controlo o acesso ao ponto de entrada da minha aplicação?"
* **Como Funciona:**
    1.  Você pode (e deve) anexar **Security Groups** diretamente ao seu ELB, criando uma primeira camada de firewall.
    2.  Você pode criar um balanceador de carga **interno**, que não é acessível pela internet, ideal para distribuir tráfego entre as camadas internas da sua aplicação.

#### <img src="https://api.iconify.design/mdi/certificate-outline.svg?color=currentColor" width="20" /> Terminação TLS (TLS Termination)
* **A Dor que Resolve:** Gerenciar certificados SSL/TLS em dezenas de servidores web é complexo, caro e consome muita CPU (o processo de criptografia e descriptografia é pesado).
* **Como Funciona:** O ELB assume essa carga. A conexão criptografada do usuário (HTTPS) "termina" no balanceador de carga. O ELB descriptografa a requisição e a encaminha para as instâncias EC2 na rede interna (e segura) da sua VPC, geralmente via HTTP.
* **Analogia:** O Maestro oferece um **"Serviço de Valet e Segurança de Cartão de Crédito"**. O cliente entrega seu cartão (conexão HTTPS) ao Maestro, que tem uma máquina super segura (o certificado TLS). Ele processa o pagamento e entrega um voucher já pago (conexão HTTP) ao restaurante. Isso tira o fardo da segurança de cada restaurante individual.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. Escolhendo seu Maestro (Recap dos Tipos de ELB)

Lembre-se, a AWS oferece diferentes "maestros" para diferentes tipos de "orquestra".

| Tipo | Camada OSI | Protocolos | Caso de Uso Principal (Analogia) |
| :--- | :---: | :--- | :--- |
| **Application (ALB)**| **7 (Aplicação)** | **HTTP, HTTPS** | Aplicações Web, Microsserviços. (O **"Maestro Gourmet"** que entende o pedido.) |
| **Network (NLB)** | **4 (Transporte)**| **TCP, UDP, TLS** | Altíssima Performance, Games, IP Estático. (O **"Maestro de Entregas Expressas"**.) |
| **Gateway (GWLB)** | **3 (Rede)** | IP | Inserir firewalls de terceiros para inspeção de tráfego. (O **"Maestro da Alfândega"**.) |
| **Classic** | 4 e 7 | TCP, HTTP, HTTPS | **Legado**. Para aplicações antigas na rede EC2-Classic. (O **"Maestro Aposentado"**.) |

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Saiba a **finalidade** do ELB: distribuir tráfego para **alta disponibilidade** e **escalabilidade**.
> 2.  Conheça os **tipos modernos** e seus casos de uso: **ALB** para **HTTP/HTTPS**, **NLB** para **TCP/Performance Extrema**.
> 3.  Entenda o que são **Health Checks** e por que são vitais para a resiliência. O ELB só envia tráfego para destinos **saudáveis**.

O Elastic Load Balancing é muito mais do que um simples distribuidor de tráfego; é um componente gerenciado, seguro e inteligente que forma o ponto de entrada para qualquer aplicação moderna e resiliente na AWS.

---

### <img src="https://api.iconify.design/logos/aws-elb.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Maestro em Ação: Guia de Casos de Uso e Tipos de ELB

Já sabemos que o ELB é o "maestro do tráfego". Mas por que exatamente a presença dele é tão transformadora para uma arquitetura? E como escolher o "maestro" certo para a sua "orquestra"? Este guia responde a essas perguntas.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. Os 4 Superpoderes de Todo Balanceador de Carga

Todo ELB, independentemente do tipo, oferece quatro benefícios de negócio fundamentais:

1.  **<img src="https://api.iconify.design/mdi/security.svg?color=currentColor" width="18" /> Segurança:**
    * **O que faz?** Atua como um **único ponto de entrada** para sua aplicação.
    * **Por quê?** Você não expõe seus servidores diretamente à internet. O ELB fica na frente, como um "porteiro", recebendo todo o tráfego. Você pode aplicar regras de segurança (Security Groups) diretamente nele.

2.  **<img src="https://api.iconify.design/mdi/vector-link-off.svg?color=currentColor" width="18" /> Desacoplamento:**
    * **O que faz?** Desacopla o cliente da sua frota de servidores.
    * **Por quê?** O cliente só conhece o endereço do ELB. Você pode adicionar, remover ou trocar os servidores por trás dele sem que o cliente nunca perceba.

3.  **<img src="https://api.iconify.design/mdi/heart-pulse.svg?color=currentColor" um="18" /> Tolerância a Falhas:**
    * **O que faz?** Realiza **verificações de integridade (Health Checks)** contínuas.
    * **Por quê?** Se um servidor falhar, o ELB para de enviar tráfego para ele **automaticamente**, garantindo que seus usuários não sejam direcionados para um "beco sem saída".

4.  **<img src="https://api.iconify.design/mdi/arrow-expand-all.svg?color=currentColor" width="18" /> Elasticidade e Escalabilidade:**
    * **O que faz?** Trabalha em conjunto com o **AWS Auto Scaling**.
    * **Por quê?** Quando o Auto Scaling adiciona novos servidores para lidar com um pico de tráfego, o ELB os detecta automaticamente e começa a enviar tráfego para eles, permitindo que sua aplicação escale de forma transparente.

---

### <img src="https://api.iconify.design/mdi/web.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Cérebro da Web: O Application Load Balancer (ALB)

O ALB é o balanceador de carga de **Camada 7 (Aplicação)**, o que significa que ele entende o tráfego **HTTP e HTTPS**.

* **Analogia:** O **"Maestro Gourmet Inteligente"**. Ele não apenas direciona os clientes, ele **lê o pedido** de cada um.

#### A Anatomia de um ALB: Listeners, Regras e Grupos de Destino
Esta é a lógica interna que torna o ALB tão poderoso para microsserviços.

<p align="center">
<img src="https://i.imgur.com/g0t6C2S.png" alt="Arquitetura do ALB" />
</p>

1.  **Listener (O Ouvido):**
    * É o processo que "escuta" por conexões em uma porta específica (ex: porta 80 para HTTP).
2.  **Regra (Rule):**
    * Para cada Listener, você define regras. A regra analisa a requisição e, com base em uma **condição** (ex: o caminho da URL), executa uma **ação**.
    * **Analogia:** "SE o pedido (`URL`) for para `/api/pagamentos`, ENTÃO encaminhe para o grupo de destino 'Servidores-de-Pagamento'."
3.  **Grupo de Destino (Target Group):**
    * É um grupo de "restaurantes" (seus servidores EC2, contêineres ou Lambdas) que executam a mesma tarefa. Cada grupo tem suas próprias verificações de integridade.

> **A Dor que o ALB Resolve:** Com um único ALB, você pode rotear o tráfego para dezenas de microsserviços diferentes com base na URL, eliminando a necessidade de um load balancer para cada serviço.

---

### <img src="https://api.iconify.design/mdi/network-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Demônio da Velocidade: O Network Load Balancer (NLB)

O NLB é o balanceador de carga de **Camada 4 (Transporte)**, focado em tráfego **TCP/UDP**.

* **Analogia:** O **"Maestro de Entregas Expressas"**. Ele não lê o pedido; ele só olha o endereço de destino (IP e porta) e o encaminha na velocidade máxima.
* **A Dor que Resolve:** Aplicações que precisam de **performance extrema** (milhões de requisições por segundo com latência ultrabaixa) ou de um **endereço IP estático** por Zona de Disponibilidade.
* **Casos de Uso:** Games online, streaming de vídeo, sistemas de negociação financeira (bolsa de valores).

---

### <img src="https://api.iconify.design/mdi/comment-question-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Debriefing (Respondendo às Perguntas-Chave)

* **1. Qual balanceador de carga seria apropriado para um site?**
    * **Resposta:** O **Application Load Balancer (ALB)**, porque sites usam os protocolos HTTP e HTTPS (Camada 7), e o ALB é o especialista nesse tipo de tráfego, oferecendo roteamento avançado.

* **2. Por que o Network Load Balancer é uma boa escolha para tráfego repentino e volátil?**
    * **Resposta:** Porque ele é projetado para **performance extrema**, capaz de lidar com milhões de requisições por segundo e manter latências ultrabaixas, o que é ideal para picos de tráfego.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** A prova **adora** a diferença entre os tipos de ELB.
> * Precisa rotear com base na **URL**? -> **Application Load Balancer (ALB)**.
> * Precisa de **performance extrema** para TCP ou um **IP estático**? -> **Network Load Balancer (NLB)**.
> * Precisa de uma solução para a rede legada **EC2-Classic**? -> **Classic Load Balancer**.

---

### <img src="https://api.iconify.design/mdi/brain.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Cérebro do Maestro: Guia de Listeners, Regras e Target Groups no ALB

Já sabemos que o Application Load Balancer (ALB) é o "maestro gourmet" que entende o tráfego HTTP/S. Mas como ele decide para qual servidor enviar cada requisição? A resposta está em sua arquitetura interna, composta por três blocos de construção: Listeners, Regras e Target Groups.

Dominar essa estrutura é a chave para construir aplicações web modernas e baseadas em microsserviços na AWS.

---

### <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Anatomia do Roteamento Inteligente

Quando uma requisição de um cliente chega ao seu ALB, ela passa por um fluxo de decisão lógico de 3 etapas.

#### <img src="https://api.iconify.design/mdi/ear-hearing.svg?color=currentColor" width="20" /> Etapa 1: O Listener (A Porta de Entrada)
* **O que é?** Um "ouvinte" é um processo que verifica por conexões em uma **porta** e **protocolo** específicos.
* **Analogia:** O **"Ouvido Atento"** do Maestro. Ele tem um ouvido para o "canal 80" (HTTP) e outro para o "canal 443" (HTTPS).
* **Na Prática:** Todo balanceador de carga precisa de pelo menos um listener para aceitar tráfego. Para um site seguro, você terá um listener na porta 443 para o tráfego HTTPS.

#### <img src="https://api.iconify.design/mdi/book-open-page-variant-outline.svg?color=currentColor" width="20" /> Etapa 2: A Regra (O Livro de Decisões)
* **O que é?** Para cada listener, você define um conjunto de regras com prioridades. Cada regra contém uma **Condição** e uma **Ação**.
* **A Lógica:** **SE** a condição for verdadeira, **ENTÃO** execute a ação.
* **Analogia:** O **"Livro de Regras"** que o Maestro consulta. "SE o pedido do cliente for para o endereço `/pizzas`, ENTÃO encaminhe para o grupo 'Pizzarias'."

> **`!!! tip "Dica de Especialista"`**
> A condição mais comum é o **Caminho da URL (`Path`)**. No entanto, arquitetos experientes também usam a condição de **Nome do Host** para rotear tráfego para diferentes sites (ex: `api.meusite.com` vs. `blog.meusite.com`) usando o mesmo ALB, o que é uma enorme otimização de custos.

#### <img src="https://api.iconify.design/mdi/account-group-outline.svg?color=currentColor" width="20" /> Etapa 3: O Grupo de Destino (O Time de Especialistas)
* **O que é?** Um **Target Group** é um grupo de "destinos" (suas instâncias EC2, contêineres, funções Lambda) que recebem o tráfego.
* **Analogia:** Um **"time de restaurantes especializados"** (ex: o time das `Pizzarias`, o time das `Sorveterias`).
* **Como Funciona:** Cada regra de um listener encaminha o tráfego para um Target Group específico. É no Target Group que você configura as **Verificações de Integridade (Health Checks)**, garantindo que o Maestro só envie clientes para os "restaurantes" que estão abertos e funcionando.

---

### <img src="https://api.iconify.design/mdi/store-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Cenário em Ação: Roteamento de um E-commerce

Vamos usar o excelente exemplo do seu material para ver a sinergia em ação.

**A Missão:** Um único ALB precisa gerenciar o tráfego para três microsserviços diferentes de um site de e-commerce (`www.exemplo.com`).

<p align="center">
  <img src="https://i.imgur.com/vHq1kS6.png" alt="Exemplo de Roteamento do ALB" />
</p>

**A Configuração do Maestro:**

1.  **O Listener:** Criamos um Listener principal na porta `443` (HTTPS).
2.  **As Regras:** Dentro deste listener, criamos 3 regras com prioridades diferentes:
    * **Regra 1 (Prioridade 10):** SE o caminho da URL for `/imagens/*`, ENTÃO encaminhe para o `Target-Group-Imagens`.
    * **Regra 2 (Prioridade 20):** SE o caminho da URL for `/pedidos/*`, ENTÃO encaminhe para o `Target-Group-Pedidos`.
    * **Regra Padrão (Default):** PARA TODAS as outras requisições (ex: `/registro`), encaminhe para o `Target-Group-Principal`.
3.  **Os Grupos de Destino:** Cada Target Group (`Imagens`, `Pedidos`, `Principal`) tem seu próprio conjunto de instâncias EC2 e suas próprias configurações de Health Check, permitindo que cada microsserviço escale de forma independente.

**O Resultado:** Uma arquitetura de microsserviços desacoplada, escalável e gerenciada por um único ponto de entrada inteligente, o que simplifica a gestão e reduz custos.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO

A hierarquia do ALB é um conceito importante para a prova. Lembre-se:

1.  O **Application Load Balancer (ALB)** opera na **Camada 7** e é ideal para tráfego **HTTP/HTTPS**.
2.  Sua principal característica é o **roteamento baseado em conteúdo** (por caminho de URL ou nome de host).
3.  A hierarquia é: um **Listener** tem **Regras**, e cada **Regra** encaminha o tráfego para um **Grupo de Destino (Target Group)**.

---

### <img src="https://api.iconify.design/logos/aws-elb.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Maestro da CLI - Construindo um Application Load Balancer

### O Cenário (A "User Story")

> **Como** um engenheiro DevOps, **EU QUERO** provisionar e configurar um Application Load Balancer usando a AWS CLI, **PARA QUE** eu possa automatizar a criação de arquiteturas web resilientes e escaláveis e integrar este processo em meus pipelines de CI/CD.

### A Dor que o Lab Resolve

Clicar no console para criar um ELB é ótimo para aprender, mas não é um processo repetível nem escalável. Se você precisa criar ambientes de teste e produção idênticos, ou se quer que seu pipeline de CI/CD crie a infraestrutura dinamicamente, você precisa de automação. Este laboratório ensina os comandos fundamentais para construir o "maestro do tráfego" via código.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Criar um Application Load Balancer (ALB) via AWS CLI.
* [ ] Criar um Grupo de Destino (Target Group).
* [ ] Registrar instâncias EC2 como destinos.
* [ ] Criar um Ouvinte (Listener) para receber o tráfego.
* [ ] Verificar a saúde dos seus destinos.

### Pré-requisitos
* AWS CLI configurada com permissões de administrador.
* **Uma VPC com pelo menos duas sub-redes públicas** em Zonas de Disponibilidade diferentes.
* **Duas instâncias EC2** rodando um servidor web na porta 80.
    > **`!!! tip "Dica Rápida"`**
    > Ao lançar suas instâncias EC2, use este script no **User Data** para instalar um servidor web simples que exibe o ID da própria instância:
    > ```bash
    > #!/bin/bash
    > yum update -y
    > yum install -y httpd
    > systemctl start httpd
    > systemctl enable httpd
    > INSTANCE_ID=$(curl -s [http://169.254.169.254/latest/meta-data/instance-id](http://169.254.169.254/latest/meta-data/instance-id))
    > echo "<h1>Olá do Servidor: ${INSTANCE_ID}</h1>" > /var/www/html/index.html
    > ```

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: Montando o Maestro via CLI

#### Passo 1: Criar o Balanceador de Carga
* **Analogia:** "Contratar o Maestro e posicioná-lo na entrada da praça de alimentação (nas suas sub-redes públicas)."
```bash
aws elbv2 create-load-balancer \
    --name meu-alb-incrivel \
    --type application \
    --subnets SUBNET_ID_1 SUBNET_ID_2 \
    --security-groups SECURITY_GROUP_ID
```
> **`!!! note "Ação Necessária"`**
> Substitua os valores de `SUBNET_ID` e `SECURITY_GROUP_ID` pelos IDs reais do seu ambiente. Anote o `"LoadBalancerArn"` da saída JSON. Você precisará dele.

#### Passo 2: Criar o Grupo de Destino
* **Analogia:** "Criar a 'prancheta' do Maestro para o 'Time de Restaurantes'."
```bash
aws elbv2 create-target-group \
    --name meu-grupo-de-alvos \
    --protocol HTTP --port 80 \
    --vpc-id SUA_VPC_ID
```
> Anote o `"TargetGroupArn"` da saída JSON. Você precisará dele.

#### Passo 3: Registrar as Instâncias no Grupo
* **Analogia:** "Anotar na prancheta o endereço dos seus dois restaurantes (instâncias)."
```bash
aws elbv2 register-targets \
    --target-group-arn SEU_TARGET_GROUP_ARN \
    --targets Id=SEU_INSTANCE_ID_1 Id=SEU_INSTANCE_ID_2
```
> Este comando não tem saída se for bem-sucedido.

#### Passo 4: Criar o Ouvinte (Listener)
* **Analogia:** "Instalar o 'ouvido' do Maestro na porta 80 e dar a ele a regra padrão: 'Qualquer pedido que chegar, encaminhe para o time na prancheta'."
```bash
aws elbv2 create-listener \
    --load-balancer-arn SEU_LOAD_BALANCER_ARN \
    --protocol HTTP --port 80 \
    --default-actions Type=forward,TargetGroupArn=SEU_TARGET_GROUP_ARN
```
> Este comando cria o Listener e a regra padrão que conecta seu ALB ao seu grupo de instâncias.

#### Passo 5: Verificar a Saúde dos Destinos
* **Analogia:** "Pedir ao Maestro para ligar para o interfone de cada restaurante e reportar se eles estão abertos e saudáveis."
```bash
aws elbv2 describe-target-health --target-group-arn SEU_TARGET_GROUP_ARN
```
* **Verificação:** Espere alguns instantes para que as verificações de saúde passem. A saída JSON deve mostrar `"State": "healthy"` para cada uma de suas instâncias.

---

### <img src="https://api.iconify.design/mdi/web-check.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Verificação Final

1.  Vá para o console do **EC2** > **Load Balancers**.
2.  Selecione seu `meu-alb-incrivel`.
3.  Na aba **Description**, copie o valor do **DNS name**.
4.  Cole este nome de DNS em uma nova aba do seu navegador.
5.  **Atualize a página várias vezes.** Você deverá ver o ID da instância mudando na mensagem "Olá do Servidor...", provando que o balanceador está distribuindo o tráfego entre suas instâncias!

---

### <img src="https://api.iconify.design/mdi/comment-question-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Debriefing (Respondendo às Perguntas-Chave)

* **Pergunta:** Como usar um balanceador de carga para melhorar o desempenho de um site com muitos subdiretórios (ex: `/login`, `/produtos`)?
    * **Resposta:** Usando um **Application Load Balancer (ALB)**. Você pode criar diferentes **Target Groups** para cada microsserviço (um para login, outro para produtos) e criar **Regras** no Listener do ALB que direcionam o tráfego para o grupo certo com base no caminho da URL.

* **Pergunta:** As verificações de integridade se aplicam ao balanceador de carga ou aos servidores de destino?
    * **Resposta:** Elas se aplicam aos **servidores de destino (targets)**. O balanceador de carga as executa para garantir que ele só envie tráfego para instâncias que estão saudáveis e prontas para responder.