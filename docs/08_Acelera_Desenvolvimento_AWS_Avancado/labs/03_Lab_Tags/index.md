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

* [ ] Encontrar e aplicar `Tags` em recursos da AWS.
* [ ] Usar a AWS CLI com filtros (`--filter`) e consultas (`--query`) para extrair informações específicas.
* [ ] Automatizar a criação e limpeza de Snapshots do EBS.
* [ ] Sincronizar arquivos entre uma instância EC2 e um bucket S3.
* [ ] Habilitar o `Versionamento (Versioning)` no S3 e recuperar um arquivo deletado.
---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: O Detetive de Tags (Encontrando e Modificando Recursos)

**Analogia:** Primeiro, vamos atuar como detetives, usando a CLI para encontrar todos os "carros" (instâncias) que pertencem a um projeto específico, usando suas "placas de identificação" (Tags).

1.  **Conecte-se ao `Host de Comando (Command Host)`** usando o método de sua preferência (SSH ou EC2 Instance Connect).
2.  **Encontre as Instâncias do Projeto:**
    * Execute o comando abaixo para encontrar todas as instâncias que têm a tag `Projeto` com o valor `ERPSystem`. A saída será um JSON gigante.
    ```bash
    aws ec2 describe-instances --filter "Name=tag:Project,Values=ERPSystem"
    ```
3.  **Refine a Busca (O Poder do `--query`):**
    * **O "Porquê":** O JSON completo é demais. Vamos usar a opção `--query` para agir como uma "lente de aumento" e extrair apenas a informação que queremos.
    * Execute este comando para ver o ID da Instância, a Zona de Disponibilidade e as Tags de cada uma:
    ```bash
    aws ec2 describe-instances \
        --filter "Name=tag:Project,Values=ERPSystem" \
        --query 'Reservations[*].Instances[*].{ID:InstanceId,AZ:Placement.AvailabilityZone,Projeto:Tags[?Key==`Project`]|[0].Value,Ambiente:Tags[?Key==`Environment`]|[0].Value,Versao:Tags[?Key==`Version`]|[0].Value}'
    ```
4.  **Filtre Ainda Mais:** Agora, vamos encontrar apenas as instâncias que são do projeto `ERPSystem` **E** do ambiente `development`.
    ```bash
    aws ec2 describe-instances \
        --filter "Name=tag:Project,Values=ERPSystem" "Name=tag:Environment,Values=development" \
        --query 'Reservations[*].Instances[*].{ID:InstanceId,Ambiente:Tags[?Key==`Environment`]|[0].Value,Versao:Tags[?Key==`Version`]|[0].Value}'
    ```
5.  **Modifique as Tags em Lote:**
    * Examine o script `change-resource-tags.sh`. Ele usa o comando que acabamos de criar para encontrar os IDs das instâncias de desenvolvimento e, em seguida, usa o comando `aws ec2 create-tags` para **atualizar a tag `Version` de `1.0` para `1.1` em todas elas de uma só vez**.
    ```bash
    # Examine o script
    nano change-resource-tags.sh
    # Execute o script
    ./change-resource-tags.sh
    ```
    * Verifique novamente com o comando de busca do passo 3. Você verá que as versões das instâncias de desenvolvimento foram atualizadas.

#### Tarefa 2: O Robô "Stopinator" (Interrompendo Recursos por Tags)
**Analogia:** Vamos usar um "robô" (um script PHP) para desligar todos os "carros" do departamento de desenvolvimento no final do dia para economizar combustível.

1.  **Examine o Robô:**
    ```bash
    cd ~/aws-tools
    nano stopinator.php
    ```
    > Observe que o script aceita uma tag (`-t`) para identificar quais instâncias deve parar ou iniciar.
2.  **Desligue as Instâncias de Desenvolvimento:**
    ```bash
    ./stopinator.php -t"Project=ERPSystem;Environment=development"
    ```
    * **Verificação:** Vá para o console do **EC2 > Instâncias (Instances)** e veja as duas instâncias de desenvolvimento sendo paradas.
3.  **Ligue as Instâncias de Desenvolvimento:**
    ```bash
    ./stopinator.php -t"Project=ERPSystem;Environment=development" -s
    ```
    * **Verificação:** No console, veja as mesmas instâncias sendo iniciadas novamente.

#### Tarefa 3: Desafio - O Cofre Sincronizado e a Máquina do Tempo

1.  **Conecte-se à instância `Processor`** via EC2 Instance Connect.
2.  **Baixe e Descompacte os Arquivos de Teste:**
    ```bash
    wget [https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-3-124627/183-lab-JAWS-managing-storage/s3/files.zip](https://aws-tc-largeobjects.s3.us-west-2.amazonaws.com/CUR-TF-100-RSJAWS-3-124627/183-lab-JAWS-managing-storage/s3/files.zip)
    unzip files.zip
    ```
3.  **Ative a "Máquina do Tempo" (Versionamento do S3):**
    * **O "Porquê":** O versionamento cria um histórico de todas as alterações em um objeto. É a sua rede de segurança contra exclusões acidentais.
    ```bash
    aws s3api put-bucket-versioning --bucket <NOME_DO_SEU_BUCKET_S3> --versioning-configuration Status=Enabled
    ```
4.  **Sincronize os Arquivos para o S3:**
    ```bash
    aws s3 sync files/ s3://<NOME_DO_SEU_BUCKET_S3>/files/
    ```
5.  **Simule um Desastre (Delete um Arquivo):**
    ```bash
    rm files/file1.txt
    ```
6.  **Sincronize a Exclusão:**
    ```bash
    aws s3 sync files/ s3://<NOME_DO_SEU_BUCKET_S3>/files/ --delete
    ```
    > O `sync --delete` espelha o diretório. Se um arquivo foi deletado localmente, ele também será "deletado" no S3 (na verdade, ele cria um *marcador de exclusão*).
7.  **A Operação de Resgate (Recuperar o Arquivo):**
    * **Encontre a versão antiga:** Liste todas as versões do arquivo.
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
Parabéns! Você atuou como um verdadeiro administrador de nuvem. Você usou tags para gerenciar recursos em lote, automatizou o ciclo de vida de ambientes de desenvolvimento para economizar custos, e aprendeu a usar o poder do S3 e do versionamento para criar um sistema de arquivos sincronizado e à prova de erros humanos.