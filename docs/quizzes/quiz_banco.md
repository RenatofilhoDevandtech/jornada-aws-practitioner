<div class="quiz-container" id="quiz-db-container">
    <h3><img src="https://api.iconify.design/mdi/database-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Quiz: Bancos de Dados na AWS</h3>
    <form class="quiz-form">
        </form>
    <button class="submit-quiz-btn">Verificar Respostas</button>
    <button class="redo-quiz-btn" style="display:none; margin-left: 1rem;">Refazer Quiz</button>
    <div class="quiz-results"></div>
</div>

<script>
    (function() {
        const quizContainer = document.getElementById('quiz-db-container');
        if (!quizContainer) return;
        
        const quizForm = quizContainer.querySelector('.quiz-form');
        const submitBtn = quizContainer.querySelector('.submit-quiz-btn');
        const redoBtn = quizContainer.querySelector('.redo-quiz-btn');
        const resultsContainer = quizContainer.querySelector('.quiz-results');
        
        const quizData = [
            {
                question: "Qual é a principal diferença entre um banco de dados Relacional (SQL) e um Não Relacional (NoSQL)?",
                options: ["SQL é mais rápido que NoSQL.", "SQL usa um schema flexível, enquanto NoSQL usa um schema rígido.", "SQL é ideal para dados não estruturados, enquanto NoSQL é para dados estruturados.", "SQL usa um schema rígido com tabelas, enquanto NoSQL é mais flexível e pode usar modelos como chave-valor ou documento."],
                answer: 3,
                explanation: "A distinção fundamental é o schema. Bancos relacionais (SQL) exigem uma estrutura de tabelas e colunas predefinida (schema rígido), enquanto bancos NoSQL permitem estruturas de dados mais dinâmicas e flexíveis."
            },
            {
                question: "Qual serviço da AWS é a escolha ideal para um banco de dados relacional totalmente gerenciado?",
                options: ["Amazon DynamoDB", "Amazon S3", "Amazon EC2", "Amazon RDS"],
                answer: 3,
                explanation: "O Amazon RDS (Relational Database Service) é o serviço gerenciado que automatiza tarefas como patching, backups e failover para motores de banco de dados relacionais como MySQL, PostgreSQL, etc."
            },
            {
                question: "Uma aplicação de e-commerce precisa de um banco de dados que garanta transações ACID (Atomicidade, Consistência, Isolamento, Durabilidade). Qual serviço AWS é o mais apropriado?",
                options: ["Amazon ElastiCache", "Amazon DynamoDB", "Amazon Aurora", "Amazon S3"],
                answer: 2,
                explanation: "O Amazon Aurora é um banco de dados relacional compatível com MySQL e PostgreSQL, projetado pela AWS para a nuvem. Ele oferece a mais alta performance e disponibilidade para cargas de trabalho transacionais que dependem das garantias ACID."
            },
            {
                question: "Qual é o propósito da cláusula `WHERE` em uma instrução SQL?",
                options: ["Para ordenar os resultados.", "Para agrupar os resultados.", "Para filtrar as linhas de uma tabela com base em uma condição.", "Para juntar duas tabelas."],
                answer: 2,
                explanation: "A cláusula `WHERE` é usada para filtrar registros, retornando apenas as linhas que satisfazem os critérios especificados."
            },
            {
                question: "Um desenvolvedor precisa de um banco de dados NoSQL que ofereça performance de milissegundos em qualquer escala para uma aplicação de games. Qual serviço da AWS ele deve escolher?",
                options: ["Amazon RDS for MySQL", "Amazon DynamoDB", "Amazon Redshift", "Amazon S3 Glacier"],
                answer: 1,
                explanation: "O Amazon DynamoDB é o serviço de banco de dados NoSQL (chave-valor e documento) da AWS, projetado especificamente para alta performance e escalabilidade massiva."
            },
            {
                question: "O que o termo 'Normalização' significa no design de bancos de dados relacionais?",
                options: ["O processo de tornar os dados ilegíveis através de criptografia.", "O processo de organizar tabelas para minimizar a redundância de dados e melhorar a integridade.", "O processo de copiar dados para múltiplas tabelas para acelerar as leituras.", "O processo de fazer backup de um banco de dados."],
                answer: 1,
                explanation: "A normalização visa reduzir a repetição de dados, quebrando tabelas grandes em tabelas menores e bem estruturadas, e conectando-as com relações. Isso previne anomalias de dados."
            },
            {
                question: "Qual comando SQL é usado para adicionar uma nova linha de dados a uma tabela?",
                options: ["`SELECT`", "`UPDATE`", "`CREATE`", "`INSERT INTO`"],
                answer: 3,
                explanation: "A instrução `INSERT INTO` é usada para inserir novos registros (linhas) em uma tabela."
            },
            {
                question: "Uma empresa precisa de uma solução de Data Warehouse para executar consultas analíticas complexas sobre petabytes de dados. Qual serviço da AWS é otimizado para essa carga de trabalho?",
                options: ["Amazon RDS", "Amazon DynamoDB", "Amazon Redshift", "Amazon ElastiCache"],
                answer: 2,
                explanation: "O Amazon Redshift é o serviço de Data Warehouse da AWS, projetado para BI (Business Intelligence) e cargas de trabalho analíticas (OLAP) em grande escala."
            },
            {
                question: "O que a cláusula `JOIN` permite que você faça em uma consulta SQL?",
                options: ["Empilhar os resultados de duas consultas, um sobre o outro.", "Ordenar os resultados em ordem alfabética.", "Combinar linhas de duas ou mais tabelas com base em uma coluna relacionada.", "Filtrar os resultados de uma consulta."],
                answer: 2,
                explanation: "O `JOIN` é a operação fundamental do modelo relacional. Ele 'costura' tabelas diferentes, permitindo que você enriqueça seus dados, como buscar o nome de um cliente a partir do ID do cliente em uma tabela de pedidos."
            },
            {
                question: "Qual é a principal vantagem de usar uma implantação Multi-AZ no Amazon RDS?",
                options: ["Melhorar a performance de leitura da aplicação.", "Reduzir o custo do banco de dados.", "Aumentar a alta disponibilidade e a tolerância a falhas.", "Permitir o acesso de usuários de múltiplas regiões."],
                answer: 2,
                explanation: "O Multi-AZ cria uma réplica síncrona do seu banco de dados em outra Zona de Disponibilidade. Em caso de falha, o RDS realiza um failover automático, garantindo a continuidade do serviço."
            },
            {
                question: "O que o termo 'Data Lake' representa na arquitetura de dados moderna?",
                options: ["Um banco de dados relacional muito grande.", "Um repositório centralizado que armazena todos os seus dados, estruturados e não estruturados, em qualquer escala.", "Um tipo de cache em memória.", "Uma cópia exata de um banco de dados para recuperação."],
                answer: 1,
                explanation: "Um Data Lake permite que você armazene volumes massivos de dados diversos em seu formato original, sem a necessidade de estruturá-los primeiro. O Amazon S3 é a fundação da maioria dos Data Lakes na AWS."
            },
            {
                question: "Qual cláusula SQL é usada para ordenar os resultados de uma consulta?",
                options: ["`GROUP BY`", "`WHERE`", "`HAVING`", "`ORDER BY`"],
                answer: 3,
                explanation: "A cláusula `ORDER BY` é usada no final de uma instrução `SELECT` para classificar o conjunto de resultados com base em uma ou mais colunas, em ordem ascendente (ASC) ou descendente (DESC)."
            },
            {
                question: "Qual serviço da AWS permite que você execute consultas SQL diretamente em arquivos armazenados no Amazon S3?",
                options: ["Amazon RDS", "Amazon Athena", "AWS Glue", "Amazon QuickSight"],
                answer: 1,
                explanation: "O Amazon Athena é um serviço de consulta interativo e serverless que facilita a análise de dados no S3 usando SQL padrão, sem a necessidade de carregar os dados em um banco de dados."
            },
            {
                question: "Qual é a principal diferença entre `DELETE` e `TRUNCATE` em SQL?",
                options: ["`DELETE` remove a tabela inteira, enquanto `TRUNCATE` remove apenas as linhas.", "`DELETE` é mais rápido que `TRUNCATE`.", "`DELETE` remove linhas uma a uma e pode ser desfeito (rollback), enquanto `TRUNCATE` remove todas as linhas de uma vez e não pode ser desfeito.", "`TRUNCATE` permite uma cláusula `WHERE`, e `DELETE` não."],
                answer: 2,
                explanation: "`DELETE` é uma operação DML que remove linhas com base em uma condição e pode ser revertida. `TRUNCATE` é uma operação DDL que esvazia a tabela de forma rápida e irreversível."
            },
            {
                question: "Uma empresa quer um cache em memória gerenciado para acelerar a performance de seu banco de dados. Qual serviço AWS é o mais indicado?",
                options: ["Amazon S3", "Amazon DynamoDB Accelerator (DAX)", "Amazon Redshift", "Amazon ElastiCache"],
                answer: 3,
                explanation: "O Amazon ElastiCache é um serviço que facilita a implantação e operação de caches em memória na nuvem, compatível com motores como Redis e Memcached."
            },
            {
                question: "O que significa dizer que uma transação de banco de dados é 'Atômica' (o 'A' de ACID)?",
                options: ["A transação é muito pequena.", "A transação é executada de forma isolada de outras.", "Toda a transação é concluída com sucesso, ou nada dela é feito (ela é desfeita).", "Uma vez confirmada, a transação é permanente."],
                answer: 2,
                explanation: "A atomicidade garante que as operações dentro de uma transação sejam tratadas como uma única unidade indivisível: ou tudo acontece, ou nada acontece."
            },
            {
                question: "Qual das seguintes opções é um benefício de um banco de dados NoSQL como o DynamoDB?",
                options: ["Suporte robusto a transações ACID.", "Schema rígido que garante a integridade dos dados.", "Facilidade para executar consultas `JOIN` complexas.", "Flexibilidade de schema e escalabilidade horizontal massiva."],
                answer: 3,
                explanation: "Bancos NoSQL como o DynamoDB brilham em cenários que exigem um schema flexível (onde os dados podem evoluir) e a capacidade de escalar horizontalmente para lidar com um tráfego imenso."
            },
            {
                question: "O que o comando `COMMIT` faz em uma transação SQL?",
                options: ["Inicia uma nova transação.", "Descarta todas as alterações feitas na transação.", "Torna todas as alterações feitas na transação permanentes.", "Mostra as alterações que serão feitas."],
                answer: 2,
                explanation: "O `COMMIT` é o 'ponto sem retorno'. Ele salva permanentemente todas as operações (INSERTs, UPDATEs, DELETEs) realizadas desde o início da transação."
            },
            {
                question: "No Amazon RDS, o que uma 'Read Replica' (Réplica de Leitura) permite que você faça?",
                options: ["Garantir o failover automático em caso de falha.", "Fazer backup do seu banco de dados.", "Escalar a capacidade de leitura, desviando as consultas `SELECT` do banco de dados principal.", "Criptografar seu banco de dados."],
                answer: 2,
                explanation: "As Read Replicas são usadas para melhorar a performance. Você cria cópias somente leitura do seu banco principal e direciona o tráfego de relatórios e consultas pesadas para elas, aliviando a carga da instância primária."
            },
            {
                question: "Qual serviço da AWS é ideal para ETL (Extrair, Transformar e Carregar) dados em escala?",
                options: ["Amazon RDS", "AWS Lambda", "AWS Glue", "Amazon S3"],
                answer: 2,
                explanation: "O AWS Glue é um serviço de ETL totalmente gerenciado que facilita a preparação e o carregamento de seus dados para análise, automatizando o processo de descoberta, limpeza e transformação."
            },
            {
                question: "Qual função de agregação SQL é usada para contar o número de linhas em um resultado?",
                options: ["`SUM()`", "`AVG()`", "`COUNT()`", "`MAX()`"],
                answer: 2,
                explanation: "A função `COUNT()` é usada para contar registros. `COUNT(*)` conta todas as linhas, enquanto `COUNT(DISTINCT coluna)` conta os valores únicos em uma coluna."
            },
            {
                question: "O que a cláusula `GROUP BY` faz?",
                options: ["Ordena os resultados.", "Filtra as linhas antes da agregação.", "Agrupa linhas que têm os mesmos valores em colunas especificadas em uma linha de resumo.", "Filtra os grupos após a agregação."],
                answer: 2,
                explanation: "O `GROUP BY` é a base da análise em SQL. Ele 'colapsa' múltiplas linhas em uma única linha de resumo, permitindo que você use funções de agregação como `SUM()` e `COUNT()` em cada grupo."
            },
            {
                question: "Em uma tabela DynamoDB, qual componente é responsável por identificar unicamente cada item?",
                options: ["O primeiro atributo.", "Um índice secundário.", "A chave primária (partition key ou partition key + sort key).", "O nome da tabela."],
                answer: 2,
                explanation: "A chave primária é fundamental. Ela não apenas garante a unicidade de cada item, mas também determina como os dados são particionados e armazenados fisicamente, impactando diretamente a performance."
            },
            {
                question: "Qual a diferença entre a cláusula `WHERE` e a `HAVING`?",
                options: ["Não há diferença, elas são intercambiáveis.", "`WHERE` filtra linhas antes da agregação, `HAVING` filtra grupos após a agregação.", "`HAVING` é mais rápida que `WHERE`.", "`WHERE` só pode ser usada com `SELECT *`."],
                answer: 1,
                explanation: "Esta é uma distinção crucial. `WHERE` atua nos dados brutos, linha por linha. `HAVING` atua no resultado do `GROUP BY`, filtrando os grupos agregados."
            },
            {
                question: "Qual das seguintes afirmações sobre o Amazon Aurora está CORRETA?",
                options: ["É um banco de dados NoSQL.", "É compatível com Microsoft SQL Server e Oracle.", "É uma versão do MySQL e PostgreSQL otimizada pela AWS para a nuvem, oferecendo maior performance e resiliência.", "Não suporta replicação ou backups."],
                answer: 2,
                explanation: "O Aurora é o motor de banco de dados relacional da própria AWS, compatível com os populares motores de código aberto, mas com uma arquitetura de armazenamento reconstruída para a nuvem."
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