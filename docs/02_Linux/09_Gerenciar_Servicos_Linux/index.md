# <img src="https://api.iconify.design/mdi/chart-timeline-variant.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Sala de Controle: Gerenciando Serviços e Monitorando a Saúde do Servidor

No último guia, vimos a fábrica cheia de "robôs operários" (processos). Mas e os robôs essenciais que precisam estar ligados 24/7 para que a fábrica sequer abra as portas? A segurança, a energia, a linha de montagem principal... Estes são os **Serviços**.

Um **serviço** (ou *daemon*) é um processo projetado para rodar continuamente em segundo plano, esperando por solicitações. O seu servidor web (Apache/Nginx) é um serviço. O seu acesso remoto (SSH) é um serviço.

Neste guia, você aprenderá a usar o **"Painel de Controle Principal"** (`systemctl`) para gerenciar esses serviços essenciais e as **"Ferramentas de Diagnóstico"** para monitorar a saúde geral do seu servidor.

---

### <img src="https://api.iconify.design/mdi/toggle-switch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Painel de Controle Principal: `systemctl`

Nos sistemas Linux modernos (como Amazon Linux 2, Ubuntu, RHEL), o `systemctl` é o comando universal para controlar os serviços. Ele é o seu canivete suíço.

**A Dor que Resolve:** A necessidade de iniciar, parar ou reiniciar um programa essencial sem precisar reiniciar a máquina inteira, o que interromperia todos os outros serviços que estão funcionando bem.

#### <img src="https://api.iconify.design/mdi/clipboard-list-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Os Comandos Essenciais do `systemctl`

| Comando | O que faz? (A Dor que Resolve) |
| :--- | :--- |
| **`sudo systemctl status httpd`** | Mostra o **status** do serviço Apache. (O servidor web está ligado? Deu erro?) |
| **`sudo systemctl start httpd`** | **Inicia** o serviço Apache. |
| **`sudo systemctl stop httpd`** | **Para** o serviço Apache. |
| **`sudo systemctl restart httpd`** | **Reinicia** o serviço. (Você acabou de alterar um arquivo de configuração e precisa que o serviço o releia). |
| **`sudo systemctl enable httpd`** | **Habilita** o serviço para iniciar automaticamente junto com o servidor (boot). |
| **`sudo systemctl disable httpd`**| **Desabilita** o serviço de iniciar automaticamente no boot. |

> **<img src="https://api.iconify.design/logos/aws-ec2.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Cenário Prático na AWS:** Você acabou de instalar o servidor web Apache em uma instância EC2 com `sudo yum install httpd`. O que fazer em seguida?
> 1.  `sudo systemctl start httpd` -> Para iniciar o site agora.
> 2.  `sudo systemctl enable httpd` -> Para garantir que, se você reiniciar a instância EC2, o site volte ao ar sozinho.
> 3.  `sudo systemctl status httpd` -> Para confirmar que tudo está rodando perfeitamente.

---

### <img src="https://api.iconify.design/mdi/pulse.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Painel de Diagnósticos: Monitorando os Sinais Vitais

Gerenciar serviços é uma parte da história. A outra é monitorar a saúde geral do servidor onde eles rodam.

#### <img src="https://api.iconify.design/mdi/harddisk.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Verificando o Espaço em Disco
* **`df -h` (Disk Free):**
    * **Pergunta que responde:** "Quanto espaço livre eu tenho em cada um dos meus discos (volumes EBS)?" O `-h` mostra os valores de forma **h**umana (GB, MB).
* **`du -h` (Disk Usage):**
    * **Pergunta que responde:** "Quanto espaço esta pasta específica está usando?"
> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** Entenda a diferença: `df` é sobre a **capacidade total** do disco. `du` é sobre o **uso de uma pasta específica**. Se o disco está cheio (`df`), você usa o `du` para encontrar qual pasta é a culpada.

#### <img src="https://api.iconify.design/mdi/cpu-64-bit.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Verificando CPU e Memória
* **`top`**: Seu painel **em tempo real** mostrando o uso de CPU e memória por processo.
* **`free -h`**: Mostra um resumo rápido do uso da memória **RAM** física.
* **`lscpu`**: Mostra informações detalhadas sobre o **processador** da sua instância EC2.

---

### <img src="https://api.iconify.design/logos/aws-cloudwatch.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Visão da Nuvem: Amazon CloudWatch

As ferramentas Linux são ótimas, mas elas têm uma limitação: você precisa estar conectado ao servidor para usá-las. E se você tiver 50 servidores?

**A Dor que o CloudWatch Resolve:** A necessidade de monitorar, visualizar e alertar sobre a saúde de **toda a sua frota de recursos AWS** de forma centralizada e automatizada.

* **Analogia:** Se as ferramentas Linux são o painel do seu carro, o **CloudWatch é a central de monitoramento da sua empresa de transportes**, vendo todos os carros no mapa ao mesmo tempo.
* **O que ele faz por você:**
    1.  <img src="https://api.iconify.design/mdi/chart-line.svg?color=currentColor" width="16" /> **Coleta Métricas:** Automaticamente coleta dados vitais da sua instância EC2, como `Uso de CPU`, `Entrada/Saída de Rede`, e `Leitura/Gravação de Disco`.
    2.  <img src="https://api.iconify.design/mdi/view-dashboard-outline.svg?color=currentColor" width="16" /> **Cria Dashboards:** Permite que você crie painéis visuais com gráficos para acompanhar a saúde dos seus sistemas.
    3.  <img src="https://api.iconify.design/mdi/bell-alert-outline.svg?color=currentColor" width="16" /> **Cria Alarmes:** Este é o superpoder. Você pode criar uma regra como: "Se o uso de CPU da minha instância EC2 ficar acima de 80% por mais de 5 minutos, me envie um e-mail de alerta através do **Amazon SNS**".

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova, entenda que o **CloudWatch** é o serviço nativo da AWS para **monitoramento e observabilidade**. Eles adoram questões de cenário que envolvem a criação de **Alarmes** para métricas de **EC2**, como o uso de CPU.