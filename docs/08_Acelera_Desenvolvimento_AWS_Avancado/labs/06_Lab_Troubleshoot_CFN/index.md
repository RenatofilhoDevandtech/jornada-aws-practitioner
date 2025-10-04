# <img src="https://api.iconify.design/mdi/magnify-scan.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab [Desafio]: O Detetive do CloudFormation - Solucionando Problemas de Pilhas

### O Cenário (A "User Story")

> **Como** um engenheiro DevOps, **EU QUERO** usar a AWS CLI para implantar uma infraestrutura complexa a partir de um template do CloudFormation, diagnosticar as falhas que ocorrerem e aplicar as correções necessárias, **PARA QUE** eu possa dominar o ciclo de vida completo da Infraestrutura como Código, da criação à depuração.

### A Dor que o Lab Resolve

Escrever um template do CloudFormation é metade da batalha. A outra metade é saber o que fazer quando a implantação falha. Este laboratório resolve a dor do **"template quebrado"** e da **"pilha travada"**, te ensinando um método sistemático para investigar, diagnosticar e consertar os problemas mais comuns do CloudFormation.

### Objetivos de Aprendizado
Ao final deste desafio, você será capaz de:

* [ ] Praticar o uso de JMESPath para filtrar saídas JSON.
* [ ] Diagnosticar e corrigir um erro de `CREATE_FAILED` em uma pilha.
* [ ] Usar a flag `--on-failure DO_NOTHING` para preservar recursos e analisar logs.
* [ ] Detectar e analisar o "desvio de configuração" (`Drift Detection`).
* [ ] Solucionar e corrigir um erro de `DELETE_FAILED` para reter recursos.


---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: A Investigação

#### Tarefa 1: Aquecendo as Ferramentas (Prática com JMESPath)
Antes de investigar, um bom detetive afia suas ferramentas. Vamos praticar o uso do JMESPath, a "lupa" para filtrar saídas JSON.

1.  Acesse [jmespath.org](http://jmespath.org/).
2.  Pratique as expressões fornecidas no seu material de laboratório para entender como selecionar elementos de uma lista (`desserts[0]`), extrair valores de um objeto (`.name`), e filtrar (`[?name=='Carrot cake']`).
    > **O "Porquê":** A AWS CLI retorna respostas em JSON. Dominar o JMESPath na opção `--query` te permite extrair *exatamente* a informação que você precisa, transformando uma montanha de dados em um insight preciso.

#### Tarefa 2: A Primeira Tentativa e a Falha
**Analogia:** Vamos entregar nossa "planta baixa" (`template1.yaml`) para a "fábrica" (CloudFormation) e ver o que acontece.

1.  **Conecte-se ao `Host da CLI (CLI Host)`** e configure a AWS CLI (`aws configure`).
2.  **Examine o Template:** Use `less template1.yaml` ou `cat template1.yaml` para analisar o que o template *tenta* fazer: criar uma VPC, uma sub-rede pública, um Security Group, um bucket S3 e uma instância EC2 que instala um servidor web.
3.  **Tente Criar a Pilha:**
    ```bash
    aws cloudformation create-stack \
        --stack-name myStack \
        --template-body file://template1.yaml \
        --capabilities CAPABILITY_NAMED_IAM \
        --parameters ParameterKey=KeyName,ParameterValue=vockey
    ```
4.  **Observe o Desastre:** Use o comando `watch` para observar os recursos sendo criados e, em seguida, deletados.
    ```bash
    watch -n 5 aws cloudformation describe-stack-resources --stack-name myStack
    ```
    > **O "Porquê":** O `watch` executa o comando a cada 5 segundos, nos dando uma visão em "tempo real". Você verá os recursos entrarem em `CREATE_IN_PROGRESS`, depois um falhar (`CREATE_FAILED`) e os outros entrarem em `DELETE_IN_PROGRESS`. Este é o **Rollback Automático** em ação.
5.  **Encontre a Pista Principal:** Após o rollback terminar, investigue o evento de falha.
    ```bash
    aws cloudformation describe-stack-events \
        --stack-name myStack \
        --query "StackEvents[?ResourceStatus == 'CREATE_FAILED']"
    ```
    > A `ResourceStatusReason` mostrará que a `WaitCondition` expirou. Isso significa que o script de `User Data` na instância EC2 falhou e nunca enviou o sinal de "sucesso".

6.  **Corrija e Tente Novamente:**
    * **O Desafio:** A instância foi deletada pelo rollback, então não podemos ver os logs.
    * **A Solução:** Crie a pilha novamente, mas desta vez diga ao CloudFormation para **não fazer o rollback** em caso de falha.
    ```bash
    # Primeiro, delete a pilha falha que ficou para trás
    aws cloudformation delete-stack --stack-name myStack
    
    # Agora, crie novamente com a flag --on-failure
    aws cloudformation create-stack \
        --stack-name myStack \
        --template-body file://template1.yaml \
        --capabilities CAPABILITY_NAMED_IAM \
        --on-failure DO_NOTHING \
        --parameters ParameterKey=KeyName,ParameterValue=vockey
    ```
    * **Investigue a Instância:** Após a falha, a instância EC2 `Web Server` permanecerá. Conecte-se a ela via SSH e examine o log: `tail -50 /var/log/cloud-init-output.log`.
    * **A Descoberta:** Você encontrará o erro: `No package http available`. O nome do pacote do servidor Apache está errado!
    * **A Correção:** Edite o `template1.yaml` (`vim template1.yaml` ou `nano`), encontre a linha `yum install -y http` e corrija para `yum install -y httpd`.
    * **Implante a Versão Corrigida:** Delete a pilha falha e crie-a novamente com o template corrigido. **Agora a pilha deve ser criada com sucesso (`CREATE_COMPLETE`)!**

#### Tarefa 3: O Desvio de Configuração (`Drift Detection`)
1.  **Faça uma Mudança Manual:** Vá para o console do **EC2 > Security Groups**. Encontre o `WebServerSG` criado pela pilha. Edite as regras de entrada e mude a origem da regra SSH de `0.0.0.0/0` para `My IP`.
2.  **Detecte o "Crime":**
    ```bash
    # Inicia a detecção de desvio
    aws cloudformation detect-stack-drift --stack-name myStack

    # Verifica o status até que o StackDriftStatus mude para "DRIFTED"
    aws cloudformation describe-stack-drift-detection-status --stack-drift-detection-id <ID_DO_COMANDO_ANTERIOR>
    ```
3.  **Veja os Detalhes do Desvio:**
    ```bash
    aws cloudformation describe-stack-resource-drifts --stack-name myStack --stack-resource-drift-status-filters MODIFIED
    ```
    > A saída mostrará exatamente qual propriedade (`CidrIp`) do seu Security Group foi alterada manualmente, provando que a "planta baixa" e a "casa construída" não estão mais em sincronia.

#### Tarefa 4: Desafio - O Mistério da Pilha que Não Deleta
1.  **Adicione um Arquivo ao Bucket:** Primeiro, adicione um objeto ao bucket S3 que a pilha criou.
2.  **Tente Deletar a Pilha:**
    ```bash
    aws cloudformation delete-stack --stack-name myStack
    ```
3.  **A Falha:** A pilha entrará no estado `DELETE_FAILED`. O motivo? O CloudFormation, por segurança, não deleta buckets S3 que não estão vazios.
4.  **A Solução do Desafio:** Para deletar a pilha **mantendo o bucket e seus arquivos**, você precisa atualizar o template, adicionando uma **`DeletionPolicy: Retain`** ao recurso do bucket S3, e depois executar a exclusão da pilha novamente. Outra forma mais direta, sem alterar o template, é usar a AWS CLI para deletar a pilha, mas especificando quais recursos devem ser retidos.
    ```bash
    # O comando --retain-resources recebe o NOME LÓGICO do recurso no template
    aws cloudformation delete-stack --stack-name myStack --retain-resources MyBucket
    ```

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns, detetive! Você usou as ferramentas da AWS e um método de investigação para diagnosticar e consertar uma infraestrutura quebrada. Você aprendeu a analisar logs, a preservar recursos para investigação, a detectar desvios de configuração e a contornar problemas de exclusão. Estas são as habilidades do dia a dia de um verdadeiro engenheiro de nuvem.