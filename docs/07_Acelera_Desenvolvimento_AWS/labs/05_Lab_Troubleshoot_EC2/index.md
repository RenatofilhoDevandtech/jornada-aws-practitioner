# <img src="https://api.iconify.design/mdi/magnify-scan.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Detetive da Nuvem - Solucionando Problemas na Criação de uma Instância

### O Cenário (A "User Story")

> **Como** um engenheiro de operações (SysOps), **EU QUERO** usar um script da AWS CLI para automatizar a criação de um servidor web completo (uma pilha LAMP), **PARA QUE** eu possa provisionar novos ambientes para minha aplicação de forma rápida e consistente.

### A Dor que o Lab Resolve

Scripts de automação são poderosos, mas frágeis. Um único erro de digitação, uma permissão faltando ou uma referência a um recurso que não existe pode fazer com que todo o processo falhe. Este laboratório resolve a dor do **"script quebrado"**, te ensinando um método lógico para investigar, diagnosticar e consertar problemas de automação.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Analisar e entender um script de shell complexo que usa a AWS CLI.
* [ ] Diagnosticar e corrigir erros comuns de provisionamento (ex: AMI inválida).
* [ ] Diagnosticar e corrigir erros comuns de configuração de rede (ex: Security Group bloqueando o tráfego).
* [ ] Usar ferramentas de diagnóstico como o `nmap` e verificar logs (`cloud-init`).

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: A Investigação

#### Tarefa 1: Acessando a "Cena do Crime"
Vamos nos conectar ao nosso host de comando, de onde a investigação começará.

1.  Use o **EC2 Instance Connect** para se conectar à instância `CLI Host` (siga os passos do laboratório anterior se precisar de um lembrete).
2.  **Configure a AWS CLI** com as credenciais fornecidas no painel de detalhes do seu laboratório, usando o comando `aws configure`.

#### Tarefa 2: Analisando o "Corpo do Delito" (O Script com Bugs)
Vamos examinar o script que deveria criar nosso servidor LAMP (Linux, Apache, MySQL, PHP).

1.  No terminal, navegue até a pasta dos scripts e crie um backup, uma prática recomendada antes de qualquer modificação.
    ```bash
    cd ~/sysops-activity-files/starters
    cp create-lamp-instance-v2.sh create-lamp-instance.backup
    ```
2.  Abra o script para análise em modo de leitura (não vamos editá-lo ainda).
    ```bash
    view create-lamp-instance-v2.sh
    ```
    > **O que este script *deveria* fazer?** Ele é um robô construtor sofisticado. Ele descobre dinamicamente a VPC e a Sub-rede, cria um Security Group, e então usa o comando `aws ec2 run-instances` com um script de `User Data` para lançar e configurar um servidor web completo com banco de dados.

3.  Agora, tente executar o script para ver o que acontece.
    ```bash
    ./create-lamp-instance-v2.sh
    ```
    > **Resultado Esperado:** O script vai falhar. **Isso é intencional.** Agora, começa o trabalho do detetive.

#### Tarefa 3: O Mistério da Imagem Fantasma (Resolvendo o Problema #1)

* **A Pista:** O terminal exibe um erro claro: `An error occurred (InvalidAMIID.NotFound) ... The image id '[ami-xxxxxxxxxx]' does not exist`.
* **A Investigação:**
    1.  Onde no script o erro está acontecendo? (Na chamada `aws ec2 run-instances`).
    2.  O script está pegando o ID da AMI dinamicamente. Por que ele estaria errado? A AMI (`amzn2-ami-hvm-x86_64-gp2`) existe em muitas regiões, mas o ID dela é **diferente em cada Região**.
    3.  Qual Região o script está usando para buscar a AMI? E qual Região ele está usando para *lançar* a instância? Elas são as mesmas?
* **A Solução:** Encontre a linha no script que define a região para o comando `run-instances` e garanta que ela seja a mesma região de onde você buscou o ID da AMI.
* **Verificação:** Execute o script novamente. Ele deve passar da criação da instância e te dar um endereço IP público.

#### Tarefa 4: O Mistério da Porta Fechada (Resolvendo o Problema #2)

* **A Pista:** O script agora funciona, a instância está no ar, mas quando você tenta acessar o IP público no navegador, a conexão falha (`ERR_CONNECTION_TIMED_OUT`).
* **A Investigação:**
    * **Analogia:** "A luz da casa está acesa, mas a porta da frente não abre." Um timeout de conexão quase sempre significa um problema de **firewall** ou **roteamento**.
    1.  O servidor web (`httpd`) está realmente rodando na instância? (Você pode se conectar à nova instância `cafeserver` via **EC2 Instance Connect** e verificar com `sudo systemctl status httpd`).
    2.  Se o serviço está rodando, a "fechadura" da porta está permitindo a entrada? O **Security Group** `cafeSG` que o script criou tem uma regra de entrada para a **porta 80 (HTTP)** a partir da **internet (`0.0.0.0/0`)**?
    3.  **Ferramenta do Detetive:** De volta ao seu `CLI Host`, instale o `nmap` para escanear as portas do seu novo servidor (substitua `<public-ip>` pelo IP do `cafeserver`).
        ```bash
        sudo yum install -y nmap
        nmap -Pn <public-ip>
        ```
        > O `nmap` te dirá se a porta 80 está `open` (aberta) ou `filtered` (filtrada/bloqueada).
* **A Solução:** Encontre a seção no script que cria o `cafeSG` e adicione a regra que falta para permitir o tráfego HTTP.
* **Verificação:** Delete os recursos da tentativa anterior (o script perguntará) e execute o script corrigido novamente. Agora, ao acessar o IP público no navegador, você deverá ver a mensagem: **"Saudações do seu servidor web"**.

#### Tarefa 5: Validando a Aplicação
Com todos os bugs corrigidos, o script deve ter implantado o site completo da cafeteria.

1.  Em um navegador, acesse `http://<public-ip>/cafe`.
2.  **Verificação:** Você deve ver a página da cafeteria. Navegue pelo Menu e faça um pedido para confirmar que o banco de dados também foi configurado corretamente.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns, detetive! Você não apenas executou um script, mas o depurou. Você usou um método lógico para analisar mensagens de erro, inspecionar configurações de rede e verificar logs, habilidades essenciais para qualquer profissional de operações de nuvem no dia a dia.
# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: Vestindo o Chapéu de Detetive na Nuvem

Até agora, minha jornada na nuvem tem sido sobre construir. Criei redes, servidores, sites... Mas, no mundo real, uma grande parte do trabalho não é construir o novo, mas sim **consertar o que quebrou**. O laboratório de hoje foi exatamente sobre isso: uma simulação de um cenário real onde recebi um script de automação com bugs e minha missão era investigar e resolver.

Foi a hora de deixar de ser só o arquiteto e virar o detetive.

### A Missão: Consertar o Robô Construtor

A tarefa era clara: executar um script que deveria criar um servidor web completo (uma pilha LAMP). O problema? O script estava cheio de "minas terrestres" de propósito.

#### Mistério #1: A Imagem Fantasma
* **A Pista:** O script quebrou logo de cara com um erro `InvalidAMIID.NotFound`. Em bom português: "A imagem de máquina que você me pediu para usar não existe."
* **A Investigação:** Como assim não existe? Eu vi o script pegando o ID da AMI mais recente do Amazon Linux! E aí veio o "momento a-ha!".
* **A Descoberta:** O ID de uma AMI (a "planta baixa" de um servidor) **não é universal**. O ID da mesma AMI do Amazon Linux em São Paulo é diferente do ID na Virgínia (EUA). O script estava pegando o ID de uma região, mas tentando lançar a instância em outra.
    * **Analogia:** É como tentar usar um CEP de São Paulo para entregar uma carta no Rio de Janeiro. O carteiro simplesmente não vai encontrar o endereço. A lição foi: a automação precisa ser consciente da Região onde está operando.

#### Mistério #2: A Porta Trancada
* **A Pista:** Com o primeiro bug corrigido, o script rodou até o fim! A instância foi criada, recebi um IP público, tudo parecia perfeito. Mas, ao tentar acessar o site no navegador... nada. O famoso `Connection Timed Out`.
* **A Investigação:** Esse erro é o clássico "pegadinha" do firewall.
    * **Analogia:** A "casa" (instância) estava construída, as "luzes" (o serviço web) estavam acesas, mas a **"porta da frente" (a porta 80 no Security Group) estava trancada**. O cliente não conseguia entrar.
* **A Descoberta:** Usei uma ferramenta de detetive chamada `nmap` para "testar a fechadura" do lado de fora. O resultado foi claro: a porta 80 estava `filtered` (bloqueada). A solução foi encontrar a parte do script que criava o Security Group e adicionar a regra que faltava para permitir a entrada de "visitantes" (tráfego HTTP).

### A Grande Lição
Este lab foi menos sobre escrever código e mais sobre **ler e entender o código dos outros**, e seguir uma **metodologia de troubleshooting**. A lição mais valiosa foi o fluxo de investigação que usei para resolver os dois mistérios:

1.  **Ler o erro** com atenção. A mensagem quase sempre te dá a melhor pista.
2.  **Isolar o problema.** Onde no script ele quebrou?
3.  **Formular uma hipótese.** "Eu acho que é um problema de Região." / "Eu acho que é o firewall."
4.  **Testar a hipótese.** Verificar as configurações de Região ou usar o `nmap`.
5.  **Aplicar a correção.**

Resolver problemas é como um quebra-cabeça. A sensação de encontrar a peça que faltava e ver tudo funcionando é incrivelmente gratificante. Hoje eu não fui só um construtor, fui um detetive, e essa é uma habilidade que sei que vou usar todos os dias na minha carreira em nuvem.

#AWS #Cloud #Troubleshooting #DevOps #SysOps #AWSreStart #EC2 #Networking
