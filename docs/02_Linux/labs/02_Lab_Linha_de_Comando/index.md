# <img src="https://api.iconify.design/mdi/magnify-scan.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab 02 (Linux): O Detetive da Instância - Inspecionando o EC2

### O Cenário (A "User Story")

> **Como** um novo engenheiro de nuvem, **EU QUERO** usar comandos Linux para inspecionar minha instância EC2 de dentro para fora, **PARA QUE** eu possa entender suas características, seu status e seu ciclo de vida sem depender apenas do Console da AWS.

### A Dor que o Lab Resolve

Quando você se conecta a uma instância EC2 pela primeira vez, você cai em uma tela preta. Como saber que tipo de "máquina" é essa? Qual o seu tamanho? Qual sistema operacional ela está rodando? Este laboratório te dá as ferramentas de linha de comando para responder a todas essas perguntas, agindo como um verdadeiro detetive.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Usar o Serviço de Metadados da Instância para descobrir informações sobre o EC2.
* [ ] Utilizar comandos Linux (`uptime`, `dmesg`) para verificar o status do sistema.
* [ ] Entender na prática a diferença crucial entre **Parar (Stop)** e **Terminar (Terminate)** uma instância.

### Pré-requisitos
* Uma instância EC2 com **Amazon Linux** já em execução (pode ser a do lab anterior).
* Acesso via **SSH** a esta instância.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: A Investigação

#### Tarefa 1: O DNA da Instância (O Serviço de Metadados)

Toda instância EC2 tem um "endereço IP mágico" interno: `169.254.169.254`. Acessar este endereço de *dentro* da instância revela tudo sobre ela. É como ler a etiqueta de DNA da sua máquina. Vamos usar o comando `curl` para conversar com ele.

1.  **Descobrindo o Tipo de Instância:**
    * **O Conceito AWS:** O *Instance Type* (ex: `t2.micro`) define a CPU e a RAM da sua máquina.
    * **O Comando Linux:**
        ```bash
        curl [http://169.254.169.254/latest/meta-data/instance-type](http://169.254.169.254/latest/meta-data/instance-type)
        ```
    * **O Resultado:** O terminal deve imprimir o tipo da sua instância (ex: `t2.micro`).

2.  **Descobrindo a Imagem (AMI):**
    * **O Conceito AWS:** A *AMI (Amazon Machine Image)* é o template do sistema operacional.
    * **O Comando Linux:**
        ```bash
        curl [http://169.254.169.254/latest/meta-data/ami-id](http://169.254.169.254/latest/meta-data/ami-id)
        ```
    * **O Resultado:** O terminal imprimirá o ID único da AMI usada para lançar seu servidor.

3.  **Descobrindo a Localização Geográfica:**
    * **O Conceito AWS:** A *Availability Zone (AZ)* é o data center específico onde sua instância está.
    * **O Comando Linux:**
        ```bash
        curl [http://169.254.169.254/latest/meta-data/placement/availability-zone](http://169.254.169.254/latest/meta-data/placement/availability-zone)
        ```
    * **O Resultado:** O terminal mostrará a AZ exata (ex: `sa-east-1a`).

> **`!!! tip "Dica de Especialista"`**
> O Serviço de Metadados é crucial para automação. Scripts rodando dentro de uma instância podem usá-lo para tomar decisões inteligentes, como "Se eu estou rodando em uma instância do tipo `micro`, use pouca memória. Se for `large`, use mais."

#### Tarefa 2: O Check-up de Saúde (Verificando o Status com Linux)
As "Verificações de Status" no console são ótimas, mas às vezes precisamos de um diagnóstico mais profundo do sistema operacional.

1.  **O Pulso Vital (`uptime`):**
    * **O Conceito AWS:** Há quanto tempo a instância está rodando sem reiniciar?
    * **O Comando Linux:**
        ```bash
        uptime
        ```
    * **O Resultado:** Ele mostra há quanto tempo o sistema está "up", o número de usuários e o "load average" (uma métrica da carga na CPU).

2.  **O Histórico Médico (`dmesg`):**
    * **O Conceito AWS:** Houve algum problema de hardware ou de driver durante a inicialização?
    * **O Comando Linux:**
        ```bash
        dmesg | tail
        ```
    * **O Resultado:** Mostra as últimas 10 mensagens do "coração" do sistema operacional (o Kernel). É o primeiro lugar que um especialista olha para diagnosticar problemas de hardware.

3.  **A Sala de Emergência (`top`):**
    * **O Conceito AWS:** Qual processo está consumindo toda a CPU agora?
    * **O Comando Linux:**
        ```bash
        top
        ```
    * **O Resultado:** Uma visão em tempo real dos processos, similar ao Gerenciador de Tarefas do Windows. Pressione a tecla **`q`** para sair.

#### Tarefa 3: O Fim da Linha (Desligando vs. Terminando)
Esta é uma das lições mais importantes sobre o ciclo de vida de uma instância.

1.  **A Pergunta:** O que acontece se eu rodar o comando de desligamento do Linux (`shutdown`) dentro da minha instância? Ela vai ser "terminada"?
2.  **O Comando Linux (Execute com cuidado!):**
    ```bash
    sudo shutdown -h now
    ```
3.  **O Resultado:** Sua conexão SSH será encerrada imediatamente.
4.  **A Investigação:** Agora, volte para o **Console da AWS** e observe o **Instance State** (Estado da instância) do seu servidor. Ele mudará de `running` para `stopping`, e finalmente para... **`stopped`**! Ele não foi terminado.

> **`!!! danger "Insight Crítico"`**
> Desligar o sistema operacional de dentro da instância (`shutdown`) é o mesmo que a ação **Stop (Parar)** no console. A ação **Terminate (Terminar)** é um comando diferente, que você só pode dar *para* a API da AWS (através do console ou da CLI). Você **não pode** "terminar" uma instância a partir de dentro dela mesma.

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos

* [ ] Como o comando `shutdown` apenas "parou" nossa instância, ela ainda existe e o seu volume EBS **continua gerando custos**.
* [ ] Vá ao console do EC2, selecione a instância no estado `stopped`.
* [ ] Vá em **Instance state** > **Terminate instance** (Terminar instância) para deletá-la permanentemente.

### <img src="https://api.iconify.design/mdi/comment-quote-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns, detetive! Você aprendeu a usar comandos Linux para descobrir os metadados da AWS, checar a saúde de um sistema e entendeu a diferença vital entre parar e terminar uma instância. Você está um passo mais perto de dominar o gerenciamento de frotas na nuvem.