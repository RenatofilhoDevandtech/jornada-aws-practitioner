# <img src="https://api.iconify.design/logos/aws-ec2.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Guia 1: Amazon EC2 - Montando o Servidor dos Seus Sonhos

Pense no **Amazon EC2 (Elastic Compute Cloud)** como o serviço que te permite **montar o PC ou servidor dos seus sonhos, peça por peça, em questão de minutos**, sem nunca precisar tocar em um componente físico.

Esqueça a dor de comprar hardware caro que fica obsoleto. Com o EC2, você aluga poder computacional e o personaliza exatamente para a sua necessidade, seja para hospedar um simples blog ou para rodar uma simulação científica complexa.

Este guia é o seu manual de montagem. Vamos passar pelos **9 passos essenciais** para criar (ou "lançar") sua primeira máquina virtual, que na linguagem da AWS, chamamos de **Instância EC2**.

---

### <img src="https://api.iconify.design/mdi/wrench-cog-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Montando seu Servidor Virtual: O Guia de 9 Passos

#### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> Passo 1: A Imagem de Máquina (AMI) - O Sistema Operacional
* **O que é?** A **Imagem de Máquina da Amazon (AMI)** é o seu ponto de partida. É um modelo que contém o sistema operacional (Linux ou Windows) e, muitas vezes, softwares pré-instalados.
* **Analogia:** É como escolher o **"disco de instalação"** do seu novo PC. Você quer um Windows 11 com Office e Photoshop já instalados? Ou um Ubuntu puro? A AMI é isso.
* **Dor que Resolve:** **Repetibilidade.** Se você configurar um servidor perfeito, pode criar uma AMI a partir dele. Agora você tem um "clone" do seu sistema para criar 1, 10 ou 1000 servidores idênticos com um clique.

#### <img src="https://api.iconify.design/mdi/cpu-64-bit.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> Passo 2: Tipo de Instância - O Hardware
* **O que é?** É a combinação de CPU, memória (RAM), armazenamento e capacidade de rede.
* **Analogia:** É a hora de escolher o **"processador, a placa de vídeo e a memória RAM"** do seu PC. Você precisa de um Core i3 para tarefas básicas ou de um Core i9 com uma RTX 4090 para rodar um jogo pesado? A AWS organiza as instâncias em famílias otimizadas:
    * **Uso Geral (Família T, M):** Equilibradas. Ótimas para sites e aplicações web.
    * **Otimizadas para Computação (Família C):** Muita CPU. Para processamento pesado, servidores de jogos.
    * **Otimizadas para Memória (Família R, X):** Muita RAM. Para grandes bancos de dados e análise de dados em memória.
* **Dor que Resolve:** Pagar apenas pelo poder que você precisa. Evita o desperdício de ter uma máquina superpotente para uma tarefa simples.

#### <img src="https://api.iconify.design/mdi/network-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> Passo 3: Configurações de Rede - A Conexão
* **O que é?** Onde sua instância vai "morar" na nuvem. Você a coloca dentro de uma **VPC** (sua rede privada) e em uma **Sub-rede** (um "bairro" dentro da sua rede).
* **Analogia:** É como conectar seu novo PC **"ao roteador da sua casa"**. Aqui você decide se ele terá um IP público para ser acessível pela internet ou se ficará apenas na rede interna.
* **Dor que Resolve:** Isola seus recursos de forma segura, garantindo que apenas o tráfego que você permite possa chegar até sua instância.

#### <img src="https://api.iconify.design/mdi/account-key-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> Passo 4: Função do IAM - O Crachá de Acesso
* **O que é?** Uma forma segura de dar permissões para que sua instância EC2 acesse outros serviços da AWS (como um bucket S3).
* **Analogia:** É como dar um **"crachá de acesso"** para o seu PC. Em vez de salvar senhas dentro dele (uma prática horrível!), o crachá dá permissão para que ele entre em outras "salas" (serviços) autorizadas.
* **Dor que Resolve:** A necessidade de armazenar credenciais de acesso dentro de uma instância, o que é uma falha de segurança grave.

#### <img src="https://api.iconify.design/mdi/script-text-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> Passo 5: Dados do Usuário - O Script de Instalação
* **O que é?** Um script (uma série de comandos) que você pode mandar para a instância e que será executado automaticamente na **primeira vez** que ela for ligada.
* **Analogia:** É o seu **"script de pós-formatação"**. Aquele que instala o Chrome, atualiza o sistema e configura tudo do seu jeito, sem que você precise fazer manualmente.
* **Dor que Resolve:** A necessidade de configurar manualmente cada nova instância. Com User Data, suas instâncias já nascem prontas para o trabalho.

#### <img src="https://api.iconify.design/mdi/harddisk.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> Passo 6: Armazenamento - O HD/SSD
* **O que é?** Onde seus dados e o sistema operacional serão armazenados. A opção principal é o **Amazon EBS**.
* **Analogia:** É a escolha do **"SSD ou HD"** do seu PC. Você pode definir o tamanho (em GB) e o tipo (SSD para velocidade, HDD para custo baixo).
* **Dor que Resolve:** Oferece armazenamento persistente. Se você desligar sua instância EC2, os dados no volume EBS continuam lá, seguros, como um HD externo.

#### <img src="https://api.iconify.design/mdi/tag-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> Passo 7: Tags - As Etiquetas
* **O que é?** Rótulos (chave-valor) que você pode anexar à sua instância.
* **Analogia:** São as **"etiquetas organizacionais"** que você cola no gabinete do seu PC. Ex: `Projeto: Blog`, `Ambiente: Produção`, `Responsável: João`.
* **Dor que Resolve:** O caos de ter dezenas ou centenas de recursos sem saber para que servem. As tags são essenciais para organizar, filtrar e, principalmente, gerenciar custos.

#### <img src="https://api.iconify.design/mdi/wall.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> Passo 8: Security Group - O Firewall
* **O que é?** Um firewall virtual que controla o tráfego de entrada e saída da sua instância.
* **Analogia:** É o **"firewall do seu roteador"**. Você cria regras para dizer quais "portas" estão abertas. Ex: "Permitir tráfego da internet na porta 80 (HTTP) para que as pessoas possam ver meu site, mas bloquear todo o resto".
* **Dor que Resolve:** É a sua primeira e mais importante linha de defesa, protegendo sua instância de acessos não autorizados.

#### <img src="https://api.iconify.design/mdi/key-variant.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> Passo 9: Par de Chaves - A Chave de Acesso
* **O que é?** Um par de chaves criptográficas (uma pública, que a AWS guarda, e uma privada, que você baixa e guarda) usado para provar sua identidade ao se conectar à sua instância.
* **Analogia:** É a **"chave da porta da sua casa"**. Para se conectar de forma segura (via SSH no Linux ou RDP no Windows), você precisa apresentar sua chave privada.
* **Dor que Resolve:** A necessidade de usar senhas, que são muito menos seguras que a criptografia de chave pública.

> **<img src="https://api.iconify.design/mdi/alert-circle-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** A prova adora perguntar sobre esses 9 passos. Entender a **finalidade** de cada um (AMI para o modelo, Tipo de Instância para o hardware, Security Group para o firewall, etc.) é muito mais importante do que decorar os nomes exatos. A analogia de "montar um PC" te ajudará a lembrar a função de cada peça.

---

### <img src="https://api.iconify.design/mdi/power-cycle.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> O Ciclo de Vida da sua Instância

Depois de montado, seu servidor pode passar por vários estados:

* **Pendente:** Ligando...
* **Em Execução:** Ligado e funcionando.
* **Parando/Interrompendo:** Desligando...
* **Interrompida (Stopped):** Desligado. Você não paga pela computação, só pelo armazenamento EBS.
* **Encerrando:** Sendo destruído...
* **Encerrada (Terminated):** Destruído para sempre. Não há como voltar atrás.

Entender esses 9 passos te dá o poder de criar o "cérebro" para praticamente qualquer solução que você queira construir na nuvem. No próximo guia, veremos como transformar um único servidor em um exército elástico.