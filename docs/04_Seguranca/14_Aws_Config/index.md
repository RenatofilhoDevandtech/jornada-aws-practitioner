# <img src="https://api.iconify.design/logos/aws-config.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Fiscal da Nuvem: Guia Definitivo do AWS Config

Em uma nuvem com milhares de recursos (instâncias EC2, buckets S3, Security Groups) mudando a todo instante, duas perguntas se tornam críticas:

1.  Qual é a configuração **atual** de todos os meus recursos?
2.  Essa configuração está **correta** e de acordo com as minhas políticas de segurança?

Responder a essas perguntas manualmente é impossível. A ferramenta que automatiza essa resposta é o **AWS Config**.

* **Analogia:** Pense no AWS Config como o **"Arquiteto-Chefe e Fiscal de Obras"** da sua fortaleza digital. Ele não é um guarda de segurança que procura por ladrões, mas um mestre da engenharia que garante que tudo está construído segundo a planta original e o "código de obras" do reino.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Os Dois Superpoderes do AWS Config

O AWS Config tem duas funções principais que trabalham juntas:

#### 1. <img src="https://api.iconify.design/mdi/camera-timer.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> O Gravador de Configuração (A "Máquina do Tempo")
* **O que faz?** O Config tira "fotos" detalhadas (chamadas de Itens de Configuração) de seus recursos da AWS sempre que uma mudança ocorre. Ele armazena essas fotos, criando um **histórico completo** de cada configuração que um recurso já teve.
* **Analogia:** O "Fiscal de Obras" tem um **caderno mágico que tira uma foto 3D** de cada torre do castelo sempre que um tijolo é alterado. Ele mantém um arquivo de todas as "plantas baixas" que o castelo já teve.
* **A Dor que Resolve:** "O site parou de funcionar às 15h02. Tenho certeza que foi uma mudança no Security Group, mas ninguém admite ter feito. O que mudou exatamente?". Com o Config, você pode "voltar no tempo" e ver a configuração exata do Security Group às 15h01 e comparar com a configuração das 15h02, encontrando a mudança exata que causou o problema.

#### 2. <img src="https://api.iconify.design/mdi/book-check-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> As Regras do Config (O "Código de Obras")
* **O que é?** Uma regra que você define para avaliar se as configurações dos seus recursos estão em conformidade com as suas políticas.
* **Analogia:** O **"Código de Obras do Reino"** que o Fiscal carrega com ele. É um livro com regras como: "Toda torre deve ter paredes de pedra" ou "Nenhum cofre pode ter sua porta virada para o pátio público."
* **A Dor que Resolve:** A auditoria manual de conformidade. Em vez de um humano ter que verificar manualmente 500 buckets S3 para ver se algum tem criptografia desabilitada, você cria uma Regra do Config para fazer isso automaticamente.
* **Como Funciona:** A cada nova "foto 3D" que o Fiscal tira, ele a **compara** com o "Código de Obras". Se ele vê um bucket sem criptografia, ele o marca como **"NÃO-CONFORME" (Noncompliant)** em um painel central.

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** A AWS já oferece dezenas de **Regras Gerenciadas** prontas para uso, baseadas nas melhores práticas. Exemplos: `s3-bucket-public-read-prohibited` (verifica se algum bucket S3 permite leitura pública) e `ec2-instance-no-public-ip` (verifica se instâncias EC2 em sub-redes privadas têm IPs públicos, o que é uma falha de segurança).

---

### <img src="https://api.iconify.design/mdi/compare-horizontal.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Batalha dos Gigantes da Auditoria: Config vs. CloudTrail

Iniciantes frequentemente confundem esses dois serviços. A diferença é crucial.

| Característica | <img src="https://api.iconify.design/logos/aws-config.svg?color=currentColor" width="18" /> AWS Config (O Fiscal de Obras) | <img src="https://api.iconify.design/logos/aws-cloudtrail.svg?color=currentColor" width="18" /> AWS CloudTrail (A Câmera de Vigilância) |
| :--- | :--- | :--- |
| **Pergunta que Responde:** | **Qual é o estado** do meu recurso agora e no passado? Ele está em conformidade? | **Quem fez uma ação** no meu recurso, e quando? |
| **Foco:** | O **"O QUÊ"** (a configuração, o estado, a "planta baixa"). | O **"QUEM" e o "QUANDO"** (a chamada de API, a "ordem"). |
| **Analogia:** | O Fiscal anota: "A porta do cofre **agora está aberta**". | A Câmera grava: "**O guarda João abriu** a porta às 14:32". |
| **Caso de Uso Principal:** | **Auditoria de Conformidade** e Gerenciamento de Mudanças. | **Investigação Forense** e Análise de Atividade de Usuários. |

---

### <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Fluxo de Trabalho na Prática

1.  **A Mudança:** Um desenvolvedor altera um Security Group para permitir acesso a uma porta perigosa.
2.  **O Registro:** O **Gravador do AWS Config** tira uma nova "foto" do Security Group e armazena seu novo estado no S3.
3.  **A Avaliação:** O Config compara a nova "foto" com uma **Regra do Config** que diz "nenhum Security Group pode ter a porta X aberta".
4.  **O Veredito:** O Security Group é marcado como **NÃO-CONFORME** no painel do AWS Config.
5.  **O Alerta (Opcional):** O Config envia uma notificação via **Amazon SNS** para a equipe de segurança.
6.  **A Remediação (Opcional):** A notificação do SNS pode até acionar uma **função Lambda** que **corrige automaticamente** a regra do Security Group.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova, a diferença entre Config e CloudTrail é um dos tópicos mais importantes.
> * **AWS Config:** Responde "O meu recurso está **configurado corretamente**?"
> * **AWS CloudTrail:** Responde "**Quem fez** uma alteração no meu recurso?"
> Saber qual serviço usar para qual tipo de pergunta (Conformidade vs. Auditoria) é a chave.

---

### <img src="https://api.iconify.design/mdi/book-check-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Código de Leis da Nuvem: Guia Prático das Regras do AWS Config

No último guia, vimos que o AWS Config é o "Fiscal de Obras" da sua fortaleza, que tira "fotos" (itens de configuração) de todos os seus recursos. Mas um fiscal não serve para nada sem um **"Código de Obras"** para comparar a construção.

As **Regras do Config** são este "Código de Obras". São elas que respondem à pergunta mais importante: "Este recurso, na sua configuração atual, está em **conformidade** com as minhas políticas de segurança e governança?".

---

### <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. Os Tipos de "Leis" (Regras Gerenciadas vs. Personalizadas)

Você tem duas maneiras de criar seu livro de regras:

#### <img src="https://api.iconify.design/mdi/aws.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Regras Gerenciadas pela AWS
* **Analogia:** O **"capítulo de regras padrão"** que já vem no Código de Obras, escrito pelos melhores engenheiros da AWS com base em anos de experiência e melhores práticas.
* **A Dor que Resolve:** "Eu não sou um especialista em segurança, por onde eu começo a criar regras?".
* **Na Prática:** A AWS oferece centenas de regras prontas para uso. Você simplesmente escolhe uma da lista, como `s3-bucket-public-read-prohibited`, e a ativa. Para 90% das necessidades de conformidade, você não precisa escrever uma única linha de código.

#### <img src="https://api.iconify.design/logos/aws-lambda.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Regras Personalizadas com AWS Lambda
* **Analogia:** A **"emenda customizada"** que você, como arquiteto-chefe, escreve para uma necessidade específica e única da sua fortaleza.
* **A Dor que Resolve:** "Minha empresa tem uma política de segurança interna muito específica que não é coberta por uma regra gerenciada."
* **Como Funciona:** Você escreve a lógica da sua regra customizada em uma função **AWS Lambda**. O AWS Config invoca sua função sempre que um recurso relevante muda, e sua função retorna um simples veredito: `COMPLIANT` ou `NON_COMPLIANT`.

---

### <img src="https://api.iconify.design/mdi/format-list-checks.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. As 4 Regras Essenciais em Ação (Casos de Uso Práticos)

Vamos ver exemplos de regras gerenciadas que resolvem dores de cabeça comuns no dia a dia da AWS.

#### <img src="https://api.iconify.design/mdi/lock-outline.svg?color=currentColor" width="20" /> Regra 1: Garantir a Criptografia
* **A Regra:** `encrypted-volumes`
* **O que ela verifica?** Se os volumes EBS anexados às suas instâncias EC2 estão criptografados.
* **A Dor que Resolve:** Garante a conformidade com políticas de segurança de dados (como LGPD/GDPR) e protege seus dados em repouso. Se a regra encontrar um volume não criptografado, ela o marca como `NÃO-CONFORME` no painel.

#### <img src="https://api.iconify.design/mdi/tag-check-outline.svg?color=currentColor" width="20" /> Regra 2: Garantir a Governança (Tags)
* **A Regra:** `required-tags`
* **O que ela verifica?** Se suas instâncias EC2 (ou outros recursos) possuem as tags que sua empresa definiu como obrigatórias (ex: `CentroDeCusto`, `Projeto`).
* **A Dor que Resolve:** O caos financeiro e organizacional. Sem tags, é impossível saber qual departamento é responsável pelo custo de um recurso. Esta regra automatiza a governança de custos.

#### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="20" /> Regra 3: Garantir o Padrão (AMIs Aprovadas)
* **A Regra:** `approved-amis-by-id`
* **O que ela verifica?** Se as instâncias EC2 estão sendo lançadas apenas a partir de uma lista de AMIs que você aprovou.
* **A Dor que Resolve:** O "Shadow IT" e a falta de padronização. Impede que desenvolvedores usem AMIs antigas, inseguras ou de fontes desconhecidas, garantindo que todos os servidores sigam a sua **linha de referência (baseline)** de segurança.

#### <img src="https://api.iconify.design/mdi/cash-remove.svg?color=currentColor" width="20" /> Regra 4: Garantir a Otimização de Custos
* **A Regra:** `ec2-ip-public-in-use`
* **O que ela verifica?** Se existem Endereços IP Elásticos na sua conta que **não estão anexados** a nenhuma instância EC2.
* **A Dor que Resolve:** O desperdício de dinheiro. A AWS cobra por IPs Elásticos que estão alocados mas não estão sendo usados. Esta regra funciona como um "caça-fantasmas" de recursos órfãos que estão gerando custo desnecessário.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova, entenda o propósito fundamental do AWS Config e suas Regras:
> * **AWS Config** é o serviço principal para **AVALIAR, AUDITAR e AVALIAR a CONFORMIDADE** das configurações dos seus recursos.
> * As **Regras** são o mecanismo que **automatiza** essa avaliação.
> * Ele não serve apenas para segurança, mas também para **governança operacional e otimização de custos**, como mostram os exemplos de tags e IPs Elásticos.

Com as Regras do Config, você transforma a conformidade de um processo manual, lento e reativo em um sistema de governança automatizado, contínuo e proativo.