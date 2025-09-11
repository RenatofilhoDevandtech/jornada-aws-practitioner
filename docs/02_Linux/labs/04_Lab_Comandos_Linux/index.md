# <img src="https://api.iconify.design/mdi/spy.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab 03 (Linux): O Agente Secreto - Comandos Essenciais e Hacks de Produtividade

### O Cenário (A "User Story")

> **Como** um analista de segurança júnior, **EU QUERO** executar comandos para obter consciência situacional sobre um servidor que acabei de acessar, **PARA QUE** eu possa entender o ambiente, verificar quem está online e otimizar meu fluxo de trabalho na linha de comando.

### A Dor que o Lab Resolve

Você conseguiu se conectar ao seu servidor EC2. E agora? Como você descobre informações básicas sobre o sistema, o tempo e seu próprio usuário? E, mais importante, como você evita ter que digitar os mesmos comandos longos de novo e de novo? Este laboratório te dá o kit de ferramentas do "agente secreto" para reconhecimento e eficiência.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Executar comandos para obter informações sobre o sistema e sua sessão.
* [ ] Usar o histórico do shell para pesquisar e reutilizar comandos.

### Pré-requisitos
* Acesso via **SSH** a uma instância EC2 com Amazon Linux. (Se precisar, revise o Lab 01 de Linux).

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: A Missão de Reconhecimento

#### Tarefa 1: Consciência Situacional (Comandos de Reconhecimento)
A primeira coisa que um agente faz em um novo território é obter informações.

1.  **Quem sou eu? (`whoami`)**
    * **Analogia:** "Qual é o meu **disfarce** (nome de usuário) atual?"
    * Digite `whoa` e pressione a tecla **`Tab`**. O shell autocompletará para `whoami`. Pressione **Enter**.
    ```bash
    whoami
    ```
    * **Resultado:** `ec2-user`.

2.  **Onde estou? (`hostname`)**
    * **Analogia:** "Qual é o **nome desta cidade** (servidor)?"
    * O comando `hostname -s` mostra o nome curto do host.
    ```bash
    hostname -s
    ```

3.  **Qual o status do sistema? (`uptime` e `who`)**
    * **Analogia:** "Há quanto tempo esta cidade está operacional e quem mais está aqui?"
    * `uptime -p` mostra o tempo de atividade de forma legível.
    * `who -H -a` mostra todos os usuários logados com detalhes.
    ```bash
    uptime -p
    who -H -a
    ```

4.  **Que horas são? (`date` e `cal`)**
    * **Analogia:** "Qual é a data e a hora locais? E no QG em outra parte do mundo?"
    * O Linux permite que você visualize a hora em qualquer fuso horário na hora de executar um comando.
    ```bash
    # Hora atual no fuso horário do servidor
    date
    
    # Hora em Nova York
    TZ=America/New_York date
    ```
    * O comando `cal` mostra um calendário.
    ```bash
    # Mostra o calendário com o domingo (Sunday) como primeiro dia da semana
    cal -s
    ```

5.  **Quais são minhas credenciais? (`id`)**
    * **Analogia:** "Quais são meus **níveis de acesso** (grupos) neste disfarce?"
    * O comando `id` mostra seu User ID (UID), Group ID (GID) e todos os grupos aos quais você pertence.
    ```bash
    id ec2-user
    ```

#### Tarefa 2: Hacks de Produtividade (A Memória Fotográfica do Agente)
Um bom agente nunca repete trabalho. Ele usa ferramentas para ser rápido e eficiente.

1.  **O Diário de Bordo (`history`)**
    * **Analogia:** Acessar o **"diário de todas as ações"** que você já realizou na sessão.
    * Digite `history` para ver uma lista numerada de todos os comandos que você executou.
    ```bash
    history
    ```

2.  **A Pesquisa Reversa (`CTRL+R`)**
    * **Analogia:** Usar a **"memória fotográfica"** para encontrar instantaneamente um comando complexo que você usou no passado.
    * Pressione as teclas **`CTRL`** e **`R`** ao mesmo tempo. O prompt mudará.
    * Comece a digitar uma parte do comando que você quer encontrar (ex: `TZ`). O shell automaticamente mostrará o último comando que corresponde à sua busca.
    * Você pode usar as setas para editar o comando encontrado antes de pressionar Enter para executá-lo.

> **`!!! tip "Dica de Especialista"`**
> Dominar o `CTRL+R` é um dos atalhos que separam um iniciante de um usuário avançado. É uma das ferramentas de produtividade mais importantes do shell.

3.  **O Reflexo Rápido (`!!`)**
    * **Analogia:** O **"reflexo rápido"** para repetir a última ação imediatamente.
    * **O que faz?** O comando `!!` é substituído pelo último comando que você executou.
    * **Como Usar:**
        1.  Primeiro, execute um comando simples: `date`
        2.  Agora, digite `!!` e pressione Enter. O comando `date` será executado novamente.

> **`!!! danger "Hack de `sudo`"`**
> O uso mais famoso do `!!` é quando você esquece de usar `sudo`. Imagine que você digitou um comando longo como `yum install nginx` e recebeu "permissão negada". Em vez de digitar tudo de novo, você simplesmente digita:
> ```bash
> sudo !! 
> ```
> O shell irá substituir o `!!` pelo comando anterior (`yum install nginx`), executando `sudo yum install nginx` e te economizando muito tempo!

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos
* [ ] Se você criou a instância EC2 manualmente para este lab, lembre-se de **terminá-la** para evitar custos.

### <img src="https://api.iconify.design/mdi/comment-quote-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns, agente! Você não apenas aprendeu a obter inteligência crítica sobre qualquer sistema Linux, mas também dominou os hacks de produtividade que te tornarão mais rápido e eficiente na linha de comando.