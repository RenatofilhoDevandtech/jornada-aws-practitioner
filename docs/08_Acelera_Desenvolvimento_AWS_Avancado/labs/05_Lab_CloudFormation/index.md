# <img src="https://api.iconify.design/logos/aws-cloudformation.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab: A Fábrica de Nuvens - Automação com o AWS CloudFormation

### O Cenário (A "User Story")

> **Como** um engenheiro de nuvem, **EU QUERO** usar um template do AWS CloudFormation para provisionar, atualizar e destruir minha infraestrutura de rede e computação de forma automatizada, **PARA QUE** eu possa criar ambientes consistentes, repetíveis e gerenciá-los como código.

### A Dor que o Lab Resolve

1.  **Inconsistência:** Criar uma VPC manualmente com todas as suas sub-redes e security groups é um processo complexo e propenso a erros. É quase impossível garantir que o ambiente de teste seja idêntico ao de produção.
2.  **Lentidão:** Fazer alterações na infraestrutura manualmente é lento.
3.  **Falta de Auditoria:** É difícil rastrear quem mudou o quê e quando.

Este laboratório resolve essas dores te ensinando a usar o CloudFormation, a "fonte única da verdade" para sua infraestrutura.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Implantar uma **Pilha (Stack)** do CloudFormation a partir de um template.
* [ ] Analisar e entender as seções de um template (Parâmetros, Recursos, Saídas).
* [ ] **Atualizar uma pilha** existente para adicionar novos recursos (um bucket S3 e uma instância EC2).
* [ ] Usar referências (`!Ref`) para conectar recursos dentro de um template.
* [ ] Terminar uma pilha e todos os seus recursos de forma limpa.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

#### Tarefa 1: Construindo a Fundação (Implantar a Pilha da VPC)

**Analogia:** Primeiro, vamos entregar a "planta baixa" da nossa "fortaleza de rede" para a "fábrica" do CloudFormation.

1.  **Baixe a "Planta Baixa":** Faça o download do arquivo de template `task1.yaml` fornecido no seu material de laboratório e abra-o em um editor de texto para analisá-lo.
    > **O "Porquê" das Seções:**
    > * `Parameters`: Permite que você insira valores customizados (como os blocos CIDR) no momento da criação, tornando o template reutilizável.
    > * `Resources`: O coração do template, onde a VPC e o Security Group são declarados.
    > * `Outputs`: Define quais informações importantes (como o ID do Security Group) serão exibidas após a criação.
2.  **Entregue para a "Fábrica":**
    * No Console da AWS, navegue até o serviço **CloudFormation**.
    * Clique em **Criar pilha (Create stack)** > **Com novos recursos (padrão)**.
    * Em `Especificar modelo (Specify template)`, selecione **Fazer upload de um arquivo de modelo (Upload a template file)** e envie o seu `task1.yaml`. Clique em **Avançar (Next)**.
    * **Nome da pilha (Stack name):** `Lab-VPC-Stack`.
    * Deixe os parâmetros com os valores padrão e clique em **Avançar** duas vezes.
    * Na página de revisão, confirme a criação e clique em **Criar pilha (Create stack)**.
3.  **Acompanhe a Construção:**
    * Observe a aba **Eventos (Events)**. Ela é o "diário de bordo" da fábrica, mostrando cada recurso sendo criado.
    * Aguarde até que o status da pilha mude para **`CREATE_COMPLETE`**. Sua fundação de rede está pronta!

#### Tarefa 2: Adicionando um "Depósito" (O Bucket S3)

**Analogia:** Agora, vamos fazer uma "reforma" na nossa planta baixa para adicionar um "depósito" (um bucket S3).

1.  **Edite a Planta Baixa:** Abra seu arquivo `task1.yaml` em um editor de texto.
2.  Na seção `Resources`, adicione o seguinte bloco de código YAML. **Atenção à indentação!**
    ```yaml
    S3Bucket:
      Type: AWS::S3::Bucket
    ```
    > **O "Porquê":** É simples assim. Estamos declarando que queremos um novo recurso do tipo `Bucket S3` e demos a ele o nome lógico `S3Bucket`.
3.  **Envie a Planta Revisada:**
    * No console do CloudFormation, selecione sua `Lab-VPC-Stack` e clique em **Atualizar (Update)**.
    * Selecione **Substituir modelo atual (Replace current template)** e faça o upload do seu arquivo `task1.yaml` modificado. Clique em **Avançar**.
    * Avance pelas próximas telas sem alterar nada.
4.  **Revise o "Relatório de Impacto" (`Change Set`):**
    * O CloudFormation irá te mostrar um preview das alterações. Você verá claramente que a única ação será **Adicionar (Add)** um novo recurso do tipo `AWS::S3::Bucket`.
    > **O "Porquê":** Esta é a inteligência do CloudFormation. Ele compara as duas "plantas" e executa apenas a mudança necessária, sem reconstruir tudo.
5.  Clique em **Atualizar pilha (Update stack)** e aguarde o status **`UPDATE_COMPLETE`**.

#### Tarefa 3: Construindo a "Casa" (A Instância EC2)

**Analogia:** A reforma final. Vamos adicionar a "casa principal" (a instância EC2) à nossa planta, conectando-a aos recursos que já existem.

1.  **Edite a Planta Baixa Novamente:** Abra seu arquivo `task1.yaml`.
2.  **Adicione um Parâmetro Inteligente:** No topo, na seção `Parameters`, adicione este novo parâmetro.
    ```yaml
    AmazonLinuxAMIID:
      Type: AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>
      Default: /aws/service/ami-amazon-linux-latest/amzn2-ami-hvm-x86_64-gp2
    ```
    > **O "Porquê":** Em vez de "chumbar" um ID de AMI, estamos usando o Parameter Store para buscar dinamicamente a **AMI mais recente** do Amazon Linux 2 para a Região onde a pilha está sendo executada.
3.  **Adicione o Recurso EC2:** Na seção `Resources`, adicione o seguinte bloco:
    ```yaml
    AppServerInstance:
      Type: AWS::EC2::Instance
      Properties:
        InstanceType: t3.micro
        ImageId: !Ref AmazonLinuxAMIID
        SecurityGroupIds:
          - !Ref AppSecurityGroup
        SubnetId: !Ref PublicSubnet
        Tags:
          - Key: Name
            Value: App-Server-via-CFN
    ```
    > **O "Porquê" do `!Ref`:** A **Função Intrínseca `!Ref`** é a "cola" do CloudFormation. Estamos dizendo: "Para esta instância, use o valor do parâmetro `AmazonLinuxAMIID` e conecte-a aos recursos `AppSecurityGroup` e `PublicSubnet` que já estão definidos **neste mesmo template**."
4.  **Atualize a Pilha:** Repita o processo de atualização da Tarefa 2, enviando seu novo template. Verifique no `Change Set` que ele irá adicionar uma nova instância EC2.

#### Tarefa 4: A Demolição (Excluir a Pilha)

**Analogia:** O projeto acabou. Com um único comando, vamos dizer à "fábrica" para demolir tudo que foi construído.

1.  No console do CloudFormation, selecione sua `Lab-VPC-Stack`.
2.  Clique em **Excluir (Delete)** e confirme.
3.  Observe a aba **Eventos (Events)**. O CloudFormation irá deletar todos os recursos na ordem inversa da criação, de forma limpa e segura.

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você atuou como um verdadeiro engenheiro DevOps. Você usou um único arquivo de texto para provisionar, atualizar iterativamente e destruir uma infraestrutura completa, demonstrando o poder, a segurança e a consistência da Infraestrutura como Código.