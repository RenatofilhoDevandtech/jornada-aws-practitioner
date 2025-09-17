# <img src="https://api.iconify.design/logos/aws-systems-manager.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Painel de Controle da Frota: Guia Definitivo do AWS Systems Manager

Gerenciar um servidor EC2 é fácil. Gerenciar 500 é um pesadelo, se feito manualmente. A dor do gerenciamento em escala é a principal razão pela qual as operações de TI tradicionais são lentas e propensas a erros.

O **AWS Systems Manager (SSM)** é a resposta da AWS para essa dor. É um serviço unificado que te dá visibilidade e controle sobre toda a sua frota de instâncias (e até mesmo servidores on-premises), sem a necessidade de se conectar a cada uma delas via SSH.

**Analogia:** Pense que suas instâncias EC2 são uma **frota de caminhões de entrega autônomos**. O Systems Manager é o seu **"Painel de Controle Central na Sede da Empresa"**.

---

### <img src="https://api.iconify.design/mdi/toolbox-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Cinto de Utilidades do Gerente da Frota (Recursos do SSM)

O SSM é uma coleção de ferramentas. Vamos conhecer as mais importantes.

#### <img src="https://api.iconify.design/mdi/clipboard-list-outline.svg?color=currentColor" width="20" /> Inventory (O Censo da Frota)
* **O que faz?** Coleta automaticamente informações detalhadas sobre suas instâncias: software instalado, configurações de rede, patches, etc.
* **A Dor que Resolve:** "Eu preciso de uma lista de todos os servidores que ainda estão rodando o Windows Server 2016 para o nosso plano de upgrade."

#### <img src="https://api.iconify.design/mdi/play-box-outline.svg?color=currentColor" width="20" /> Run Command (O Intercomunicador)
* **O que faz?** Permite que você execute um comando ou script em um ou mais servidores de uma só vez, a partir do painel central.
* **A Dor que Resolve:** "Preciso reiniciar o serviço web em todos os 50 servidores de produção. Fazer isso via SSH, um por um, levaria uma hora."

#### <img src="https://api.iconify.design/mdi/lan-connect.svg?color=currentColor" width="20" /> Session Manager (O Túnel de Acesso Seguro)
* **O que faz?** Permite que você inicie uma sessão de terminal (um shell) segura com uma instância, **diretamente do console da AWS ou da CLI**, sem precisar de chaves SSH e sem precisar que a porta 22 esteja aberta no Security Group.
* **A Dor que Resolve:** A complexidade e o risco de segurança de gerenciar pares de chaves SSH e de expor portas de gerenciamento para a internet.

#### <img src="https://api.iconify.design/mdi/shield-patch-outline.svg?color=currentColor" width="20" /> Patch Manager (A Equipe de Manutenção Noturna)
* **O que faz?** Automatiza o processo de escanear suas instâncias em busca de patches de segurança faltando e de aplicá-los de acordo com uma agenda.
* **A Dor que Resolve:** A tarefa manual e crítica de manter toda a sua frota de servidores atualizada com as últimas correções de segurança.

#### <img src="https://api.iconify.design/mdi/calendar-clock.svg?color=currentColor" width="20" /> Maintenance Windows (A Janela de Manutenção)
* **O que faz?** Permite que você defina janelas de tempo recorrentes (ex: "todo sábado, das 22h às 02h") durante as quais tarefas disruptivas, como a aplicação de patches ou atualizações, podem ser executadas.
* **A Dor que Resolve:** Evitar que uma atualização automática aconteça no meio do pico de vendas da Black Friday.

#### <img src="https://api.iconify.design/mdi/list-status.svg?color=currentColor" width="20" /> State Manager (O Fiscal de Conformidade)
* **O que é?** Uma ferramenta que garante que sua frota **permaneça** em um estado de configuração que você define.
* **Analogia:** Você cria a regra: "Todo caminhão na minha frota **DEVE** ter o software antivírus instalado e rodando". O State Manager verifica continuamente a frota e, se encontrar um caminhão sem o antivírus, ele o instala automaticamente.

#### <img src="https://api.iconify.design/mdi/key-chain-variant.svg?color=currentColor" width="20" /> Parameter Store (O Cofre de Segredos)
* **O que faz?** Um local centralizado e seguro para armazenar dados de configuração e segredos, como senhas de banco de dados, chaves de API e strings de licença.
* **A Dor que Resolve:** A prática insegura de salvar senhas diretamente no código ou em arquivos de configuração não criptografados.

#### <img src="https://api.iconify.design/mdi/script-text-play-outline.svg?color=currentColor" width="20" /> Automation (O Maestro da Orquestra)
* **O que faz?** É a ferramenta que junta tudo. Permite que você crie **"Runbooks"** (Documentos SSM) que orquestram sequências complexas de ações, combinando chamadas de API da AWS, scripts e outros recursos do Systems Manager.
* **Cenário Prático:** Você pode criar um runbook de automação que:
    1.  Cria uma AMI "dourada" a partir de uma instância EC2.
    2.  Testa a AMI.
    3.  Aplica os últimos patches de segurança nela.
    4.  Compartilha a AMI com outras contas da sua organização.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova Cloud Practitioner:
> 1.  Entenda o **AWS Systems Manager (SSM)** como a sua principal ferramenta para **gerenciamento operacional e automação** de sua frota de instâncias **EC2**.
> 2.  Saiba a finalidade dos seus recursos mais importantes: **Run Command** (executar comandos), **Patch Manager** (aplicar patches) e **Parameter Store** (armazenar segredos).
> 3.  Lembre-se do **Session Manager** como a alternativa segura ao SSH.

---

### <img src="https://api.iconify.design/logos/aws-systems-manager.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Cinto de Utilidades do SysOps: Guia dos Recursos do AWS Systems Manager

Já estabelecemos que o Systems Manager é o nosso "Painel de Controle Central" para gerenciar nossa frota de instâncias EC2. Agora, vamos abrir a caixa de ferramentas e conhecer cada um dos "botões" e "aplicativos" deste painel. Cada recurso foi projetado para resolver uma dor específica do gerenciamento em escala.

---

### <img src="https://api.iconify.design/mdi/toolbox-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Arsenal de Ferramentas do SSM

#### <img src="https://api.iconify.design/mdi/play-box-outline.svg?color=currentColor" width="20" /> Run Command (O Intercomunicador)
* **A Missão (A Dor que Resolve):** "Preciso verificar a versão do kernel em 100 servidores Linux. Conectar via SSH em cada um levaria horas."
* **A Ferramenta (Como Funciona):** O Run Command permite que você execute um comando ou script (como `uname -r`) em um grupo de instâncias (selecionadas por tags, por exemplo) de uma só vez, com um único clique.
* **O Resultado (Valor de Negócio):** Redução drástica do tempo para executar tarefas ad-hoc. Ações que levavam horas agora levam segundos.

#### <img src="https://api.iconify.design/mdi/lan-connect.svg?color=currentColor" width="20" /> Session Manager (O Túnel de Acesso Seguro)
* **A Missão:** "Preciso de acesso ao terminal de uma instância que está em uma sub-rede privada, e nossa política de segurança proíbe abrir a porta 22 (SSH) para qualquer lugar."
* **A Ferramenta:** O Session Manager usa o Agente SSM para criar um túnel de comunicação seguro para a sua instância, permitindo que você abra um shell interativo diretamente do console da AWS ou da CLI.
* **O Resultado:** **Segurança imensamente aprimorada**. Você elimina a necessidade de gerenciar chaves SSH, de configurar hosts bastião e de expor portas de gerenciamento. Todo o acesso é autenticado via IAM e registrado no CloudTrail.

#### <img src="https://api.iconify.design/mdi/shield-patch-outline.svg?color=currentColor" width="20" /> Patch Manager (A Equipe de Manutenção Automatizada)
* **A Missão:** "Garantir que toda a minha frota de servidores Windows e Linux esteja sempre atualizada com os últimos patches de segurança é uma tarefa manual, repetitiva e fácil de esquecer."
* **A Ferramenta:** O Patch Manager escaneia suas instâncias, compara os softwares instalados com uma "linha de base" de patches aprovados e aplica as atualizações que estiverem faltando.
* **O Resultado:** Melhoria da postura de segurança e conformidade, automatizando uma das tarefas mais críticas e tediosas da administração de sistemas.

#### <img src="https://api.iconify.design/mdi/calendar-clock.svg?color=currentColor" width="20" /> Maintenance Windows (A Janela de Manutenção Programada)
* **A Missão:** "Eu preciso aplicar os patches, mas não posso arriscar reiniciar um servidor no meio do horário de pico do meu e-commerce."
* **A Ferramenta:** Permite que você defina janelas de tempo recorrentes (ex: "todo domingo, das 02h às 04h da manhã") durante as quais tarefas disruptivas (como as do Patch Manager ou Run Command) têm permissão para serem executadas.
* **O Resultado:** Controle e previsibilidade. A manutenção acontece em um horário de baixo impacto para o negócio, evitando interrupções inesperadas.

#### <img src="https://api.iconify.design/mdi/list-status.svg?color=currentColor" width="20" /> State Manager (O Fiscal de Conformidade Contínuo)
* **A Missão:** "Eu instalei o antivírus em todas as minhas instâncias, mas como eu garanto que ele **permaneça** instalado e rodando, e que ninguém o desative por engano?"
* **A Ferramenta:** Você define uma "Associação" que diz: "O estado desejado para todas as instâncias com a tag `Producao` é ter o `antivirus.exe` instalado e rodando". O State Manager verifica continuamente a frota e, se encontrar uma instância fora de conformidade, ele a corrige automaticamente.
* **O Resultado:** Infraestrutura consistente e que se auto-corrige, prevenindo o "configuration drift".

#### <img src="https://api.iconify.design/mdi/script-text-play-outline.svg?color=currentColor" width="20" /> Automation (O Maestro da Orquestra)
* **A Missão:** "Para criar uma nova AMI (Imagem de Máquina) segura, eu preciso seguir um processo de 10 passos: lançar uma instância, aplicar patches, instalar softwares, rodar testes, criar a imagem e depois limpar tudo. É um processo complexo e manual."
* **A Ferramenta:** O Automation permite que você crie "Runbooks" (Documentos SSM) que orquestram sequências complexas de ações, combinando chamadas de API da AWS, scripts e outros recursos do Systems Manager em um único fluxo de trabalho.
* **O Resultado:** Automação de processos complexos, reduzindo o risco de erro humano e garantindo que as melhores práticas sejam seguidas todas as vezes.

---

### <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Sinergia em Ação: Um Cenário Real

Imagine que sua missão é: **"Aplicar patches de segurança em toda a frota de servidores web mensalmente, de forma segura e sem interromper o negócio."**

1.  **Defina a Regra:** Use o **Patch Manager** para criar uma "linha de base" de patches aprovados.
2.  **Agende a Janela:** Crie uma **Janela de Manutenção** para rodar todo primeiro sábado do mês, às 02:00 da manhã.
3.  **Defina a Tarefa:** Dentro da Janela, registre uma tarefa que usa o **Run Command** para executar o documento `AWS-RunPatchBaseline` em todas as instâncias com a tag `App:WebServer`.
4.  **Monitore a Conformidade:** Use o **State Manager** para verificar a conformidade de patches *diariamente* e te alertar sobre qualquer servidor que esteja desalinhado.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova Cloud Practitioner, o **AWS Systems Manager (SSM)** é a resposta para quase qualquer pergunta sobre **gerenciamento operacional em escala** de instâncias EC2.
> * Precisa **aplicar patches**? -> **Patch Manager**.
> * Precisa **executar um comando** em várias máquinas? -> **Run Command**.
> * Precisa de **acesso ao terminal sem SSH**? -> **Session Manager**.

---

### <img src="https://api.iconify.design/logos/aws-systems-manager.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Cinto de Utilidades do SysOps: Guia Completo do AWS Systems Manager

Gerenciar um servidor EC2 é fácil. Gerenciar 500 é um pesadelo, se feito manualmente. O **AWS Systems Manager (SSM)** é a resposta da AWS para a dor do gerenciamento em escala. É um serviço unificado que te dá visibilidade e controle sobre toda a sua frota de instâncias.

**Analogia:** Pense que suas instâncias EC2 são uma **frota de caminhões de entrega autônomos**. O Systems Manager é o seu **"Painel de Controle Central na Sede da Empresa"**.

---

### <img src="https://api.iconify.design/mdi/toolbox-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Arsenal de Ferramentas de Ação

Estas são as ferramentas que você usa para **executar** tarefas na sua frota.

* **<img src="https://api.iconify.design/mdi/play-box-outline.svg?color=currentColor" width="18" /> Run Command:** O "Intercomunicador" para enviar comandos imediatos.
* **<img src="https://api.iconify.design/mdi/lan-connect.svg?color=currentColor" width="18" /> Session Manager:** O "Túnel de Acesso Seguro" para um terminal sem SSH.
* **<img src="https://api.iconify.design/mdi/shield-patch-outline.svg?color=currentColor" width="18" /> Patch Manager:** A "Equipe de Manutenção Automatizada" para patches de segurança.
* **<img src="https://api.iconify.design/mdi/calendar-clock.svg?color=currentColor" width="18" /> Maintenance Windows:** O "Agendamento da Oficina" para tarefas disruptivas.
* **<img src="https://api.iconify.design/mdi/list-status.svg?color=currentColor" width="18" /> State Manager:** O "Fiscal de Conformidade Contínuo" que garante a configuração correta.
* **<img src="https://api.iconify.design/mdi/script-text-play-outline.svg?color=currentColor" width="18" /> Automation:** O "Maestro da Orquestra" para automatizar fluxos de trabalho complexos.

---

### <img src="https://api.iconify.design/mdi/database-eye-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. As Ferramentas de Suporte e Visibilidade

Estas ferramentas fornecem a inteligência e os dados para que as ferramentas de ação funcionem de forma segura e eficaz.

#### <img src="https://api.iconify.design/mdi/key-chain-variant.svg?color=currentColor" width="20" /> Parameter Store (O Cofre de Segredos)
* **A Missão (A Dor que Resolve):** "Minha aplicação precisa da senha para se conectar ao banco de dados. É uma péssima prática de segurança salvá-la diretamente no meu código-fonte ou em um arquivo de configuração no servidor."
* **A Ferramenta (Como Funciona):** O Parameter Store é um local centralizado para armazenar dados de configuração e segredos. Você pode armazenar senhas, chaves de API, licenças, etc., como parâmetros.
* **O Resultado (Valor de Negócio):**
    * **Segurança:** Você separa os segredos do código. Para uma segurança ainda maior, você pode criar um parâmetro do tipo `SecureString`, que integra com o **AWS KMS** para criptografar o valor.
    * **Gerenciamento Centralizado:** Se você precisar rotacionar a senha do banco de dados, você a altera em **um único lugar** (no Parameter Store), em vez de ter que alterar o código em 100 servidores diferentes.

#### <img src="https://api.iconify.design/mdi/clipboard-list-outline.svg?color=currentColor" width="20" /> Inventory (O Censo da Frota)
* **A Missão:** "Um novo bug crítico foi descoberto no Nginx versão 1.20. Preciso de uma lista de todas as instâncias na minha frota que estão rodando essa versão específica, e preciso disso agora."
* **A Ferramenta:** O Inventory coleta metadados sobre suas instâncias e o software instalado nelas. Ele pode coletar tudo: aplicações, configurações de rede, serviços do Windows, atualizações, etc.
* **O Resultado:** Visibilidade completa. Você pode executar consultas complexas sobre o estado da sua frota sem precisar se conectar a uma única máquina, facilitando auditorias, rastreamento de licenças e investigações de segurança.

#### <img src="https://api.iconify.design/mdi/view-dashboard-outline.svg?color=currentColor" width="20" /> Insights Dashboard (O Painel Executivo)
* **A Missão:** "Para entender a saúde da minha frota, eu preciso olhar em cinco painéis diferentes: CloudWatch para performance, Config para conformidade, Trusted Advisor para custos... É ineficiente."
* **A Ferramenta:** O Insights Dashboard agrega dados operacionais de múltiplas fontes da AWS em uma **única visão consolidada**.
* **O Resultado:** Redução da complexidade. Você tem uma visão de "big picture" do estado operacional da sua frota, podendo identificar problemas e tendências mais rapidamente, pois ele integra dados do CloudTrail, AWS Config, Patch Manager, e pode até incluir seus próprios painéis do CloudWatch.

---

### <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Sinergia em Ação: Rotacionando uma Senha

Imagine a missão: **"Automatizar a rotação da senha de um banco de dados usada pela nossa frota de aplicações."**

1.  A senha do banco está armazenada no **Parameter Store** como um `SecureString`.
2.  Uma **função Lambda**, acionada por um evento agendado do **CloudWatch** a cada 30 dias, gera uma nova senha.
3.  A Lambda atualiza a senha no banco de dados **Amazon RDS**.
4.  Em seguida, a Lambda atualiza o valor do parâmetro no **Parameter Store**.
5.  As aplicações, que são programadas para ler a senha do Parameter Store, pegarão a nova senha na próxima vez que precisarem, sem nenhuma alteração no código.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Lembre-se do **AWS Systems Manager (SSM)** como a suíte de ferramentas para **gerenciamento operacional em escala** de instâncias EC2.
> 2.  Associe **Patch Manager** com patches, **Run Command** com execução de comandos, **Session Manager** com acesso shell seguro, e **Parameter Store** com armazenamento de segredos.

---

### <img src="https://api.iconify.design/mdi/robot-industrial-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Painel de Controle da Frota: Guia de Ferramentas e Automação na AWS

Lançar uma instância EC2 é fácil. Mas como você gerencia 10, 100 ou 1000 instâncias? Como garante que todas estão com os patches de segurança em dia? Como executa um comando em todas elas ao mesmo tempo? Fazer isso manualmente é impossível.

Este módulo apresenta o arsenal de ferramentas que a AWS oferece para resolver a dor do **gerenciamento em escala**.

**Analogia:** Pense na sua frota de instâncias EC2 como uma **frota de caminhões de entrega autônomos**. Gerenciá-los um por um via rádio (SSH) é ineficiente. Você precisa de um **"Painel de Controle Central"**.

---

### <img src="https://api.iconify.design/logos/aws-systems-manager.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Coração da Automação: AWS Systems Manager (SSM)

O Systems Manager é o seu "Painel de Controle Central". É um serviço unificado que te dá visibilidade e controle sobre toda a sua infraestrutura na AWS.

* **A Dor que Resolve:** A necessidade de se conectar via SSH em cada instância para realizar tarefas operacionais, o que é lento, inseguro e não escalável.
* **A Mágica (O Agente SSM):** Cada "caminhão" (instância EC2) pode vir com um pequeno "agente de comunicação" (o SSM Agent) instalado. Este agente se reporta de forma segura ao "Painel de Controle" (o serviço SSM), permitindo que você gerencie a frota sem precisar abrir portas de firewall para SSH.

#### Recursos-Chave do Systems Manager:
* **<img src="https://api.iconify.design/mdi/console-line.svg?color=currentColor" width="18" /> Run Command:** Permite que você execute comandos (ex: `sudo yum update`) em centenas de instâncias de uma só vez.
* **<img src="https://api.iconify.design/mdi/shield-patch-outline.svg?color=currentColor" width="18" /> Patch Manager:** Automatiza o processo de escanear e aplicar patches de segurança em toda a sua frota.
* **<img src="https://api.iconify.design/mdi/card-account-details-outline.svg?color=currentColor" width="18" /> Inventory:** Coleta metadados sobre suas instâncias, como os softwares instalados e suas configurações.
* **<img src="https://api.iconify.design/mdi/lan-connect.svg?color=currentColor" width="18" /> Session Manager:** Permite que você inicie uma sessão de terminal segura com uma instância **diretamente do console da AWS ou da CLI**, sem precisar de chaves SSH.

---

### <img src="https://api.iconify.design/mdi/toolbox-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Arsenal de Ferramentas Adicionais

Além do painel de controle principal, o engenheiro de nuvem tem outras ferramentas especializadas:

* **<img src="https://api.iconify.design/logos/aws-cloudformation.svg?color=currentColor" width="18" /> AWS CloudFormation:**
    * **Analogia:** A **"planta da fábrica"** que constrói os caminhões.
    * **Função:** É a ferramenta de **Infraestrutura como Código (IaC)** para provisionar e gerenciar a criação da sua infraestrutura.

* **<img src="https://api.iconify.design/mdi/language-python.svg?color=currentColor" width="18" /> AWS SDKs (ex: Boto3 para Python):**
    * **Analogia:** A **"biblioteca de programação"** que permite que seus próprios aplicativos conversem com o Painel de Controle.
    * **Função:** Para desenvolvedores que precisam integrar a automação da AWS dentro de suas aplicações customizadas.

* **<img src="https://api.iconify.design/mdi/powershell.svg?color=currentColor" width="18" /> AWS Tools for PowerShell:**
    * **O que é?** Uma versão da CLI e do SDK otimizada para administradores que vivem no mundo Windows e amam a linguagem de script PowerShell.

* **<img src="https://api.iconify.design/mdi/chef-hat.svg?color=currentColor" width="18" /> AWS OpsWorks:**
    * **O que é?** Um serviço de gerenciamento de configuração que usa ferramentas populares como **Chef** e **Puppet**.
    * **Insight:** É uma ferramenta para equipes que já têm um grande investimento e conhecimento nessas tecnologias e querem trazê-las para a AWS de forma gerenciada.

---

### <img src="https://api.iconify.design/logos/aws-s3.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. A Automação Definitiva (Recap do Site Estático no S3)

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> Insight de Especialista:** Às vezes, a melhor automação é **eliminar o trabalho completamente**.

* **O que é?** A prática de hospedar um site estático diretamente no Amazon S3.
* **Como se conecta à automação?**
    * **Analogia:** Por que enviar um **caminhão gigante com motorista (EC2)** para entregar um envelope (um site estático), se você pode usar um **drone de entrega totalmente autônomo (S3)**?
    * Ao usar o S3, você **automatiza a remoção** de toda a necessidade de gerenciar servidores, patches, sistemas operacionais e escalabilidade. É o nível máximo de eficiência operacional para este caso de uso.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  **AWS Systems Manager (SSM)** é o serviço para **gerenciamento operacional** da sua frota de EC2 (patching, execução de comandos).
> 2.  **AWS CloudFormation** é para **provisionamento de infraestrutura** (Infraestrutura como Código).
> 3.  Entenda que **SDKs** e a **CLI** são as ferramentas para **interação programática** e automação via scripts.

Com este guia, você tem uma visão geral do arsenal de ferramentas que a AWS oferece para transformar o gerenciamento de infraestrutura de uma tarefa manual e reativa para um processo automatizado e proativo.

---

### <img src="https://api.iconify.design/logos/aws-systems-manager.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Painel de Controle da Frota - Usando o AWS Systems Manager

### O Cenário (A "User Story")

> **Como** um engenheiro de operações (SysOps), **EU QUERO** usar o AWS Systems Manager para instalar uma aplicação, gerenciar sua configuração e acessar o servidor de forma segura, **PARA QUE** eu possa gerenciar minha frota de instâncias EC2 de forma automatizada, escalável e sem expor portas de gerenciamento.

### A Dor que o Lab Resolve

1.  **O Risco do SSH:** Abrir a porta 22 (SSH) para o mundo é uma das maiores vetores de ataque. Gerenciar centenas de chaves `.pem` é complexo e inseguro.
2.  **A Lentidão da Escala:** Conectar em 50 servidores, um por um, para instalar um software ou aplicar um patch é uma tarefa manual que não escala e é extremamente propensa a erros.

Este laboratório mostra como o Systems Manager resolve essas duas dores fundamentais, introduzindo uma forma moderna e segura de gerenciar sua infraestrutura.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Usar o **Run Command** para instalar uma aplicação em uma instância EC2.
* [ ] Usar o **Inventory** para verificar o software instalado.
* [ ] Usar o **Parameter Store** para guardar uma configuração.
* [ ] Usar o **Session Manager** para acessar o terminal da instância sem SSH.

### Pré-requisitos
* Uma conta AWS.
* Uma instância EC2 com o **Amazon Linux** já em execução e com o **SSM Agent** instalado (isso é padrão para AMIs do Amazon Linux).
* **Importante:** A instância precisa de uma **IAM Role** anexada com a política `AmazonSSMManagedInstanceCore` para que o SSM possa se comunicar com ela.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1 e 2: O Intercomunicador - Instalando uma Aplicação com o Run Command

**Analogia:** Em vez de ir até cada "caminhão" (instância) para instalar um novo software de GPS, vamos usar o "intercomunicador da sede" (**Run Command**) para enviar a ordem de instalação para toda a frota de uma vez.

1.  No Console da AWS, navegue até o serviço **Systems Manager**.
2.  No painel esquerdo, role para baixo e clique em **Run Command**.
3.  Clique no botão **Run command**.
4.  Na barra de busca de **Command document**, procure e selecione `AWS-RunShellScript`.
5.  Na seção **Commands**, cole o seguinte script de instalação:
    ```bash
    #!/bin/bash
    sudo yum install -y httpd php
    sudo systemctl start httpd
    sudo systemctl enable httpd
    echo "<?php phpinfo(); ?>" | sudo tee /var/www/html/index.php
    ```
    > **`!!! note "O que este script faz?"`**
    > Ele instala o servidor web Apache e o PHP, inicia o serviço e cria uma página de teste que exibe as informações do PHP.
6.  Na seção **Targets** (Alvos), selecione **Choose instances manually** (Escolher instâncias manualmente).
7.  Marque a caixa de seleção ao lado da sua instância EC2.
8.  Deixe as outras opções como padrão e role até o final. Clique em **Run**.
9.  A tela de status do comando aparecerá. Aguarde até que o **Status** geral mude para **Success** (Sucesso).

**Verificação:**
* **Verificando a Aplicação:** Copie o IP Público da sua instância EC2, cole em uma nova aba do navegador e você deverá ver a página de informações do PHP. **A instalação funcionou!**
* **Verificando com o Inventory:**
    1.  No Systems Manager, navegue para **Inventory**.
    2.  Se for a primeira vez, clique em **Setup Inventory**. Siga os passos para habilitar a coleta em todas as suas instâncias.
    3.  Após alguns minutos, você poderá selecionar sua instância na lista de **Managed Instances** e, na aba **Inventory**, procurar pelo tipo `AWS:Application` para confirmar que `httpd` e `php` estão na lista de softwares instalados.

#### Tarefa 3: O Cofre de Segredos - Gerenciando a Configuração com o Parameter Store

**Analogia:** Em vez de escrever uma "senha" em um post-it (arquivo de configuração) dentro do caminhão, vamos guardá-la no "cofre central da empresa" (**Parameter Store**).

1.  No Systems Manager, navegue para **Parameter Store**.
2.  Clique em **Create parameter** (Criar parâmetro).
3.  **Name** (Nome): `/MinhaApp/Config/MensagemDeBoasVindas`
    > **`!!! tip "Dica de Especialista"`**
    > Usar uma hierarquia com barras (`/`) é a melhor prática para organizar seus parâmetros.
4.  **Tier** (Camada): Deixe `Standard`.
5.  **Type** (Tipo): Selecione `String`.
    > Para senhas, você selecionaria `SecureString` para criptografar o valor com o KMS.
6.  **Value** (Valor): Digite `Bem-vindo ao meu site gerenciado pelo SSM!`.
7.  Clique em **Create parameter**.

#### Tarefa 4: O Túnel Mágico - Acessando a Instância com o Session Manager

**Analogia:** Vamos usar o "terminal de acesso seguro da sede" para nos conectar diretamente ao painel de um caminhão, sem precisar ir até a garagem com uma chave física (SSH).

1.  No Systems Manager, navegue para **Session Manager**.
2.  Clique no botão **Start session**.
3.  Selecione sua instância EC2 na lista.
4.  Clique em **Start session**.
5.  **Mágica!** Uma nova aba se abrirá com um terminal de linha de comando, já conectado à sua instância como o usuário `ssm-user`. Você tem acesso total ao shell.
6.  **Vamos testar nosso parâmetro:** Execute o seguinte comando da AWS CLI (já vem instalada) para ler o valor que guardamos no Parameter Store.
    ```bash
    aws ssm get-parameter --name "/MinhaApp/Config/MensagemDeBoasVindas" --query "Parameter.Value" --output text
    ```
7.  **Verificação:** O terminal deve imprimir a mensagem: `Bem-vindo ao meu site gerenciado pelo SSM!`.
8.  Para sair, digite `exit` e clique em **Terminate** na janela pop-up.

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos
* [ ] No **Systems Manager**, vá para **Parameter Store**, selecione o parâmetro que você criou e delete-o.
* [ ] No console do **EC2**, **termine** a instância que você usou neste laboratório.