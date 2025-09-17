# <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: A Arquitetura Elástica - Dimensionando e Balanceando com ELB e Auto Scaling

### O Cenário (A "User Story")

> **Como** um arquiteto de nuvem, **EU QUERO** construir uma arquitetura web que distribua o tráfego de forma inteligente e que se adapte automaticamente aos picos de demanda, **PARA QUE** minha aplicação seja altamente disponível, performática e com custos otimizados.

### A Dor que o Lab Resolve

Até agora, lançamos instâncias individuais. Mas uma única instância é um ponto único de falha e não consegue lidar com o tráfego de uma aplicação real. Este laboratório resolve a dor da **infraestrutura estática e frágil**, ensinando o padrão de arquitetura mais fundamental da nuvem para aplicações web.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Criar uma Imagem de Máquina da Amazon (AMI) customizada a partir de uma instância existente.
* [ ] Criar e configurar um Application Load Balancer.
* [ ] Criar um Modelo de Lançamento (Launch Template) para padronizar suas instâncias.
* [ ] Configurar um Grupo de Auto Scaling para automatizar a escalabilidade e a auto-cura.
* [ ] Testar e verificar a arquitetura sob carga.

### Duração
* Aproximadamente 45 minutos.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: Construindo a Arquitetura

#### Tarefa 1: A Receita da Pizza Perfeita (Criando a AMI)

**Analogia:** Antes de contratar pizzaiolos, precisamos da **"receita e do método de treinamento padrão"**. Uma AMI é isso: o molde perfeito do nosso servidor.

1.  No Console da AWS, navegue até **EC2 > Instâncias (Instances)**.
2.  Selecione a instância `Web Server 1`, que já foi provisionada para você.
3.  Vá em **Ações (Actions)** > **Imagem e modelos (Image and templates)** > **Criar imagem (Create image)**.
4.  Configure:
    * **Nome da imagem (Image name):** `AMI-ServidorWeb`
    * **Descrição da imagem (Image description):** `AMI do Lab para o Servidor Web`
5.  Clique em **Criar imagem (Create image)**.

#### Tarefa 2: O Gerente do Balcão (Criando o Load Balancer)

**Analogia:** Agora, vamos contratar o **"gerente do balcão" (ELB)**, que irá distribuir os pedidos.

1.  No menu do EC2, vá em **Balanceadores de Carga (Load Balancers)** e clique em **Criar balanceador de carga (Create Load Balancer)**.
2.  Selecione **Criar (Create)** sob **Application Load Balancer**.
3.  **Configuração básica (Basic configuration):**
    * **Nome:** `LabELB`
4.  **Mapeamento de rede (Network mapping):**
    * **VPC:** `VPC do laboratório (Lab VPC)`.
    * **Mapeamentos (Mappings):** Marque as **duas Zonas de Disponibilidade**. Associe a `Sub-rede pública 1` à primeira e a `Sub-rede pública 2` à segunda.
5.  **Grupos de segurança (Security groups):** Remova o grupo padrão e selecione `Grupo de segurança da web (WebSecurityGroup)`.
6.  **Ouvintes e roteamento (Listeners and routing):**
    * Na regra padrão da porta 80, clique em **Criar grupo de destino (Create target group)**. (Isso abrirá uma nova aba).
7.  **Na nova aba (Criar grupo de destino):**
    * **Tipo de destino (target type):** `Instâncias (Instances)`.
    * **Nome do grupo de destino:** `lab-target-group`.
    * Clique em **Próximo (Next)** e depois em **Criar grupo de destino (Create target group)**. Feche esta aba.
8.  **De volta à aba de criação do Load Balancer:**
    * Clique no ícone de atualização ao lado da lista de grupos de destino.
    * Selecione `lab-target-group` na lista.
9.  Clique em **Criar balanceador de carga (Create load balancer)**.
10. Após a criação, copie o **Nome DNS (DNS name)** do seu `LabELB`. Guarde-o para mais tarde.

#### Tarefa 3: O Manual de Contratação (Criando o Modelo de Lançamento)

**Analogia:** Agora, vamos criar o **"manual de contratação" (Launch Template)** que o nosso gerente geral usará.

1.  No menu do EC2, vá em **Modelos de execução (Launch Templates)** e clique em **Criar modelo de execução**.
2.  **Nome:** `lab-app-launch-template`.
3.  **Descrição:** `Servidor web para o app de teste de carga`.
4.  Marque a caixa **Orientação sobre o Auto Scaling**.
5.  **AMI:** Na aba **Minhas AMIs (My AMIs)**, selecione a `AMI-ServidorWeb`.
6.  **Tipo de instância:** `t3.micro`.
7.  **Par de chaves (Key pair):** `Não incluir no modelo de execução`.
8.  **Configurações de rede (Network settings):** Em *Grupos de segurança*, selecione `Grupo de segurança da web (WebSecurityGroup)`.
9.  Clique em **Criar modelo de execução (Create launch template)**.

#### Tarefa 4: O Gerente Geral Autônomo (Criando o Auto Scaling Group)

**Analogia:** É hora de contratar nosso **"Gerente Geral"** e dar a ele as regras da loja.

1.  Na página do seu novo modelo, vá em **Ações > Criar grupo do Auto Scaling**.
2.  **Nome do grupo:** `Lab-Auto-Scaling-Group`. Clique em **Próximo**.
3.  **Rede:**
    * **VPC:** `VPC do laboratório (Lab VPC)`.
    * **Zonas de disponibilidade e sub-redes:** Selecione a `Sub-rede privada 1` e a `Sub-rede privada 2`.
4.  Clique em **Próximo**.
5.  **Configurar opções avançadas:**
    * **Balanceamento de carga:** Selecione **Anexar a um balanceador de carga existente**.
    * Escolha **entre seus grupos de destino** e selecione `lab-target-group`.
    * **Verificações de integridade:** Marque a caixa **ELB**.
6.  Clique em **Próximo**.
7.  **Configurar tamanho do grupo e políticas:**
    * **Capacidade desejada:** `2`
    * **Capacidade mínima:** `2`
    * **Capacidade máxima:** `4`
    * **Políticas de escalabilidade:** Selecione **Política de escalabilidade de rastreamento de destino (Target tracking scaling policy)**.
    * **Tipo de métrica:** `Média de utilização da CPU (Average CPU utilization)`.
    * **Valor de destino:** `50`.
8.  Clique em **Próximo** até a última tela e clique em **Criar grupo do Auto Scaling**.

#### Tarefa 5 e 6: Verificando e Testando a Arquitetura

1.  **Verifique os Alvos:** No menu do EC2, vá em **Grupos de destino (Target groups)**, selecione `lab-target-group` e vá para a aba **Destinos (Targets)**. Aguarde até que o **Status** de ambas as instâncias mude para **íntegro (healthy)**.
2.  **Teste o ELB:** Cole o **Nome DNS** do seu `LabELB` no navegador. A aplicação "Teste de Carga" deve aparecer.
3.  **Teste o Auto Scaling:** Na página da aplicação no navegador, clique em **Load Test**. Isso iniciará um processo para aumentar o uso de CPU nos servidores.
4.  **Monitore o Alarme:** No console, vá para o serviço **CloudWatch** > **Todos os alarmes**. Você verá que o alarme `AlarmHigh` entrará no estado **Em alarme (In alarm)** após alguns minutos.
5.  **Veja a Mágica:** Volte para a lista de **Instâncias** do EC2. Você verá que o Auto Scaling está lançando **novas instâncias** (até o máximo de 4) para lidar com a carga!

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos
* [ ] No **Auto Scaling**, delete o `Lab-Auto-Scaling-Group`.
* [ ] Delete o **Launch Template**.
* [ ] Delete o **Load Balancer** `LabELB` e seu **Target Group**.
* [ ] Em **AMIs**, desregistre a `AMI-ServidorWeb` e delete o snapshot associado.
* [ ] Termine a instância `Web Server 1` original.

#### Tarefa 7: Limpando o Molde Original

Agora que nossa fábrica de servidores (o Auto Scaling Group) está funcionando e usando nossa nova AMI, não precisamos mais da instância original que usamos como molde. Vamos encerrá-la para seguir as melhores práticas e evitar custos.

1.  No console do **EC2**, no menu esquerdo, vá para **Instâncias (Instances)**.
2.  Selecione a instância **Web Server 1**. Tenha certeza de que é a instância original, e não as que foram criadas pelo Auto Scaling (que têm o nome `Lab Instance`).
3.  Com ela selecionada, vá no menu **Estado da instância (Instance state)** e clique em **Encerrar instância (Terminate instance)**.
4.  Confirme a ação.

---

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: O Dia em que Minha Aplicação Ganhou Vida

Hoje foi um daqueles dias que marcam a jornada de aprendizado. Até agora, eu vinha construindo as "peças" da minha infraestrutura na AWS: um servidor aqui, um firewall ali. Mas hoje, no lab do AWS re/Start, eu juntei todas essas peças para criar algo que se parece com um organismo vivo: uma arquitetura que se adapta, cresce e se cura sozinha.

A missão era construir uma aplicação web totalmente elástica, usando o "Trio Fantástico" da AWS: ELB, Auto Scaling e AMIs customizadas.

### A Jornada em 4 Atos

#### Ato 1: A Receita da Pizza Perfeita (A "Golden AMI")
* **A Dor:** Se eu preciso de 10 servidores web para lidar com o tráfego, como garanto que todos sejam *exatamente* iguais e já venham prontos para trabalhar?
* **O Que Eu Fiz:** Primeiro, eu configurei um servidor "molde" com tudo que era necessário (servidor web, arquivos do site, etc.). Depois, tirei uma "fotografia" dele, criando uma **Imagem de Máquina da Amazon (AMI)** customizada.
* **O "Aha!" Moment:** A AMI é a **"receita-mestra"**. Em vez de ensinar cada novo "pizzaiolo" (instância) do zero, eu criei um manual de treinamento perfeito. Agora, toda nova contratação resulta em um pizzaiolo clone, pronto para trabalhar em segundos.

#### Ato 2: O Manual de Contratação (O Launch Template)
* **A Dor:** Como o "gerente geral" (o Auto Scaling) sabe exatamente como contratar um novo "pizzaiolo"?
* **O Que Eu Fiz:** Criei um **Modelo de Lançamento (Launch Template)**.
* **O "Aha!" Moment:** O Launch Template é o **"manual de contratação"** oficial. Ele diz: "Para todo novo contratado, use a 'receita-mestra' (`AMI-ServidorWeb`), dê a ele o uniforme `t3.micro` e o crachá de acesso do `SG-Servidor-Web`." É a padronização em ação.

#### Ato 3: O Gerente Geral Autônomo (O Auto Scaling Group)
* **A Dor:** Como o sistema reage sozinho aos picos de pedidos da sexta-feira à noite e à calmaria da segunda de manhã?
* **O Que Eu Fiz:** Criei o **Grupo de Auto Scaling (ASG)** e o conectei ao **Elastic Load Balancer (ELB)**.
* **O "Aha!" Moment:** Essa foi a parte mais incrível. Eu contratei o **"Gerente Geral" (o ASG)** e dei a ele regras simples:
    1.  **A Meta:** "Mantenha a 'taxa de estresse' (`CPUUtilization`) média dos pizzaiolos em 50%."
    2.  **Os Limites:** "Tenha sempre no mínimo 2 pizzaiolos, e no máximo 4."
    3.  **O Contato:** "Converse com o 'Gerente do Balcão' (o ELB) para saber quais pizzaiolos estão saudáveis."

#### Ato 4: O Teste de Estresse (Ver a Mágica Acontecer)
* **A Experiência:** A melhor parte foi simular um pico de tráfego. Ver o alarme do CloudWatch disparar e, segundos depois, ver as novas instâncias aparecendo **sozinhas** na lista do EC2 foi... mágico.
* **A Prova Final:** O teste de "auto-cura". Eu deliberadamente **deletei** uma das instâncias em execução. Em vez de pânico, o "Gerente Geral" (ASG) calmamente detectou a "doença", removeu o servidor da lista e **contratou um novo clone saudável** para manter a meta de 2 pizzaiolos.

### A Grande Lição
O lab de hoje me mostrou que a nuvem não é sobre servidores. É sobre construir **sistemas**. Cada serviço (AMI, ELB, ASG, CloudWatch) é uma peça de um quebra-cabeça, e a habilidade do arquiteto é saber como juntá-las para criar um organismo que se adapta e se cura sozinho.

Construir essa arquitetura elástica do zero foi como ver o motor de um carro funcionando pela primeira vez. De repente, os conceitos de **Alta Disponibilidade** e **Elasticidade** deixaram de ser palavras em um slide e se tornaram algo real, que eu construí. É um divisor de águas na minha jornada.

#AWS #Cloud #AutoScaling #HighAvailability #DevOps #AWSreStart #CloudPractitioner