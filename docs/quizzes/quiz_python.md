<div class="quiz-container" id="quiz-python-container">
    <h3><img src="https://api.iconify.design/mdi/language-python.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Quiz: Python para Nuvem e Automação</h3>
    <form class="quiz-form">
        </form>
    <button class="submit-quiz-btn">Verificar Respostas</button>
    <button class="redo-quiz-btn" style="display:none; margin-left: 1rem;">Refazer Quiz</button>
    <div class="quiz-results"></div>
</div>

<script>
    (function() {
        const quizContainer = document.getElementById('quiz-python-container');
        if (!quizContainer) return;

        const quizForm = quizContainer.querySelector('.quiz-form');
        const submitBtn = quizContainer.querySelector('.submit-quiz-btn');
        const redoBtn = quizContainer.querySelector('.redo-quiz-btn');
        const resultsContainer = quizContainer.querySelector('.quiz-results');

        const quizData = [
            {
                question: "Qual é a principal finalidade de usar uma função em Python?",
                options: ["Para armazenar um único valor.", "Para criar um loop que se repete indefinidamente.", "Para agrupar um bloco de código reutilizável que executa uma tarefa específica.", "Para garantir que o código seja executado em ordem alfabética."],
                answer: 2,
                explanation: "Funções são a base do princípio DRY (Don't Repeat Yourself). Elas permitem que você escreva um bloco de código uma vez e o chame quantas vezes forem necessárias, tornando o código mais limpo e fácil de manter."
            },
            {
                question: "Qual estrutura de dados em Python é uma coleção não ordenada de pares chave-valor?",
                options: ["Lista (List)", "Tupla (Tuple)", "Dicionário (Dictionary)", "Conjunto (Set)"],
                answer: 2,
                explanation: "Um dicionário é como uma 'agenda de contatos', onde você acessa um valor (o número de telefone) através de sua chave única (o nome do contato), e a ordem não importa."
            },
            {
                question: "Um desenvolvedor precisa ler um arquivo de configuração `settings.conf`. Qual é a forma mais segura e recomendada de abrir o arquivo em Python?",
                options: ["file = open('settings.conf')", "read('settings.conf')", "with open('settings.conf', 'r') as file:", "import settings.conf"],
                answer: 2,
                explanation: "Usar a declaração `with` garante que o arquivo seja fechado automaticamente, mesmo que ocorram erros. É a prática moderna para manipulação de arquivos."
            },
            {
                question: "Qual biblioteca (SDK) é o padrão da indústria para interagir com os serviços da AWS usando Python?",
                options: ["Requests", "Pandas", "Boto3", "AWS SDK for Java"],
                answer: 2,
                explanation: "Boto3 é o Kit de Desenvolvimento de Software (SDK) oficial da AWS para Python, fornecendo uma API para interagir com serviços como EC2, S3, IAM, etc."
            },
            {
                question: "O que o seguinte código Python fará: `numeros = [10, 20, 30]; print(numeros[1])`?",
                options: ["Imprimirá a lista inteira.", "Imprimirá o primeiro item da lista (10).", "Imprimirá o segundo item da lista (20).", "Gerará um erro de índice."],
                answer: 2,
                explanation: "Em Python, a indexação de listas começa em 0. Portanto, o índice `[0]` é o primeiro item, e o índice `[1]` é o segundo."
            },
            {
                question: "Qual é a principal vantagem de usar `subprocess.run()` em vez de `os.system()` para executar comandos do sistema?",
                options: ["É mais curto de digitar.", "É mais seguro contra ataques de Injeção de Comando.", "Funciona em mais sistemas operacionais.", "É a única forma de executar comandos com `sudo`."],
                answer: 1,
                explanation: "`subprocess.run()` trata os argumentos como uma lista de dados, e não como uma string de texto a ser interpretada pelo shell, o que previne que um atacante injete comandos maliciosos."
            },
            {
                question: "O que o loop `for` em Python faz?",
                options: ["Executa um bloco de código enquanto uma condição for verdadeira.", "Define uma nova função.", "Itera sobre os itens de uma sequência (como uma lista ou string).", "Para a execução do script."],
                answer: 2,
                explanation: "O loop `for` é projetado para percorrer cada item de uma coleção (uma lista, uma tupla, um dicionário, etc.) e executar um bloco de código para cada item."
            },
            {
                question: "Um script precisa tomar uma decisão com base no valor de uma variável. Qual estrutura de controle de fluxo é usada para isso?",
                options: ["try / except", "for / in", "def / return", "if / elif / else"],
                answer: 3,
                explanation: "A estrutura `if/elif/else` é a base da lógica condicional em Python, permitindo que seu programa execute diferentes caminhos com base em condições que você define."
            },
            {
                question: "Qual é a principal diferença entre os modos de arquivo 'w' e 'a'?",
                options: ["'w' é para ler (read), 'a' é para escrever (write).", "'w' (write) sobrescreve o arquivo, 'a' (append) adiciona ao final.", "'w' só funciona com texto, 'a' só com números.", "'w' cria um arquivo, 'a' não pode criá-lo."],
                answer: 1,
                explanation: "Usar o modo 'w' apagará todo o conteúdo de um arquivo existente antes de escrever. O modo 'a' é mais seguro quando você quer apenas adicionar novas informações a um log, por exemplo."
            },
            {
                question: "Como você transforma uma string de texto em formato JSON em um dicionário Python?",
                options: ["Usando a função `dict()`.", "Usando `json.loads()`.", "Usando `json.dumps()`.", "Usando o operador `+`."],
                answer: 1,
                explanation: "`json.loads()` (load string) pega uma string JSON e a 'carrega' em uma estrutura de dados Python (um dicionário ou lista). `json.dumps()` faz o oposto."
            },
            {
                question: "O que é um 'módulo' em Python?",
                options: ["Um tipo de variável para armazenar números.", "Um arquivo `.py` contendo funções e variáveis que podem ser importadas em outros scripts.", "Um comentário no código.", "O nome de um loop."],
                answer: 1,
                explanation: "Módulos são a forma como o Python organiza o código para reutilização. A biblioteca padrão do Python é uma vasta coleção de módulos."
            },
            {
                question: "Qual das seguintes opções é uma prática recomendada da filosofia DevOps?",
                options: ["Manter as equipes de Desenvolvimento e Operações em silos separados.", "Focar em grandes lançamentos anuais de software.", "Automatizar a construção, o teste e a implantação de software.", "Evitar o monitoramento para melhorar a performance."],
                answer: 2,
                explanation: "A automação é um dos pilares do DevOps (representado pela letra 'A' no acrônimo CALMS). Ela visa eliminar tarefas manuais e repetitivas para aumentar a velocidade e a confiabilidade."
            },
            {
                question: "No contexto de CI/CD, o que significa 'Integração Contínua' (CI)?",
                options: ["Implantar o código em produção automaticamente a cada alteração.", "A prática de desenvolvedores mesclarem seu código ao repositório principal frequentemente.", "Um tipo de teste de segurança.", "A fase de planejamento do projeto."],
                answer: 1,
                explanation: "A CI foca em integrar o trabalho de múltiplos desenvolvedores de forma frequente para detectar problemas de integração o mais cedo possível, geralmente acionando uma construção e testes automatizados."
            },
            {
                question: "Qual serviço da AWS atua como o orquestrador de um pipeline de CI/CD, conectando serviços como CodeCommit e CodeBuild?",
                options: ["AWS CodeDeploy", "AWS CodeStar", "AWS CodePipeline", "AWS CloudFormation"],
                answer: 2,
                explanation: "O AWS CodePipeline modela, visualiza e automatiza as etapas do seu processo de lançamento de software. Ele é a 'esteira rolante' que conecta todas as estações."
            },
            {
                question: "O que é 'Infraestrutura como Código' (IaC)?",
                options: ["Escrever o código da aplicação em uma linguagem de infraestrutura.", "A prática de gerenciar e provisionar infraestrutura através de arquivos de definição legíveis por máquina.", "Um serviço que converte hardware em software.", "O firmware de um roteador."],
                answer: 1,
                explanation: "O IaC trata a sua infraestrutura (VPCs, EC2, etc.) como código, permitindo que ela seja versionada, testada e implantada de forma automatizada e consistente. O AWS CloudFormation é o serviço nativo da AWS para IaC."
            },
            {
                question: "Qual é a principal função de uma docstring (`\"\"\"...\"\"\"`) em uma função Python?",
                options: ["Impedir que a função seja executada.", "Definir o valor de retorno da função.", "Fornecer documentação sobre o que a função faz, seus parâmetros e o que ela retorna.", "Armazenar uma variável de texto longa."],
                answer: 2,
                explanation: "Docstrings são a forma padrão do Python para documentar o código. Ferramentas e IDEs podem extrair essa informação para gerar documentação automaticamente."
            },
            {
                question: "Um script está tentando ler um arquivo que pode não existir. Para evitar que o programa quebre, qual estrutura o desenvolvedor deve usar?",
                options: ["Um loop `for`.", "Uma declaração `if/else`.", "Um bloco `try/except`.", "A função `assert`."],
                answer: 2,
                explanation: "O bloco `try/except` é o mecanismo do Python para tratamento de exceções. Ele permite que você 'capture' um erro (como um `FileNotFoundError`) e execute um 'plano B' em vez de deixar o programa falhar."
            },
            {
                question: "O que o comando `import os` permite que seu script Python faça?",
                options: ["Realizar operações matemáticas complexas.", "Interagir com funcionalidades do sistema operacional, como manipular arquivos e diretórios.", "Fazer requisições HTTP para APIs.", "Analisar grandes volumes de dados."],
                answer: 1,
                explanation: "O módulo `os` é a sua ponte para o sistema operacional, fornecendo funções como `os.getcwd()` (obter diretório atual) e `os.mkdir()` (criar diretório)."
            },
            {
                question: "Qual é a principal diferença entre uma lista e uma tupla em Python?",
                options: ["Listas podem conter números, e tuplas, apenas texto.", "Listas são ordenadas, e tuplas, não.", "Listas são mutáveis (podem ser alteradas), enquanto tuplas são imutáveis (não podem ser alteradas).", "Listas usam `()` e tuplas usam `[]`."],
                answer: 2,
                explanation: "A imutabilidade é a característica chave. Uma vez que você cria uma tupla, não pode adicionar, remover ou alterar seus elementos. Isso as torna úteis para dados que não devem mudar, como as chaves de um dicionário."
            },
            {
                question: "Qual serviço da AWS é ideal para orquestrar a execução de scripts Python em frotas de instâncias EC2 para tarefas como gerenciamento de configuração?",
                options: ["AWS Lambda", "AWS Step Functions", "AWS Systems Manager", "Amazon S3"],
                answer: 2,
                explanation: "O AWS Systems Manager, especialmente com seu recurso 'Run Command', permite que você execute scripts (Python ou Shell) em centenas de instâncias de uma só vez, sendo a ferramenta ideal para automação em escala."
            },
            {
                question: "O que a sigla 'PEP 8' representa no mundo Python?",
                options: ["Uma versão do interpretador Python.", "Um erro de programação comum.", "O guia de estilo oficial para código Python.", "Um tipo de licença de software."],
                answer: 2,
                explanation: "PEP 8 é o documento que estabelece as convenções de como escrever código Python de forma limpa e legível. Ferramentas como `flake8` ajudam a verificar se seu código está em conformidade."
            },
            {
                question: "Qual das seguintes opções é um benefício de usar um Linter (como Pylint) durante o desenvolvimento?",
                options: ["Garante que o programa rodará mais rápido.", "Realiza a implantação automática em produção.", "Analisa o código estaticamente para encontrar erros, bugs e problemas de estilo.", "Criptografa seu código-fonte."],
                answer: 2,
                explanation: "Um linter é uma ferramenta de análise estática. Ele 'lê' seu código sem executá-lo e aponta possíveis problemas, ajudando a melhorar a qualidade antes mesmo dos testes."
            },
            {
                question: "Em um pipeline de CI/CD, onde os testes de unidade (`unittest` ou `pytest`) são tipicamente executados?",
                options: ["No ambiente de produção, após a implantação.", "Na máquina do desenvolvedor, antes de enviar o código.", "Na etapa de 'Build' ou 'Test', automatizada por um serviço como o AWS CodeBuild.", "Manualmente pela equipe de QA, uma vez por semana."],
                answer: 2,
                explanation: "A automação dos testes de unidade é um pilar da Integração Contínua (CI). Eles são executados a cada nova alteração de código para fornecer feedback rápido ao desenvolvedor."
            },
            {
                question: "Como você acessa o valor associado à chave 'cidade' em um dicionário Python chamado `cliente`?",
                options: ["cliente(cidade)", "cliente.cidade", "cliente[cidade]", "cliente['cidade']"],
                answer: 3,
                explanation: "Em Python, você acessa os valores de um dicionário usando a notação de colchetes `[]` e passando a chave (que, neste caso, é uma string) como o índice."
            },
            {
                question: "O que o seguinte código fará: `valor = 10; valor += 5; print(valor)`?",
                options: ["Imprimirá 5.", "Imprimirá 10.", "Imprimirá 15.", "Gerará um erro de sintaxe."],
                answer: 2,
                explanation: "O operador de atribuição `+=` é um atalho para `valor = valor + 5`. Ele pega o valor atual da variável, soma 5 a ele e armazena o novo resultado na mesma variável."
            }
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