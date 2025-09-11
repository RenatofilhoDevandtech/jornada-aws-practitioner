<div class="quiz-container">
    <h3><img src="https://api.iconify.design/mdi/shield-lock-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Quiz: Segurança na Nuvem AWS</h3>
    <form id="security-quiz">
        </form>
    <button id="submit-quiz-btn">Verificar Respostas</button>
    <button id="redo-quiz-btn" style="display:none; margin-left: 1rem;">Refazer Quiz</button>
    <div id="quiz-results"></div>
</div>

<script>
    const quizData = [
        {
            question: "Um ataque de Negação de Serviço Distribuída (DDoS) visa comprometer qual pilar da Tríade CIA?",
            options: [
                "Confidencialidade",
                "Integridade",
                "Disponibilidade",
                "Autenticação"
            ],
            answer: 2,
            explanation: "Um ataque DDoS sobrecarrega um sistema com tráfego para torná-lo inacessível a usuários legítimos, impactando diretamente a **Disponibilidade** do serviço."
        },
        {
            question: "Qual é a prática de segurança mais importante e recomendada pela AWS para a conta raiz (root)?",
            options: [
                "Compartilhar as credenciais com a equipe de administradores.",
                "Criar chaves de acesso para o usuário root e usá-las em scripts.",
                "Ativar a Autenticação Multi-Fator (MFA).",
                "Usar o usuário root para todas as tarefas administrativas diárias."
            ],
            answer: 2,
            explanation: "A AWS recomenda enfaticamente a ativação do MFA na conta raiz como a medida de segurança mais crítica para proteger sua conta contra acesso não autorizado."
        },
        {
            question: "Uma empresa precisa de um relatório de auditoria detalhado sobre quem criou uma instância EC2 específica, quando e a partir de qual endereço IP. Qual serviço da AWS fornece essa informação?",
            options: [
                "Amazon CloudWatch",
                "AWS Config",
                "AWS CloudTrail",
                "AWS Trusted Advisor"
            ],
            answer: 2,
            explanation: "O AWS CloudTrail é o serviço de auditoria que grava um histórico de todas as chamadas de API feitas na sua conta, respondendo exatamente às perguntas 'quem, o quê, quando e de onde'."
        },
        {
            question: "Qual serviço da AWS atua como um firewall no nível da instância para controlar o tráfego de entrada e saída?",
            options: [
                "Network ACL (NACL)",
                "AWS WAF",
                "Security Group",
                "Internet Gateway"
            ],
            answer: 2,
            explanation: "Os Security Groups funcionam como um firewall virtual para suas instâncias EC2, controlando o tráfego com base em portas, protocolos e origens/destinos. Eles são stateful."
        },
        {
            question: "Qual serviço da AWS usa machine learning para detectar atividades maliciosas ou anômalas na sua conta, como uma instância EC2 se comunicando com um servidor de mineração de criptomoedas?",
            options: [
                "Amazon Inspector",
                "Amazon Macie",
                "Amazon GuardDuty",
                "AWS Shield"
            ],
            answer: 2,
            explanation: "O Amazon GuardDuty é um serviço de detecção de ameaças inteligente que analisa continuamente os logs (CloudTrail, VPC Flow Logs, DNS logs) para identificar atividades suspeitas e maliciosas."
        },
        {
            question: "De acordo com o Modelo de Responsabilidade Compartilhada, qual das seguintes opções é uma responsabilidade do CLIENTE?",
            options: [
                "A segurança física dos data centers.",
                "A configuração dos Security Groups.",
                "O patching do hypervisor de virtualização.",
                "A redundância da infraestrutura de rede global."
            ],
            answer: 1,
            explanation: "A AWS é responsável pela segurança *DA* nuvem. O cliente é responsável pela segurança *NA* nuvem, o que inclui a configuração de seus próprios controles, como firewalls (Security Groups), permissões (IAM) e a criptografia de seus dados."
        },
        {
            question: "Um desenvolvedor precisa de permissões temporárias para acessar um bucket S3 a partir de uma instância EC2. Qual é a forma mais segura de conceder esse acesso?",
            options: [
                "Salvar as chaves de acesso do desenvolvedor em um arquivo de texto na instância EC2.",
                "Criar uma IAM Role com as permissões necessárias e anexá-la à instância EC2.",
                "Abrir o bucket S3 para acesso público.",
                "Usar as credenciais do usuário root na aplicação."
            ],
            answer: 1,
            explanation: "As IAM Roles são o mecanismo seguro para conceder permissões a serviços da AWS. Elas fornecem credenciais temporárias e automáticas para a instância, eliminando a necessidade de armazenar chaves de acesso de longo prazo no código."
        },
        {
            question: "Qual serviço da AWS você usaria para obter os relatórios de conformidade da AWS, como os relatórios SOC 2 e ISO 27001?",
            options: [
                "AWS Trusted Advisor",
                "AWS Artifact",
                "AWS Config",
                "AWS Security Hub"
            ],
            answer: 1,
            explanation: "O AWS Artifact é um portal de autoatendimento que fornece acesso sob demanda aos relatórios de conformidade e segurança da AWS. É a ferramenta para provar a conformidade da infraestrutura da AWS para seus auditores."
        },
        {
            question: "Um ataque de injeção de SQL (SQL Injection) em uma aplicação web é melhor mitigado por qual serviço da AWS?",
            options: [
                "Security Group",
                "AWS Shield",
                "AWS WAF (Web Application Firewall)",
                "Network ACL"
            ],
            answer: 2,
            explanation: "O AWS WAF opera na Camada 7 (Aplicação) e é projetado para inspecionar o tráfego HTTP/S, permitindo que você crie regras para bloquear padrões de ataques web comuns, como SQL Injection e Cross-Site Scripting (XSS)."
        },
        {
            question: "Qual é a principal diferença entre criptografia de dados em repouso (at-rest) e em trânsito (in-transit)?",
            options: [
                "Criptografia em repouso usa chaves assimétricas, e em trânsito, chaves simétricas.",
                "Criptografia em repouso protege dados armazenados em disco (S3, EBS), enquanto a em trânsito protege dados enquanto viajam pela rede (HTTPS).",
                "Apenas a criptografia em repouso é gerenciada pelo AWS KMS.",
                "A criptografia em trânsito é mais lenta que a em repouso."
            ],
            answer: 1,
            explanation: "São dois estados diferentes dos dados que exigem proteção. 'Em repouso' refere-se aos dados armazenados. 'Em trânsito' refere-se aos dados enquanto estão sendo transferidos entre sistemas."
        },
        {
            question: "Uma empresa precisa escanear suas instâncias EC2 em busca de vulnerabilidades de software conhecidas (CVEs). Qual serviço da AWS automatiza essa tarefa?",
            options: [
                "Amazon GuardDuty",
                "Amazon Inspector",
                "AWS Config",
                "AWS Systems Manager"
            ],
            answer: 1,
            explanation: "O Amazon Inspector é o serviço de gerenciamento de vulnerabilidades que escaneia continuamente suas cargas de trabalho na AWS em busca de vulnerabilidades de software e exposição de rede não intencional."
        },
        {
            question: "Um usuário IAM pertence a um grupo que tem uma política `Allow s3:*`. No entanto, uma política diretamente anexada ao usuário contém uma instrução `Deny s3:DeleteBucket`. O que acontece quando o usuário tenta deletar um bucket?",
            options: [
                "A ação é permitida porque a política do grupo é mais ampla.",
                "A ação é negada porque a política anexada ao usuário tem prioridade.",
                "A ação resulta em um erro de permissões conflitantes.",
                "A ação é negada porque uma negação explícita sempre se sobrepõe a qualquer permissão."
            ],
            answer: 3,
            explanation: "Esta é a regra de ouro da lógica de avaliação do IAM. Uma instrução de `Deny` explícita em qualquer política aplicável sempre terá precedência sobre qualquer instrução de `Allow`."
        },
        {
            question: "O que o AWS Shield Standard oferece a todos os clientes da AWS sem custo adicional?",
            options: [
                "Acesso à Equipe de Resposta a Incidentes (DRT) da AWS.",
                "Proteção contra ataques de injeção de SQL.",
                "Um Technical Account Manager (TAM).",
                "Proteção contra os ataques de Negação de Serviço Distribuída (DDoS) mais comuns."
            ],
            answer: 3,
            explanation: "O AWS Shield Standard é ativado automaticamente para todos os clientes e fornece proteção contra ataques DDoS de infraestrutura (camadas 3 e 4) mais frequentes, sem custo adicional."
        },
        {
            question: "Em qual fase do Ciclo de Vida da Segurança a atividade de 'restaurar um banco de dados a partir de um backup após um ataque de ransomware' se encaixa?",
            options: [
                "Prevenção",
                "Detecção",
                "Resposta e Recuperação",
                "Análise"
            ],
            answer: 2,
            explanation: "A restauração de sistemas e dados para um estado funcional após a contenção de um incidente é uma parte crucial da fase de Resposta e Recuperação."
        },
        {
            question: "O que o serviço Amazon Macie faz?",
            options: [
                "Gerencia chaves de criptografia.",
                "Usa machine learning para descobrir, classificar e proteger dados sensíveis (como PII) no Amazon S3.",
                "Fornece um desktop virtual seguro na nuvem.",
                "Aplica patches de segurança em instâncias EC2."
            ],
            answer: 1,
            explanation: "O Macie é um serviço de segurança e privacidade de dados que ajuda a prevenir o vazamento de dados sensíveis, como informações de identificação pessoal (PII) e propriedade intelectual, armazenados no S3."
        },
        {
            question: "Qual das seguintes opções é um exemplo de controle de segurança **preventivo** na AWS?",
            options: [
                "Um alarme do CloudWatch que notifica sobre alta utilização de CPU.",
                "Um log do CloudTrail registrando uma ação de login.",
                "Uma política do IAM que nega o acesso a um bucket S3.",
                "Um relatório do Amazon Inspector mostrando vulnerabilidades."
            ],
            answer: 2,
            explanation: "Controles preventivos visam impedir que um incidente aconteça. Uma política do IAM que nega o acesso impede ativamente a ação. Os outros são exemplos de controles detectivos."
        },
        {
            question: "Uma empresa quer que seus desenvolvedores usem o mesmo login e senha corporativos para acessar o Console da AWS. Qual tecnologia do IAM permite isso?",
            options: [
                "Políticas de Senha do IAM",
                "Autenticação Multi-Fator (MFA)",
                "Chaves de Acesso",
                "Federação de Identidade (com SAML ou OpenID Connect)"
            ],
            answer: 3,
            explanation: "A Federação de Identidade permite que você estabeleça uma relação de confiança entre seu provedor de identidade corporativo (como o Active Directory) e a AWS, permitindo que seus usuários façam login na AWS com suas credenciais existentes (Single Sign-On)."
        },
        {
            question: "O que o serviço AWS Key Management Service (KMS) gerencia primariamente?",
            options: [
                "As senhas dos usuários IAM.",
                "As chaves de criptografia usadas para proteger seus dados em outros serviços da AWS.",
                "Os certificados SSL/TLS para seus sites.",
                "Os pares de chaves para acesso SSH a instâncias EC2."
            ],
            answer: 1,
            explanation: "O KMS é um serviço gerenciado que facilita a criação e o controle das chaves de criptografia usadas para proteger seus dados em repouso em serviços como S3, EBS e RDS."
        },
        {
            question: "O que é 'defesa em profundidade' no contexto de segurança da nuvem?",
            options: [
                "Usar apenas um controle de segurança, mas que seja muito forte.",
                "Focar a segurança apenas no nível da rede.",
                "Aplicar múltiplas camadas de controles de segurança independentes para proteger seus ativos.",
                "Criptografar os dados várias vezes com a mesma chave."
            ],
            answer: 2,
            explanation: "A defesa em profundidade é uma estratégia fundamental que assume que qualquer controle pode falhar. Por isso, você implementa múltiplos controles em diferentes camadas (borda da rede, VPC, sub-rede, instância, aplicação, dados) para fornecer resiliência."
        },
        {
            question: "Qual serviço da AWS te dá recomendações de melhores práticas em 5 pilares, incluindo Segurança e Otimização de Custos?",
            options: [
                "AWS Config",
                "AWS CloudTrail",
                "Amazon GuardDuty",
                "AWS Trusted Advisor"
            ],
            answer: 3,
            explanation: "O AWS Trusted Advisor atua como seu consultor em nuvem automatizado, inspecionando seu ambiente e fornecendo recomendações para melhorar a segurança, a tolerância a falhas, a performance e otimizar os custos."
        },
        {
            question: "Qual das seguintes afirmações sobre Network ACLs (NACLs) está CORRETA?",
            options: [
                "Elas são stateful.",
                "Elas operam no nível da instância.",
                "As regras são avaliadas em ordem, do menor número para o maior.",
                "Por padrão, uma NACL customizada permite todo o tráfego."
            ],
            answer: 2,
            explanation: "As regras em uma NACL são numeradas e a primeira regra que corresponde ao tráfego é aplicada. Elas são stateless e operam no nível da sub-rede. NACLs customizadas, por padrão, negam todo o tráfego."
        },
        {
            question: "Qual serviço da AWS você usaria para provisionar certificados SSL/TLS para seu Application Load Balancer?",
            options: [
                "AWS Secrets Manager",
                "AWS Key Management Service (KMS)",
                "AWS Certificate Manager (ACM)",
                "AWS IAM"
            ],
            answer: 2,
            explanation: "O ACM é o serviço para provisionar, gerenciar e implantar certificados SSL/TLS públicos e privados. Sua grande vantagem é a integração com outros serviços da AWS e a renovação automática de certificados públicos."
        },
        {
            question: "Um ataque que engana um usuário para que ele clique em um link malicioso em um e-mail é um exemplo de:",
            options: [
                "Negação de Serviço (DoS)",
                "Man-in-the-Middle",
                "Força Bruta",
                "Phishing"
            ],
            answer: 3,
            explanation: "Phishing é um tipo de ataque de engenharia social que usa e-mails ou mensagens fraudulentas para enganar as vítimas e fazê-las revelar informações sensíveis ou instalar malware."
        },
        {
            question: "O que o serviço AWS Config permite que você faça?",
            options: [
                "Executar scripts de automação em suas instâncias EC2.",
                "Auditar e avaliar continuamente as configurações dos seus recursos da AWS para garantir a conformidade.",
                "Receber um único painel com todos os alertas de segurança da sua conta.",
                "Proteger suas aplicações contra DDoS."
            ],
            answer: 1,
            explanation: "O AWS Config é o seu 'fiscal de obras'. Ele grava o histórico de configuração dos seus recursos e usa regras para avaliar se essas configurações estão em conformidade com suas políticas de segurança e governança."
        },
        {
            question: "A melhor maneira de proteger dados em repouso em um bucket S3 é:",
            options: [
                "Usar uma Network ACL para restringir o acesso.",
                "Manter o bucket em uma sub-rede privada.",
                "Habilitar a Criptografia do Lado do Servidor (SSE), por exemplo, com chaves gerenciadas pelo KMS.",
                "Habilitar o Versionamento de Objetos."
            ],
            answer: 2,
            explanation: "A criptografia em repouso (SSE) é o controle de segurança que protege a confidencialidade dos dados, tornando-os ilegíveis para qualquer pessoa que não tenha as permissões de decriptografia, mesmo que consigam acessar o arquivo."
        }
    ];

    document.addEventListener('DOMContentLoaded', () => {
        const quizContainer = document.getElementById('security-quiz');
        if (!quizContainer) return;

        const submitBtn = document.getElementById('submit-quiz-btn');
        const redoBtn = document.getElementById('redo-quiz-btn');
        const resultsContainer = document.getElementById('quiz-results');
        const quizForm = document.getElementById('security-quiz');

        function renderQuiz() {
            quizForm.innerHTML = ''; // Limpa o quiz anterior
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
                const selectedOption = document.querySelector(`input[name="q${index}"]:checked`);
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
            window.scrollTo({ top: 0, behavior: 'smooth' });
        });

        redoBtn.addEventListener('click', () => {
            resultsContainer.innerHTML = '';
            resultsContainer.classList.remove('success', 'fail');
            submitBtn.style.display = 'inline-block';
            redoBtn.style.display = 'none';
            renderQuiz();
        });

        // Renderiza o quiz pela primeira vez
        renderQuiz();
    });
</script>