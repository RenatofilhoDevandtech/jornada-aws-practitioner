# <img src="https://api.iconify.design/logos/aws-vpc.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Fortaleza Digital: Guia da Arquitetura de Redes com Amazon VPC

Antes de construir qualquer "casa" (instância EC2) ou "armazém" (banco de dados), um bom arquiteto primeiro cerca o terreno e planeja as ruas. Na AWS, essa fundação é a **Amazon VPC (Virtual Private Cloud)**.

É a sua fatia privada e logicamente isolada da Nuvem AWS, onde você tem controle total sobre seu ambiente de rede, como se fosse seu próprio data center virtual.

**Analogia:** Pense na AWS como o **"mundo inteiro"**. Uma VPC é o seu **"terreno murado e particular"** dentro desse mundo.

---

### <img src="https://api.iconify.design/mdi/floor-plan.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Planta Baixa da Fortaleza (Os Componentes da VPC)

Dentro do seu "terreno murado", você precisa construir a infraestrutura.

* **<img src="https://api.iconify.design/mdi/ip-network-outline.svg?color=currentColor" width="18" /> Bloco CIDR:**
    * **O que é?** A faixa de endereços IP privados para sua VPC (ex: `10.0.0.0/16`).
    * **Analogia:** O **"endereço e o tamanho do seu terreno"**.
* **<img src="https://api.iconify.design/mdi/road-variant.svg?color=currentColor" width="18" /> Sub-redes (Subnets):**
    * **O que são?** Segmentos da sua faixa de IP da VPC, onde você de fato lança seus recursos. Cada sub-rede vive em uma única Zona de Disponibilidade.
    * **Analogia:** As **"ruas"** dentro do seu condomínio.
        * **Sub-rede Pública:** A "rua da portaria", com acesso direto à internet.
        * **Sub-rede Privada:** As "ruas internas", sem acesso direto da internet.
* **<img src="https://api.iconify.design/mdi/sign-direction.svg?color=currentColor" width="18" /> Tabelas de Rotas (Route Tables):**
    * **O que são?** Um conjunto de regras que determina para onde o tráfego de rede é direcionado.
    * **Analogia:** O **"mapa de trânsito e as placas de sinalização"** do condomínio.

---

### <img src="https://api.iconify.design/mdi/tunnel-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. As Pontes e Túneis (Conectando sua Fortaleza)

Como sua fortaleza se conecta a outros locais?

* **<img src="https://api.iconify.design/mdi/gate-arrow-right.svg?color=currentColor" width="18" /> Internet Gateway:**
    * **O que é?** Um componente que você anexa à sua VPC para permitir a comunicação com a internet.
    * **Analogia:** A **"portaria principal"** do condomínio, a única saída e entrada para o mundo exterior.
* **<img src="https://api.iconify.design/mdi/vpn.svg?color=currentColor" width="18" /> Virtual Private Gateway (VGW):**
    * **O que é?** O ponto de ancoragem do lado da AWS para uma conexão VPN.
    * **Analogia:** A **"doca de submarinos"** da sua ilha.
* **<img src="https://api.iconify.design/mdi/office-building-marker-outline.svg?color=currentColor" width="18" /> Customer Gateway:**
    * **O que é?** O dispositivo físico ou software do seu lado da conexão VPN.
    * **Analogia:** O **"portão da garagem do submarino"** no seu "continente" (seu data center on-premises).

---

### <img src="https://api.iconify.design/mdi/wall.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. As Muralhas e Fechaduras (A Defesa em Camadas)

A segurança em uma VPC é feita em camadas. A principal ferramenta para isso é o Security Group.

* **<img src="https://api.iconify.design/logos/aws-security-group.svg?color=currentColor" width="18" /> Security Group (Grupo de Segurança):**
    * **O que é?** Um firewall **stateful** (com estado) que atua no nível da **instância**.
    * **Analogia:** A **"fechadura eletrônica na porta de cada casa"**. Você define regras de `Allow` (Permitir) para o tráfego de entrada. Como é *stateful*, se o tráfego de entrada é permitido, a resposta de saída é automaticamente liberada, sem precisar de uma regra extra.

> **`!!! tip "Insight de Especialista"`**
> Além dos Security Groups, existe outra camada de segurança: as **Network ACLs (NACLs)**. Elas atuam como os **"guardas nos portões de cada rua (sub-rede)"**. São *stateless* e permitem regras de `Allow` e `Deny`, sendo sua primeira linha de defesa.

---

### <img src="https://api.iconify.design/mdi/notebook-edit-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 4. Lembrete do Projeto: Base de Conhecimento
> **`!!! tip "Registre suas Descobertas"`**
> Este módulo é rico em oportunidades para popular sua **Base de Conhecimento**.
> * **Categoria `Redes`:** Documente a diferença entre sub-rede pública e privada, ou o passo a passo para criar uma VPC.
> * **Categoria `Segurança e Conformidade`:** Documente a diferença crucial entre Security Groups e Network ACLs.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  A **VPC** é a sua **rede privada** na AWS.
> 2.  Entenda a diferença: **Sub-rede Pública** (tem uma rota para um Internet Gateway) e **Sub-rede Privada** (não tem).
> 3.  Domine a diferença: **Security Group** (nível da instância, *stateful*, só `Allow`) e **Network ACL** (nível da sub-rede, *stateless*, `Allow` e `Deny`).

---

### <img src="https://api.iconify.design/logos/aws-vpc.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Loteamento da Nuvem: Guia de VPC e Endereçamento CIDR

Já sabemos que uma VPC é a sua "fortaleza" ou "ilha particular" na AWS. Mas antes de construir as ruas e as casas, todo bom urbanista precisa fazer uma coisa: **planejar o loteamento**.

No mundo das redes, esse planejamento é feito através do **endereçamento IP**, e a linguagem que usamos para isso é a **notação CIDR**.

---

### <img src="https://api.iconify.design/mdi/ip-network-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. Decifrando o CIDR (A Ferramenta do Urbanista)

**A Dor que o CIDR Resolve:** O sistema antigo de classes de IP (Classe A, B, C) era muito rígido. O **CIDR (Classless Inter-Domain Routing)** foi criado para nos dar flexibilidade total para criar redes de qualquer tamanho.

A notação é `x.x.x.x/n`.

* **`x.x.x.x`**: O endereço de IP inicial da sua rede.
* **`/n`**: O **Tamanho do Prefixo**. Esta é a parte mais importante.
    * **Analogia:** Pense na **barra (`/`)** como um **"cadeado"** no seu mapa de loteamento. O número `n` diz quantos "dígitos" do endereço estão travados. O resto está "livre" para criar os lotes.

#### A Regra de Ouro da Barra (`/`)
É um conceito inverso, mas muito simples de lembrar:

> **Quanto MENOR o número depois da barra, MAIOR a rede (mais IPs).**
> **Quanto MAIOR o número depois da barra, MENOR a rede (menos IPs).**

#### O "Cheat Sheet" do Arquiteto:
* **`/16`**: Um **terreno gigante** para uma cidade inteira. (ex: `10.0.0.0/16` tem 65.536 endereços).
* **`/24`**: Um **terreno para uma única rua**. (ex: `10.0.1.0/24` tem 256 endereços).
* **`/28`**: Um **quarteirão pequeno**. (ex: `10.0.1.0/28` tem 16 endereços).
* **`/32`**: Uma **casa individual**. (ex: `10.0.1.5/32` é um único endereço IP).
* **`0.0.0.0/0`**: O **planeta inteiro**. Representa **toda a internet**.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. As Regras de Ouro do Planejamento de VPC

Ao criar sua "ilha particular", siga estas duas regras para evitar dores de cabeça no futuro.

#### Regra 1: Use os Endereços de Condomínio Fechado (RFC 1918)
* **A Dor que Resolve:** Conflitos de IP com a internet pública.
* **A Regra:** Sempre use as faixas de IP **privadas** para suas VPCs. Elas foram reservadas para uso interno e nunca entrarão em conflito com sites da internet.
    * **Analogia:** São os "CEPs internos" que todos os condomínios do mundo concordaram em usar.
* **As Faixas:**
    * `10.0.0.0` a `10.255.255.255` (um bloco /8)
    * `172.16.0.0` a `172.31.255.255` (um bloco /12)
    * `192.168.0.0` a `192.168.255.255` (um bloco /16)

#### Regra 2: Não Sobreponha seus Loteamentos
* **A Dor que Resolve:** A incapacidade de conectar suas redes no futuro.
* **A Regra:** **Nunca** crie duas VPCs com o mesmo bloco CIDR (ou com blocos que se sobreponham) se você acha que um dia poderá precisar conectá-las.
* **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> Insight de Arquiteto:** Se você tem uma VPC de `Desenvolvimento` e uma de `Produção`, ambas com o CIDR `10.0.0.0/16`, o sistema de roteamento não saberá para qual "cidade" enviar o tráfego se você tentar conectá-las com **VPC Peering** ou **Transit Gateway**. Planeje seu espaço de IPs antes de começar a construir.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO
Para a prova Cloud Practitioner:
1.  Uma **VPC** requer um **bloco CIDR IPv4** na sua criação.
2.  Entenda a regra da barra: **`/16` é uma rede grande**, **`/24` é uma rede menor**.
3.  Saiba o que **`0.0.0.0/0`** significa: **todos os endereços IP**. É usado em Tabelas de Rotas e Security Groups para se referir à internet.
4.  Lembre-se da melhor prática de usar os endereços **privados (RFC 1918)**.

---

### <img src="https://api.iconify.design/logos/aws-vpc.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Planta da Ilha: Guia de Sub-redes, Rotas e IPs Reservados na VPC

Já definimos o "tamanho do nosso terreno" (o bloco CIDR da VPC). Agora, vamos aprender a dividi-lo em "lotes" (as **Sub-redes**) e entender as "regras de zoneamento" que a AWS aplica para garantir que tudo funcione perfeitamente.

---

### <img src="https://api.iconify.design/mdi/island.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. As Características da Ilha (A VPC)

Toda VPC que você cria já vem com algumas características fundamentais:
* **<img src="https://api.iconify.design/mdi/earth.svg?color=currentColor" width="18" /> Abrangência Regional:** Uma VPC é um recurso **Regional**. Ela se estende por todas as Zonas de Disponibilidade (AZs) daquela Região.
    * **Analogia:** Sua "ilha" pode ter múltiplas "costas" (as AZs), mas ainda é uma única ilha.
* **<img src="https://api.iconify.design/mdi/router-network.svg?color=currentColor" width="18" /> Roteador Implícito:** Toda VPC vem com um "roteador" virtual, implícito e altamente disponível. Você não o vê, mas ele está lá, conectando todas as suas "ruas" (sub-redes).
* **<img src="https://api.iconify.design/mdi/sign-direction.svg?color=currentColor" width="18" /> Tabela de Rotas Padrão:** O roteador vem com um "mapa de trânsito" padrão. A regra principal neste mapa é: **permitir que todas as sub-redes dentro da VPC conversem entre si**.

---

### <img src="https://api.iconify.design/mdi/road-variant.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Loteamento (Planejando as Sub-redes)

Sub-redes são os "lotes de terreno" onde você de fato constrói suas "casas" (lança seus recursos, como instâncias EC2).

**A Dor que as Sub-redes Resolvem:** A necessidade de segmentar sua rede por razões de organização e, principalmente, de segurança. É com as sub-redes que você cria as camadas "pública" e "privada" da sua arquitetura.

#### As 3 Regras de Ouro do Loteamento:
1.  **Uma Sub-rede por AZ:** Cada "lote" pertence a uma única "costa" da ilha (uma única Zona de Disponibilidade).
2.  **Subconjunto do CIDR da VPC:** O endereço da sua "rua" (o CIDR da sub-rede) deve estar contido no endereço da sua "cidade" (o CIDR da VPC).
3.  **Sem Sobreposição:** Duas "ruas" dentro da mesma "cidade" não podem ter o mesmo nome/endereço. Os blocos CIDR das sub-redes não podem se sobrepor.

---

### <img src="https://api.iconify.design/mdi/numeric-5-box-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. As "Taxas da Prefeitura" (Os 5 IPs Reservados)

**A Dor que Resolve (A Dúvida do Iniciante):** "Eu criei uma sub-rede com um CIDR `/24`, que deveria ter 256 endereços IP. Mas o console da AWS me diz que eu só tenho 251 disponíveis. Para onde foram os outros 5?"

**A Resposta:** A AWS reserva os primeiros quatro e o último endereço IP de cada sub-rede para fins de rede.

* **Analogia:** Quando você loteia uma rua, a "prefeitura" (AWS) automaticamente reserva 5 lotes para a **infraestrutura** daquela rua. Eles não podem ser usados para construir casas.

| Endereço na Sub-rede (`10.0.0.0/24`) | Finalidade | Analogia (O Lote Reservado) |
| :--- | :--- | :--- |
| **`10.0.0.0`** | Endereço de Rede | O "endereço oficial da rua". |
| **`10.0.0.1`** | Roteador da VPC | A "cabine de controle de trânsito" da rua. |
| **`10.0.0.2`** | Servidor DNS | A "central telefônica" da rua. |
| **`10.0.0.3`** | Reservado para Uso Futuro | Um "lote para expansão futura" da prefeitura. |
| **`10.0.0.255`**| Endereço de Broadcast | O "endereço do megafone", não usado na VPC. |

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> INSIGHT DE ESPECIALISTA:** Esta é uma regra universal. Não importa o tamanho da sua sub-rede, você **sempre** perderá 5 endereços IP para essas reservas da AWS. Lembre-se disso ao planejar o tamanho das suas sub-redes.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Uma **VPC** é um recurso **Regional**.
> 2.  Uma **Sub-rede** é um recurso de **Zona de Disponibilidade** (vive em uma única AZ).
> 3.  Lembre-se da regra dos **5 IPs reservados**: ao calcular os IPs disponíveis em uma sub-rede, você sempre perde 5 endereços para a AWS.
> 4.  Por padrão, todas as sub-redes em uma VPC **podem se comunicar entre si** através do roteador implícito.

---
### <img src="https://api.iconify.design/mdi/road-variant.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> As Estradas e Conexões: Guia de Tabelas de Rotas e Interfaces de Rede

Já temos nosso "terreno" (a VPC) e nossos "lotes" (as Sub-redes). Agora, vamos construir as **estradas** que conectam tudo e instalar as **conexões** em cada casa.

---

### <img src="https://api.iconify.design/mdi/sign-direction.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O GPS da Ilha (As Tabelas de Rotas)

**A Dor que Resolve:** Como uma instância em uma sub-rede sabe como chegar à internet ou a outra sub-rede? Ela consulta a Tabela de Rotas.

* **O que é?** Uma Tabela de Rotas é um conjunto de regras, chamadas **rotas**, que determinam para onde o tráfego de rede é direcionado.
* **Analogia:** É o **"GPS Central"** ou o **"mapa de trânsito"** da sua ilha. Cada "rua" (sub-rede) tem um mapa associado a ela.

#### A Anatomia de uma Rota:
Toda rota tem duas partes:
* **`Destino`:** Para onde o tráfego quer ir (um bloco CIDR).
* **`Alvo`:** Por onde o tráfego deve passar para chegar lá (ex: um Internet Gateway).

#### A Regra de Ouro: Pública vs. Privada
> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> INSIGHT DE ARQUITETO:** A definição *real* de uma sub-rede pública ou privada não tem a ver com os IPs das instâncias, mas sim com sua Tabela de Rotas.
> * Uma sub-rede é **Pública** se sua Tabela de Rotas associada tem uma rota para a internet: `Destino: 0.0.0.0/0` -> `Alvo: Internet Gateway`.
> * Uma sub-rede é **Privada** se sua Tabela de Rotas **NÃO** tem uma rota para um Internet Gateway.

Por padrão, toda VPC já vem com uma Tabela de Rotas "Principal" que contém uma única rota: `Destino: [Seu Bloco CIDR da VPC]` -> `Alvo: local`. Isso garante que todas as sub-redes possam conversar entre si dentro da VPC.

---

### <img src="https://api.iconify.design/mdi/network-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Conexão Física (As Interfaces de Rede Elástica - ENIs)

**A Dor que Resolve:** Como uma instância EC2 fisicamente (virtualmente) se conecta à rede da sub-rede?

* **O que é?** Uma **Interface de Rede Elástica (ENI)** é uma placa de rede virtual (NIC) para sua instância EC2.
* **Analogia:** É a **"caixa de entrada de cabos de rede e telefone"** de cada "casa" (instância).

#### Componentes de uma ENI:
* Um endereço **IP Privado** primário.
* Um endereço **MAC** único.
* Um ou mais **Security Groups** associados.
* Opcionalmente, um endereço **IP Público** ou **Elástico**.

> **`!!! note "Primária vs. Secundária"`**
> Toda instância EC2 tem uma **ENI primária** (`eth0`), que é criada com a instância e destruída com ela. Você pode criar e anexar **ENIs secundárias** a uma instância, o que é útil para cenários avançados como a criação de redes de gerenciamento separadas ou o uso de dispositivos de rede virtuais.

---

### <img src="https://api.iconify.design/mdi/ip-network-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. A Conveniência (Atribuição Automática de IP Público)

**A Dor que Resolve:** O passo manual de ter que atribuir um IP público a cada instância que eu lanço em uma sub-rede pública.

* **A Solução:** É uma configuração na **própria sub-rede**. Você pode marcar uma caixa de seleção que diz: "Atribuir IPs públicos automaticamente a todas as novas instâncias nesta sub-rede."
* **O Resultado:** Toda "casa" construída na sua "rua da praia" (sub-rede pública) já vem com uma "linha de telefone pública temporária" instalada por padrão.
* **Lembrete:** Este IP é público, mas **não é Elástico**. Ele será perdido e um novo será atribuído se a instância for parada (`Stop`) e iniciada (`Start`).

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Uma **Tabela de Rotas** controla o fluxo de tráfego de uma **sub-rede**.
> 2.  A rota **`0.0.0.0/0 -> Internet Gateway`** é o que torna uma sub-rede **Pública**.
> 3.  Uma **ENI** é a **placa de rede virtual** de uma instância EC2.
> 4.  Um **Security Group** é associado a uma **ENI** (um detalhe técnico sutil, mas correto).

---

### <img src="https://api.iconify.design/mdi/island.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Ilha Pré-Fabricada: Guia da VPC Padrão e do DNS Privado

A AWS quer que você comece a construir o mais rápido possível. Para eliminar a complexidade inicial de configurar uma rede do zero, ela te dá uma "ilha pré-fabricada" em cada Região: a **VPC Padrão (Default VPC)**.

---

### <img src="https://api.iconify.design/logos/aws-vpc.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Ilha para Iniciantes (A VPC Padrão)

**A Dor que Resolve:** A complexidade de criar e configurar uma rede funcional do zero (VPC, sub-redes, Internet Gateway, tabelas de rotas) apenas para lançar uma única instância EC2.

#### O Kit de Início Rápido
Quando você cria sua conta, a AWS automaticamente provisiona em cada Região uma VPC Padrão com tudo que você precisa para começar:
* **<img src="https://api.iconify.design/mdi/ip-network-outline.svg?color=currentColor" width="18" /> Um Bloco CIDR:** Sempre `172.31.0.0/16`.
* **<img src="https://api.iconify.design/mdi/road-variant.svg?color=currentColor" width="18" /> Sub-redes Públicas:** Uma sub-rede em cada Zona de Disponibilidade da Região, já configurada como pública.
* **<img src="https://api.iconify.design/mdi/gate-arrow-right.svg?color=currentColor" width="18" /> Um Internet Gateway:** Já criado e anexado.
* **<img src="https://api.iconify.design/mdi/sign-direction.svg?color=currentColor" width="18" /> Uma Tabela de Rotas:** Já configurada com uma rota para a internet (`0.0.0.0/0`).
* **<img src="https://api.iconify.design/mdi/ip.svg?color=currentColor" width="18" /> Atribuição de IP Público:** As sub-redes já vêm com a opção **"Atribuir IP público automaticamente"** habilitada.

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> O Veredito do Arquiteto:**
> * **Prós:** Excelente para aprendizado, testes rápidos e para lançar recursos simples sem se preocupar com a configuração de rede.
> * **Contras:** **Não é recomendada para ambientes de produção.** Por padrão, tudo é público, o que não segue o princípio de "defesa em profundidade". O espaço de IP fixo também pode conflitar com a rede da sua empresa se você precisar conectar as duas no futuro.

---

### <img src="https://api.iconify.design/logos/aws-route-53.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Lista Telefônica da Ilha (DNS na VPC)

Como seus recursos (instâncias EC2, etc.) se encontram usando nomes em vez de apenas endereços IP? Através do DNS.

**Analogia:** O DNS é o serviço de **"lista telefônica"** da sua ilha.

#### 1. <img src="https://api.iconify.design/mdi/phone-log-outline.svg?color=currentColor" width="18" /> O Padrão (Amazon Route 53 Resolver)
* **O que é?** Por padrão, toda VPC vem com um servidor DNS embutido e gerenciado pela AWS (o IP `.2` da sua sub-rede).
* **Como Funciona:** Ele funciona como a "lista telefônica padrão" da ilha. Ele sabe o "ramal" (IP privado) de todas as "casas" (recursos) na ilha e, se você perguntar por um endereço de fora (como `www.google.com`), ele sabe como procurar na lista telefônica mundial.

#### 2. <img src="https://api.iconify.design/mdi/notebook-edit-outline.svg?color=currentColor" width="18" /> A Opção Customizada (Private Hosted Zones)
* **A Dor que Resolve:** "Eu não quero que meu servidor de aplicação se conecte ao banco de dados usando um IP como `10.0.1.54`. Eu quero usar um nome amigável e fácil de lembrar, como `banco.interno.minhaempresa`."
* **A Solução:** Uma **Zona Hospedada Privada (Private Hosted Zone)** no Amazon Route 53.
* **O que é?** É uma "lista telefônica" privada e customizada que só funciona **dentro** da sua VPC.

> **<img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> O Truque Mágico (DNS de Horizonte Dividido - Split-Horizon):**
> Este é um padrão de arquitetura poderoso. Imagine que sua empresa tem o site público `meusite.com`. Mas, *dentro* da sua VPC, você tem uma versão interna do site com ferramentas administrativas. Com uma Private Hosted Zone, você pode configurar para que:
> * Se alguém **de dentro** da VPC perguntar pelo endereço de `meusite.com`, a lista privada responde com o **IP interno** do site administrativo.
> * Se alguém **de fora** da VPC perguntar, a lista telefônica mundial responde com o **IP público** do site para clientes.
>
> É o mesmo nome, mas com duas respostas diferentes, dependendo de quem pergunta.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Saiba que uma **VPC Padrão** é criada automaticamente em cada Região para facilitar o início.
> 2.  A principal característica da VPC Padrão é que suas sub-redes são **públicas por padrão**.
> 3.  O **Amazon Route 53** pode ser usado para criar **Zonas Hospedadas Privadas (Private Hosted Zones)** para gerenciar o DNS *dentro* de uma VPC.