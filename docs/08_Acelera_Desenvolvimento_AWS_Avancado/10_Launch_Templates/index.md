# <img src="https://api.iconify.design/mdi/clipboard-file-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Pedido Favorito da Nuvem: Guia dos Modelos de Execução do EC2

**A Dor:** Lançar uma instância EC2 no console exige que você configure mais de uma dúzia de opções: AMI, tipo de instância, rede, security group, par de chaves, etc. Fazer isso manualmente toda vez é:
* **Lento:** Leva tempo para preencher tudo.
* **Propenso a Erros:** É fácil esquecer uma configuração ou escolher a opção errada.
* **Inconsistente:** Sua instância pode ficar diferente da instância do seu colega.

**A Solução:** Um **Modelo de Execução (Launch Template)**.
* **Analogia:** Pense nisso como o botão **"Salvar como Pedido Favorito"** no seu aplicativo de delivery de comida.
* **Como Funciona:** Você configura seu "pedido" perfeito **uma única vez** e o salva como um modelo. Na próxima vez que precisar de uma instância, em vez de passar por todas as telas, você simplesmente usa seu modelo salvo.

---

### <img src="https://api.iconify.design/mdi/format-list-bulleted-square.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Receita Completa (O que um Modelo Armazena?)

Um Modelo de Execução armazena todos os parâmetros de lançamento de uma instância, incluindo:
* **<img src="https://api.iconify.design/mdi/image-multiple-outline.svg?color=currentColor" width="18" /> A "Planta Baixa":** O ID da **AMI**.
* **<img src="https://api.iconify.design/mdi/cpu-64-bit.svg?color=currentColor" width="18" /> O "Motor":** O **Tipo de Instância** (ex: `t3.micro`).
* **<img src="https://api.iconify.design/mdi/key-chain-variant.svg?color=currentColor" width="18" /> A "Chave da Porta":** O **Par de Chaves** para acesso SSH.
* **<img src="https://api.iconify.design/mdi/lan-connect.svg?color=currentColor" width="18" /> O "Endereço":** A **VPC** e a **Sub-rede**.
* **<img src="https://api.iconify.design/logos/aws-security-group.svg?color=currentColor" width="18" /> A "Fechadura":** Os **Security Groups**.
* **<img src="https://api.iconify.design/logos/aws-iam.svg?color=currentColor" width="18" /> O "Crachá de Acesso":** A **Função do IAM (IAM Role)**.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. Os Benefícios de Salvar seu Pedido

* **<img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="18" /> Velocidade e Consistência:** Reduz o risco de erro humano e garante que todas as instâncias lançadas a partir do mesmo modelo sejam idênticas.
* **<img src="https://api.iconify.design/mdi/gavel.svg?color=currentColor" width="18" /> Governança e Melhores Práticas:** Um arquiteto sênior pode criar um "Template Aprovado" que já inclui o Security Group correto e a "Golden AMI" segura, garantindo que os desenvolvedores juniores não lancem instâncias fora do padrão de segurança da empresa.
* **<img src="https://api.iconify.design/logos/aws-auto-scaling.svg?color=currentColor" width="18" /> Integração com Automação:** É a base para serviços como o **EC2 Auto Scaling**. O Auto Scaling Group usa o Modelo de Execução como seu "manual de contratação" para criar novas instâncias.

---

### <img src="https://api.iconify.design/mdi/history.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Superpoder do Versionamento

**A Dor:** "Eu preciso testar uma pequena mudança (como uma nova AMI ou um novo tipo de instância) sem destruir minha configuração antiga que eu sei que funciona."

* **A Solução:** Os Modelos de Execução suportam **versões**.
* **Analogia:** No seu app de delivery, em vez de editar seu "Pedido Favorito" original, você pode **"Criar uma nova versão"**:
    * **Versão 1:** Pizza + Refrigerante.
    * **Versão 2:** Pizza + Refrigerante **+ Brownie**.
* **Como Funciona:** Você pode criar múltiplas versões de um mesmo modelo. Um Auto Scaling Group pode ser configurado para usar a `Versão Padrão (Default)`. Você pode criar e testar uma `Versão 2` e, quando estiver confiante, promovê-la para ser a nova `Padrão`, o que pode acionar uma atualização gradual da sua frota.

---

### <img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Insight de Especialista: A Evolução

> **`!!! tip "Modelos de Execução (Launch Templates) vs. Configurações de Execução (Launch Configurations)"`**
> Você pode encontrar o termo "Launch Configuration" em documentações mais antigas. Ele era a ferramenta original para isso. No entanto, ele é **legado** e **imutável** (como um "pedido favorito" que não pode ser editado).
> **A AWS recomenda enfaticamente o uso de Modelos de Execução (Launch Templates) para todas as novas configurações.** Eles são mais flexíveis, suportam versionamento e recebem todos os novos recursos do EC2.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Um **Modelo de Execução (Launch Template)** é um template que armazena os **parâmetros de lançamento** de uma instância EC2.
> 2.  É a ferramenta **moderna e recomendada** para ser usada com o **EC2 Auto Scaling**.
> 3.  Sua principal vantagem sobre a antiga **Configuração de Execução (Launch Configuration)** é o suporte a **múltiplas versões**.

