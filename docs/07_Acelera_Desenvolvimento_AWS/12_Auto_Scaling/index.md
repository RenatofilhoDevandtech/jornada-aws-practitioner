# <img src="https://api.iconify.design/logos/aws-auto-scaling.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Frota Autônoma: Guia Prático do Amazon EC2 Auto Scaling

**A Dor:** No mundo tradicional, você enfrenta um dilema impossível.
* **Se comprar servidores para o pico de tráfego (Black Friday):** Você desperdiça dinheiro 99% do tempo, com máquinas caras e ociosas.
* **Se comprar servidores para o tráfego médio:** Você perde clientes e dinheiro durante os picos, pois seu site fica lento ou sai do ar.

O **Amazon EC2 Auto Scaling** resolve essa dor, garantindo que você tenha **sempre** a quantidade certa de capacidade computacional: nem mais, nem menos.

**Analogia:** Pense no Auto Scaling como o **"Sistema de Gerenciamento de Pessoal Autônomo"** da sua pizzaria.

---

### <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Anatomia do Auto Scaling

Para configurar um sistema autônomo, você precisa de dois componentes principais:

#### <img src="https://api.iconify.design/mdi/clipboard-file-outline.svg?color=currentColor" width="20" /> O Modelo de Lançamento (Launch Template)
* **O que é?** A "planta baixa" ou a "receita" de como criar uma nova instância EC2.
* **Analogia:** O **"Manual de Contratação e Treinamento do Pizzaiolo Padrão"**.
* **Como Funciona:** Você define tudo o que uma nova instância precisa: a AMI, o tipo de instância, o par de chaves, os security groups, o user data, etc.

#### <img src="https://api.iconify.design/mdi/account-group-outline.svg?color=currentColor" width="20" /> O Grupo de Auto Scaling (Auto Scaling Group - ASG)
* **O que é?** O "gerente" que usa o Modelo de Lançamento para criar e gerenciar a frota de instâncias.
* **Analogia:** O **"Gerente Geral"** da pizzaria.
* **As 3 Métricas Mágicas:** Ao configurar um ASG, você define três números:
    * **Mínimo:** "Devemos ter **no mínimo 2** pizzaiolos na loja, para garantir a alta disponibilidade."
    * **Máximo:** "Não podemos ter **mais de 10** pizzaiolos, para controlar os custos."
    * **Capacidade Desejada:** "Neste momento, o ideal é ter **3** pizzaiolos trabalhando."

---

### <img src="https://api.iconify.design/mdi/brain.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Cérebro da Operação (As Políticas de Escalabilidade)

Como o "Gerente Geral" (ASG) sabe quando contratar ou dispensar? Através das Políticas de Escalabilidade.

* **<img src="https://api.iconify.design/mdi/target-account.svg?color=currentColor" width="18" /> Rastreamento de Alvo (Target Tracking) - O Piloto Automático:**
    * **O que é?** A forma mais simples e recomendada. Você define um alvo para uma métrica.
    * **Analogia:** "Mantenha a 'taxa de estresse' (`CPUUtilization`) média dos pizzaiolos em **50%**." Se a média subir, o ASG contrata mais gente. Se cair, ele dispensa.

* **<img src="https://api.iconify.design/mdi/calendar-clock.svg?color=currentColor" width="18" /> Agendado (Scheduled Scaling) - O Planejador:**
    * **O que é?** Para picos de demanda previsíveis.
    * **Analogia:** "**Toda sexta-feira às 18h**, contrate 5 pizzaiolos extras. No **domingo à noite**, dispense-os."

* **<img src="https://api.iconify.design/mdi/stairs.svg?color=currentColor" width="18" /> Por Etapas (Step Scaling) - O Controle Fino:**
    * **O que é?** Uma forma mais avançada, onde você define regras como: "Se a CPU passar de 70%, adicione 1 instância. Se passar de 90%, adicione mais 3 instâncias."

---

### <img src="https://api.iconify.design/mdi/heart-pulse.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Sistema Imunológico (Health Checks e Auto-cura)

**A Dor que Resolve:** O que acontece quando uma instância EC2 trava ou falha?

* **Como Funciona:** O Auto Scaling monitora continuamente a saúde de cada instância na frota. Ele pode usar as verificações de status do próprio EC2 ou, de forma ainda mais inteligente, as **verificações de saúde do Elastic Load Balancer**.
* **O Resultado (Auto-cura):** Se uma instância é marcada como "não saudável" (`unhealthy`), o ASG entra em ação:
    1.  **Termina** a instância doente.
    2.  **Lança** uma nova instância, idêntica e saudável, a partir do Modelo de Lançamento para substituí-la.
* **Analogia:** A **"política de saúde e segurança"** da pizzaria. Se um pizzaiolo passar mal, o sistema o dispensa e contrata imediatamente um novo clone treinado pelo "Manual de Contratação".

#### <img src="https://api.iconify.design/mdi/account-remove-outline.svg?color=currentColor" width="20" /> A Política de Encerramento (Termination Policy)
* **O que é?** A regra que o ASG usa para decidir **qual** instância demitir durante um evento de *scale in* (redução).
* **A Regra Padrão:** Geralmente, ele escolhe a instância mais antiga para garantir que a frota esteja sempre se renovando.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova Cloud Practitioner:
> 1.  **Auto Scaling** é o serviço que adiciona (`scale out`) e remove (`scale in`) instâncias **EC2** automaticamente.
> 2.  Os três componentes principais são: **Launch Template** (o quê lançar), **Auto Scaling Group** (onde e como gerenciar) e **Scaling Policy** (quando escalar).
> 3.  Entenda que o Auto Scaling é a chave para a **Elasticidade** e, quando combinado com múltiplas AZs e um ELB, para a **Alta Disponibilidade** e **Tolerância a Falhas** (através da auto-cura).

---

### <img src="https://api.iconify.design/mdi/brain.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Cérebro da Elasticidade: Guia de Políticas de Auto Scaling

Já sabemos que o Auto Scaling é o nosso "Gerente Geral Autônomo". Mas como ele sabe quando contratar ou dispensar "pizzaiolos" (instâncias EC2)? Ele segue um **livro de regras** que nós definimos: as **Políticas de Escalabilidade**.

Dominar estas políticas é a chave para criar uma arquitetura que se adapta perfeitamente ao ritmo do seu negócio, otimizando tanto a performance quanto os custos.

---

### <img src="https://api.iconify.design/mdi-chart-line.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. As Políticas de Escalabilidade (O Livro de Regras)

Existem três tipos principais de regras que podemos dar ao nosso "Gerente".

#### <img src="https://api.iconify.design/mdi/calendar-clock.svg?color=currentColor" width="20" /> O Planejador (Dimensionamento Agendado)
* **A Dor que Resolve:** Picos de demanda **previsíveis e recorrentes**.
* **Analogia:** A **"Regra de Calendário"**.
* **Como Funciona:** Você cria uma regra baseada em data e hora.
    * **Exemplo:** "Toda sexta-feira às 18:00, aumente a `Capacidade Desejada` para 10 instâncias. Todo domingo às 23:00, reduza a `Capacidade Desejada` de volta para 2."

#### <img src="https://api.iconify.design/mdi/thermostat.svg?color=currentColor" width="20" /> O Piloto Automático (Rastreamento de Alvo - Target Tracking)
* **A Dor que Resolve:** Picos de demanda **imprevisíveis**.
* **Analogia:** A **"Regra do Termostato"**.
* **Como Funciona:** Você escolhe uma métrica (como `Utilização Média da CPU`) e define um alvo. O Auto Scaling faz todo o trabalho de adicionar e remover instâncias para manter a métrica perto do seu alvo.
    * **Exemplo:** "Mantenha a utilização média de CPU da minha frota em **50%**." Se a CPU subir para 70%, ele adiciona instâncias. Se cair para 30%, ele remove.
> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> Insight:** Esta é a política **mais recomendada pela AWS** para a maioria dos casos de uso. É a mais simples de configurar e a mais eficaz.

#### <img src="https://api.iconify.design/mdi/stairs.svg?color=currentColor" width="20" /> A Resposta de Emergência (Dimensionamento por Etapas - Step Scaling)
* **A Dor que Resolve:** A necessidade de uma resposta mais agressiva para picos muito súbitos.
* **Analogia:** A **"Regra de Emergência Gradual"**.
* **Como Funciona:** Você define diferentes ações com base no tamanho da violação de um alarme do CloudWatch.
    * **Exemplo:** "SE a CPU passar de 70%, adicione 1 instância. MAS SE ela passar de 90%, adicione 5 instâncias de uma vez!"

---

### <img src="https://api.iconify.design/mdi/account-remove-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Lado Oposto: As Políticas de Encerramento

**A Dor que Resolve:** "Quando o Auto Scaling precisa reduzir a frota (scale in), como ele escolhe qual instância 'demitir'?"

O Auto Scaling segue uma **Política de Encerramento (Termination Policy)**. A padrão é segura e busca balancear as instâncias entre as Zonas de Disponibilidade. Mas você pode customizá-la:

* **`OldestInstance`:** Demite a instância mais antiga. Útil para gradualmente renovar sua frota com novos tipos de instância.
* **`NewestInstance`:** Demite a instância mais nova. Útil para testar um novo Modelo de Lançamento e fazer rollback rapidamente se algo der errado.
* **`OldestLaunchTemplate`:** Demite instâncias que foram criadas com uma versão mais antiga do seu Modelo de Lançamento.
* **`ClosestToNextInstanceHour`:** Demite a instância que está mais perto de completar uma hora cheia de faturamento (uma estratégia de otimização de custos mais antiga).

---

### <img src="https://api.iconify.design/mdi/security.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Caso de Uso Especial: O Grupo de Estado Fixo

**A Dor que Resolve:** "Eu tenho um serviço crítico, como um servidor NAT ou um host bastião, que não precisa escalar, mas eu preciso garantir que **sempre** haja *exatamente um* rodando e que ele seja substituído automaticamente se falhar."

* **A Solução:** Crie um Auto Scaling Group com a seguinte configuração:
    * **Mínimo = 1**
    * **Máximo = 1**
    * **Capacidade Desejada = 1**
* **Analogia:** A **"Política do Guarda Noturno"**.
* **O Resultado:** O Auto Scaling não irá escalar para cima ou para baixo. Sua única função será atuar como um **sistema de auto-cura**. Se a única instância falhar em uma verificação de saúde, o ASG a terminará e lançará um clone perfeito para substituí-la, garantindo a resiliência do seu serviço.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Conheça os **três tipos de políticas de escalabilidade**: **Agendada** (para picos previsíveis), **Dinâmica** (para picos imprevisíveis) e **Preditiva** (um tipo mais novo que usa Machine Learning).
> 2.  **Target Tracking** é o tipo de política dinâmica mais simples e recomendado.
> 3.  O Auto Scaling não serve apenas para **escalabilidade**, mas também para **manter a saúde da frota (auto-cura)**, substituindo instâncias não íntegras.

---

### <img src="https://api.iconify.design/logos/aws-auto-scaling.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Frota Autônoma: Guia Definitivo do Amazon EC2 Auto Scaling

**A Dor:** No mundo tradicional, você enfrenta um dilema impossível: comprar servidores para o pico de tráfego (e desperdiçar dinheiro 99% do tempo) ou para o tráfego médio (e perder clientes nos picos).

O **Amazon EC2 Auto Scaling** resolve essa dor, garantindo que você tenha **sempre** a quantidade certa de capacidade.

**Analogia:** Pense no Auto Scaling como o **"Sistema de Gerenciamento de Pessoal Autônomo"** da sua pizzaria.

---

### <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Anatomia do Auto Scaling

* **<img src="https://api.iconify.design/mdi/clipboard-file-outline.svg?color=currentColor" width="18" /> Modelo de Lançamento (Launch Template):** O **"Manual de Contratação e Treinamento"** que define como criar um "pizzaiolo" (instância) perfeito.
* **<img src="https://api.iconify.design/mdi/account-group-outline.svg?color=currentColor" width="18" /> Grupo de Auto Scaling (ASG):** O **"Gerente Geral"** que usa o manual para gerenciar a frota, mantendo-a entre os tamanhos **Mínimo**, **Máximo** e **Desejado**.

---

### <img src="https://api.iconify.design/mdi/brain.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Cérebro da Operação (As Políticas de Escalabilidade)

Estas são as "regras de negócio" do seu Gerente Geral Autônomo.

* **<img src="https://api.iconify.design/mdi/calendar-clock.svg?color=currentColor" width="18" /> Dimensionamento Agendado:** A **"Regra de Calendário"** para picos previsíveis. ("Toda sexta às 18h, contrate 5 pizzaiolos").
* **<img src="https://api.iconify.design/mdi/thermostat.svg?color=currentColor" width="18" /> Rastreamento de Alvo (Target Tracking):** O **"Piloto Automático Reativo"**. ("Mantenha o 'estresse' médio da cozinha em 50%").
* **<img src="https://api.iconify.design/mdi/stairs.svg?color=currentColor" width="18" /> Dimensionamento por Etapas (Step Scaling):** A **"Resposta de Emergência Gradual"** para picos súbitos. ("Se o estresse passar de 90%, contrate 5 de uma vez!").

#### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="20" /> O Vidente (Dimensionamento Preditivo - Predictive Scaling)
* **A Dor que Resolve:** O dimensionamento dinâmico é **reativo**. Pode haver um pequeno atraso entre o início do pico de tráfego e as novas instâncias estarem prontas.
* **Como Funciona:** Usa **Machine Learning** para analisar o histórico de tráfego da sua aplicação (padrões diários e semanais) e **prever** os picos futuros.
* **Analogia:** O **"Gerente Geral com uma Bola de Cristal"**. Ele prevê que no sábado, por causa de um jogo, haverá um pico às 19h. Em vez de esperar a fila se formar, ele **contrata os pizzaiolos extras às 18:30**, para que eles já estejam prontos **antes** do pico começar.
* **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> Insight de Especialista:** A melhor abordagem é usar o Preditivo e o Dinâmico **juntos**. O Preditivo define a capacidade base (o "piso" de instâncias para o pico previsto), e o Dinâmico (Target Tracking) lida com qualquer tráfego inesperado que exceda a previsão.

---

### <img src="https://api.iconify.design/mdi/account-remove-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. As Políticas de Encerramento

Quando o ASG precisa reduzir a frota, ele segue uma **Política de Encerramento**. Você pode customizá-la para:
* **`OldestInstance`:** Remover a instância mais antiga (bom para renovar a frota).
* **`NewestInstance`:** Remover a instância mais nova (bom para reverter um teste).
* **`OldestLaunchTemplate`:** Remover instâncias com a configuração mais antiga.

---

### <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 4. Workshop do Arquiteto: Gerenciando uma Atualização de Frota

Vamos usar as perguntas do seu material para simular um cenário real.

* **A Missão:** Sua equipe criou uma nova AMI com uma versão atualizada da aplicação. Você precisa implantá-la na produção com o mínimo de risco.

* **Pergunta 1:** Qual política de encerramento você usaria?
    * **Resposta:** **`NewestInstance`**.
    * **O Raciocínio:** Ao fazer o *rollout* das novas instâncias, elas serão as "mais novas". Se algo der errado e você precisar fazer um *rollback* (reduzir a frota), esta política garante que as novas instâncias problemáticas sejam as primeiras a serem removidas, revertendo o ambiente para o estado anterior.

* **Pergunta 2:** Como você força a criação das novas instâncias e, se necessário, as remove?
    * **Resposta:**
        1.  **Para criar (Rollout):** Atualize o **Modelo de Lançamento** para usar a nova AMI. Em seguida, **aumente a `Capacidade Desejada`** do seu Auto Scaling Group. O ASG lançará novas instâncias usando o novo modelo.
        2.  **Para remover (Rollback):** Simplesmente **diminua a `Capacidade Desejada`** de volta ao normal. Graças à política `NewestInstance`, as instâncias que serão terminadas são as que você acabou de criar.

* **Pergunta 3:** Todos os servidores recém-criados estão falhando. O que os engenheiros deveriam ter feito?
    * **Resposta:** O erro fundamental foi não ter uma estratégia de reversão para a "planta baixa".
    * **A Ação Correta:** A primeira ação não é apenas diminuir a capacidade. É **atualizar o Modelo de Lançamento de volta para a versão anterior**, que usava a AMI antiga e estável. Isso garante que, mesmo que o ASG precise lançar uma nova instância por qualquer outro motivo, ele lançará uma versão saudável, contendo a falha.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Conheça os **três tipos de políticas de escalabilidade**: **Agendada** (previsível), **Dinâmica** (imprevisível, ex: Target Tracking), e **Preditiva** (usa Machine Learning).
> 2.  O Auto Scaling não serve apenas para **escalabilidade**, mas também para **manter a saúde da frota (auto-cura)**.
> 3.  O **Modelo de Lançamento (Launch Template)** é a "fonte da verdade" sobre como as instâncias devem ser. Para corrigir uma frota com falha, você corrige o modelo.

---

### <img src="https://api.iconify.design/logos/aws-auto-scaling.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: A Pizzaria Elástica - Construindo uma Arquitetura com Auto Scaling

### O Cenário (A "User Story")

> **Como** o dono de uma pizzaria online de sucesso, **EU QUERO** criar uma infraestrutura web que cresça sozinha durante os picos de pedidos de sexta à noite e encolha na calmaria da segunda-feira, **PARA QUE** eu nunca perca uma venda por lentidão e nunca desperdice dinheiro com servidores ociosos.

### A Dor que o Lab Resolve

Um único servidor (instância EC2) não consegue lidar com a variação de tráfego de um negócio real. Ele fica sobrecarregado nos picos (clientes frustrados) e ocioso na baixa (dinheiro desperdiçado). Este laboratório resolve a dor da **capacidade fixa**, criando uma arquitetura que respira junto com o seu negócio.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Criar uma Imagem de Máquina da Amazon (AMI) customizada.
* [ ] Criar uma Configuração de Lançamento (Launch Configuration).
* [ ] Configurar um Grupo de Auto Scaling (Auto Scaling Group).
* [ ] Integrar o grupo com um Balanceador de Carga (ELB).
* [ ] Criar Políticas de Escalabilidade baseadas em alarmes.
* [ ] Testar e verificar o sistema de auto-cura e escalabilidade.

### Pré-requisitos
* Uma VPC com pelo menos duas sub-redes públicas.
* Conhecimento de como lançar uma instância EC2 e configurar um Security Group.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: A Construção da Pizzaria

#### Parte 1: A Receita da Pizza Perfeita (Criando a AMI)

**Analogia:** Antes de contratar pizzaiolos, precisamos da **"receita e do método de treinamento padrão"**. Uma AMI é isso: o molde perfeito do nosso servidor.

1.  **Lance uma Instância "Molde":**
    * Vá para o console do **EC2** e lance uma nova instância `t2.micro` com Amazon Linux.
    * Crie um Security Group que permita acesso **HTTP (porta 80)** de `Anywhere` e **SSH (porta 22)** do `My IP`.
    * No campo **User Data**, cole o script abaixo para instalar o servidor web:
        ```bash
        #!/bin/bash
        yum update -y
        yum install -y httpd
        systemctl start httpd
        systemctl enable httpd
        INSTANCE_ID=$(curl -s [http://169.254.169.254/latest/meta-data/instance-id](http://169.254.169.254/latest/meta-data/instance-id))
        echo "<h1>Servidor Web gerado pela AMI - ID: ${INSTANCE_ID}</h1>" > /var/www/html/index.html
        ```
2.  **Crie a Imagem (a "Receita"):**
    * Após a instância estar no estado `running`, selecione-a.
    * Vá em **Actions** > **Image and templates** > **Create image**.
    * **Image name:** `AMI-ServidorWeb-Pizzaria`.
    * Clique em **Create image**.

> **`!!! tip "Insight de Arquiteto"`**
> Este processo de criar uma "Golden AMI" é uma das melhores práticas do pilar de **Excelência Operacional**. Garante que toda nova instância lançada pelo Auto Scaling seja idêntica e já venha configurada.

#### Parte 2: O Manual de Contratação (A Configuração de Lançamento)

**Analogia:** Agora, vamos criar o **"manual de contratação"** que o nosso gerente geral usará.

1.  No painel do EC2, role para baixo e, em *Auto Scaling*, clique em **Launch Configurations**.
2.  Clique em **Create launch configuration**.
3.  **Name:** `Config-ServidorWeb-Pizzaria`.
4.  **Amazon machine image (AMI):** Clique em `My AMIs` e selecione a `AMI-ServidorWeb-Pizzaria` que você acabou de criar.
5.  **Instance type:** Escolha `t2.micro`.
6.  **Security groups:** Selecione **Select an existing security group** e escolha o grupo que você criou no passo anterior.
7.  **Key pair (login):** Escolha **Proceed without a key pair**.
8.  Clique em **Create launch configuration**.

> **Nota:** A AWS hoje recomenda usar **Launch Templates** em vez de Launch Configurations, pois são mais modernos e flexíveis. No entanto, o conceito é exatamente o mesmo.

#### Parte 3: O Gerente Geral Autônomo (O Grupo de Auto Scaling)

**Analogia:** É hora de contratar nosso **"Gerente Geral"** e dar a ele as regras da loja.

1.  A partir da página de sucesso da criação da Launch Configuration, selecione **Create an Auto Scaling group using this launch configuration**.
2.  **Group name:** `ASG-ServidoresWeb-Pizzaria`.
3.  **Network (Rede):**
    * **VPC:** Escolha sua VPC.
    * **Subnets:** **Selecione as duas sub-redes públicas** da sua VPC.
        > **(Pilar de Confiabilidade):** Ao selecionar múltiplas sub-redes em diferentes AZs, você está construindo uma arquitetura de **alta disponibilidade**.
4.  Clique em **Next**.
5.  **Load balancing:**
    * Selecione **Attach to a new load balancer**.
    * **Load balancer type:** `Application Load Balancer`.
    * **Load balancer name:** `ALB-Pizzaria`.
    * **Health checks:** Marque a caixa `Enable ELB health checks`.
6.  Clique em **Next**.
7.  **Group size (Tamanho do Grupo):**
    * **Desired capacity (Capacidade desejada):** `2`
    * **Minimum capacity (Capacidade mínima):** `2`
    * **Maximum capacity (Capacidade máxima):** `4`
8.  **Scaling policies (Políticas de Escalabilidade):**
    * Selecione **Target tracking scaling policy**.
    * **Metric type:** `Average CPU utilization`.
    * **Target value:** `50` (Isso significa: "Mantenha a CPU média da frota em 50%").
9.  Clique em **Next** até chegar na página final e clique em **Create Auto Scaling group**.

---

### <img src="https://api.iconify.design/mdi/check-all.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Verificação

1.  Vá para a lista de **Instâncias** do EC2. Você verá duas novas instâncias sendo criadas pelo Auto Scaling.
2.  Vá para **Load Balancers**, selecione o `ALB-Pizzaria` e copie seu **DNS name**.
3.  Cole o DNS no seu navegador. Você verá a página do seu servidor web. Atualize a página várias vezes e observe como o ID da instância muda, provando que o ELB está funcionando.
4.  **Teste a Auto-Cura:** Vá para a lista de instâncias e **termine (`Terminate`) uma das duas instâncias** do ASG. Observe o painel do Auto Scaling: ele detectará a "doença", terminará a instância e, para manter a capacidade desejada de 2, lançará um novo clone saudável automaticamente!

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos
* [ ] No painel do **Auto Scaling**, delete o `ASG-ServidoresWeb-Pizzaria` (isso também terminará as instâncias).
* [ ] Delete a **Launch Configuration** `Config-ServidorWeb-Pizzaria`.
* [ ] Delete o **Load Balancer** `ALB-Pizzaria` e seu **Target Group**.
* [ ] Em **AMIs**, desregistre a `AMI-ServidorWeb-Pizzaria` e delete o snapshot associado.
* [ ] Delete a instância "molde" original e seu Security Group.

---

### <img src="https://api.iconify.design/mdi/tune-variant.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Ajuste Fino da Frota: Guia de Estabilidade e Hooks de Ciclo de Vida

Já sabemos como fazer nossa frota de servidores crescer e encolher. Mas um sistema de escalabilidade mal configurado pode ser "ansioso": ele contrata e demite "pizzaiolos" rápido demais, causando instabilidade e custos desnecessários.

Este guia ensina as técnicas de especialista para dar "bom senso" ao seu Auto Scaling Group e para inserir etapas customizadas no processo de escalabilidade.

---

### <img src="https://api.iconify.design/mdi/timer-sand.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Problema da Hiperatividade (Evitando o "Thrashing")

**A Dor:** Se a CPU sobe por 30 segundos, o Auto Scaling adiciona uma instância. Se 1 minuto depois ela cai, ele remove a instância. Esse ciclo de escalar para cima e para baixo rapidamente é chamado de **thrashing**. Ele é ineficiente e instável.

**A Solução:** Ensinar "paciência" ao nosso "Gerente Geral Autônomo" com três ferramentas de estabilização.

* **<img src="https://api.iconify.design/mdi/timelapse.svg?color=currentColor" width="18" /> Período de Sustentação do Alarme:**
    * **A Regra:** "Só tome uma decisão se a condição (ex: CPU alta) persistir por um **período contínuo** (ex: 5 minutos)."
    * **Por quê?** Ignora picos de tráfego transitórios e age apenas em tendências reais.

* **<img src="https://api.iconify.design/mdi/coffee-outline.svg?color=currentColor" width="18" /> Período de Cooldown:**
    * **A Regra:** "Depois que você tomar uma ação de escalabilidade (contratar ou demitir), faça uma **pausa** (ex: 5 minutos) antes de avaliar a situação novamente."
    * **Por quê?** Dá tempo para que a nova instância comece a trabalhar e o sistema se estabilize antes de tomar outra decisão precipitada.

* **<img src="https://api.iconify.design/mdi/heat-wave.svg?color=currentColor" width="18" /> Período de Aquecimento da Instância (Warm-up):**
    * **A Regra:** "Quando um novo 'pizzaiolo' (instância) é contratado, ele leva 3 minutos para 'esquentar' (iniciar a aplicação). **Não o inclua no cálculo da 'taxa de estresse' média** da frota até que ele esteja 100% pronto."
    * **Por quê?** Evita que o Auto Scaling contrate ainda mais gente desnecessariamente, pois ele ignora a capacidade das instâncias que ainda estão inicializando.

---

### <img src="https://api.iconify.design/mdi/hook.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Procedimento Customizado (Ganchos de Ciclo de Vida - Lifecycle Hooks)

**A Dor:** "Quando uma nova instância é lançada, ela precisa baixar arquivos de configuração ou se registrar em um sistema antes de poder receber tráfego. Se o Load Balancer mandar tráfego para ela imediatamente, os usuários verão erros."

**A Solução:** **Lifecycle Hooks**. Eles permitem que você **pause** o processo de escalabilidade para executar ações customizadas.

* **Analogia:** Um **"Procedimento de Onboarding e Offboarding Personalizado"**.

* **<img src="https://api.iconify.design/mdi/arrow-up-bold-box-outline.svg?color=currentColor" width="18" /> Hook de Scale-Out:**
    * **Como Funciona:** Quando o ASG lança uma nova instância, o hook a coloca em um estado de espera (`Pending:Wait`).
    * **Analogia:** "Gerente, quando você contratar um novo pizzaiolo, **não o coloque para fazer pizza imediatamente**. Chame o 'Chef de Treinamento' (um script ou uma função Lambda) para ensinar a ele a receita secreta. **Só depois que o Chef der o 'ok'**, libere o pizzaiolo para o balcão."

* **<img src="https://api.iconify.design/mdi/arrow-down-bold-box-outline.svg?color=currentColor" width="18" /> Hook de Scale-In:**
    * **Como Funciona:** Quando o ASG decide terminar uma instância, o hook a coloca em um estado de espera (`Terminating:Wait`).
    * **Analogia:** "Gerente, quando for dispensar um pizzaiolo, **não o mande embora imediatamente**. Chame a 'Equipe de TI' (um script) para **fazer o backup dos logs e anotações** dele. **Só depois que a equipe der o 'ok'**, dispense-o."

---

### <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. Workshop do Arquiteto (Revisão Prática)

Vamos usar as perguntas do seu material para simular um cenário real.

* **A Missão:** Sua equipe criou uma nova AMI. Você precisa implantá-la na produção com o mínimo de risco.

* **Pergunta 1:** Qual política de encerramento você usaria?
    * **Resposta:** **`NewestInstance`**.
    * **O Raciocínio:** Ao fazer o *rollout* das novas instâncias, elas serão as "mais novas". Se algo der errado e você precisar fazer um *rollback*, esta política garante que as novas instâncias problemáticas sejam as primeiras a serem removidas.

* **Pergunta 2 e 3:** Como forçar a criação e, se necessário, a remoção das novas instâncias?
    * **Resposta:**
        1.  **Para criar:** Atualize o **Modelo de Lançamento** para usar a nova AMI. Em seguida, **aumente a `Capacidade Desejada`** do ASG.
        2.  **Para remover:** Simplesmente **diminua a `Capacidade Desejada`**. Graças à política `NewestInstance`, as instâncias que serão terminadas são as que você acabou de criar.

* **Pergunta 4:** Todos os servidores recém-criados estão falhando. O que os engenheiros deveriam ter feito?
    * **Resposta:** O erro foi não ter uma estratégia de reversão para a "planta baixa". A primeira ação é **atualizar o Modelo de Lançamento de volta para a versão que usava a AMI antiga e estável**. Isso garante que qualquer nova instância que o ASG precise lançar (mesmo que por uma falha de AZ) já nascerá saudável.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  O conceito de **Cooldown** e **Warm-up** é importante para entender como o Auto Scaling evita instabilidade.
> 2.  Os **Lifecycle Hooks** são um conceito mais avançado, mas saber que eles existem para executar **ações customizadas durante o lançamento ou o término** de uma instância é um diferencial.
> 3.  O Auto Scaling usa **Health Checks** para manter a saúde da frota.