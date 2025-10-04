# <img src="https://api.iconify.design/logos/aws-cloudformation.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab [Desafio Final]: O Arquiteto Chefe - Construindo uma VPC e EC2 com CloudFormation

### O Cenário (A "User Story")

> **Como** um Arquiteto de Nuvem, **EU QUERO** escrever um template do CloudFormation do zero para provisionar uma VPC segura com uma instância EC2 em uma sub-rede privada, **PARA QUE** eu possa demonstrar minha habilidade em criar infraestrutura como código de forma automatizada, repetível e seguindo as melhores práticas.

### A Dor que o Lab Resolve

Até agora, usamos templates prontos ou fizemos pequenas modificações. A dor que este desafio resolve é o **medo da "página em branco"**. Ao final, você terá a confiança de que consegue traduzir um requisito de arquitetura em um template do CloudFormation funcional.

### Objetivos de Aprendizado
Ao final deste desafio, você terá construído, via código, os seguintes recursos:
* [ ] Uma **VPC** customizada.
* [ ] Um **Gateway da Internet (Internet Gateway)**.
* [ ] Uma **Sub-rede Privada (Private Subnet)**.
* [ ] Um **Grupo de Segurança (Security Group)**.
* [ ] Uma **Instância EC2 (EC2 Instance)**.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Plano de Ação: Desenhando a Planta Baixa

**Analogia:** Nossa missão é ser o **"Arquiteto Chefe"** e desenhar a planta baixa completa de um novo "condomínio fechado".

#### Passo 1: Preparando a Mesa de Desenho
Vamos usar o terminal no navegador fornecido pelo laboratório.

1.  Primeiro, crie um arquivo em branco para o nosso template:
    ```bash
    touch meu-template.yaml
    ```
2.  Abra o arquivo em um editor de texto. O `nano` é mais simples que o `vi` para iniciantes.
    ```bash
    nano meu-template.yaml
    ```
3.  Dentro do arquivo, comece com a estrutura básica de um template CloudFormation.
    ```yaml
    AWSTemplateFormatVersion: '2010-09-09'
    Description: Meu primeiro template de VPC e EC2, criado do zero.

    Resources:
      # Nossos recursos virão aqui...
    ```

#### Passo 2: Desenhando os Muros (O Recurso VPC)
1.  Abaixo de `Resources:`, adicione o código para criar a VPC. **Atenção: a indentação (2 espaços) é crucial em YAML!**
    ```yaml
      MinhaVPC:
        Type: AWS::EC2::VPC
        Properties:
          CidrBlock: 10.0.0.0/16
          EnableDnsSupport: true
          EnableDnsHostnames: true
          Tags:
            - Key: Name
              Value: VPC-Desafio-Final
    ```
    > **O "Porquê":** `MinhaVPC` é o nome lógico que usaremos para nos referir a este recurso dentro do nosso template. `AWS::EC2::VPC` é o tipo de recurso oficial. Em `Properties`, definimos suas configurações.

#### Passo 3: Desenhando a Portaria (O Internet Gateway)
1.  Abaixo do recurso VPC, adicione o código para o Internet Gateway e, crucialmente, para **associá-lo** à nossa VPC.
    ```yaml
      MeuInternetGateway:
        Type: AWS::EC2::InternetGateway
        Properties:
          Tags:
            - Key: Name
              Value: IGW-Desafio-Final

      AnexarGatewayNaVPC:
        Type: AWS::EC2::VPCGatewayAttachment
        Properties:
          VpcId: !Ref MinhaVPC
          InternetGatewayId: !Ref MeuInternetGateway
    ```
    > **O "Porquê":** Não basta criar o "portão"; você precisa **"aparafusá-lo"** no muro. O recurso `VPCGatewayAttachment` faz essa conexão. Usamos `!Ref MinhaVPC` para nos referirmos à VPC que criamos no passo anterior.

#### Passo 4: Desenhando a Rua (A Sub-rede)
1.  Adicione o código para a sub-rede.
    ```yaml
      MinhaSubRedePrivada:
        Type: AWS::EC2::Subnet
        Properties:
          VpcId: !Ref MinhaVPC
          CidrBlock: 10.0.1.0/24
          Tags:
            - Key: Name
              Value: Sub-rede-Privada-Desafio
    ```

#### Passo 5: Desenhando a Fechadura (O Security Group)
1.  Adicione o código para o grupo de segurança, permitindo acesso SSH.
    ```yaml
      MeuSecurityGroup:
        Type: AWS::EC2::SecurityGroup
        Properties:
          GroupName: "SG-Desafio-Final"
          GroupDescription: "Permite acesso SSH"
          VpcId: !Ref MinhaVPC
          SecurityGroupIngress:
            - IpProtocol: tcp
              FromPort: 22
              ToPort: 22
              CidrIp: 0.0.0.0/0
    ```

#### Passo 6: Desenhando a Casa (A Instância EC2)
1.  Finalmente, adicione o código para a instância EC2, conectando todas as peças.
    ```yaml
      MinhaInstanciaEC2:
        Type: AWS::EC2::Instance
        Properties:
          InstanceType: t3.micro
          ImageId: ami-0c55b159cbfafe1f0 # AMI do Amazon Linux 2 para us-east-1 (N. Virginia), ajuste se necessário
          SubnetId: !Ref MinhaSubRedePrivada
          SecurityGroupIds:
            - !Ref MeuSecurityGroup
          Tags:
            - Key: Name
              Value: Servidor-Desafio-Final
    ```
    > **O "Aha!" Moment:** Veja como usamos `!Ref` para conectar a instância à `MinhaSubRedePrivada` e ao `MeuSecurityGroup` que definimos no mesmo template. É assim que o CloudFormation entende as dependências e constrói tudo na ordem certa.
2.  **Salve e saia do editor:** Pressione `CTRL + X`, depois `Y` e `Enter`.

---

### <img src="https://api.iconify.design/mdi/factory.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A "Fábrica" em Ação (Implantando a Pilha)

1.  **Valide a Planta Baixa:** Antes de construir, verifique se há erros de sintaxe no seu template.
    ```bash
    aws cloudformation validate-template --template-body file://meu-template.yaml
    ```
2.  **Envie para a Produção:** Use o comando `deploy`, que cria a pilha se ela não existir ou a atualiza se já existir.
    ```bash
    aws cloudformation deploy \
        --template-file meu-template.yaml \
        --stack-name Desafio-Final-Stack
    ```
    > O terminal mostrará o progresso da criação dos recursos.

### Verificação Final
1.  No console do **CloudFormation**, você verá sua `Desafio-Final-Stack` com o status `CREATE_COMPLETE`.
2.  Vá para os consoles do **VPC** e **EC2** para ver todos os recursos que sua "fábrica" construiu automaticamente a partir da sua "planta baixa".

### Limpeza
Quando terminar de admirar seu trabalho, limpe tudo com um único comando:
```bash
aws cloudformation delete-stack --stack-name Desafio-Final-Stack
```
### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns, Arquiteto Chefe! Você completou o desafio final. Você traduziu um conjunto de requisitos de negócio em um template de Infraestrutura como Código e o usou para provisionar um ambiente de nuvem completo, do zero. Esta é a habilidade mais fundamental e poderosa de um profissional de DevOps e nuvem.
