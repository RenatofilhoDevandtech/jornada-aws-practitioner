# <img src="https://api.iconify.design/logos/aws-route-53.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Plano de Contingência - Configurando Roteamento de Failover com Route 53

### O Cenário (A "User Story")

> **Como** o arquiteto de uma aplicação crítica, **EU QUERO** configurar o DNS para detectar falhas no meu servidor principal e redirecionar automaticamente o tráfego para um servidor de backup, **PARA QUE** minha aplicação permaneça disponível para os usuários mesmo durante uma interrupção.

### A Dor que o Lab Resolve

Ter servidores em múltiplas Zonas de Disponibilidade é ótimo, mas não adianta se seus usuários continuam sendo enviados para o servidor que acabou de falhar. A dor que este lab resolve é a **falta de detecção e resposta automática a falhas**. Vamos ensinar o Route 53 a ser o "vigia" inteligente da nossa aplicação.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Configurar uma Verificação de Integridade (Health Check) no Route 53.
* [ ] Criar um tópico SNS para receber notificações de falha por e-mail.
* [ ] Configurar uma Política de Roteamento de Failover (Failover Routing Policy).
* [ ] Simular uma falha e verificar o redirecionamento automático do tráfego.


### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Confirmando as "Pizzarias"

**Analogia:** Primeiro, vamos confirmar que nossas duas lojas de pizza, a `Primária` e a `Secundária`, estão abertas e funcionando em "bairros" (AZs) diferentes.

1.  No painel do laboratório, clique em **Detalhes > Mostrar (Details > Show)**.
2.  Copie os valores de `PrimaryWebSiteURL` e `SecondaryWebsiteURL`.
3.  Abra cada URL em uma nova aba do navegador. Confirme que ambos os sites da cafeteria estão no ar. Observe na seção **Informações do servidor (Server Information)** que eles estão em Zonas de Disponibilidade diferentes (ex: `us-west-2a` e `us-west-2b`).

#### Tarefa 2: Contratando o "Vigia" (Configurando a Health Check)

**Analogia:** Vamos configurar um "vigia" automático que fica "ligando" para a nossa pizzaria principal a cada 10 segundos para ver se ela atende.

1.  No Console da AWS, navegue até o serviço **Route 53**.
2.  No menu esquerdo, selecione **Verificações de integridade (Health checks)**.
3.  Clique em **Criar verificação de integridade (Create health check)** e configure:
    * **Nome (Name):** `Verificacao-Site-Primario`.
    * **O que monitorar (What to monitor):** `Endpoint`.
    * **Especificar endpoint por (Specify endpoint by):** `Endereço IP (IP address)`.
    * **Endereço IP (IP address):** Cole o valor de `CafeInstance1IPAddress` do painel de detalhes do lab.
    * **Caminho (Path):** `cafe`.
4.  Expanda **Configuração avançada (Advanced configuration)**:
    * **Intervalo de solicitações (Request interval):** `Rápido (10 segundos)`.
    * **Limite de falha (Failure threshold):** `2`.
        > **O "Porquê":** Estamos dizendo ao "vigia" para ligar a cada 10 segundos. Se a pizzaria não atender por 2 vezes seguidas (20 segundos), ele deve declarar que a loja está "fechada" (não íntegra).
5.  Clique em **Próximo (Next)**.
6.  **Criar alarme (Create alarm):** Selecione **Sim (Yes)**.
    * **Enviar notificação para (Send notification to):** `Novo tópico do SNS (New SNS topic)`.
    * **Nome do tópico (Topic name):** `Alerta-Site-Primario-Fora`.
    * **Endereço de e-mail do destinatário (Recipient email address):** Insira seu e-mail.
7.  Clique em **Criar verificação de integridade (Create health check)**.
8.  **Ação Crítica:** Vá para sua caixa de e-mail, encontre o e-mail da "AWS Notifications" e clique no link **Confirm subscription**. Sem isso, você não receberá os alertas.

#### Tarefa 3: Desenhando o "Mapa de Contingência" (Configurando os Registros)

**Analogia:** Agora, vamos ensinar à nossa "central telefônica" (Route 53) o plano de contingência.

1.  No console do **Route 53**, vá em **Zonas hospedadas (Hosted zones)**.
2.  Clique no nome de domínio do seu laboratório (ex: `...vocareum.training`).
3.  Clique em **Criar registro (Create record)**.

##### Registro A - O Primário
1.  **Nome do registro (Record name):** `www`.
2.  **Tipo de registro (Record type):** `A`.
3.  **Valor (Value):** Cole o IP de `CafeInstance1IPAddress`.
4.  **Política de roteamento (Routing policy):** `Failover`.
5.  **Tipo de registro de failover (Failover record type):** `Primário (Primary)`.
6.  **ID da verificação de integridade (Health check ID):** Selecione a `Verificacao-Site-Primario` que criamos.
7.  **ID do registro (Record ID):** `Site-Primario`.
8.  Clique em **Criar registros (Create records)**.

##### Registro A - O Secundário
1.  Clique em **Criar registro (Create record)** novamente.
2.  **Nome do registro:** `www`.
3.  **Tipo de registro:** `A`.
4.  **Valor:** Cole o IP de `CafeInstance2IPAddress`.
5.  **Política de roteamento:** `Failover`.
6.  **Tipo de registro de failover:** `Secundário (Secondary)`.
7.  **ID do registro:** `Site-Secundario`.
8.  Clique em **Criar registros**.

#### Tarefa 4: Simular o Desastre e Verificar o Failover
1.  **Verifique o Acesso Normal:** Em uma nova aba, acesse `http://www.<SEU_DOMINIO_DO_LAB>/cafe`. Você deve ver o site da **CafeInstance1**.
2.  **Simule a Falha:** Volte para o console do **EC2**. Selecione a `CafeInstance1` e vá em **Estado da instância (Instance state) > Interromper instância (Stop instance)**.
3.  **Monitore o Vigia:** Volte para **Route 53 > Verificações de integridade**. Após um ou dois minutos, o status da sua verificação mudará para **Não íntegro (Unhealthy)**. Você também receberá um e-mail de **ALERTA**.
4.  **Teste o Failover:** Volte para a aba do site (`http://www.<SEU_DOMINIO_DO_LAB>/cafe`) e **atualize a página**.
5.  **Verificação:** **Mágica!** O site agora carregará a partir da **CafeInstance2**, mostrando a Zona de Disponibilidade diferente.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você acaba de construir uma arquitetura de recuperação de desastres no nível do DNS. Você configurou o Route 53 para não apenas direcionar o tráfego, mas para ativamente monitorar a saúde da sua aplicação e tomar ações automáticas para garantir que seus usuários permaneçam online, mesmo durante uma falha.

---

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: Ensinando meu Site a Sobreviver a um Desastre

Sempre que a gente pensa em um site "cair", a imagem é de uma tela de erro e clientes frustrados. É o pesadelo de qualquer negócio. Hoje, na minha jornada com o AWS re/Start, aprendi a construir um sistema que se recusa a cair. Aprendi a criar um plano de contingência automático.

A missão foi usar o **Amazon Route 53**, o "GPS da nuvem", para ensinar nossa aplicação a sobreviver a um desastre.

### A Jornada em 3 Atos

#### Ato 1: O Plano de Contingência (A Arquitetura)

* **A Dor:** Ter um único servidor é um risco enorme. Se ele falhar, seu negócio fica offline. Ter um servidor de backup é bom, mas não adianta se a troca para ele for manual e lenta.
* **O Que Eu Fiz:** O laboratório começou com a base de qualquer arquitetura resiliente.
    * **Analogia:** Tínhamos duas **"pizzarias" idênticas** (instâncias EC2) em **"bairros" (Zonas de Disponibilidade) diferentes**. Se um bairro inteiro ficasse sem luz, a outra loja poderia continuar operando.

#### Ato 2: O Vigia Inteligente (A Health Check)

* **A Dor:** Como o sistema sabe, automaticamente e em segundos, que a pizzaria principal ficou sem luz?
* **O Que Eu Fiz:** Criei uma **Verificação de Integridade (Health Check)** no Route 53.
* **O "Aha!" Moment:** Essa foi a parte genial.
    * **Analogia:** Eu contratei um **"vigia robô"**. A única função dele é **"ligar" para a pizzaria principal a cada 10 segundos**. Se o telefone tocar e ninguém atender por duas vezes seguidas, ele tem autorização para apertar o "botão de emergência". E, como bônus, ele ainda me envia um e-mail avisando do problema!

#### Ato 3: O Desvio Automático (O Roteamento de Failover)

* **A Dor:** Ok, o vigia detectou o problema. E agora? Eu preciso acordar às 3 da manhã para redirecionar o tráfego manualmente?
* **O Que Eu Fiz:** Configurei a **Política de Roteamento de Failover**.
* **O "Aha!" Moment:** Aqui a mágica se completa.
    * **Analogia:** Eu dei um **"manual de contingência"** para a minha **"central telefônica" (o Route 53)**. O manual diz: "Sempre envie os clientes para a pizzaria principal. No entanto, **SE** o 'vigia robô' apertar o botão de emergência, **imediatamente e sem perguntar a ninguém**, desvie todas as novas ligações para a pizzaria de backup".

### O Teste de Desastre
A melhor parte foi simular o desastre. Eu fui lá e deliberadamente "cortei a energia" da minha instância principal. Voltei para o console do Route 53 e vi o status do meu "vigia" mudar para `Unhealthy`. Em seguida, atualizei a página do site e... lá estava ele, sendo servido pela minha instância de backup. Funcionou perfeitamente.

### A Grande Lição
O lab de hoje me ensinou que **Alta Disponibilidade** não é apenas sobre ter redundância (múltiplos servidores). É sobre ter um **sistema de detecção e resposta automático**. A combinação da **Health Check** com a **Política de Failover** do Route 53 cria exatamente isso: um sistema que se cura no nível da rede, de forma inteligente e sem intervenção humana.

Construir um sistema que sobrevive a uma falha que eu mesmo causei foi uma das experiências mais poderosas até agora. Deu uma sensação de confiança de que é possível construir aplicações realmente robustas na AWS. Não estamos apenas construindo sites, estamos construindo fortalezas digitais.

#AWS #Cloud #Route53 #HighAvailability #DisasterRecovery #DevOps #AWSreStart