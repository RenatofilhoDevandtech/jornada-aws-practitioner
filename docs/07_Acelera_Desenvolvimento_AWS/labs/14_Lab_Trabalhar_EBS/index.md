# <img src="https://api.iconify.design/logos/aws-ebs.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O HD da Nuvem - Trabalhando com o Amazon EBS

### O Cenário (A "User Story")

> **Como** um administrador de sistemas (SysOps), **EU QUERO** adicionar um novo disco de dados a um servidor, fazer um backup seguro dele e depois restaurar esse backup, **PARA QUE** eu possa gerenciar o armazenamento de forma flexível e garantir a recuperação dos dados em caso de falha ou erro humano.

### A Dor que o Lab Resolve

1.  **Capacidade Fixa:** No mundo físico, se um servidor fica sem espaço em disco, o processo de adicionar um novo HD é complexo e geralmente requer tempo de inatividade.
2.  **Backups Lentos:** Fazer backups completos de discos inteiros é um processo lento e que consome muitos recursos.
3.  **Recuperação Complexa:** Restaurar dados de um backup pode ser um processo demorado e propenso a erros.

Este laboratório mostra como o EBS transforma essas tarefas complexas em operações simples e rápidas no console e na linha de comando.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Criar um volume EBS.
* [ ] Anexar e montar o volume em uma instância EC2 Linux.
* [ ] Criar um Snapshot (backup) do volume.
* [ ] Restaurar um novo volume a partir de um Snapshot.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Comprando um "HD Externo" (Criar um Volume EBS)

1.  No Console da AWS, navegue até o serviço **EC2**.
2.  Primeiro, anote a **Zona de Disponibilidade (Availability Zone)** da sua instância `Lab`. Você precisará dela.
3.  No menu esquerdo, em `Elastic Block Store`, selecione **Volumes** e clique em **Criar volume (Create volume)**.
4.  Configure as opções:
    * **Tipo de volume (Volume type):** `SSD de Uso Geral (gp2)`.
    * **Tamanho (Size - GiB):** `1`.
    * **Zona de Disponibilidade (Availability Zone):** **Selecione a MESMA AZ** da sua instância `Lab`.
        > **O "Porquê":** Um volume EBS é como um HD físico. Ele vive em um único "prédio" (AZ). Você só pode conectar um HD a um computador que está no mesmo prédio.
    * **Tag de Nome:** Chave `Name`, Valor `Meu-Volume`.
5.  Clique em **Criar volume**. Aguarde o `Estado (State)` mudar de `creating` para `available`.

#### Tarefa 2: "Plugando" o HD (Anexar o Volume)
1.  Selecione o seu `Meu-Volume`.
2.  Vá em **Ações (Actions) > Anexar volume (Attach volume)**.
3.  **Instância (Instance):** Selecione a instância `Lab`.
4.  Deixe o **Nome do dispositivo (Device name)** como `/dev/sdf`.
5.  Clique em **Anexar volume (Attach volume)**. O `Estado (State)` mudará para `in-use`.

#### Tarefa 3 e 4: Formatando e Montando o Disco
**Analogia:** Você "plugou" o HD no computador, mas o sistema operacional ainda não sabe como usá-lo. Precisamos formatá-lo e dar um "nome de drive" a ele.

1.  **Conecte-se à instância `Lab`** usando o **EC2 Instance Connect**.
2.  **Verifique os discos:** O comando `df -h` mostra os discos montados. Note que o novo disco ainda não aparece.
    ```bash
    df -h
    ```
3.  **Formate o novo volume:** Crie um sistema de arquivos nele.
    ```bash
    sudo mkfs -t ext3 /dev/sdf
    ```
4.  **Crie um "ponto de montagem"** (a pasta onde o disco aparecerá):
    ```bash
    sudo mkdir /mnt/data-store
    ```
5.  **Monte o disco** e configure-o para montar automaticamente a cada reinicialização:
    ```bash
    sudo mount /dev/sdf /mnt/data-store
    echo "/dev/sdf /mnt/data-store ext3 defaults,noatime 1 2" | sudo tee -a /etc/fstab
    ```
6.  **Verifique novamente:** `df -h`. Agora você deve ver seu novo disco de 1GB montado em `/mnt/data-store`.
7.  **Crie um arquivo de teste** para termos algo para fazer backup:
    ```bash
    sudo sh -c "echo dados importantes > /mnt/data-store/arquivo.txt"
    cat /mnt/data-store/arquivo.txt
    ```

#### Tarefa 5: A "Fotografia" de Segurança (Criar um Snapshot)
**Analogia:** Um Snapshot é uma "fotografia" do estado exato do seu HD em um momento, que serve como backup.

1.  Volte para o console do **EC2 > Volumes**. Selecione o `Meu-Volume`.
2.  Vá em **Ações > Criar snapshot (Create snapshot)**.
3.  Adicione uma **Tag de Nome** `Meu-Snapshot` e clique em **Criar snapshot**.
4.  **Simule um Desastre:** Agora que o backup está feito, vamos deletar o arquivo original. No terminal, execute:
    ```bash
    sudo rm /mnt/data-store/arquivo.txt
    ls /mnt/data-store/
    ```
    > O arquivo desapareceu! Pânico!

#### Tarefa 6: A Restauração Mágica (Restaurar o Snapshot)
**Analogia:** Vamos usar nossa "fotografia" de segurança para reconstruir uma cópia perfeita do nosso HD perdido.

1.  No console do **EC2**, vá em **Snapshots**. Selecione o `Meu-Snapshot`.
2.  Vá em **Ações > Criar volume com o snapshot (Create volume from snapshot)**.
3.  Garanta que a **Zona de Disponibilidade** esteja correta e dê uma **Tag de Nome** `Volume-Restaurado`. Clique em **Criar volume**.
4.  **Anexe o volume restaurado:** Siga os mesmos passos da Tarefa 2 para anexar o `Volume-Restaurado` à sua instância `Lab`. O nome do dispositivo provavelmente será `/dev/sdg`.
5.  **Monte o volume restaurado:** No terminal, crie um novo ponto de montagem e monte o novo disco.
    ```bash
    sudo mkdir /mnt/data-restaurada
    sudo mount /dev/sdg /mnt/data-restaurada
    ```
6.  **Verificação Final:** Verifique o conteúdo da pasta restaurada:
    ```bash
    ls /mnt/data-restaurada/
    ```
    > **O Resultado:** O `arquivo.txt` está de volta! A restauração foi um sucesso.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você completou o ciclo de vida de gerenciamento de um volume EBS. Você provisionou armazenamento adicional, configurou-o para uso, protegeu os dados com um snapshot e simulou uma recuperação de desastre, restaurando os dados a partir do backup. Estas são habilidades fundamentais para qualquer administrador de sistemas na AWS.

---

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: O HD Mágico que se Clona

Um dos maiores medos de quem trabalha com tecnologia é a perda de dados. Um servidor que fica sem espaço em disco no meio da noite, um arquivo deletado por engano... são pesadelos que tiram o sono de qualquer um.

O laboratório de hoje no AWS re/Start foi uma terapia de choque contra esse medo. Foi uma aula prática sobre como o **Amazon EBS**, o "HD da nuvem", nos dá as ferramentas para expandir, proteger e recuperar nossos dados de forma simples e poderosa.

### A Jornada em 3 Atos

#### Ato 1: A Expansão (Adicionando um Novo "HD")

* **A Dor:** No mundo físico, se um servidor fica sem espaço, adicionar um novo HD é uma operação complexa, que geralmente envolve desligar a máquina e abrir o gabinete.
* **O Que Eu Fiz:** Criei um novo volume EBS de 1GB no console da AWS e o anexei à minha instância EC2.
* **O "Aha!" Moment:**
    * **Analogia:** Foi como plugar um **"HD externo virtual"** com alguns cliques. Mas a grande lição foi que, assim como um HD de verdade, não basta só plugar. Tive que entrar no servidor via terminal para **"formatar" e "montar"** o disco, para que o sistema operacional soubesse como usá-lo. Foi a junção perfeita do conceito da nuvem com a prática do Linux.

#### Ato 2: A Máquina do Tempo (Criando um Snapshot)

* **A Dor:** Backups são complicados, lentos e fáceis de esquecer.
* **O Que Eu Fiz:** Com meu novo volume funcionando e com um arquivo de teste dentro dele, eu criei um **Snapshot**.
* **O "Aha!" Moment:**
    * **Analogia:** Um Snapshot do EBS é como tirar uma **"fotografia" perfeita e instantânea** de todo o conteúdo do meu HD. Essa "foto" é guardada de forma super segura e durável no Amazon S3, pronta para ser usada se algo der errado.

#### Ato 3: O Clone (Restaurando o Backup)

* **A Dor:** Ok, o backup está feito. Mas e se o pior acontecer? E se eu deletar um arquivo importante por acidente?
* **O Que Eu Fiz:** Eu simulei o desastre. Deletei meu arquivo de teste e, em seguida, usei o Snapshot para criar um novo volume.
* **O "Aha!" Moment:**
    * **Analogia:** Eu peguei a "fotografia" (o Snapshot) que tinha tirado e disse para a AWS: "Por favor, crie um **novo HD clone** exatamente como este". Em minutos, um novo volume apareceu. Eu o "pluguei" na minha máquina, montei e, ao abrir, lá estava o arquivo que eu tinha deletado.
* **O Resultado:** A sensação de segurança que isso dá é indescritível. A recuperação de um "desastre" se tornou um processo simples e rápido.

### A Grande Lição
O lab de hoje me mostrou o ciclo de vida completo do armazenamento na nuvem. Ele não é estático. Ele é **elástico** (posso adicionar mais a qualquer momento), **resiliente** (posso fazer backups com snapshots) e **recuperável** (posso restaurar esses backups para recriar meus dados).

Simular um "desastre" e conseguir se recuperar em minutos foi uma lição poderosa. Mostrou na prática o que significa "tolerância a falhas". Não é sobre evitar que erros aconteçam, é sobre ter um sistema robusto que te permita se recuperar deles rapidamente.

#AWS #Cloud #EBS #Storage #Backup #Snapshot #DevOps #AWSreStart