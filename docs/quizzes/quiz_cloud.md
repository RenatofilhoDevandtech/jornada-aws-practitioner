<div class="quiz-container" id="quiz-cloud-container">
    <h3><img src="https://api.iconify.design/mdi/cloud-question-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Quiz: Fundamentos da Nuvem AWS</h3>
    <form class="quiz-form">
        </form>
    <button class="submit-quiz-btn">Verificar Respostas</button>
    <button class="redo-quiz-btn" style="display:none; margin-left: 1rem;">Refazer Quiz</button>
    <div class="quiz-results"></div>
</div>

<script>
    (function() {
        const quizContainer = document.getElementById('quiz-cloud-container');
        if (!quizContainer) return;

        const quizForm = quizContainer.querySelector('.quiz-form');
        const submitBtn = quizContainer.querySelector('.submit-quiz-btn');
        const redoBtn = quizContainer.querySelector('.redo-quiz-btn');
        const resultsContainer = quizContainer.querySelector('.quiz-results');

        const quizData = [
            {
                question: "Qual das seguintes opções é uma das seis vantagens da computação em nuvem da AWS?",
                options: ["Aumentar as despesas de capital (CapEx).", "Adivinhar a capacidade de infraestrutura.", "Trocar despesas de capital por despesas variáveis (OpEx).", "Implementação lenta de recursos."],
                answer: 2,
                explanation: "Uma das principais vantagens da nuvem é trocar o grande investimento inicial em hardware (CapEx) por um modelo de pagamento sob demanda (OpEx), onde você paga apenas pelo que usa."
            },
            {
                question: "No Modelo de Responsabilidade Compartilhada, qual das seguintes é uma responsabilidade da AWS?",
                options: ["Configurar as regras do Security Group.", "Criptografar os dados armazenados em um bucket S3.", "Gerenciar as permissões dos usuários IAM.", "Garantir a segurança física dos data centers."],
                answer: 3,
                explanation: "A AWS é responsável pela segurança *DA* nuvem, o que inclui o hardware, a infraestrutura global e a segurança física das instalações onde os serviços rodam."
            },
            {
                question: "Uma empresa precisa de servidores virtuais na nuvem para hospedar sua aplicação. Qual serviço da AWS ela deve usar?",
                options: ["Amazon S3", "AWS Lambda", "Amazon EC2", "Amazon RDS"],
                answer: 2,
                explanation: "O Amazon EC2 (Elastic Compute Cloud) é o serviço fundamental que fornece capacidade de computação segura e redimensionável na nuvem, permitindo que você provisione servidores virtuais (instâncias)."
            },
            {
                question: "Qual serviço da AWS é projetado para armazenamento de objetos e é ideal para guardar arquivos como imagens, vídeos e backups?",
                options: ["Amazon EBS", "Amazon EFS", "Amazon S3", "Amazon Glacier"],
                answer: 2,
                explanation: "O Amazon S3 (Simple Storage Service) é o serviço de armazenamento de objetos da AWS, conhecido por sua escalabilidade, durabilidade e baixo custo."
            },
            {
                question: "O que é uma Região da AWS?",
                options: ["Um único data center.", "Um local físico no mundo onde a AWS possui múltiplos data centers isolados.", "Um ponto de presença para entrega de conteúdo em cache.", "Uma rede virtual privada para um cliente."],
                answer: 1,
                explanation: "Uma Região é uma área geográfica, como São Paulo ou Norte da Virgínia. Cada Região é composta por múltiplas Zonas de Disponibilidade (AZs), que são data centers isolados."
            },
            {
                question: "Para obter alta disponibilidade e tolerância a falhas, um arquiteto deve projetar sua aplicação para rodar em:",
                options: ["Múltiplas instâncias na mesma Zona de Disponibilidade.", "Múltiplas Zonas de Disponibilidade.", "Múltiplas contas da AWS.", "Um único servidor de grande porte."],
                answer: 1,
                explanation: "As Zonas de Disponibilidade (AZs) são projetadas para serem independentes umas das outras. Distribuir sua aplicação entre múltiplas AZs garante que ela continue funcionando mesmo que um data center inteiro falhe."
            },
            {
                question: "Qual modelo de computação em nuvem remove a necessidade de gerenciar o sistema operacional e a plataforma, permitindo que o desenvolvedor foque apenas no código da aplicação?",
                options: ["IaaS (Infraestrutura como Serviço)", "PaaS (Plataforma como Serviço)", "SaaS (Software como Serviço)", "On-premises"],
                answer: 1,
                explanation: "Na PaaS, o provedor de nuvem gerencia o hardware, o sistema operacional e o ambiente de execução (como Java ou Python). O cliente apenas implanta e gerencia sua aplicação. O AWS Elastic Beanstalk é um exemplo."
            },
            {
                question: "Qual serviço da AWS é usado para criar uma rede virtual privada e isolada na nuvem?",
                options: ["Amazon CloudFront", "Amazon VPC", "Amazon Route 53", "AWS Direct Connect"],
                answer: 1,
                explanation: "O Amazon VPC (Virtual Private Cloud) é a sua fortaleza de rede na nuvem, permitindo que você defina seu próprio espaço de IP, sub-redes, tabelas de rotas e gateways."
            },
            {
                question: "Qual serviço da AWS é um banco de dados NoSQL totalmente gerenciado que oferece performance de milissegundos em qualquer escala?",
                options: ["Amazon RDS", "Amazon Aurora", "Amazon DynamoDB", "Amazon Redshift"],
                answer: 2,
                explanation: "O Amazon DynamoDB é o principal serviço NoSQL da AWS, ideal para aplicações que precisam de alta performance e escalabilidade, como games, e-commerce e IoT."
            },
            {
                question: "O princípio de 'pagar conforme o uso' (pay-as-you-go) é um exemplo de qual vantagem da nuvem AWS?",
                options: ["Agilidade", "Elasticidade", "Economia de custos", "Alcance global"],
                answer: 2,
                explanation: "O modelo de pagamento sob demanda elimina a necessidade de grandes investimentos iniciais em hardware, permitindo que as empresas paguem apenas pelos recursos que efetivamente consomem, o que leva a uma significativa economia de custos."
            },
            {
                question: "Qual serviço da AWS atua como uma CDN (Rede de Distribuição de Conteúdo) global?",
                options: ["Amazon S3", "Elastic Load Balancing", "Amazon CloudFront", "Amazon EC2"],
                answer: 2,
                explanation: "O Amazon CloudFront distribui seu conteúdo (vídeos, imagens, APIs) através de uma rede global de Pontos de Presença (Edge Locations), entregando-o aos usuários com baixa latência."
            },
            {
                question: "Qual serviço você usaria para gerenciar centralmente o acesso de usuários e permissões aos recursos da AWS?",
                options: ["AWS Organizations", "AWS IAM", "Amazon Cognito", "AWS Secrets Manager"],
                answer: 1,
                explanation: "O AWS IAM (Identity and Access Management) é o serviço fundamental para gerenciar quem pode fazer o quê na sua conta AWS, através de usuários, grupos, roles e políticas."
            },
            {
                question: "O que é escalabilidade horizontal (scaling out)?",
                options: ["Aumentar a potência (CPU/RAM) de uma única instância.", "Adicionar mais instâncias para distribuir a carga.", "Fazer backup de uma instância para outra Região.", "Reduzir o tamanho de uma instância para economizar."],
                answer: 1,
                explanation: "A escalabilidade horizontal adiciona mais 'trabalhadores' (instâncias) à frota, distribuindo o trabalho. É o oposto da escalabilidade vertical, que torna um único trabalhador mais forte."
            },
            {
                question: "Qual dos pilares do AWS Well-Architected Framework foca em garantir que os sistemas possam se recuperar de falhas e mitigar interrupções?",
                options: ["Excelência Operacional", "Segurança", "Confiabilidade (Reliability)", "Otimização de Custos"],
                answer: 2,
                explanation: "O pilar de Confiabilidade (ou Resiliência) cobre a capacidade de um sistema se recuperar de falhas de infraestrutura ou serviço, além de adquirir dinamicamente recursos para atender à demanda."
            },
            {
                question: "Qual serviço da AWS oferece um consultor automatizado que inspeciona seu ambiente e fornece recomendações de melhores práticas?",
                options: ["AWS Config", "Amazon Inspector", "AWS Trusted Advisor", "Amazon GuardDuty"],
                answer: 2,
                explanation: "O AWS Trusted Advisor analisa sua conta em cinco pilares (Custo, Performance, Segurança, Tolerância a Falhas, Limites de Serviço) e oferece recomendações para otimizar seu ambiente."
            },
            {
                question: "Qual modelo de implantação de nuvem combina infraestrutura local (on-premises) com a nuvem da AWS?",
                options: ["Nuvem Pública", "Nuvem Privada", "Nuvem Híbrida", "Nuvem Comunitária"],
                answer: 2,
                explanation: "Uma nuvem híbrida permite que dados e aplicações se movam entre um data center privado e uma nuvem pública, oferecendo maior flexibilidade e mais opções de implantação."
            },
            {
                question: "Qual serviço da AWS é um banco de dados relacional gerenciado?",
                options: ["Amazon DynamoDB", "Amazon S3", "Amazon EC2", "Amazon RDS"],
                answer: 3,
                explanation: "O Amazon RDS (Relational Database Service) facilita a configuração, operação e escalabilidade de bancos de dados relacionais na nuvem, suportando motores como MySQL, PostgreSQL, etc."
            },
            {
                question: "O que é o AWS Marketplace?",
                options: ["Um serviço para comprar nomes de domínio.", "Um fórum comunitário para usuários da AWS.", "Um catálogo digital de software de terceiros que rodam na AWS.", "Um serviço de monitoramento de custos."],
                answer: 2,
                explanation: "O AWS Marketplace é uma loja online onde você pode encontrar, comprar e implantar software de fornecedores independentes que já estão pré-configurados para rodar na AWS."
            },
            {
                question: "Qual é a principal função de um Elastic Load Balancer (ELB)?",
                options: ["Armazenar dados de forma durável.", "Distribuir o tráfego de entrada entre múltiplas instâncias EC2.", "Executar código serverless.", "Proteger contra ataques de negação de serviço."],
                answer: 1,
                explanation: "O ELB atua como um 'sinaleiro', distribuindo as requisições para um conjunto de servidores saudáveis, o que aumenta a disponibilidade e a tolerância a falhas da sua aplicação."
            },
            {
                question: "O que o serviço AWS Auto Scaling permite que você faça?",
                options: ["Aumentar manualmente o tamanho de uma instância.", "Ajustar automaticamente o número de instâncias EC2 para atender à demanda.", "Fazer backup automático de instâncias.", "Criptografar o tráfego de rede."],
                answer: 1,
                explanation: "O Auto Scaling monitora suas aplicações e ajusta automaticamente a capacidade (adicionando ou removendo instâncias EC2) para manter uma performance estável e previsível com o menor custo possível."
            },
            {
                question: "Qual serviço da AWS você usaria para auditar todas as chamadas de API feitas na sua conta?",
                options: ["Amazon CloudWatch", "AWS IAM", "AWS CloudTrail", "AWS Config"],
                answer: 2,
                explanation: "O AWS CloudTrail grava um histórico de todas as chamadas de API, fornecendo uma trilha de auditoria completa de quem fez o quê, quando e de onde na sua conta AWS."
            },
            {
                question: "Qual das seguintes opções NÃO é uma das cinco fases do Ciclo de Vida da Adoção da Nuvem?",
                options: ["Visão", "Fundação", "Migração", "Aquisição de Hardware"],
                answer: 3,
                explanation: "O Cloud Adoption Framework (CAF) descreve as fases de Visão, Fundação, Migração e Reinvenção. A aquisição de hardware é um conceito de data center tradicional, não da nuvem."
            },
            {
                question: "Qual serviço da AWS é usado para criar uma conexão de rede privada e dedicada entre seu data center e a AWS?",
                options: ["AWS VPN", "Amazon VPC", "AWS Direct Connect", "Internet Gateway"],
                answer: 2,
                explanation: "O AWS Direct Connect estabelece uma conexão de rede privada que contorna a internet pública, oferecendo maior largura de banda e uma experiência de rede mais consistente."
            },
            {
                question: "O que o Amazon S3 Glacier é projetado para fazer?",
                options: ["Hospedar sites estáticos de alta performance.", "Servir como um banco de dados de baixa latência.", "Armazenamento de longo prazo e arquivamento de dados a um custo extremamente baixo.", "Executar aplicações de contêineres."],
                answer: 2,
                explanation: "O S3 Glacier e o S3 Glacier Deep Archive são classes de armazenamento otimizadas para arquivamento de dados, onde os dados são acessados raramente e um tempo de recuperação de minutos ou horas é aceitável."
            },
            {
                question: "Qual plano de suporte da AWS oferece acesso a um Technical Account Manager (TAM) dedicado?",
                options: ["Basic", "Developer", "Business", "Enterprise"],
                answer: 3,
                explanation: "O suporte Enterprise é o nível mais alto, projetado para clientes de missão crítica, e inclui um TAM como um recurso proativo para ajudar a otimizar a arquitetura e as operações."
            }
        ];

        // O resto do script é genérico e não precisa ser colado novamente.
        // Apenas a função auto-invocável precisa ter o ID do container correto.
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