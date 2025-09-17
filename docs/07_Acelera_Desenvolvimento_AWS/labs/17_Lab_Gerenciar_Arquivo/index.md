# <img src="https://api.iconify.design/mdi/archive-cog-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: O Cofre Automatizado - Gerenciando Armazenamento com CLI e Scripts

### O Cenário (A "User Story")

> **Como** um engenheiro de operações (SysOps), **EU QUERO** automatizar a criação e a limpeza de backups (Snapshots) do meu servidor e sincronizar seus dados com um bucket S3, **PARA QUE** eu possa garantir a proteção dos dados, otimizar custos de armazenamento e ter uma cópia segura dos arquivos na nuvem.

### A Dor que o Lab Resolve

1.  **Backups Manuais:** Criar snapshots manualmente é um processo propenso ao esquecimento, o que coloca os dados em risco.
2.  **Acúmulo de Custos:** Esquecer de deletar snapshots antigos pode levar a custos de armazenamento inesperados e crescentes.
3.  **Recuperação de Arquivos:** Deletar um arquivo por engano pode ser catastrófico se não houver um plano de recuperação.

Este laboratório mostra como usar scripts e a AWS CLI para resolver essas dores, criando um sistema de gerenciamento de armazenamento robusto e automatizado.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Criar snapshots de um volume EBS usando a AWS CLI.
* [ ] Usar o `cron` do Linux para agendar a criação de snapshots.
* [ ] Usar um script Python para automatizar a limpeza de snapshots antigos.
* [ ] Sincronizar arquivos entre uma instância EC2 e um bucket S3.
* [ ] Habilitar o versionamento no S3 e recuperar um arquivo deletado.

### Duração
* Aproximadamente 45 minutos.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Preparando o Ambiente
1.  **Crie o "Depósito" (Bucket S3):** No console da AWS, vá para o **S3** e crie um bucket com um nome globalmente único (ex: `desafio-sincronizacao-renato-123`).
2.  **Dê Permissões à Instância:** Vá para o console do **EC2**, selecione a instância `Processor`, e em **Ações (Actions) > Segurança (Security) > Modificar função do IAM (Modify IAM role)**, anexe a `Função (Role)` chamada `S3BucketAccess`.
    > **O "Porquê":** Estamos dando um "crachá" para a instância `Processor` que a autoriza a "conversar" com o S3.

#### Tarefa 2: Gerenciando os Backups (Snapshots) via CLI

**Analogia:** Vamos programar um "robô fotógrafo" para tirar fotos (snapshots) do nosso "HD" (volume EBS) e depois um "robô faxineiro" para jogar fora as fotos antigas.

1.  **Conecte-se ao `Host de Comando (Command Host)`** usando o EC2 Instance Connect.
2.  **Identifique o Alvo:** Primeiro, precisamos saber qual volume "fotografar".
    ```bash
    aws ec2 describe-instances --filter 'Name=tag:Name,Values=Processor' --query 'Reservations[0].Instances[0].BlockDeviceMappings[0].Ebs.VolumeId' --output text
    ```
    > Anote o `VolumeId` retornado.
3.  **Crie o Snapshot Inicial (Manual):**
    * Obtenha o ID da instância `Processor`.
    ```bash
    aws ec2 describe-instances --filters 'Name=tag:Name,Values=Processor' --query 'Reservations[0].Instances[0].InstanceId' --output text
    ```
    * Pare a instância para garantir um backup consistente.
    ```bash
    aws ec2 stop-instances --instance-ids <ID_DA_INSTANCIA_PROCESSOR>
    aws ec2 wait instance-stopped --instance-ids <ID_DA_INSTANCIA_PROCESSOR>
    ```
    * Crie o snapshot.
    ```bash
    aws ec2 create-snapshot --volume-id <ID_DO_SEU_VOLUME> --description "Backup Inicial Manual"
    ```
    > Anote o `SnapshotId` retornado e aguarde a conclusão.
    ```bash
    aws ec2 wait snapshot-completed --snapshot-id <ID_DO_SEU_SNAPSHOT>
    ```
    * Inicie a instância novamente.
    ```bash
    aws ec2 start-instances --instance-ids <ID_DA_INSTANCIA_PROCESSOR>
    ```
4.  **Agende os Backups Automáticos (O Robô Fotógrafo):**
    * Vamos usar o `cron`, o agendador de tarefas do Linux, para criar um snapshot a cada minuto (para fins de teste).
    ```bash
    echo "* * * * * aws ec2 create-snapshot --volume-id <ID_DO_SEU_VOLUME> --description 'Backup Automatico' &>> /tmp/cronlog" > cronjob
    crontab cronjob
    ```
    > Aguarde alguns minutos. Vários snapshots serão criados.
5.  **Limpe os Backups Antigos (O Robô Faxineiro):**
    * Interrompa o agendador de backups:
    ```bash
    crontab -r
    ```
    * Execute o script Python que já está no host para deletar todos, exceto os 2 snapshots mais recentes.
    ```bash
    python3 /home/ec2-user/snapshotter_v2.py
    ```
    * **Verificação:** Verifique quantos snapshots restaram.
    ```bash
    aws ec2 describe-snapshots --filters "Name=volume-id,Values=<ID_DO_SEU_VOLUME>" --query 'Snapshots[*].SnapshotId' --output text | wc -l
    ```
    > A saída deve ser `2`.

#### Tarefa 3: Desafio - Sincronizando e Recuperando Arquivos com S3

1.  **Conecte-se à instância `Processor`** via EC2 Instance Connect.
2.  **Baixe e Descompacte os Arquivos de Teste:**
    ```bash
    wget [https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-3-124627/183-lab-JAWS-managing-storage/s3/files.zip](https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-3-124627/183-lab-JAWS-managing-storage/s3/files.zip)
    unzip files.zip
    ```
3.  **Ative a "Máquina do Tempo" (Versionamento do S3):**
    ```bash
    aws s3api put-bucket-versioning --bucket <NOME_DO_SEU_BUCKET_S3> --versioning-configuration Status=Enabled
    ```
4.  **Sincronize os Arquivos para o S3:**
    ```bash
    aws s3 sync files/ s3://<NOME_DO_SEU_BUCKET_S3>/files/
    ```
5.  **Simule um Desastre (Delete um Arquivo Localmente):**
    ```bash
    rm files/file1.txt
    ```
6.  **Sincronize a Exclusão para o S3:**
    ```bash
    aws s3 sync files/ s3://<NOME_DO_SEU_BUCKET_S3>/files/ --delete
    ```
    > O comando `sync --delete` espelha o diretório local. Se um arquivo foi deletado localmente, ele também será deletado no S3.
7.  **A Operação de Resgate (Recuperar o Arquivo):**
    * **Encontre a versão antiga:** Primeiro, liste todas as versões do arquivo deletado.
    ```bash
    aws s3api list-object-versions --bucket <NOME_DO_SEU_BUCKET_S3> --prefix files/file1.txt
    ```
    * Anote o `VersionId` da versão que **não** é um `DeleteMarker`.
    * **Restaure o arquivo:** Baixe a versão antiga de volta para sua máquina.
    ```bash
    aws s3api get-object --bucket <NOME_DO_SEU_BUCKET_S3> --key files/file1.txt --version-id <ID_DA_VERSAO_ANTIGA> files/file1.txt
    ```
8.  **Verificação Final:** Execute `ls files/`. O `file1.txt` está de volta!

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você atuou como um verdadeiro administrador de nuvem. Você automatizou o ciclo de vida de backups para proteger seus volumes e otimizar custos, e aprendeu a usar o poder do S3 e do versionamento para criar um sistema de arquivos sincronizado e à prova de erros humanos.

---

# <img src="https://api.iconify.design/mdi/notebook-heart-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Meu Diário de Bordo: Ensinando a Nuvem a Lembrar e a Esquecer

No mundo da tecnologia, gerenciar dados de forma responsável é tudo. Não basta apenas guardá-los; é preciso protegê-los (lembrar) e, ao mesmo tempo, otimizar os custos (esquecer o que não é mais necessário). O laboratório de hoje no AWS re/Start foi uma aula prática sobre exatamente isso.

A missão foi criar um sistema de backup automatizado para nossos "HDs virtuais" (volumes EBS) e, em seguida, construir um espelho seguro dos nossos arquivos no Amazon S3.

### A Jornada em 3 Atos

#### Ato 1: O Fotógrafo Robô (Automatizando os Snapshots)
* **A Dor:** Fazer backups manuais é a receita para o desastre. Um dia você esquece, e é exatamente nesse dia que o servidor falha.
* **O Que Eu Fiz:** Usei o `cron`, o agendador de tarefas do Linux, para dar uma ordem simples à AWS CLI.
* **O "Aha!" Moment:**
    * **Analogia:** Eu programei um **"robô fotógrafo"**. A ordem era clara: "A cada minuto, tire uma 'foto' (um **Snapshot**) do meu 'HD' (volume EBS)". Ver os snapshots aparecendo sozinhos no console, de forma automática, foi a prova de como a automação pode ser simples e poderosa.

#### Ato 2: O Faxineiro Robô (Automatizando a Limpeza)
* **A Dor:** Backups automáticos são ótimos. Mas se eu criar um snapshot por minuto, em um dia terei mais de 1400 snapshots ocupando espaço e gerando custos. Gerenciar isso manualmente é inviável.
* **O Que Eu Fiz:** Executei um script Python que tinha uma lógica de retenção.
* **O "Aha!" Moment:**
    * **Analogia:** Eu soltei um **"robô faxineiro"**. A regra dele era simples: "Não importa quantos backups existam, mantenha **apenas os 2 mais recentes** e jogue o resto fora". Ver a lista de snapshots diminuir automaticamente foi uma lição poderosa sobre como a automação é crucial para a otimização de custos.

#### Ato 3: O Cofre com Máquina do Tempo (S3 Sync e Versionamento)
* **A Dor:** Eu preciso de uma cópia dos meus arquivos de trabalho em um local super seguro e acessível, e também de proteção contra o clássico "ops, deletei o arquivo errado".
* **O Que Eu Fiz:** Sincronizei uma pasta local com um bucket S3 onde eu havia ativado o **Versionamento**.
* **O "Aha!" Moment:**
    * **Analogia:** Primeiro, usei o `aws s3 sync` para criar um **"espelho"** perfeito da minha pasta no S3. Depois, ativei a **"máquina do tempo" (o Versionamento)** no meu "cofre" (o bucket).
    * O teste final foi deletar um arquivo localmente e rodar o `sync --delete`. O arquivo sumiu do S3, como esperado. Mas, graças à máquina do tempo, a versão antiga não foi realmente apagada; ela estava apenas "escondida". Com alguns comandos da CLI, eu pude "viajar no tempo", pegar a versão antiga e restaurá-la. É a rede de segurança definitiva contra erro humano.

### A Grande Lição
O lab de hoje foi sobre o **ciclo de vida completo dos dados**. Não basta apenas criar e guardar. Um profissional de nuvem precisa pensar em:
1.  **Proteção:** Como automatizar os backups? (Snapshots com `cron`).
2.  **Otimização de Custos:** Como limpar o que não é mais necessário? (Scripts de retenção).
3.  **Resiliência a Erros:** Como me recuperar de uma exclusão acidental? (S3 Sync + Versionamento).

Este foi um dos labs mais "próximos da realidade" até agora. Lidar com backups e recuperação de arquivos é o pão com manteiga de qualquer equipe de operações. Ter construído automações que resolvem exatamente essas dores me deu uma visão clara de como a nuvem transforma tarefas complexas em processos gerenciáveis e inteligentes.

#AWS #Cloud #DevOps #SysOps #Backup #Automation #S3 #EBS #AWSreStart