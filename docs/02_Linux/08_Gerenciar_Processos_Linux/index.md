# <img src="https://api.iconify.design/mdi/memory.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Os Bastidores do Servidor: Gerenciando Processos, Tarefas e Agendamentos

Quando você usa seu computador, vários programas rodam ao mesmo tempo, mesmo que você não os veja. No Linux, cada um desses programas em execução é chamado de **processo**.

Pense no seu servidor como uma **fábrica robótica automatizada**. Cada **processo** é um **"robô operário"** executando uma tarefa específica: o robô do servidor web, o robô do banco de dados, o robô do sistema de logs, etc.

Sua missão como "Gerente de Turno" é saber como usar o painel de controle para ver o que todos os robôs estão fazendo, intervir quando um deles apresentar defeito e agendar tarefas para serem executadas no futuro.

---

### <img src="https://api.iconify.design/mdi/monitor-dashboard.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Parte 1: O Painel de Controle (Visualizando os Robôs)

Antes de gerenciar, você precisa enxergar. Estas são suas câmeras de segurança.

* **`ps` (Process Status): A Foto Instantânea**
    * **Analogia:** Tira uma **"foto"** de todos os robôs que estão trabalhando no exato momento em que você executa o comando.
    * **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" /> Hack de Mestre:** O comando `ps` sozinho é pouco útil. A combinação que você usará 99% do tempo é `ps aux`.
        * `a`: Mostra os processos de **t**odos (**a**ll) os usuários.
        * `u`: Mostra os processos em um formato **u**m pouco mais detalhado.
        * `x`: Mostra também os processos que não estão atrelados a um terminal (os "daemons").
    * **Dor que Resolve:** "Será que o meu programa `meu_app` está rodando?". Use `ps aux | grep meu_app`.

* **`top`: O Monitoramento Ao Vivo**
    * **Analogia:** É a **"transmissão ao vivo das câmeras de segurança"** da sua fábrica.
    * **O que faz?** Mostra uma lista de processos que se atualiza em tempo real, ordenada por padrão por uso de CPU. É o "Gerenciador de Tarefas" do Linux.
    * **Dor que Resolve:** "Minha instância EC2 está lenta e com a CPU em 100%! Qual robô está consumindo todos os recursos?" O `top` te mostra o culpado no topo da lista.
    * **Como Usar:** Digite `top`. Para sair, pressione a tecla `q`.

---

### <img src="https://api.iconify.design/mdi/robot-industrial-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Parte 2: Gerenciando os Robôs em Tempo Real

Às vezes, um robô trava ou precisa de um "empurrãozinho".

* **`kill`: O Botão de Desligamento de Emergência**
    * **Analogia:** Envia um **"sinal"** para um robô específico (identificado pelo seu **PID** - Process ID).
    * **A Dor que Resolve:** Um programa travou e não responde mais.
    * **Os Sinais Mais Importantes:**
        * `kill -15 [PID]`: O **"pedido educado"**. Envia o sinal **SIGTERM**, pedindo para o processo se encerrar de forma organizada (salvar arquivos, fechar conexões). **Sempre tente este primeiro!**
        * `kill -9 [PID]`: O **"corte do cabo de energia"**. Envia o sinal **SIGKILL**, que força o encerramento imediato e incondicional do processo. É o último recurso, pois pode corromper dados.

* **`nice` e `renice`: O Botão de Prioridade**
    * **Analogia:** Ajusta a **"prioridade"** de um robô na fila de tarefas do Chef (Kernel). O valor vai de `-20` (prioridade máxima) a `19` (prioridade mínima, mais "bonzinho").
    * **Dor que Resolve:** "Preciso rodar uma tarefa de análise de dados que consome muita CPU, mas não quero que ela deixe o meu site lento." Você pode iniciá-la com `nice -n 10 minha_analise.sh` para que ela rode com baixa prioridade.

* **`jobs`, `fg`, `bg`: Gerenciando Tarefas na Sua Bancada**
    * **Analogia:** Gerenciar os robôs que estão trabalhando na sua frente (foreground) ou no fundo da fábrica (background).
    * **`fg` (foreground):** Traz um robô do fundo da fábrica para a sua bancada.
    * **`bg` (background):** Manda um robô da sua bancada trabalhar no fundo da fábrica.
    * **`Ctrl + Z`:** **Pausa** o robô que está na sua frente e o coloca em "stand-by".
    * **`&` (no final de um comando):** Já inicia a tarefa diretamente no fundo da fábrica. Ex: `sleep 300 &`.

> **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação:** Entender a diferença brutal entre `kill -15` (o jeito certo) e `kill -9` (o último recurso) é um conceito de segurança e estabilidade muito cobrado.

---

### <img src="https://api.iconify.design/mdi/clock-start.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Parte 3: O Piloto Automático (Agendando Tarefas)

A verdadeira automação acontece quando você ensina os robôs a trabalharem sozinhos em horários específicos.

* **`at`: Agendar uma Tarefa Única**
    * **Analogia:** "Robô #123, por favor, execute o script de backup **hoje às 23:00 e só.**"
    * **Dor que Resolve:** A necessidade de executar um comando demorado mais tarde, sem precisar ficar na frente do terminal esperando.

* **`cron`: O Agendador de Tarefas Recorrentes**
    * **Analogia:** "Robôs de limpeza, por favor, executem a rotina de limpeza **todos os dias às 03:00 da manhã.**"
    * **O que é?** O `cron` é um daemon (um "robô de apoio") que lê um arquivo de agendamento chamado `crontab` e executa as tarefas na hora certa.
    * **Dor que Resolve:** A necessidade de automatizar tarefas repetitivas: backups diários, limpeza de logs semanal, relatórios mensais, etc.

#### <img src="https://api.iconify.design/mdi/table-edit.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> Editando o Quadro de Agendamento (`crontab -e`)
Para agendar uma tarefa `cron`, você edita o arquivo `crontab` do seu usuário com o comando `crontab -e`. Cada linha é uma nova tarefa e segue o formato:

`MIN HOR DIA MÊS DIA_SEMANA /caminho/para/o/comando`

| Campo | Valores | Exemplo (`*`) |
| :--- | :--- | :--- |
| **MIN** | Minuto (0-59) | `*` = todo minuto |
| **HOR** | Hora (0-23) | `*` = toda hora |
| **DIA** | Dia do Mês (1-31)| `*` = todo dia do mês |
| **MÊS** | Mês (1-12) | `*` = todo mês |
| **DSE** | Dia da Semana (0-6, 0=Domingo) | `*` = todo dia da semana |

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** A sintaxe do crontab é um clássico dos exames!
> * **`0 2 * * * /scripts/backup.sh`** -> Roda o backup **todos os dias, às 02:00 da manhã**.
> * **`*/15 * * * * /scripts/monitor.sh`** -> Roda o monitoramento **a cada 15 minutos**.