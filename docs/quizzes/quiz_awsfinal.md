<div class="quiz-container" id="quiz-simulado-container">
    <h3><img src="https://api.iconify.design/logos/aws-certified-cloud-practitioner.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Simulado Final: AWS Certified Cloud Practitioner</h3>
    <form class="quiz-form">
        </form>
    <button class="submit-quiz-btn">Verificar Respostas</button>
    <button class="redo-quiz-btn" style="display:none; margin-left: 1rem;">Refazer Quiz</button>
    <div class="quiz-results"></div>
</div>

<script>
    (function() {
        const quizContainer = document.getElementById('quiz-simulado-container');
        if (!quizContainer) return;

        const quizForm = quizContainer.querySelector('.quiz-form');
        const submitBtn = quizContainer.querySelector('.submit-quiz-btn');
        const redoBtn = quizContainer.querySelector('.redo-quiz-btn');
        const resultsContainer = quizContainer.querySelector('.quiz-results');

        const quizData = [
            // Domínio 1: Conceitos de Nuvem (~16 questões)
            { question: "Qual vantagem da nuvem AWS se refere à capacidade de trocar grandes despesas de capital (CapEx) por despesas operacionais (OpEx)?", options: ["Agilidade", "Elasticidade", "Pagar conforme o uso", "Economia de escala"], answer: 2, explanation: "Uma das principais vantagens da nuvem é trocar o grande investimento inicial em hardware (CapEx) por um modelo de pagamento sob demanda (OpEx), onde você paga apenas pelo que usa." },
            { question: "Uma empresa está crescendo rapidamente e precisa que sua infraestrutura se ajuste automaticamente à demanda dos usuários. Qual conceito da nuvem AWS melhor descreve essa capacidade?", options: ["Tolerância a falhas", "Elasticidade", "Agilidade", "Alcance Global"], answer: 1, explanation: "A elasticidade é a capacidade de escalar recursos para cima e para baixo automaticamente em resposta à demanda, garantindo performance e otimização de custos." },
            { question: "No modelo IaaS (Infraestrutura como Serviço), qual das seguintes opções é uma responsabilidade do cliente?", options: ["A virtualização", "O hardware do servidor", "A segurança física", "O sistema operacional"], answer: 3, explanation: "No modelo IaaS, a AWS gerencia a infraestrutura física e a camada de virtualização. O cliente é responsável pelo sistema operacional, aplicações e dados." },
            { question: "Qual serviço representa um exemplo de SaaS (Software como Serviço) da AWS?", options: ["Amazon EC2", "Amazon S3", "Amazon Chime", "Amazon RDS"], answer: 2, explanation: "O Amazon Chime é uma aplicação de comunicação completa (software) que você consome como um serviço. EC2 é IaaS, e RDS é PaaS." },
            { question: "Qual pilar do AWS Well-Architected Framework foca na execução de cargas de trabalho de forma eficaz e na melhoria contínua dos processos?", options: ["Segurança", "Confiabilidade", "Excelência Operacional", "Otimização de Custos"], answer: 2, explanation: "A Excelência Operacional é sobre como você opera e monitora seus sistemas para entregar valor de negócio e como você melhora continuamente seus processos e procedimentos." },
            { question: "O que são Zonas de Disponibilidade (AZs)?", options: ["Países onde a AWS opera.", "Um ou mais data centers distintos com energia, rede e conectividade redundantes dentro de uma Região.", "Pontos de presença para cache de conteúdo.", "Redes virtuais privadas para os clientes."], answer: 1, explanation: "As AZs são a base da alta disponibilidade na AWS. Elas são data centers fisicamente isolados dentro da mesma Região, permitindo a construção de aplicações tolerantes a falhas." },
            { question: "Qual benefício da nuvem permite que uma startup tenha acesso à mesma infraestrutura de ponta que grandes empresas?", options: ["Elasticidade", "Pagar conforme o uso", "Agilidade", "Beneficiar-se de economias de escala massivas"], answer: 3, explanation: "Como a AWS compra hardware em uma escala gigantesca, ela repassa essa economia para os clientes. Isso permite que empresas de todos os tamanhos acessem tecnologia de nível mundial a um custo baixo." },
            { question: "Qual modelo de implantação de nuvem envolve o uso exclusivo de recursos de nuvem em um provedor como a AWS?", options: ["Nuvem Híbrida", "Nuvem Privada", "Nuvem Pública", "On-premises"], answer: 2, explanation: "Uma implantação 'all-in' na AWS é um exemplo de uso da Nuvem Pública." },
            { question: "Qual o propósito principal de uma Região da AWS?", options: ["Fornecer a menor latência possível para todos os usuários globais.", "Isolar recursos e dados em uma área geográfica específica por motivos de conformidade e latência.", "Servir como um ponto de backup para uma Zona de Disponibilidade.", "Hospedar apenas serviços de armazenamento."], answer: 1, explanation: "As Regiões permitem que os clientes implantem suas aplicações perto de seus usuários finais e cumpram com os requisitos de soberania de dados." },
            { question: "O que a AWS define como sua responsabilidade no Modelo de Responsabilidade Compartilhada?", options: ["Criptografia dos dados do cliente em um bucket S3.", "Configuração de um Security Group.", "Gerenciamento de patches do sistema operacional em uma instância EC2.", "Gerenciamento do software de virtualização (hypervisor)."], answer: 3, explanation: "A AWS é responsável pela segurança *DA* nuvem. Isso inclui o hardware, a infraestrutura global, a rede e a camada de virtualização." },
            { question: "O que significa 'Agilidade' como um benefício da nuvem?", options: ["A capacidade de escalar recursos automaticamente.", "A velocidade com que você pode provisionar novos recursos e experimentar novas ideias.", "A resiliência da infraestrutura.", "A economia de custos do modelo de pagamento."], answer: 1, explanation: "Agilidade na nuvem refere-se à capacidade de inovar mais rapidamente, pois o tempo para provisionar um novo servidor ou um banco de dados cai de semanas para minutos." },
            { question: "Qual pilar do Well-Architected Framework se preocupa com a escolha correta dos tipos de instância e com o monitoramento dos gastos?", options: ["Segurança", "Eficiência de Performance", "Otimização de Custos", "Confiabilidade"], answer: 2, explanation: "O pilar de Otimização de Custos foca em evitar custos desnecessários, selecionando os recursos e os modelos de preços mais apropriados para sua carga de trabalho." },
            { question: "Qual benefício da AWS se refere à capacidade de implantar aplicações em todo o mundo com apenas alguns cliques?", options: ["Elasticidade", "Pagar conforme o uso", "Alcance Global", "Segurança"], answer: 2, explanation: "O Alcance Global da AWS, com suas múltiplas Regiões, permite que você implante suas aplicações perto de seus clientes, onde quer que eles estejam." },
            { question: "Qual modelo de serviço de nuvem (IaaS, PaaS, SaaS) oferece o maior nível de controle sobre a infraestrutura de TI?", options: ["PaaS", "IaaS", "SaaS", "Todos oferecem o mesmo nível de controle."], answer: 1, explanation: "IaaS (Infraestrutura como Serviço), como o Amazon EC2, oferece o maior nível de controle, pois você gerencia o sistema operacional, o middleware e a aplicação." },
            { question: "Qual das seguintes é uma responsabilidade do cliente em relação a um banco de dados Amazon RDS?", options: ["Aplicar patches no sistema operacional do servidor.", "Gerenciar o schema e os dados do banco de dados.", "Fazer o backup do banco de dados.", "Configurar o failover Multi-AZ."], answer: 1, explanation: "No RDS (um serviço PaaS), a AWS gerencia a infraestrutura e o software do banco de dados. O cliente é sempre responsável pelos seus próprios dados, o que inclui o design do schema, a otimização das queries e o controle de acesso." },
            { question: "O que é tolerância a falhas?", options: ["A habilidade de escalar para atender à demanda.", "A capacidade de um sistema permanecer operacional mesmo se um ou mais de seus componentes falharem.", "A segurança de um sistema contra ataques externos.", "A otimização de custos de uma aplicação."], answer: 1, explanation: "Tolerância a falhas é um conceito central da Confiabilidade. Na AWS, ela é alcançada principalmente através da distribuição de recursos em múltiplas Zonas de Disponibilidade." },
            // Domínio 2: Segurança e Conformidade (~19 questões)
            { question: "Qual serviço é fundamental para gerenciar usuários, grupos e permissões na AWS?", options: ["Amazon VPC", "AWS Shield", "AWS IAM", "Amazon GuardDuty"], answer: 2, explanation: "O AWS IAM (Identity and Access Management) é o serviço central que permite gerenciar de forma segura o acesso aos serviços e recursos da AWS." },
            { question: "Qual é a melhor prática de segurança para a conta raiz da AWS?", options: ["Usá-la para todas as tarefas administrativas.", "Compartilhar suas credenciais com a equipe de TI.", "Excluir a conta raiz após criar um usuário IAM.", "Habilitar o MFA e não usá-la para tarefas diárias."], answer: 3, explanation: "A conta raiz tem poder total. A prática recomendada é protegê-la com MFA e usá-la apenas para tarefas que exigem especificamente as credenciais raiz." },
            { question: "Um Security Group atua como um firewall em qual nível?", options: ["Região", "Sub-rede", "Instância EC2", "VPC"], answer: 2, explanation: "Os Security Groups são a principal ferramenta de firewall para instâncias, atuando como um 'guarda-costas' que controla o tráfego de entrada e saída." },
            { question: "Qual serviço da AWS oferece proteção gerenciada contra ataques de Negação de Serviço Distribuída (DDoS)?", options: ["Amazon Inspector", "AWS WAF", "AWS Shield", "Network ACL"], answer: 2, explanation: "O AWS Shield é o serviço projetado para proteger suas aplicações contra ataques DDoS. O Shield Standard é ativado por padrão para todos os clientes." },
            { question: "Uma empresa precisa de um log de auditoria de todas as chamadas de API feitas em sua conta. Qual serviço fornece essa funcionalidade?", options: ["Amazon CloudWatch", "AWS Config", "VPC Flow Logs", "AWS CloudTrail"], answer: 3, explanation: "O AWS CloudTrail grava as chamadas de API, fornecendo uma trilha de auditoria essencial para segurança, conformidade e governança." },
            { question: "Qual a principal diferença entre um Security Group e uma Network ACL?", options: ["SGs operam na sub-rede, NACLs na instância.", "SGs são stateless, NACLs são stateful.", "SGs suportam apenas regras de 'Permitir', enquanto NACLs suportam 'Permitir' e 'Negar'.", "Não há diferença funcional."], answer: 2, explanation: "NACLs são stateless e podem ter regras de 'Deny', tornando-as úteis para bloquear IPs. Security Groups são stateful e só têm regras de 'Allow'." },
            { question: "Qual serviço você usaria para provisionar certificados SSL/TLS para seu Application Load Balancer?", options: ["AWS KMS", "AWS Secrets Manager", "AWS Certificate Manager (ACM)", "AWS IAM"], answer: 2, explanation: "O ACM simplifica e automatiza o gerenciamento de certificados SSL/TLS, incluindo o provisionamento e a renovação, integrando-se com serviços como ELB e CloudFront." },
            { question: "Uma empresa quer escanear suas instâncias EC2 em busca de vulnerabilidades de software conhecidas. Qual serviço é o mais indicado?", options: ["Amazon GuardDuty", "AWS Trusted Advisor", "Amazon Inspector", "AWS Config"], answer: 2, explanation: "O Amazon Inspector é o serviço de gerenciamento de vulnerabilidades que escaneia continuamente suas cargas de trabalho em busca de vulnerabilidades de software e exposição de rede." },
            { question: "O que é o princípio do menor privilégio?", options: ["Dar a todos os usuários privilégios de administrador.", "Conceder aos usuários e serviços apenas as permissões estritamente necessárias para realizar suas tarefas.", "Usar a menor instância EC2 possível.", "Manter o menor número possível de arquivos no S3."], answer: 1, explanation: "Este é um princípio de segurança fundamental. Ao conceder apenas as permissões mínimas, você limita o dano potencial caso as credenciais sejam comprometidas." },
            { question: "O que uma IAM Role permite?", options: ["Agrupar múltiplos usuários.", "Definir uma política de senha.", "Que uma identidade (como uma instância EC2) assuma permissões temporárias de forma segura.", "Bloquear permanentemente o acesso de um usuário."], answer: 2, explanation: "As Roles são o mecanismo seguro para delegação de permissões. Elas fornecem credenciais temporárias, eliminando a necessidade de armazenar chaves de acesso de longo prazo." },
            { question: "Qual serviço da AWS você usaria para proteger sua aplicação web contra SQL Injection e Cross-Site Scripting (XSS)?", options: ["AWS Shield", "Security Group", "Network ACL", "AWS WAF"], answer: 3, explanation: "O AWS WAF (Web Application Firewall) opera na camada de aplicação (Camada 7) e permite criar regras para filtrar e bloquear padrões de ataques web comuns." },
            { question: "Qual é a forma mais eficaz de proteger uma conta de usuário IAM contra o roubo de senha?", options: ["Usar uma senha muito longa.", "Trocar a senha toda semana.", "Habilitar a Autenticação Multi-Fator (MFA).", "Anexar uma política de negação explícita."], answer: 2, explanation: "O MFA adiciona uma segunda camada de segurança (algo que você tem), tornando uma senha roubada inútil para o atacante." },
            { question: "Onde um cliente da AWS pode encontrar os relatórios de conformidade da AWS, como SOC 2?", options: ["AWS Trusted Advisor", "AWS Personal Health Dashboard", "AWS Artifact", "Console do Amazon S3"], answer: 2, explanation: "O AWS Artifact é o portal central para acessar os relatórios de conformidade e segurança da AWS. É a ferramenta para provar a conformidade da infraestrutura da AWS para seus auditores." },
            { question: "Qual serviço ajuda a auditar a conformidade das configurações dos seus recursos?", options: ["AWS CloudTrail", "AWS Config", "Amazon GuardDuty", "Amazon Inspector"], answer: 1, explanation: "O AWS Config é o 'fiscal de obras' da sua conta. Ele monitora e grava o estado de configuração dos seus recursos e os avalia em relação às regras de conformidade." },
            { question: "Qual serviço é usado primariamente para gerenciar chaves de criptografia para proteger dados em repouso?", options: ["AWS Certificate Manager (ACM)", "AWS Secrets Manager", "AWS Key Management Service (KMS)", "AWS Shield"], answer: 2, explanation: "O KMS é o serviço central para criar e controlar as chaves criptográficas usadas para proteger seus dados em serviços como S3, EBS e RDS." },
            { question: "Uma empresa quer que seus funcionários usem o login corporativo para acessar o Console da AWS. Qual tecnologia permite isso?", options: ["MFA", "Políticas de Senha", "Grupos do IAM", "Federação de Identidade"], answer: 3, explanation: "A Federação permite que você estabeleça uma relação de confiança entre um Provedor de Identidade (como o Active Directory) e a AWS, permitindo o Single Sign-On (SSO)." },
            // Domínio 3: Tecnologia e Serviços (~22 questões)
            { question: "Qual serviço é um banco de dados relacional compatível com MySQL e PostgreSQL, otimizado pela AWS para a nuvem?", options: ["Amazon RDS", "Amazon Redshift", "Amazon DynamoDB", "Amazon Aurora"], answer: 3, explanation: "O Amazon Aurora é o motor de banco de dados da AWS, reconstruído para a nuvem, oferecendo performance e resiliência superiores às versões padrão de MySQL e PostgreSQL." },
            { question: "Uma equipe precisa de um sistema de arquivos compartilhado para múltiplas instâncias EC2 Linux. Qual serviço é o ideal?", options: ["Amazon S3", "Amazon EBS", "Amazon EFS", "AWS Storage Gateway"], answer: 2, explanation: "O Amazon EFS (Elastic File System) fornece um sistema de arquivos de rede (NFS) simples e escalável para ser usado com instâncias EC2." },
            { question: "Qual serviço você usaria para orquestrar um fluxo de trabalho complexo com múltiplas funções Lambda?", options: ["AWS CodePipeline", "AWS Step Functions", "Amazon SQS", "Amazon SNS"], answer: 1, explanation: "O AWS Step Functions permite coordenar múltiplos serviços da AWS em fluxos de trabalho serverless, visualizando o fluxo como um diagrama de estados." },
            { question: "Qual a diferença fundamental entre o Amazon SQS e o Amazon SNS?", options: ["SQS é para mensagens, SNS é para arquivos.", "SQS é uma Fila (um consumidor), SNS é um Tópico (múltiplos consumidores).", "SQS é mais rápido que SNS.", "SQS é regional, SNS é global."], answer: 1, explanation: "SQS (Simple Queue Service) desacopla componentes através de filas (um-para-um). SNS (Simple Notification Service) usa o padrão pub/sub para enviar uma notificação para múltiplos endpoints (um-para-muitos)." },
            { question: "O que o AWS Storage Gateway permite que você faça?", options: ["Fazer backup de instâncias EC2.", "Estender um bucket S3.", "Conectar sua infraestrutura de armazenamento local à nuvem AWS de forma híbrida.", "Acelerar o upload para o S3."], answer: 2, explanation: "O Storage Gateway é um serviço de armazenamento híbrido que permite que suas aplicações locais usem o armazenamento da AWS de forma transparente." },
            { question: "Qual serviço você usaria para executar contêineres Docker sem gerenciar o cluster de instâncias EC2 subjacente?", options: ["AWS Fargate", "Amazon ECS com EC2", "Amazon EKS", "AWS Lambda"], answer: 0, explanation: "O AWS Fargate é um motor de computação serverless para contêineres. Com o Fargate, você não precisa provisionar ou gerenciar servidores." },
            { question: "Uma empresa precisa de um serviço de Data Warehouse para executar consultas analíticas complexas. Qual serviço é o mais indicado?", options: ["Amazon RDS", "Amazon DynamoDB", "Amazon Redshift", "Amazon S3"], answer: 2, explanation: "O Amazon Redshift é o serviço de Data Warehouse da AWS, projetado para BI e cargas de trabalho analíticas (OLAP) em grande escala." },
            { question: "Qual serviço da AWS é uma plataforma totalmente gerenciada para construir, treinar e implantar modelos de machine learning?", options: ["Amazon Rekognition", "Amazon SageMaker", "Amazon Polly", "Amazon Lex"], answer: 1, explanation: "O Amazon SageMaker é a plataforma completa que permite que desenvolvedores e cientistas de dados preparem, construam, treinem e implantem modelos de ML." },
            { question: "Uma aplicação precisa de um cache em memória para reduzir a latência de acesso a um banco de dados. Qual serviço você usaria?", options: ["Amazon DynamoDB", "Amazon S3", "Amazon ElastiCache", "Amazon EBS"], answer: 2, explanation: "O Amazon ElastiCache é um serviço que facilita a implantação e operação de caches em memória na nuvem, compatível com Redis e Memcached." },
            { question: "Qual ferramenta da AWS permite orquestrar um pipeline de CI/CD, do código à implantação?", options: ["AWS CodeCommit", "AWS CodeBuild", "AWS CodeDeploy", "AWS CodePipeline"], answer: 3, explanation: "O AWS CodePipeline é o serviço de orquestração que automatiza as fases de construção, teste e implantação do seu processo de lançamento de software." },
            { question: "Qual serviço fornece armazenamento em blocos persistente para uso com instâncias Amazon EC2?", options: ["Amazon S3", "Amazon EFS", "Amazon EBS", "Amazon S3 Glacier"], answer: 2, explanation: "O Amazon EBS (Elastic Block Store) funciona como um disco rígido virtual de alta performance para suas instâncias EC2." },
            { question: "Uma empresa quer uma conexão de rede privada e dedicada entre seu data center local e a AWS. Qual serviço atende a essa necessidade?", options: ["Amazon VPC Peering", "AWS VPN", "AWS Direct Connect", "Internet Gateway"], answer: 2, explanation: "O AWS Direct Connect estabelece uma conexão de rede privada que contorna a internet pública, oferecendo maior largura de banda e uma experiência de rede mais consistente." },
            // Domínio 4: Faturamento, Preços e Suporte (~8 questões)
            { question: "Qual ferramenta da AWS permite criar um alarme para ser notificado quando seus custos excederem um determinado valor?", options: ["AWS Cost Explorer", "AWS Pricing Calculator", "AWS Budgets", "AWS Cost and Usage Report"], answer: 2, explanation: "O AWS Budgets permite que você defina orçamentos customizados e envia alertas quando seus custos ou uso excedem (ou estão previstos para exceder) o valor orçado." },
            { question: "Qual modelo de preços do EC2 oferece o maior desconto em troca de um compromisso de uso de 1 ou 3 anos?", options: ["On-Demand", "Spot Instances", "Dedicated Hosts", "Reserved Instances / Savings Plans"], answer: 3, explanation: "As Instâncias Reservadas (RIs) e os Savings Plans oferecem descontos significativos em comparação com os preços On-Demand, em troca de um compromisso de longo prazo." },
            { question: "Qual ferramenta da AWS oferece uma visualização detalhada e gráficos sobre os gastos?", options: ["AWS Trusted Advisor", "AWS Cost Explorer", "AWS Budgets", "AWS Personal Health Dashboard"], answer: 1, explanation: "O AWS Cost Explorer possui uma interface fácil de usar que permite visualizar, entender e gerenciar seus custos e uso da AWS ao longo do tempo." },
            { question: "Qual plano de suporte da AWS é recomendado para ambientes de produção críticos, com tempo de resposta de < 1 hora?", options: ["Basic", "Developer", "Business", "Enterprise"], answer: 2, explanation: "O plano Business oferece tempos de resposta mais rápidos (incluindo < 1 hora para produção fora do ar) e acesso ao suporte 24/7." },
            { question: "O que a calculadora de Custo Total de Propriedade (TCO) da AWS ajuda uma empresa a fazer?", options: ["Pagar a fatura mensal.", "Estimar a economia de custos ao mover sua infraestrutura on-premises para a AWS.", "Criar um orçamento para gastos.", "Visualizar os limites de serviço."], answer: 1, explanation: "A calculadora de TCO ajuda você a comparar o custo de executar suas aplicações em um ambiente local com o custo na AWS, mostrando a potencial economia." },
            { question: "Qual recurso do AWS Organizations é uma de suas principais vantagens de faturamento?", options: ["Políticas de Serviço (SCPs)", "Faturamento Consolidado (Consolidated Billing)", "Unidades Organizacionais (OUs)", "AWS Single Sign-On"], answer: 1, explanation: "O Faturamento Consolidado permite gerenciar o faturamento de múltiplas contas a partir de uma única conta principal, simplificando o pagamento e agregando o uso para descontos por volume." },
            { question: "Qual modelo de preços do EC2 é ideal para cargas de trabalho que podem ser interrompidas, oferecendo os maiores descontos?", options: ["On-Demand", "Reserved Instances", "Spot Instances", "Savings Plans"], answer: 2, explanation: "As Instâncias Spot permitem que você utilize a capacidade de computação não utilizada da AWS com descontos de até 90%. A AWS pode retomar a instância com um aviso de dois minutos." },
            { question: "Todos os clientes da AWS têm acesso a qual plano de suporte, sem custo adicional?", options: ["Developer", "Basic", "Business", "Enterprise"], answer: 1, explanation: "O plano Basic Support está incluído para todas as contas da AWS e oferece acesso ao suporte para questões de faturamento e conta, além de acesso à documentação e fóruns." },
            // Preenchendo até 65...
            { question: "Qual serviço é mais adequado para armazenar e servir arquivos de vídeo para um site de streaming?", options: ["Amazon RDS", "Amazon DynamoDB", "Amazon S3", "Amazon EFS"], answer: 2, explanation: "O Amazon S3 é otimizado para armazenar e entregar grandes objetos, como arquivos de mídia, e se integra perfeitamente com a CDN Amazon CloudFront para distribuição global." },
            { question: "Qual das seguintes opções é um benefício do AWS Global Accelerator?", options: ["Ele criptografa os dados em repouso automaticamente.", "Ele fornece um endereço IP estático que atua como um ponto de entrada fixo para sua aplicação.", "Ele é um banco de dados em memória.", "Ele gerencia repositórios Git."], answer: 1, explanation: "O AWS Global Accelerator usa a rede global da AWS para melhorar a performance e a disponibilidade de suas aplicações, fornecendo IPs estáticos que roteiam o tráfego para o endpoint ideal." },
            { question: "Para que serve o AWS Secrets Manager?", options: ["Para gerenciar chaves de criptografia.", "Para armazenar, rotacionar e recuperar segredos, como senhas de banco de dados e chaves de API.", "Para armazenar artefatos de build.", "Para escanear por segredos expostos no código."], answer: 1, explanation: "O Secrets Manager ajuda a proteger o acesso a suas aplicações, serviços e recursos de TI, eliminando a necessidade de codificar segredos diretamente no código-fonte." },
            { question: "Uma empresa quer migrar um grande volume de dados (petabytes) de seu data center para a AWS. Qual serviço físico a AWS oferece para essa tarefa?", options: ["AWS Snowball", "AWS DataSync", "Amazon S3 Transfer Acceleration", "AWS VPN"], answer: 0, explanation: "O AWS Snowball é um serviço de transporte de dados em escala de petabytes que usa dispositivos físicos seguros para transferir grandes quantidades de dados para dentro e fora da nuvem AWS." },
            { question: "Qual serviço permite a criação de uma área de trabalho (desktop) virtual baseada na nuvem?", options: ["Amazon EC2", "AWS Lambda", "Amazon WorkSpaces", "Amazon AppStream 2.0"], answer: 2, explanation: "O Amazon WorkSpaces é um serviço de Desktop-as-a-Service (DaaS) totalmente gerenciado, ideal para funcionários remotos e para o modelo BYOD." },
            { question: "O que o Amazon Elastic Beanstalk oferece?", options: ["Um cluster Kubernetes gerenciado.", "Uma forma fácil de implantar e escalar aplicações web sem se preocupar com a infraestrutura subjacente.", "Um serviço de fila de mensagens.", "Um data warehouse."], answer: 1, explanation: "O Elastic Beanstalk é um serviço PaaS (Plataforma como Serviço). Você simplesmente faz o upload do seu código, e ele automaticamente cuida do provisionamento, load balancing, auto-scaling e monitoramento." },
            { question: "Qual é a função principal de uma Amazon Machine Image (AMI)?", options: ["É um snapshot de um volume EBS.", "É um template que contém as informações necessárias para lançar uma instância EC2.", "É um contêiner Docker.", "É um tipo de banco de dados."], answer: 1, explanation: "Uma AMI serve como um blueprint para suas instâncias. Ela inclui o sistema operacional, um servidor de aplicação e as aplicações. Lançar uma instância é iniciar uma cópia da AMI." },
            { question: "Se você precisa de um banco de dados relacional com a maior compatibilidade com o Microsoft SQL Server, qual serviço você escolheria?", options: ["Amazon Aurora", "Amazon DynamoDB", "Amazon RDS for PostgreSQL", "Amazon RDS for SQL Server"], answer: 3, explanation: "O Amazon RDS oferece motores de banco de dados comerciais como o Microsoft SQL Server de forma gerenciada, facilitando a migração de aplicações existentes." },
            { question: "O que o Amazon Connect oferece?", options: ["Uma conexão de rede privada.", "Uma central de atendimento ao cliente (contact center) omnicanal baseada na nuvem.", "Um serviço para conectar dispositivos IoT.", "Um balanceador de carga."], answer: 1, explanation: "O Amazon Connect permite que você crie uma central de atendimento em poucos minutos, com um modelo de pagamento sob demanda, escalando para atender a milhares de agentes." },
            { question: "Qual serviço da AWS você usaria para registrar um nome de domínio, como `minhaempresa.com`?", options: ["Amazon VPC", "AWS Certificate Manager", "Amazon Route 53", "Elastic Load Balancing"], answer: 2, explanation: "Além de ser o serviço de DNS, o Amazon Route 53 também atua como um registrador de nomes de domínio, permitindo que você compre e gerencie seus domínios." },
            { question: "Para que serve o AWS Organizations?", options: ["Para organizar seus arquivos no S3.", "Para gerenciar centralmente múltiplas contas da AWS e aplicar políticas de governança.", "Para visualizar a organização da sua rede VPC.", "Para organizar sua equipe de desenvolvimento."], answer: 1, explanation: "O AWS Organizations é crucial para a governança em escala. Ele permite o faturamento consolidado e a aplicação de Service Control Policies (SCPs) para restringir as permissões em todas as contas da organização." }
        ];

        function renderQuiz() {
            quizForm.innerHTML = '';
            quizData.forEach((q, index) => {
                const questionBlock = document.createElement('div');
                questionBlock.className = 'question-block';
                questionBlock.id = `q${index}`;
                const questionText = document.createElement('p');
                questionText.className = 'question-text';
                questionText.textContent = `${index + 1}. ${q.question}`;
                questionBlock.appendChild(questionText);
                const optionsList = document.createElement('ul');
                optionsList.className = 'options';
                q.options.forEach((option, optionIndex) => {
                    const listItem = document.createElement('li');
                    const label = document.createElement('label');
                    const radio = document.createElement('input');
                    radio.type = 'radio';
                    radio.name = `q${index}`;
                    radio.value = optionIndex;
                    label.appendChild(radio);
                    label.appendChild(document.createTextNode(' ' + option));
                    listItem.appendChild(label);
                    optionsList.appendChild(listItem);
                });
                questionBlock.appendChild(optionsList);
                const explanation = document.createElement('div');
                explanation.className = 'explanation';
                explanation.innerHTML = `<strong>Resposta e Explicação:</strong> ${q.explanation}`;
                questionBlock.appendChild(explanation);
                quizForm.appendChild(questionBlock);
            });
        }

        submitBtn.addEventListener('click', () => {
            let score = 0;
            quizData.forEach((q, index) => {
                const selectedOption = quizForm.querySelector(`input[name="q${index}"]:checked`);
                const questionBlock = document.getElementById(`q${index}`);
                const listItems = questionBlock.querySelectorAll('.options li');
                listItems.forEach(li => li.classList.remove('correct', 'incorrect'));
                questionBlock.querySelector('.explanation').style.display = 'none';

                if (selectedOption) {
                    const userAnswer = parseInt(selectedOption.value, 10);
                    const correctLi = listItems[q.answer];
                    const userLi = selectedOption.parentElement.parentElement;
                    if (userAnswer === q.answer) {
                        score++;
                        userLi.classList.add('correct');
                    } else {
                        userLi.classList.add('incorrect');
                        correctLi.classList.add('correct');
                    }
                } else {
                    const correctLi = listItems[q.answer];
                    correctLi.classList.add('correct');
                }
                questionBlock.querySelector('.explanation').style.display = 'block';
            });

            const percentage = Math.round((score / quizData.length) * 100);
            resultsContainer.innerHTML = `Sua pontuação final: ${score} de ${quizData.length} (${percentage}%)`;
            resultsContainer.classList.remove('success', 'fail');
            if (percentage >= 70) {
                resultsContainer.classList.add('success');
            } else {
                resultsContainer.classList.add('fail');
            }
            submitBtn.style.display = 'none';
            redoBtn.style.display = 'inline-block';
            quizContainer.scrollIntoView({ behavior: 'smooth' });
        });

        redoBtn.addEventListener('click', () => {
            resultsContainer.innerHTML = '';
            resultsContainer.classList.remove('success', 'fail');
            submitBtn.style.display = 'inline-block';
            redoBtn.style.display = 'none';
            renderQuiz();
            quizContainer.scrollIntoView({ behavior: 'smooth' });
        });

        renderQuiz();
    })();
</script>