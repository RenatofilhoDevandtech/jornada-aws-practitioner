# <img src="https://api.iconify.design/logos/aws-iam.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Porteiro da Nuvem: Uma Análise Operacional do AWS IAM

Para um profissional de Operações de Sistema (SysOps), o IAM não é apenas uma ferramenta de segurança; é o **sistema nervoso central** que controla toda a sua infraestrutura na nuvem. Cada ação, cada automação, cada acesso começa com uma pergunta ao IAM: **"Isso é permitido?"**.

Dominar o IAM é a habilidade fundamental para construir um ambiente seguro, governado e pronto para a automação.

**Analogia:** Pense no IAM como o **"Departamento de Segurança e Controle de Acesso"** da sua fortaleza na nuvem.

---

### <img src="https://api.iconify.design/mdi/account-key-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Revisão Essencial (Os Pilares do IAM)

O IAM opera com base em dois processos fundamentais:

* **Autenticação (Quem é você?):** O processo de verificar a identidade de quem está tentando acessar.
    * **Na Prática:** Um usuário fornecendo sua senha e código MFA.
* **Autorização (O que você pode fazer?):** Após a autenticação, o processo de verificar quais ações essa identidade tem permissão para executar.
    * **Na Prática:** O IAM checa as **Políticas** anexadas à identidade para permitir ou negar uma ação, como "terminar uma instância EC2".

Esses processos se aplicam a um **Principal**, que é o termo técnico para qualquer entidade que faz uma solicitação: um **Usuário**, uma **Role** (Função) ou um serviço da AWS.

---

### <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. SysOps em Ação (Resolvendo Dores com IAM)

Como um profissional de operações usa o IAM para resolver problemas do dia a dia?

#### <img src="https://api.iconify.design/mdi/account-plus-outline.svg?color=currentColor" width="20" /> Cenário 1: Onboarding de um Novo Desenvolvedor
* **A Dor:** "Um novo desenvolvedor precisa de acesso ao ambiente de teste, mas de forma alguma pode ter acesso ao de produção. Como fazer isso de forma segura e escalável?"
* **A Solução SysOps:**
    1.  Você **não** cria permissões do zero para o novo funcionário.
    2.  Você o adiciona ao **Grupo** `Desenvolvedores-Junior` no IAM.
    3.  Este grupo já tem uma **Política** anexada que permite ações de desenvolvimento (`ec2:RunInstances`, `s3:PutObject`, etc.), mas apenas em recursos que tenham a tag `Ambiente: Teste`. Qualquer tentativa de tocar em um recurso de produção será negada.

#### <img src="https://api.iconify.design/mdi/robot-industrial-outline.svg?color=currentColor" width="20" /> Cenário 2: A Automação Segura
* **A Dor:** "Uma instância EC2 que hospeda minha aplicação precisa de permissão para ler arquivos de um bucket S3. Como dar essa permissão sem salvar chaves de acesso no servidor, o que é um grande risco de segurança?"
* **A Solução SysOps:**
    1.  Você cria uma **IAM Role** com uma política que permite apenas a ação `s3:GetObject` no bucket específico.
    2.  Você anexa esta Role à instância EC2.
    3.  A instância "assume" essa role automaticamente e obtém credenciais de segurança **temporárias**, que são rotacionadas pela AWS. Nenhuma chave de longo prazo é exposta.

---

### <img src="https://api.iconify.design/mdi/playlist-check.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Checklist de Ouro (As Melhores Práticas de IAM)

Esta é a lista que todo profissional de nuvem deve seguir rigorosamente.

1.  **<img src="https://api.iconify.design/mdi/crown-off-outline.svg?color=currentColor" width="18" /> Proteja a Conta Raiz:** Habilite o **MFA** e **nunca** use o usuário root para tarefas diárias. Ele é o "dono do prédio", guarde a chave mestra em um cofre.

2.  **<img src="https://api.iconify.design/mdi/account-outline.svg?color=currentColor" width="18" /> Use Usuários IAM Individuais:** Crie credenciais individuais para cada pessoa. Nunca compartilhe senhas ou chaves de acesso.

3.  **<img src="https://api.iconify.design/mdi/account-group-outline.svg?color=currentColor" width="18" /> Use Grupos para Gerenciar Permissões:** É a forma mais escalável e organizada. Quando um funcionário muda de função, você simplesmente o move de um grupo para outro.

4.  **<img src="https://api.iconify.design/mdi/key-minus.svg?color=currentColor" width="18" /> Aplique o Menor Privilégio:** Conceda apenas as permissões estritamente necessárias para uma função. Comece com zero e adicione conforme a necessidade, nunca o contrário.

5.  **<img src="https://api.iconify.design/mdi/account-switch-outline.svg?color=currentColor" width="18" /> Use Roles para Permissões de Serviço:** **Nunca** salve chaves de acesso (`AWS_ACCESS_KEY_ID`, etc.) em uma instância EC2. Sempre use IAM Roles.

6.  **<img src="https://api.iconify.design/mdi/lock-reset.svg?color=currentColor" width="18" /> Rotacione as Credenciais:** Configure uma política de senha forte no IAM para forçar a rotação de senhas e rotacione as chaves de acesso programáticas regularmente.

7.  **<img src="https://api.iconify.design/mdi/shoe-print.svg?color=currentColor" width="18" /> Monitore a Atividade:** Use o **AWS CloudTrail** para auditar todas as ações realizadas por usuários e roles na sua conta.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** A prova Cloud Practitioner é **cheia** de perguntas sobre o IAM. Os conceitos mais importantes são:
> * A diferença entre **Usuário** (identidade permanente), **Grupo** (coleção de usuários) e **Role** (identidade temporária).
> * O **Princípio do Menor Privilégio**.
> * A melhor prática número um: **Habilitar o MFA no usuário Root**.
> * Saber a diferença entre **Autenticação** (provar quem você é) e **Autorização** (o que você tem permissão para fazer).

---

### <img src="https://api.iconify.design/mdi/key-chain-variant.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> As Chaves da Fortaleza: Guia Prático de Credenciais e Acesso à AWS

Entender o IAM é como ser o chefe de segurança de uma fortaleza digital. Agora, vamos conhecer os **portões de entrada** e o **molho de chaves** que usamos para acessá-la. Na AWS, existem diferentes "portões" para diferentes finalidades (um para humanos, outro para máquinas), e cada um exige um tipo específico de "chave".

---

### <img src="https://api.iconify.design/mdi/door-sliding-open.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. Os Dois Portões de Entrada para a AWS

#### <img src="https://api.iconify.design/mdi/console.svg?color=currentColor" width="20" /> O Portão Principal (Acesso ao Console de Gerenciamento da AWS)
* **Para quem?** **Humanos** (Administradores, Desenvolvedores, Analistas).
* **O que é?** A interface web, gráfica e interativa que você acessa pelo seu navegador.
* **Analogia:** O **"portão principal da fortaleza, com um guarda"**. É projetado para a interação humana.
* **As Chaves Necessárias:**
    1.  **Nome de Usuário** e **Senha** do IAM.
    2.  (Recomendado) Um **Código de Autenticação Multi-Fator (MFA)**.

#### <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="20" /> A Doca de Carga (Acesso Programático)
* **Para quem?** **Máquinas e Automações** (Scripts, AWS CLI, SDKs, Terraform).
* **O que é?** A forma de interagir com a AWS através de código, sem uma interface gráfica.
* **Analogia:** A **"doca de carga automatizada para robôs"**, nos fundos da fortaleza. Não há guardas para conversar, apenas fechaduras eletrônicas.
* **As Chaves Necessárias:**
    1.  **ID da Chave de Acesso (Access Key ID):** O "número de série" público da sua chave.
    2.  **Chave de Acesso Secreta (Secret Access Key):** A "senha" secreta da sua chave.

---

### <img src="https://api.iconify.design/mdi/key-variant.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Chaveiro do Profissional de Nuvem (Resumo das Credenciais)

É crucial não confundir os diferentes tipos de "chaves".

| Tipo de Credencial | Analogia (A Chave) | Para que Serve? | Quando Usar? |
| :--- | :--- | :--- | :--- |
| **Credenciais do Usuário Raiz** | A **"Chave Mestra do Dono do Prédio"** | Acesso total e irrestrito. | **APENAS** para tarefas de gerenciamento da conta que só o root pode fazer. |
| **Nome de Usuário e Senha do IAM** | "Seu Rosto e Senha Falada" | Acesso ao **Console de Gerenciamento da AWS**. | Para o trabalho diário de qualquer humano na nuvem. |
| **Autenticação Multi-Fator (MFA)** | "O Código de Confirmação via Rádio" | Uma segunda camada de segurança para o login. | **SEMPRE**, tanto no Root quanto em todos os usuários IAM. |
| **Chaves de Acesso** | "A Chave Eletrônica para a Doca dos Robôs" | **Acesso Programático** (AWS CLI, SDKs). | Para scripts, automações e aplicações que precisam interagir com a AWS. |
| **Pares de Chaves (EC2 Key Pair)** | "A Chave da Porta do seu Escritório" | Acesso via **SSH** a uma instância EC2 Linux. | Para se conectar a um servidor específico e gerenciá-lo pela linha de comando. |

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT CRUCIAL:** A **senha** do seu usuário IAM te dá acesso ao "prédio" (o Console). O **par de chaves** do EC2 te dá acesso ao seu "escritório" (a instância). São duas coisas completamente diferentes e independentes!

---

### <img src="https://api.iconify.design/mdi/shield-check-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Veredito do Chefe de Segurança (Melhores Práticas)

O erro número um de segurança na nuvem é o **mau gerenciamento de credenciais**. Siga estas regras de ouro:

1.  **<img src="https://api.iconify.design/mdi/crown-off-outline.svg?color=currentColor" width="18" /> Aposente o Root:** Após a configuração inicial, guarde as credenciais do usuário root em um cofre e não as use. Crie um usuário administrativo no IAM para o dia a dia.

2.  **<img src="https://api.iconify.design/mdi/cellphone-lock.svg?color=currentColor" width="18" /> MFA em TUDO:** Habilite o MFA para o usuário root e para todos os usuários IAM. Não é negociável.

3.  **<img src="https://api.iconify.design/mdi/key-remove-variant.svg?color=currentColor" width="18" /> Chaves de Acesso São Tóxicas:** Nunca, jamais, salve Chaves de Acesso diretamente no seu código ou em uma instância EC2.
    > **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" /> HACK DE ARQUITETURA:** Para dar permissões a uma aplicação rodando em uma instância EC2, a prática correta é sempre usar **IAM Roles**. A role concede credenciais temporárias e rotacionadas automaticamente para a instância, eliminando o risco de chaves de longo prazo serem vazadas.

> **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação:** Para a prova, você **precisa** saber a diferença entre os **dois tipos de acesso** (Console vs. Programático) e as **credenciais usadas em cada um**. A distinção entre a **Senha do IAM**, as **Chaves de Acesso** e o **Par de Chaves do EC2** é um tópico frequente.

---

### <img src="https://api.iconify.design/mdi/file-document-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> As Leis da Nuvem: Guia Prático de Políticas e Funções (Roles) no IAM

Já sabemos que o IAM gerencia usuários, grupos e roles. Mas o que realmente dá poder a eles é a **Política**. Uma política é o "documento legal" que define as permissões. Entender como criar e aplicar essas "leis" é a essência da segurança na AWS.

**Analogia:** Pense na sua conta AWS como uma fortaleza. As políticas são os diferentes tipos de **"documentos de permissão"** que os guardas no portão consultam.

---

### <img src="https://api.iconify.design/mdi/account-card-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Crachá vs. A Placa na Porta (Políticas de Identidade vs. de Recurso)

Existem dois tipos principais de políticas, e a diferença é crucial.

#### <img src="https://api.iconify.design/mdi/badge-account-outline.svg?color=currentColor" width="20" /> Políticas Baseadas em Identidade
* **Analogia:** O **"Crachá de Acesso"** de um funcionário.
* **Como Funciona:** A política é **anexada a uma identidade** (um usuário, grupo ou role). As permissões andam *com a pessoa*. Onde quer que o funcionário vá, seu crachá diz o que ele pode fazer.
* **Pergunta que Responde:** "Onde **este funcionário** (João) pode entrar?"
* **É o tipo mais comum de política.**

#### <img src="https://api.iconify.design/mdi/door-closed-lock.svg?color=currentColor" width="20" /> Políticas Baseadas em Recurso
* **Analogia:** A **"Placa de Acesso na Porta de uma Sala"**.
* **Como Funciona:** A política é **anexada diretamente a um recurso** (como um bucket S3 ou uma fila SQS).
* **Pergunta que Responde:** "Quem pode entrar **nesta sala** (neste bucket S3)?"
> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> O Superpoder da Colaboração:** Políticas baseadas em recurso são a principal forma de conceder acesso a **outra conta da AWS**. A "placa na porta" do seu bucket S3 pode dizer: "Permitida a entrada de funcionários da Conta AWS #987654321".

---

### <img src="https://api.iconify.design/mdi/file-document-multiple-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. As Leis Especiais (SCPs e ACLs)

Existem outros dois tipos de políticas para casos de uso específicos:

* **<img src="https://api.iconify.design/logos/aws-organizations.svg?color=currentColor" width="18" /> Políticas de Controle de Serviço (SCPs):**
    * **Analogia:** As **"Leis Municipais"** da cidade-fortaleza.
    * **O que fazem?** Usadas com o **AWS Organizations**, as SCPs não concedem permissões, mas definem os **limites máximos** para as contas. O "Prefeito" (a conta principal da organização) pode decretar: "Nenhuma conta nesta Unidade Organizacional pode usar serviços de Inteligência Artificial". Mesmo que o administrador de uma conta dê a si mesmo `Allow IA:*`, a SCP o bloqueará.

* **<img src="https://api.iconify.design/mdi/format-list-checks.svg?color=currentColor" width="18" /> Listas de Controle de Acesso (ACLs):**
    * **Analogia:** O **"caderno antigo do porteiro"**.
    * **O que são?** Um sistema de permissões mais antigo e menos flexível que as políticas. Hoje, seu uso é raro, sendo mais comum em cenários legados do Amazon S3. A AWS recomenda usar políticas sempre que possível.

---

### <img src="https://api.iconify.design/mdi/code-json.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. Decifrando o "Juridiquês" (A Anatomia de uma Política)

As políticas são escritas em JSON. Vamos decifrar o exemplo do seu material:
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "MFA-Access",
            "Effect": "Allow",
            "Action": "ec2:*",
            "Resource": "*",
            "Condition": {
                "BoolIfExists": {
                    "aws:MultiFactorAuthPresent": "true"
                },
                "IpAddress": {
                    "aws:SourceIp": "1.2.3.4/32"
                }
            }
        }
    ]
}
```
* **`Effect`: "Allow"**: O efeito desta regra é **Permitir**.
* **`Action`: "ec2:*"**: A permissão é para **todas as ações** do serviço EC2.
* **`Resource`: "*"**: E se aplica a **todos os recursos** do EC2.
* **`Condition` (A Cláusula Condicional):** Esta é a parte mais poderosa! A permissão acima só é válida **SE** as seguintes condições forem verdadeiras:
    * `aws:MultiFactorAuthPresent: "true"`: **SE** o usuário estiver logado com MFA.
    * `aws:SourceIp: "1.2.3.4/32"`: **E SE** o acesso estiver vindo deste endereço IP específico.

> **A Dor que a `Condition` Resolve:** "Como eu posso dar a um administrador poder total, mas apenas quando ele estiver trabalhando do escritório e usando seu token de segurança?". O elemento `Condition` é a resposta.

---

### <img src="https://api.iconify.design/mdi/account-switch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 4. O "Crachá de Visitante" em Ação (Revisitando as Roles)

Agora que entendemos os tipos de políticas, podemos entender como uma **IAM Role** realmente funciona. Ela tem duas políticas:

1.  **Política de Confiança (Trust Policy):** É uma **Política Baseada em Recurso**. É a "placa na porta" da Role que diz **QUEM** (o `Principal`) tem permissão para "assumir" esta função.
2.  **Política de Permissão (Permissions Policy):** É uma **Política Baseada em Identidade**. É o "crachá" que a Role te dá, definindo o que você pode fazer **DEPOIS** de assumi-la.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 
> 1.  Saiba a diferença entre uma **Política Baseada em Identidade** (o que *este usuário* pode fazer?) e uma **Política Baseada em Recurso** (quem pode acessar *este recurso*?).
> 2.  Lembre-se que um `Deny` explícito **sempre vence** qualquer `Allow`.
> 3.  Entenda que uma **IAM Role** é o mecanismo para acesso **temporário** e seguro entre serviços ou contas.

---

### <img src="https://api.iconify.design/mdi/lock-check-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Dupla Fechadura Digital: Guia Prático de Autenticação Multi-Fator (MFA)

### O Cenário
> **Como** um administrador de nuvem responsável, **EU QUERO** implementar a mais forte camada de proteção de acesso para minhas contas, **PARA QUE** eu possa prevenir o acesso não autorizado mesmo que uma senha seja roubada.

### A Dor que o MFA Resolve: A Fragilidade das Senhas
No mundo digital, uma senha é um segredo. E segredos podem ser roubados, vazados ou adivinhados. A principal dor que o MFA resolve é a vulnerabilidade de depender de um **único fator de autenticação** (algo que você sabe). Se esse único segredo for comprometido, o invasor tem acesso total.

---

### <img src="https://api.iconify.design/mdi/key-chain-variant.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Como a Dupla Fechadura (MFA) Funciona?

A Autenticação Multi-Fator (MFA) exige que o usuário apresente **pelo menos duas provas** de identidade de **categorias diferentes**.

**Analogia:** Pense em **sacar dinheiro em um caixa eletrônico**. Você precisa de:
1.  **Algo que você TEM:** O **cartão do banco** (um objeto físico).
2.  **Algo que você SABE:** A **sua senha (PIN)** (um segredo).

Um ladrão pode roubar seu cartão, mas sem a senha, ele é inútil. Ele pode te espionar digitando a senha, mas sem o cartão, a senha é inútil. A segurança está na **combinação** de fatores de diferentes categorias.

As três categorias de fatores são:
* **<img src="https://api.iconify.design/mdi/form-textbox-password.svg?color=currentColor" width="18" /> Algo que você SABE:** Senha, PIN, frase secreta.
* **<img src="https://api.iconify.design/mdi/cellphone-key.svg?color=currentColor" width="18" /> Algo que você TEM:** Seu celular com um app autenticador, uma chave de segurança física (YubiKey).
* **<img src="https://api.iconify.design/mdi/fingerprint.svg?color=currentColor" width="18" /> Algo que você É:** Sua impressão digital, reconhecimento facial.

---

### <img src="https://api.iconify.design/logos/aws-iam.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Implementando o MFA na Sua Fortaleza AWS

Na AWS, a implementação do MFA é uma responsabilidade crítica.

#### <img src="https://api.iconify.design/mdi/crown-outline.svg?color=currentColor" width="20" /> 1. A Chave Mestra (O Usuário Root)
* **A Prática:** A **primeira e mais importante** ação que você deve tomar em qualquer conta AWS é **habilitar o MFA para o usuário Root**.
* **Por quê?** O usuário Root é o "dono do prédio". Comprometê-lo significa o fim do jogo. O **AWS Trusted Advisor** tem uma verificação de segurança gratuita que te alertará com um ícone vermelho se o MFA não estiver ativado no seu usuário Root.

#### <img src="https://api.iconify.design/mdi/account-outline.svg?color=currentColor" width="20" /> 2. Os Crachás dos Funcionários (Usuários IAM)
* **A Prática:** Habilite e **exija** o uso de MFA para todos os seus usuários IAM, especialmente aqueles com permissões administrativas.
* **Como?** Cada usuário pode habilitar o MFA em suas próprias credenciais de segurança.
* **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> O Hack do Administrador (Forçar o MFA):** Você pode anexar uma política IAM a um grupo de usuários que nega (`Deny`) todas as ações, **A NÃO SER QUE** (`Condition`) eles tenham se autenticado com MFA.
    ```json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "BlockEverythingUnlessMFA",
                "Effect": "Deny",
                "Action": "*",
                "Resource": "*",
                "Condition": {
                    "BoolIfExists": {
                        "aws:MultiFactorAuthPresent": "false"
                    }
                }
            }
        ]
    }
    ```
    Esta política diz: "Negue tudo, a menos que a 'chave' `aws:MultiFactorAuthPresent` seja verdadeira". Isso força toda a sua equipe a adotar a melhor prática de segurança.

---

### <img src="https://api.iconify.design/mdi/cellphone-check.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> As Ferramentas (Tipos de Dispositivos MFA)

* **Aplicativos Virtuais (O Mais Comum):** Use um aplicativo no seu smartphone, como o **Google Authenticator** ou **Authy**. Eles geram um novo código de 6 dígitos a cada 30 segundos. Esta é a forma mais comum e recomendada.
* **Chaves de Segurança de Hardware (O Mais Seguro):** Dispositivos Físicos como uma **YubiKey** que você conecta ao seu computador via USB. Eles oferecem a maior proteção.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Perguntas sobre MFA são **garantidas** na prova Cloud Practitioner. Lembre-se:
> 1.  É a melhor prática para proteger **TODAS** as contas, mas **ESPECIALMENTE a conta raiz**.
> 2.  O objetivo é adicionar uma **segunda camada de segurança**, exigindo uma prova de identidade de uma categoria diferente (algo que você tem) além da senha (algo que você sabe).

---

### <img src="https://api.iconify.design/logos/aws-iam.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Demonstração Prática: IAM em Ação (Menor Privilégio e Roles)

### O Cenário (A "User Story")

> **Como** um administrador de nuvem, **EU QUERO** criar um usuário com permissões limitadas para um novo estagiário e uma role segura para minha aplicação, **PARA QUE** eu possa seguir o Princípio do Menor Privilégio, protegendo meu ambiente contra erros acidentais e automatizando permissões de serviço de forma segura.

### A Dor que o Lab Resolve

1.  **O Risco do "Super Admin":** Dar permissões de administrador para todos é fácil, mas perigoso. Um único erro de um usuário com poder total pode deletar recursos críticos.
2.  **O Perigo das Senhas no Código:** Salvar chaves de acesso (`Access Keys`) dentro de uma aplicação em uma instância EC2 é um grande risco de segurança. Se o servidor for comprometido, as chaves são roubadas.

Este laboratório resolve essas duas dores, ensinando as melhores práticas de gerenciamento de identidade.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:
* [ ] Criar uma política IAM customizada com permissões de somente leitura.
* [ ] Criar um grupo IAM e anexar uma política a ele.
* [ ] Criar um usuário IAM e testar suas permissões restritas.
* [ ] Criar uma IAM Role para o serviço EC2.
* [ ] Anexar a Role a uma instância EC2 e verificar suas permissões temporárias.

### Pré-requisitos
* Uma conta AWS.
* Acesso como um usuário administrativo (como o `admin-seu-nome` que criamos no lab de Fundamentos).
* Uma instância EC2 já em execução (se não tiver, crie uma `t2.micro` com Amazon Linux).

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo

### Parte 1: O Crachá do Estagiário (Usuário de Somente Leitura)

**Analogia:** Vamos criar um "crachá de estagiário" que permite que ele veja o que está acontecendo na fortaleza, mas não lhe dá nenhuma chave para abrir portas ou modificar equipamentos.

#### Passo 1: Criando a "Lei" (A Política de Somente Leitura)
1.  No Console da AWS, navegue até o serviço **IAM**.
2.  No painel esquerdo, clique em **Policies** (Políticas) e depois em **Create policy** (Criar política).
3.  Você verá o editor de políticas. Selecione a aba **Visual editor**.
4.  **Service** (Serviço): Clique em `Choose a service` e procure por `EC2`.
5.  **Actions** (Ações): Para dar permissão de "leitura", precisamos de ações que descrevem e listam recursos.
    * Expanda a seção **List**. Marque a caixa no topo da lista para selecionar todas as ações de listagem.
    * Expanda a seção **Read**. Marque a caixa no topo da lista para selecionar todas as ações de leitura.
6.  **Resources** (Recursos): Para simplificar, vamos permitir que ele leia *todos* os recursos do EC2. Selecione **All resources**.
7.  Clique em **Next: Tags** e depois em **Next: Review**.
8.  **Name** (Nome): `Politica-EC2-ApenasLeitura`.
9.  Clique em **Create policy**.

#### Passo 2: Criando o "Departamento" (O Grupo de Acesso Limitado)
1.  No painel esquerdo do IAM, clique em **User groups** (Grupos de usuários) e em **Create group**.
2.  **User group name:** `Grupo-Estagiarios-TI`.
3.  Na lista de políticas, procure e marque a caixa da política que acabamos de criar: `Politica-EC2-ApenasLeitura`.
4.  Clique em **Create group**.

#### Passo 3: "Contratando" o Estagiário (O Usuário IAM)
1.  No painel esquerdo, clique em **Users** (Usuários) e em **Add users**.
2.  **User name:** `estagiario-joao`.
3.  **AWS credential type:** Marque **Password - AWS Management Console access**.
4.  Crie uma senha customizada e **desmarque** a opção para forçar a troca de senha no primeiro login (apenas para facilitar o lab).
5.  Clique em **Next: Permissions**.
6.  Selecione **Add user to group** e marque a caixa do `Grupo-Estagiarios-TI`.
7.  Clique em **Next: Tags**, depois **Next: Review**, e finalmente em **Create user**.

#### Passo 4: Testando as Restrições
> **`!!! tip "O Momento 'A-Ha!' do Menor Privilégio"`**
> Esta é a hora de ver o poder do IAM na prática.

1.  Faça **logout** da sua conta de administrador.
2.  Faça **login** novamente, mas desta vez como o usuário IAM `estagiario-joao`.
3.  Navegue até o serviço **EC2**. Você conseguirá **ver** a lista de instâncias perfeitamente.
4.  Agora, selecione uma instância, clique em **Instance state** e tente clicar em **Stop instance** ou **Terminate instance**.
5.  **Verificação:** Você receberá uma grande mensagem de erro vermelha na tela: **"Failed to stop instances... You are not authorized..."**.

**Parabéns!** Você acabou de implementar o Princípio do Menor Privilégio. Você deu ao João o acesso que ele precisava, e nada mais, protegendo sua infraestrutura.

---

### Parte 2: O Uniforme do Robô (IAM Role para EC2)

Agora, vamos resolver a segunda dor: dar permissão a uma máquina de forma segura.

**Analogia:** Vamos criar um "uniforme de leitor de arquivos do S3" e entregá-lo ao nosso "robô de inventário" (a instância EC2).

#### Passo 1: Criando o "Uniforme" (A Role)
1.  Faça **logout** do estagiário e **login** novamente com seu usuário **administrador**.
2.  Vá para o serviço **IAM**.
3.  No painel esquerdo, clique em **Roles** (Funções) e em **Create role**.
4.  **Trusted entity type** (Tipo de entidade confiável): Deixe selecionado **AWS service**.
5.  **Use case** (Caso de uso): Selecione **EC2** e clique em **Next**.
6.  Na página **Add permissions**, procure pela política gerenciada pela AWS chamada `AmazonS3ReadOnlyAccess`. Marque a caixa de seleção.
7.  Clique em **Next**.
8.  **Role name** (Nome da função): `Role-EC2-LeituraS3`.
9.  Revise e clique em **Create role**.

#### Passo 2: "Vestindo" o Robô com o Uniforme
1.  Vá para o console do **EC2** e selecione a sua instância.
2.  Clique em **Actions** > **Security** > **Modify IAM role** (Modificar IAM role).
3.  Na lista suspensa, selecione a role que acabamos de criar: `Role-EC2-LeituraS3`.
4.  Clique em **Update IAM role**.

#### Passo 3: Verificando os Superpoderes Temporários
1.  Conecte-se à sua instância EC2 via **SSH** (revise o Lab de Linux se precisar).
2.  **O Teste Final:** Dentro da instância, execute o seguinte comando da AWS CLI (ela já vem instalada no Amazon Linux):
    ```bash
    aws s3 ls
    ```
3.  **Verificação:** Mesmo que você **não tenha configurado nenhuma chave de acesso** na instância, o comando **funcionará** e listará seus buckets S3! A instância obteve as permissões temporárias e seguras diretamente da Role que anexamos.

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos
* [ ] No console do **EC2**, desanexe a IAM Role da sua instância.
* [ ] No console do **IAM**, delete a `Role-EC2-LeituraS3`.
* [ ] Delete o usuário `estagiario-joao`.
* [ ] Delete o grupo `Grupo-Estagiarios-TI`.
* [ ] Delete a política `Politica-EC2-ApenasLeitura`.