<div class="quiz-container" id="quiz-linux-container">
    <h3><img src="https://api.iconify.design/mdi/linux.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Quiz: Fundamentos de Linux para Nuvem</h3>
    <form class="quiz-form">
        </form>
    <button class="submit-quiz-btn">Verificar Respostas</button>
    <button class="redo-quiz-btn" style="display:none; margin-left: 1rem;">Refazer Quiz</button>
    <div class="quiz-results"></div>
</div>

<script>
    (function() {
        const quizContainer = document.getElementById('quiz-linux-container');
        if (!quizContainer) return;

        const quizForm = quizContainer.querySelector('.quiz-form');
        const submitBtn = quizContainer.querySelector('.submit-quiz-btn');
        const redoBtn = quizContainer.querySelector('.redo-quiz-btn');
        const resultsContainer = quizContainer.querySelector('.quiz-results');

        const quizData = [
            {
                question: "Qual comando é usado para listar o conteúdo de um diretório, incluindo arquivos ocultos e com detalhes completos?",
                options: ["ls -a", "list all", "ls -l", "ls -lah"],
                answer: 3,
                explanation: "O comando `ls -lah` é a combinação mais comum. `l` para formato longo, `a` para todos os arquivos (incluindo ocultos) e `h` para tamanhos legíveis (human-readable)."
            },
            {
                question: "Um administrador precisa editar um arquivo de configuração em um servidor sem interface gráfica. Qual dos seguintes editores de texto é conhecido por sua simplicidade e por exibir os atalhos de comando na tela?",
                options: ["Vim", "Emacs", "gedit", "nano"],
                answer: 3,
                explanation: "O `nano` é famoso por ser um editor de texto de terminal amigável para iniciantes, pois exibe os comandos principais (como Salvar e Sair) na parte inferior da tela."
            },
            {
                question: "Qual é o propósito do comando `sudo` no Linux?",
                options: ["Trocar para o diretório raiz do sistema.", "Executar um único comando com privilégios de superusuário (root).", "Listar todos os usuários do sistema.", "Desligar o servidor de forma segura."],
                answer: 1,
                explanation: "`sudo` (Superuser Do) permite que um usuário autorizado execute um comando como se fosse o usuário root, o que é a prática recomendada para tarefas administrativas."
            },
            {
                question: "Para onde a saída do seguinte comando será direcionada: `echo 'Olá Mundo' > arquivo.txt`?",
                options: ["Para a tela do terminal.", "Para um novo diretório chamado 'arquivo.txt'.", "Para o arquivo `arquivo.txt`, sobrescrevendo seu conteúdo anterior.", "Será adicionada ao final do arquivo `arquivo.txt`."],
                answer: 2,
                explanation: "O operador de redirecionamento `>` pega a saída do comando e a escreve em um arquivo, sobrescrevendo o conteúdo. O operador `>>` é usado para adicionar ao final (append)."
            },
            {
                question: "Qual comando você usaria para encontrar todas as linhas contendo a palavra 'ERROR' em um arquivo de log chamado `app.log`?",
                options: ["find ERROR in app.log", "search ERROR app.log", "grep 'ERROR' app.log", "cat app.log | filter ERROR"],
                answer: 2,
                explanation: "O comando `grep` é a ferramenta padrão e mais poderosa do Linux para pesquisar padrões de texto dentro de arquivos. É essencial para analisar logs."
            },
            {
                question: "Um desenvolvedor criou um script chamado `backup.sh`. Ao tentar executá-lo com `./backup.sh`, ele recebe um erro de 'Permissão negada'. O que provavelmente está faltando?",
                options: ["O script precisa ser movido para o diretório `/bin`.", "O usuário precisa usar `sudo`.", "O script precisa da permissão de execução.", "O nome do arquivo precisa terminar em `.exe`."],
                answer: 2,
                explanation: "Por padrão, novos arquivos no Linux não têm permissão de execução. O desenvolvedor precisa executar `chmod +x backup.sh` para torná-lo executável."
            },
            {
                question: "Qual é a principal função do arquivo `/etc/passwd` em um sistema Linux?",
                options: ["Armazenar as senhas criptografadas dos usuários.", "Conter a lista de todos os grupos do sistema.", "Manter o registro de todos os comandos executados.", "Conter informações sobre as contas de usuário, como nome de usuário, UID e diretório home."],
                answer: 3,
                explanation: "O arquivo `/etc/passwd` é o banco de dados principal de contas de usuário. As senhas criptografadas são, na verdade, armazenadas de forma mais segura no arquivo `/etc/shadow`."
            },
            {
                question: "Como você instalaria o servidor web Apache (pacote `httpd`) em uma instância EC2 que usa Amazon Linux 2?",
                options: ["sudo apt install httpd", "sudo yum install httpd", "install-package httpd", "sudo get httpd"],
                answer: 1,
                explanation: "O Amazon Linux 2 é baseado na família Red Hat, que usa o gerenciador de pacotes `yum`. O `apt` é usado em distribuições da família Debian, como o Ubuntu."
            },
            {
                question: "Qual comando é usado para visualizar os processos em execução no sistema em tempo real, ordenados por uso de CPU?",
                options: ["ps -ef", "list-processes", "top", "jobs"],
                answer: 2,
                explanation: "O comando `top` é o 'Gerenciador de Tarefas' do Linux, fornecendo uma visão dinâmica e em tempo real dos processos e do consumo de recursos do sistema."
            },
            {
                question: "O que o comando `pwd` faz?",
                options: ["Altera a senha do usuário atual.", "Lista o conteúdo do diretório de trabalho.", "Mostra o caminho completo do diretório de trabalho atual.", "Cria um novo diretório."],
                answer: 2,
                explanation: "`pwd` significa 'Print Working Directory'. É um comando fundamental para a orientação, mostrando exatamente onde você está no sistema de arquivos."
            },
            {
                question: "Qual é a diferença entre um caminho absoluto e um caminho relativo?",
                options: ["Caminhos absolutos são mais curtos que os relativos.", "Caminhos absolutos começam com `/` (a raiz), enquanto os relativos partem do diretório atual.", "Apenas caminhos absolutos podem ser usados com o comando `cd`.", "Caminhos relativos são sempre fixos, enquanto os absolutos mudam."],
                answer: 1,
                explanation: "Um caminho absoluto (ex: `/home/user/docs`) funciona de qualquer lugar do sistema. Um caminho relativo (ex: `docs/file.txt`) só funciona se você estiver no diretório correto."
            },
            {
                question: "Um administrador de sistemas precisa mover todos os arquivos de um diretório chamado `logs_antigos` para `backup_logs`. Qual comando ele deve usar?",
                options: ["cp logs_antigos/* backup_logs/", "mv logs_antigos/* backup_logs/", "link logs_antigos/* backup_logs/", "rm logs_antigos/* backup_logs/"],
                answer: 1,
                explanation: "O comando `mv` (move) é usado tanto para renomear quanto para mover arquivos e diretórios. O curinga `*` garante que todos os arquivos dentro do diretório de origem sejam movidos."
            },
            {
                question: "O que o comando `tail -f /var/log/messages` permite fazer?",
                options: ["Ver as 10 primeiras linhas do arquivo de log.", "Apagar o arquivo de log.", "Ver o final do arquivo de log e continuar exibindo novas linhas em tempo real.", "Filtrar o arquivo de log por mensagens de erro."],
                answer: 2,
                explanation: "A opção `-f` (follow) é uma das ferramentas mais poderosas para administradores, permitindo monitorar arquivos de log em tempo real à medida que novos eventos são registrados."
            },
            {
                question: "No Linux, como o sistema de arquivos diferencia `Arquivo.txt` de `arquivo.txt`?",
                options: ["Ele os trata como o mesmo arquivo.", "Ele os trata como dois arquivos diferentes.", "Ele converte ambos para minúsculas.", "Ele não permite nomes de arquivos com maiúsculas."],
                answer: 1,
                explanation: "O sistema de arquivos do Linux é *case-sensitive*, o que significa que maiúsculas e minúsculas importam. `Arquivo.txt` e `arquivo.txt` são duas entidades distintas."
            },
            {
                question: "Qual comando é usado para criar um pacote de arquivos (um 'tarball') e comprimi-lo com gzip de uma só vez?",
                options: ["zip -c -z -f", "tar -czf", "gzip -cf", "archive -c"],
                answer: 1,
                explanation: "O comando `tar` com a opção `z` invoca o `gzip` para compressão. O mnemônico é **C**reate **Z**ipped **F**ile. Para extrair, usa-se `tar -xzf` (**E**xtract **Z**ipped **F**ile)."
            },
            {
                question: "Qual das seguintes afirmações sobre o usuário `root` está CORRETA?",
                options: ["É recomendado fazer login como `root` para todas as tarefas diárias por conveniência.", "O usuário `root` tem permissões limitadas para proteger o sistema.", "O usuário `root` tem poder absoluto e irrestrito sobre todo o sistema.", "Contas de usuário `root` não podem ser protegidas com senha."],
                answer: 2,
                explanation: "O `root` é o superusuário, com poder total. A melhor prática de segurança é NUNCA fazer login diretamente como `root`, mas sim usar `sudo` para elevar privilégios quando necessário."
            },
            {
                question: "Qual arquivo é lido pelo shell `bash` toda vez que uma nova sessão de terminal é iniciada, sendo o local ideal para definir aliases permanentes?",
                options: ["/etc/profile", "~/.bash_history", "~/.bash_profile", "~/.bashrc"],
                answer: 3,
                explanation: "O arquivo `.bashrc` no diretório home do usuário é executado a cada nova sessão interativa, tornando-o o local perfeito para customizações pessoais do shell."
            },
            {
                question: "O que o comando `chmod 755 meu_script.sh` faz?",
                options: ["Dá permissão total (ler, escrever, executar) para todos.", "Dá permissão de leitura para todos e de escrita apenas para o dono.", "Dá ao dono permissão total, e ao grupo e outros, permissão de leitura e execução.", "Remove todas as permissões do script."],
                answer: 2,
                explanation: "Na notação octal, `7` é `rwx` (4+2+1), e `5` é `r-x` (4+0+1). Portanto, `755` se traduz em `rwxr-xr-x`, uma permissão muito comum para scripts e diretórios."
            },
            {
                question: "Qual comando é usado para verificar a conectividade de rede com o servidor `google.com`?",
                options: ["connect google.com", "traceroute google.com", "netstat google.com", "ping google.com"],
                answer: 3,
                explanation: "O comando `ping` usa o protocolo ICMP para enviar um pequeno pacote a um destino e verificar se ele responde, testando a conectividade básica da rede."
            },
            {
                question: "Para que serve o comando `systemctl enable httpd`?",
                options: ["Para iniciar o serviço httpd imediatamente.", "Para verificar o status do serviço httpd.", "Para configurar o serviço httpd para iniciar automaticamente no boot do sistema.", "Para parar o serviço httpd."],
                answer: 2,
                explanation: "`systemctl start` inicia o serviço agora. `systemctl enable` garante que, se o servidor for reiniciado, o serviço subirá junto com ele. A melhor prática é quase sempre executar ambos."
            },
            {
                question: "Qual comando é usado para criar um 'atalho' para um arquivo ou diretório em outro local do sistema de arquivos?",
                options: ["cp -s", "mv -l", "ln -s", "alias"],
                answer: 2,
                explanation: "O comando `ln -s` (link) cria um link simbólico, que é um ponteiro para o arquivo ou diretório original, muito útil para organizar o acesso a arquivos."
            },
            {
                question: "O que o Pipe `|` faz na linha de comando?",
                options: ["Executa dois comandos em paralelo.", "Pega a saída de um comando e a usa como entrada para o comando seguinte.", "Salva a saída de um comando em um arquivo.", "Compara a saída de dois comandos."],
                answer: 1,
                explanation: "O Pipe é uma das ferramentas mais poderosas do shell, permitindo encadear comandos simples para criar fluxos de processamento de texto complexos, como em `ps aux | grep nginx`."
            },
            {
                question: "Qual comando é usado para visualizar o uso da memória RAM do sistema?",
                options: ["df -h", "memstat", "free -h", "top"],
                answer: 2,
                explanation: "Enquanto `top` mostra o uso de memória em tempo real, `free -h` (free memory, human-readable) dá um resumo instantâneo e claro da memória RAM total, usada e livre."
            },
            {
                question: "Um administrador quer mudar a propriedade de um arquivo para o usuário `ana` e o grupo `financeiro`. Qual comando faz isso de uma só vez?",
                options: ["chown ana relatorio.txt && chgrp financeiro relatorio.txt", "chown ana:financeiro relatorio.txt", "chmod ana:financeiro relatorio.txt", "setowner ana financeiro relatorio.txt"],
                answer: 1,
                explanation: "O comando `chown` (change owner) aceita a sintaxe `usuario:grupo`, permitindo alterar o usuário e o grupo dono em uma única e eficiente operação."
            },
            {
                question: "Qual é a principal função de um repositório de pacotes (como os usados por `yum` e `apt`)?",
                options: ["Armazenar o código-fonte de todos os programas Linux.", "Ser um servidor central que armazena pacotes de software testados e aprovados para uma distribuição.", "Manter um registro de todos os arquivos de log do sistema.", "Controlar as permissões de acesso dos usuários aos softwares."],
                answer: 1,
                explanation: "Um repositório é a 'App Store' da sua distribuição. Ele fornece um local confiável para baixar, instalar e atualizar software, gerenciando automaticamente as dependências."
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