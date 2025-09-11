<div class="quiz-container" id="quiz-network-container">
    <h3><img src="https://api.iconify.design/mdi/lan.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Quiz: Redes na AWS</h3>
    <form class="quiz-form">
        </form>
    <button class="submit-quiz-btn">Verificar Respostas</button>
    <button class="redo-quiz-btn" style="display:none; margin-left: 1rem;">Refazer Quiz</button>
    <div class="quiz-results"></div>
</div>

<script>
    (function() {
        const quizContainer = document.getElementById('quiz-network-container');
        if (!quizContainer) return;
        
        const quizForm = quizContainer.querySelector('.quiz-form');
        const submitBtn = quizContainer.querySelector('.submit-quiz-btn');
        const redoBtn = quizContainer.querySelector('.redo-quiz-btn');
        const resultsContainer = quizContainer.querySelector('.quiz-results');
        
        const quizData = [
            {
                question: "Qual componente da Amazon VPC é responsável por permitir a comunicação entre sua VPC e a internet?",
                options: ["NAT Gateway", "Internet Gateway", "Security Group", "Network ACL"],
                answer: 1,
                explanation: "O Internet Gateway (IGW) é um componente altamente disponível que você anexa à sua VPC para permitir a comunicação de entrada e saída com a internet."
            },
            {
                question: "Um administrador precisa garantir que um banco de dados em uma sub-rede privada possa baixar atualizações, mas sem que a internet possa iniciar uma conexão com ele. Qual serviço deve ser utilizado?",
                options: ["Internet Gateway na sub-rede privada.", "Um Security Group com a porta 443 aberta.", "Um NAT Gateway na sub-rede pública.", "AWS Direct Connect."],
                answer: 2,
                explanation: "Um NAT Gateway é colocado em uma sub-rede pública e permite que recursos em sub-redes privadas acessem a internet (tráfego de saída), enquanto bloqueia conexões iniciadas pela internet."
            },
            {
                question: "Qual a principal diferença entre um Security Group (SG) e uma Network ACL (NACL)?",
                options: ["SGs operam no nível da sub-rede, enquanto NACLs operam no nível da instância.", "SGs são stateless, enquanto NACLs são stateful.", "SGs permitem apenas regras de 'Permitir', enquanto NACLs permitem regras de 'Permitir' e 'Negar'.", "SGs são usados apenas para tráfego de entrada, e NACLs apenas para tráfego de saída."],
                answer: 2,
                explanation: "Esta é uma distinção fundamental. Security Groups são stateful e só possuem regras de 'Allow'. Network ACLs são stateless e possuem regras de 'Allow' e 'Deny'."
            },
            {
                question: "Uma empresa quer distribuir o tráfego de seu site entre múltiplas instâncias EC2. Qual serviço é projetado para essa finalidade?",
                options: ["Amazon Route 53", "Amazon CloudFront", "Elastic Load Balancing (ELB)", "AWS Auto Scaling"],
                answer: 2,
                explanation: "O Elastic Load Balancing (ELB) distribui automaticamente o tráfego de entrada entre múltiplos destinos, como instâncias EC2, aumentando a tolerância a falhas."
            },
            {
                question: "O que o CIDR `0.0.0.0/0` representa em uma regra de Security Group?",
                options: ["Apenas o endereço de loopback.", "Todos os endereços IP dentro da VPC.", "Nenhum endereço IP.", "Qualquer endereço IP na internet."],
                answer: 3,
                explanation: "A notação CIDR `0.0.0.0/0` é a forma padrão de representar 'qualquer lugar' na internet. Usá-la em regras de entrada para portas de gerenciamento é uma prática de segurança muito ruim."
            },
            {
                question: "Qual serviço da AWS atua como um DNS (Domain Name System) global?",
                options: ["Amazon VPC", "AWS Direct Connect", "Amazon Route 53", "AWS Certificate Manager"],
                answer: 2,
                explanation: "O Amazon Route 53 é o serviço de DNS da AWS que traduz nomes de domínio para endereços IP e pode ser usado para rotear o tráfego para sua infraestrutura."
            },
            {
                question: "Uma sub-rede é considerada 'pública' quando:",
                options: ["Ela contém instâncias EC2 com Elastic IPs.", "Sua Network ACL permite todo o tráfego.", "Sua tabela de rotas associada tem uma rota para um Internet Gateway.", "Ela está localizada na Zona de Disponibilidade 'a'."],
                answer: 2,
                explanation: "A definição de uma sub-rede pública está ligada ao roteamento. Se sua tabela de rotas envia o tráfego para a internet (0.0.0.0/0) para um Internet Gateway, a sub-rede é pública."
            },
            {
                question: "Qual é a principal vantagem de usar o AWS Direct Connect em vez de uma VPN?",
                options: ["É mais fácil de configurar.", "É uma solução gratuita.", "Oferece criptografia de ponta a ponta por padrão.", "Fornece uma conexão de rede privada, dedicada e mais consistente."],
                answer: 3,
                explanation: "O AWS Direct Connect estabelece uma conexão de fibra óptica privada entre seu data center e a AWS, contornando a internet pública, resultando em maior largura de banda e menor latência."
            },
            {
                question: "Ao criar uma VPC com um bloco CIDR de `10.0.0.0/16`, quantas sub-redes com o CIDR `/24` você pode criar?",
                options: ["16", "64", "256", "1024"],
                answer: 2,
                explanation: "Um CIDR /16 tem 16 bits de rede, e um /24 tem 24. A diferença de 8 bits (24 - 16) significa que você pode criar 2^8 = 256 sub-redes /24 dentro do bloco /16."
            },
            {
                question: "Qual serviço da AWS é uma CDN (Content Delivery Network)?",
                options: ["Elastic Load Balancer", "Amazon S3 Transfer Acceleration", "Amazon CloudFront", "Amazon API Gateway"],
                answer: 2,
                explanation: "O Amazon CloudFront é a CDN da AWS. Ele armazena em cache seu conteúdo em Pontos de Presença (Edge Locations) globais, entregando-o a partir do local mais próximo do seu usuário."
            },
            {
                question: "Qual é a forma mais simples de conectar duas VPCs na mesma Região para que se comuniquem com IPs privados?",
                options: ["Usar um Internet Gateway em ambas.", "Configurar um AWS Direct Connect.", "Criar um VPC Peering.", "Usar o AWS Transit Gateway."],
                answer: 2,
                explanation: "O VPC Peering é uma conexão de rede entre duas VPCs que permite rotear o tráfego entre elas usando IPs privados, como se estivessem na mesma rede."
            },
            {
                question: "Qual protocolo é a melhor escolha para um serviço de streaming de vídeo ao vivo?",
                options: ["TCP", "UDP", "ICMP", "HTTP"],
                answer: 1,
                explanation: "O UDP (User Datagram Protocol) prioriza a velocidade e a baixa latência, tornando-o ideal para aplicações em tempo real como streaming e jogos online."
            },
            {
                question: "Qual é o propósito da Tabela de Rotas (Route Table) em uma VPC?",
                options: ["Atuar como um firewall para instâncias EC2.", "Conter regras que determinam para onde o tráfego de rede é direcionado.", "Traduzir nomes de domínio para endereços IP.", "Armazenar os logs de todo o tráfego de rede."],
                answer: 1,
                explanation: "A Tabela de Rotas funciona como o 'mapa de sinalização' da sua VPC, definindo os caminhos que o tráfego pode seguir."
            },
            {
                question: "Qual das seguintes afirmações sobre um NAT Gateway está CORRETA?",
                options: ["Ele deve ser colocado em uma sub-rede privada.", "Ele permite que a internet inicie conexões com instâncias privadas.", "Ele precisa de um Elastic IP para funcionar.", "Ele opera no nível da instância."],
                answer: 2,
                explanation: "Um NAT Gateway deve ser colocado em uma sub-rede pública e precisa de um Elastic IP (IP público estático) para funcionar. Sua função é permitir que instâncias privadas acessem a internet."
            },
            {
                question: "O que são VPC Flow Logs?",
                options: ["Um serviço para conectar seu data center à AWS.", "Um recurso que captura informações sobre o tráfego IP que entra e sai das interfaces de rede.", "Um tipo de instância EC2 otimizada para rede.", "Um log de todas as chamadas de API feitas na sua VPC."],
                answer: 1,
                explanation: "VPC Flow Logs são essenciais para monitoramento de rede. Eles fornecem metadados detalhados sobre cada fluxo de rede para análise."
            },
            {
                question: "Uma Network ACL (NACL) opera em qual nível da sua infraestrutura VPC?",
                options: ["Região", "Instância", "Interface de Rede Elástica (ENI)", "Sub-rede"],
                answer: 3,
                explanation: "As NACLs atuam como um firewall para o tráfego que entra e sai de uma ou mais sub-redes."
            },
            {
                question: "Qual é o comportamento padrão de um Security Group recém-criado?",
                options: ["Permite todo o tráfego de entrada e de saída.", "Nega todo o tráfego de entrada e de saída.", "Permite todo o tráfego de entrada e nega todo o de saída.", "Nega todo o tráfego de entrada e permite todo o de saída."],
                answer: 3,
                explanation: "Por segurança, um Security Group recém-criado bloqueia todo o tráfego de entrada por padrão, mas permite todo o tráfego de saída."
            },
            {
                question: "No Modelo OSI, em qual camada os roteadores tomam suas decisões?",
                options: ["Camada 1 (Física)", "Camada 2 (Link de Dados)", "Camada 3 (Rede)", "Camada 4 (Transporte)"],
                answer: 2,
                explanation: "A Camada 3 (Rede) é onde o endereçamento lógico (endereços IP) e o roteamento acontecem."
            },
            {
                question: "O que significa dizer que um Security Group é 'stateful'?",
                options: ["Só pode ser usado por instâncias em estado 'running'.", "Ele lembra o estado da conexão. Se você permite a entrada, a resposta de saída é automaticamente permitida.", "Requer que você defina regras separadas para entrada e resposta.", "Só pode ter um número limitado de regras."],
                answer: 1,
                explanation: "A natureza 'stateful' dos Security Groups simplifica a configuração, pois não é preciso criar regras de saída correspondentes para o tráfego de resposta."
            },
            {
                question: "Para simplificar a interconexão de muitas VPCs, qual serviço atua como um hub central?",
                options: ["VPC Peering", "Internet Gateway", "AWS Transit Gateway", "AWS Direct Connect"],
                answer: 2,
                explanation: "Enquanto o VPC Peering é ótimo para poucas VPCs, o AWS Transit Gateway atua como um hub de nuvem, simplificando a conectividade em escala."
            },
            {
                question: "Qual das seguintes afirmações sobre Sub-redes em uma VPC é VERDADEIRA?",
                options: ["Uma sub-rede pode abranger múltiplas Zonas de Disponibilidade.", "Os blocos CIDR de sub-redes na mesma VPC podem se sobrepor.", "Cada sub-rede deve estar associada a uma Tabela de Rotas.", "Uma sub-rede privada não pode ter um Security Group."],
                answer: 2,
                explanation: "Cada sub-rede reside em uma única AZ. Os CIDRs não podem se sobrepor. Todo recurso pode ter um Security Group. A afirmação correta é que cada sub-rede precisa de uma Tabela de Rotas."
            },
            {
                question: "Para se conectar a um servidor Windows em uma EC2, qual porta você normalmente permitiria?",
                options: ["Porta 22 / TCP (SSH)", "Porta 443 / TCP (HTTPS)", "Porta 3389 / TCP (RDP)", "Porta 53 / UDP (DNS)"],
                answer: 2,
                explanation: "O RDP (Remote Desktop Protocol), na porta TCP 3389, é o protocolo padrão da Microsoft para acessar a área de trabalho gráfica de sistemas Windows."
            },
            {
                question: "Qual tipo de ELB é ideal para rotear tráfego com base no caminho da URL (ex: /api/users)?",
                options: ["Classic Load Balancer", "Network Load Balancer", "Application Load Balancer", "Gateway Load Balancer"],
                answer: 2,
                explanation: "O Application Load Balancer (ALB) opera na Camada 7 e pode inspecionar o conteúdo da requisição, como o caminho da URL, para tomar decisões de roteamento inteligentes."
            },
            {
                question: "Qual benefício o Amazon CloudFront oferece como uma CDN?",
                options: ["Aumentar a latência para usuários distantes.", "Reduzir a segurança do conteúdo estático.", "Centralizar a entrega de conteúdo em uma única Região.", "Reduzir a carga nos servidores de origem e melhorar a performance."],
                answer: 3,
                explanation: "Ao armazenar seu conteúdo em cache nos Pontos de Presença (Edge Locations), o CloudFront atende às requisições diretamente da borda, diminuindo a latência e a carga nos seus servidores."
            },
            {
                question: "Qual das seguintes é uma característica de uma Network ACL (NACL), mas NÃO de um Security Group?",
                options: ["É stateful.", "Pode ter regras baseadas em outros Security Groups.", "Possui regras com números de prioridade para avaliação.", "Opera no nível da interface de rede (ENI)."],
                answer: 2,
                explanation: "As regras em uma NACL são avaliadas em ordem, do menor número para o maior. Security Groups não usam números de prioridade; todas as suas regras de 'Allow' são avaliadas."
            }
        ];

        // O resto do script é genérico e não precisa ser colado novamente.
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