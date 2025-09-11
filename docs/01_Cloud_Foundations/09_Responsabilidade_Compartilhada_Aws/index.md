# <img src="https://api.iconify.design/mdi/handshake-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> O Contrato de Parceria: Desvendando o Modelo de Responsabilidade Compartilhada

Ao se mudar para a nuvem, a primeira pergunta que muitos fazem é: "Então a AWS cuida de toda a segurança para mim, certo?". A resposta é um sonoro **NÃO**.

A segurança na AWS não é uma transferência de tarefas, é uma **parceria**. Pensar que a AWS faz tudo é o maior e mais perigoso mito da nuvem. Para deixar essa parceria clara, a AWS criou o **Modelo de Responsabilidade Compartilhada**.

Pense nisso como **morar em um condomínio de altíssima segurança**.

* A **administração do condomínio (AWS)** é responsável pela segurança do prédio em si.
* Você, o **morador (Cliente)**, é responsável pela segurança do seu apartamento.

Este guia vai te mostrar exatamente quais são as tarefas da administração e quais são as suas, e o insight mais importante: como o tipo de "apartamento" que você aluga (o serviço que você usa) muda completamente a divisão de tarefas.

---

### <img src="https://api.iconify.design/mdi/domain.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Responsabilidade da AWS: Segurança *DA* Nuvem

A AWS é a "administração do condomínio". A missão dela é proteger a **infraestrutura global** que sustenta tudo. Eles são responsáveis pelos componentes que você não pode ver nem tocar.

**As tarefas deles incluem:**
* <img src="https://api.iconify.design/mdi/cctv.svg?color=currentColor" width="16" style="vertical-align:middle; margin-right:5px;" /> **Segurança Física dos Data Centers:** Guardas 24/7, cercas, controle de acesso biométrico, câmeras. Ninguém entra sem autorização.
* <img src="https://api.iconify.design/mdi/server-network.svg?color=currentColor" width="16" style="vertical-align:middle; margin-right:5px;" /> **Infraestrutura de Hardware e Rede:** Garantir que os servidores, roteadores, switches e cabos estejam funcionando, seguros e com proteção contra intrusão.
* <img src="https://api.iconify.design/mdi/layers-outline.svg?color=currentColor" width="16" style="vertical-align:middle; margin-right:5px;" /> **Infraestrutura de Virtualização:** Proteger o software (o *hypervisor*) que cria e isola as instâncias EC2 umas das outras.

Em resumo: a AWS garante que o "prédio" seja impenetrável e que a eletricidade, a água e a estrutura nunca falhem.

---

### <img src="https://api.iconify.design/mdi/key-chain-variant.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Sua Responsabilidade: Segurança *NA* Nuvem

Você é o "morador". A AWS te entrega um apartamento seguro, mas o que você faz dentro dele e como você protege sua porta de entrada é sua responsabilidade.

**As SUAS tarefas incluem:**
* <img src="https://api.iconify.design/mdi/file-lock-outline.svg?color=currentColor" width="16" style="vertical-align:middle; margin-right:5px;" /> **Dados do Cliente:** Você é o dono dos seus dados. Isso inclui a decisão de criptografá-los, anonimizá-los e classificá-los.
* <img src="https://api.iconify.design/mdi/account-key-outline.svg?color=currentColor" width="16" style="vertical-align:middle; margin-right:5px;" /> **Gerenciamento de Identidade e Acesso (IAM):** A tarefa **mais crítica**. É você quem decide quem tem as chaves do seu apartamento. Configurar usuários, senhas, roles e permissões é sua responsabilidade.
* <img src="https://api.iconify.design/mdi/wall.svg?color=currentColor" width="16" style="vertical-align:middle; margin-right:5px;" /> **Configuração do Sistema Operacional, Rede e Firewall:** Instalar atualizações de segurança (patches) no SO dos seus servidores EC2 e configurar as regras do seu firewall (**Security Groups**) para dizer quem pode "bater na sua porta".
* <img src="https://api.iconify.design/mdi/shield-lock-outline.svg?color=currentColor" width="16" style="vertical-align:middle; margin-right:5px;" /> **Criptografia:** Você decide se vai criptografar os dados "em trânsito" (enquanto viajam pela rede) e "em repouso" (enquanto estão armazenados no disco).

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** A AWS te dá o prédio mais seguro do mundo, mas a chave do seu apartamento está na sua mão. Isso não é um fardo, é o **poder de controlar seu próprio destino e segurança**. A maioria das falhas de segurança na nuvem acontece por erros de configuração do cliente (uma "porta de apartamento" deixada aberta).

---

### <img src="https://api.iconify.design/mdi/chart-line-variant.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> A Linha que se Move: O Fator Mais Importante

Este é o conceito mais avançado e crucial. A linha que divide as responsabilidades **não é fixa**. Ela muda dependendo do tipo de "apartamento" (serviço) que você escolhe.

#### <img src="https://api.iconify.design/mdi/package-variant.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> IaaS (Infraestrutura como Serviço)
* **Exemplo:** Amazon EC2
* **Analogia:** Você está alugando um **apartamento vazio e sem mobília**.
* **Sua Responsabilidade:** É MÁXIMA. A AWS te dá as paredes, o teto e as conexões de água e luz. Mas você é responsável por trazer os móveis (instalar o Sistema Operacional), pintá-los (aplicar patches de segurança), instalar os eletrodomésticos (seus aplicativos) e trancar a porta (configurar Security Groups).

#### <img src="https://api.iconify.design/mdi/sofa-single-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> PaaS (Plataforma como Serviço)
* **Exemplo:** Amazon RDS, AWS Elastic Beanstalk
* **Analogia:** Você está alugando um **apartamento mobiliado**.
* **Sua Responsabilidade:** É MÉDIA. A AWS já te entrega a cama, o fogão e a geladeira (a plataforma de banco de dados, o servidor web) e cuida da manutenção deles (patches do SO e do banco de dados). Sua responsabilidade é cuidar dos seus pertences pessoais (seus dados e seu código) e, claro, trancar a porta.

#### <img src="https://api.iconify.design/mdi/bed-king-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> SaaS (Software como Serviço)
* **Exemplo:** AWS Shield, Amazon Chime, AWS Trusted Advisor
* **Analogia:** Você está se hospedando em um **hotel com serviço de quarto**.
* **Sua Responsabilidade:** É MÍNIMA. O hotel cuida de tudo: limpeza, mobília, TV a cabo. Sua única preocupação é não perder a chave do quarto e proteger sua própria mala.

---

### <img src="https://api.iconify.design/mdi/head-question-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Cenário do Mundo Real: Teste seu Conhecimento

Vamos usar o exemplo da atividade para solidificar o conceito da "linha que se move".

**Cenário:** Você precisa de um banco de dados Oracle.
* **Opção A:** Você instala o Oracle em um servidor **Amazon EC2** (IaaS).
* **Opção B:** Você usa o **Amazon RDS** para Oracle (PaaS).

**Pergunta:** Quem é responsável por aplicar uma atualização de segurança crítica (patch) no software da Oracle?

**Respostas:**
* **Na Opção A (EC2):** **VOCÊ, O CLIENTE.** Você está no "apartamento vazio". O Oracle é um "móvel" que você trouxe, então a manutenção dele é sua.
* **Na Opção B (RDS):** **A AWS.** Você está no "apartamento mobiliado". O Oracle é parte da "mobília" que a AWS forneceu, então a manutenção da plataforma é responsabilidade dela.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** A prova VAI te testar nisso. Eles darão um cenário com um serviço (EC2, RDS, S3) e perguntarão quem é responsável por uma tarefa. Se você entender a analogia do **Apartamento Vazio (IaaS) vs. Mobiliado (PaaS) vs. Hotel (SaaS)**, você acertará 99% das questões sobre este tema.