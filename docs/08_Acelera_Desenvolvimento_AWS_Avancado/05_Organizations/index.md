# <img src="https://api.iconify.design/logos/aws-organizations.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O CEO da Nuvem: Guia Prático do AWS Organizations

No início, você tem uma única conta AWS. Mas, à medida que sua empresa cresce, as melhores práticas ditam que você crie contas separadas para diferentes ambientes (desenvolvimento, produção), equipes (marketing, engenharia) ou unidades de negócio. E aí, o caos começa.

**A Dor:** Gerenciar dezenas de contas separadas é um pesadelo. Cada uma tem sua própria fatura, suas próprias políticas de segurança e nenhum controle central.

**A Solução:** **AWS Organizations**.
* **O que é?** Um serviço de gerenciamento que permite que você **consolide e gerencie centralmente múltiplas contas AWS**.
* **Analogia:** Pense na sua empresa como uma **"grande corporação"**. O AWS Organizations é a ferramenta que te permite criar a **"Holding"** (a Organização) e organizar suas **"filiais" (as contas AWS)** em **"departamentos" (as Unidades Organizacionais - OUs)**.

---

### <img src="https://api.iconify.design/mdi/sitemap-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Estrutura da Corporação

<p align="center">
  <img src="https://i.imgur.com/gKkCjLp.png" alt="Estrutura do AWS Organizations" />
</p>

* **<img src="https://api.iconify.design/mdi/flag-variant-outline.svg?color=currentColor" width="18" /> A Raiz (Root):** A "Holding Corporativa". É o contêiner para todas as suas contas.
* **<img src="https://api.iconify.design/mdi/folder-multiple-outline.svg?color=currentColor" width="18" /> Unidades Organizacionais (OUs):** Os "Departamentos". Você pode criar OUs para `Producao`, `Desenvolvimento`, `Seguranca`, e até mesmo aninhar OUs (ex: um departamento de `Marketing` dentro da OU `Producao`).
* **<img src="https://api.iconify.design/mdi/account-outline.svg?color=currentColor" width="18" /> Contas (Accounts):** As "Filiais". Cada conta AWS individual é uma "folha" na sua árvore organizacional.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. Os 4 Superpoderes do "CEO"

O Organizations te dá quatro benefícios principais para governar seu "império".

#### 1. <img src="https://api.iconify.design/mdi/cash-multiple.svg?color=currentColor" width="20" /> Faturamento Consolidado (Consolidated Billing)
* **A Dor que Resolve:** Receber e pagar dezenas de faturas separadas.
* **A Solução:** Você recebe **uma única fatura** da "holding" (a conta de gerenciamento). Além disso, o uso de todos os "departamentos" é somado, o que te ajuda a alcançar descontos por volume mais rapidamente.

#### 2. <img src="https://api.iconify.design/mdi/account-group-outline.svg?color=currentColor" width="20" /> Gerenciamento de Contas em Grupo
* **A Dor que Resolve:** Aplicar a mesma política de segurança em 10 contas de desenvolvimento, uma por uma.
* **A Solução:** Você anexa a política diretamente ao "departamento" (a OU `Desenvolvimento`), e todos os "funcionários" (as contas) dentro dela herdam automaticamente essa política.

#### 3. <img src="https://api.iconify.design/mdi/gavel.svg?color=currentColor" width="20" /> Gerenciamento Baseado em Políticas (SCPs)
* **A Dor que Resolve:** "Como eu garanto que a equipe de desenvolvimento, mesmo sendo administradora de sua própria conta, **nunca** consiga mexer nos logs de segurança do CloudTrail?"
* **A Solução:** **Políticas de Controle de Serviço (Service Control Policies - SCPs)**.
* **Analogia:** São as **"Leis Corporativas"** que vêm da matriz.
* **Como Funciona:** Uma SCP não concede permissões; ela define os **limites máximos**. Você anexa uma SCP à OU `Desenvolvimento` que diz: "`Deny cloudtrail:DeleteTrail`". Agora, nenhuma identidade em nenhuma conta dentro daquela OU poderá deletar uma trilha, nem mesmo o usuário root daquela conta.

#### 4. <img src="https://api.iconify.design/mdi/robot-industrial-outline.svg?color=currentColor" width="20" /> Gerenciamento de Contas via APIs
* **A Dor que Resolve:** Criar novas contas AWS para novos projetos é um processo manual.
* **A Solução:** O Organizations te dá APIs para **automatizar a criação e o gerenciamento de contas**, permitindo que você provisione novos ambientes de forma programática.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  **AWS Organizations** é para gerenciar **MÚLTIPLAS CONTAS AWS** de forma centralizada.
> 2.  Seu principal benefício de faturamento é o **Faturamento Consolidado (Consolidated Billing)**.
> 3.  As **Políticas de Controle de Serviço (SCPs)** são usadas para aplicar **restrições de permissão** em contas ou OUs, funcionando como "guard rails" de governança.

---

### <img src="https://api.iconify.design/logos/aws-organizations.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Governo da Nuvem: Guia de Segurança e Configuração do AWS Organizations

Já sabemos que o Organizations é a nossa "holding corporativa". Mas como a "matriz" garante que as "filiais" (contas AWS) sigam as regras da empresa? A resposta está na poderosa interação entre as políticas do IAM e a principal ferramenta de governança do Organizations: as **Políticas de Controle de Serviço (SCPs)**.

---

### <img src="https://api.iconify.design/mdi/scale-balance.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Lei e a Ordem (O Duelo: IAM vs. SCPs)

**A Dor que Resolve:** "Como eu, da matriz, posso garantir que a equipe de desenvolvimento, mesmo sendo administradora de sua própria conta, **NUNCA** consiga desativar os logs de segurança do CloudTrail?"

A solução é entender que as permissões em uma organização são o resultado de duas avaliações:

#### <img src="https://api.iconify.design/logos/aws-iam.svg?color=currentColor" width="20" /> Política do IAM (O Crachá)
* **Analogia:** O **"Crachá de Acesso"** dado a um funcionário pela **"gerência da filial local"**.
* **O que faz?** **CONCEDE** permissões. Ela diz o que um usuário, grupo ou role *pode* fazer.
* **Escopo:** Atua *dentro* de uma única conta.
* **Afeta o Root?** **Não**. Uma política do IAM não pode restringir o usuário root da conta.

#### <img src="https://api.iconify.design/mdi/gavel.svg?color=currentColor" width="20" /> Política de Controle de Serviço (SCP)
* **Analogia:** As **"Leis Corporativas"** ou os **"Decretos da Matriz"**.
* **O que faz?** **LIMITA** as permissões. Ela define as permissões **máximas** para uma conta. Ela não concede nada, apenas estabelece as "grades de proteção".
* **Escopo:** Atua sobre **contas inteiras** ou **Unidades Organizacionais (OUs)**.
* **Afeta o Root?** **Sim**. As SCPs se aplicam a **TODAS** as identidades da conta, incluindo o usuário root.

> **`!!! tip "A Lógica Final da Permissão"`**
> Para uma ação ser permitida, ela precisa ser permitida **TANTO** pela Política do IAM **QUANTO** pela SCP. Um `Deny` (Negação) em qualquer uma delas **SEMPRE VENCE**.
>
> **Exemplo:** Se o crachá do IAM de um usuário permite `ec2:TerminateInstances`, mas a Lei Corporativa (SCP) daquele departamento nega `ec2:TerminateInstances`, a permissão final é **NEGADA**.

---

### <img src="https://api.iconify.design/mdi/format-list-numbered.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Manual de Montagem (Configurando sua Organização)

O processo de configurar uma organização segue 4 passos lógicos:

1.  **<img src="https://api.iconify.design/mdi/office-building-outline.svg?color=currentColor" width="18" /> Crie a Matriz:** Escolha uma conta AWS para ser sua **conta de gerenciamento**. A partir dela, crie a Organização. Você pode então convidar contas existentes ou criar novas contas diretamente a partir da sua organização.
2.  **<img src="https://api.iconify.design/mdi/folder-multiple-outline.svg?color=currentColor" width="18" /> Crie os Departamentos:** Crie **Unidades Organizacionais (OUs)** para agrupar suas contas de forma lógica (ex: `Producao`, `Desenvolvimento`, `Seguranca`).
3.  **<img src="https://api.iconify.design/mdi/file-document-edit-outline.svg?color=currentColor" width="18" /> Escreva as Leis:** Crie **SCPs** e anexe-as às OUs ou a contas individuais para impor suas "grades de proteção" de governança.
4.  **<img src="https://api.iconify.design/mdi/check-decagram-outline.svg?color=currentColor" width="18" /> Audite a Conformidade:** Faça login em uma conta membro com um usuário de teste e verifique se as restrições da SCP estão funcionando como esperado.

---

### <img src="https://api.iconify.design/mdi/ruler-square.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. As Regras do Jogo (Limites e Acesso)

* **Limites:** O Organizations tem alguns limites arquiteturais a serem lembrados, como um máximo de **5 níveis de profundidade** para o aninhamento de OUs.
* **Acesso:** Lembre-se que você pode gerenciar sua organização de todas as formas padrão da AWS:
    * **Console de Gerenciamento da AWS** (para gerenciamento visual).
    * **AWS CLI** (para automação via script).
    * **AWS SDKs** (para integração com suas aplicações).

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  **IAM** concede permissões. **SCP** define os **limites** (grades de proteção).
> 2.  Uma **SCP** pode restringir o **usuário root** de uma conta membro.
> 3.  Para uma ação ser permitida, ela precisa ser permitida por **ambos**, IAM e SCP.