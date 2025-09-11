# <img src="https://api.iconify.design/mdi/account-key-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> As Chaves do Reino: Gerenciando Usuários, Grupos e Permissões

Até agora, aprendemos a navegar pelo sistema e a executar comandos. Mas quem tem o direito de executar esses comandos? Quem pode ler ou apagar um arquivo? A resposta para essas perguntas é a base da segurança no Linux.

Gerenciar usuários e grupos pode parecer uma tarefa administrativa, mas na verdade é a arte de construir um sistema seguro e organizado.

Pense nisso como gerenciar o acesso a um **prédio corporativo de alta segurança**. Cada conceito do Linux tem um paralelo perfeito nesse cenário.

---

### <img src="https://api.iconify.design/mdi/account-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Parte 1: Os Funcionários (Contas de Usuário)

Uma conta de usuário representa uma identidade no sistema.

* **Analogia:** Cada usuário é um **"funcionário"** com um crachá de identificação único.
* **Dor que Resolve:** A necessidade de **rastreabilidade e responsabilidade**. Se todos usassem a mesma conta, seria impossível saber quem apagou aquele arquivo importante. Contas individuais garantem que cada ação seja vinculada a uma pessoa.
* **Onde Ficam Cadastrados?** As "fichas cadastrais" de todos os funcionários ficam no arquivo `/etc/passwd`. Cada linha contém informações como nome de usuário, ID de usuário (UID), diretório home e o shell padrão.

#### <img src="https://api.iconify.design/mdi/card-account-details-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Comandos para Gerenciar Funcionários

* **`sudo useradd jdoe`**: **Contrata um novo funcionário** chamado "jdoe". Este comando cria a conta, o grupo principal e o diretório home (`/home/jdoe`).
* **`sudo usermod -c "Jane Doe" jdoe`**: **Atualiza a ficha cadastral** do funcionário. A opção `-c` adiciona um comentário (geralmente o nome completo).
* **`sudo userdel -r jdoe`**: **Demite o funcionário** e apaga todos os seus pertences (`-r` remove o diretório home).
* **`sudo passwd jdoe`**: **Define ou altera a senha** do funcionário "jdoe". (A senha é armazenada de forma criptografada no arquivo `/etc/shadow`).

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** A prática de **não compartilhar contas** é a regra número um da segurança de TI. Cada pessoa deve ter seu próprio usuário. Isso é válido tanto para o Linux quanto para sua conta da AWS.

---

### <img src="https://api.iconify.design/mdi/account-group-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Parte 2: Os Departamentos (Grupos)

Um grupo é simplesmente uma coleção de usuários.

* **Analogia:** Os grupos são os **"Departamentos"** da empresa: "Engenharia", "Marketing", "Financeiro".
* **Dor que Resolve:** **Gerenciamento de permissões em escala.** Em vez de dar acesso à pasta de relatórios financeiros para cada um dos 30 funcionários do financeiro individualmente, você dá permissão ao grupo "Financeiro" uma única vez. É mais fácil, mais rápido e muito menos propenso a erros.

#### <img src="https://api.iconify.design/mdi/clipboard-list-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Comandos para Gerenciar Departamentos

* **`sudo groupadd engenharia`**: **Cria um novo departamento** chamado "engenharia".
* **`sudo groupdel engenharia`**: **Extingue um departamento**.
* **`sudo usermod -aG engenharia jdoe`**: **Adiciona a funcionária "jdoe" ao departamento "engenharia"**.
    * **Hack:** A opção `-aG` significa **a**dicionar (**a**ppend) a um **G**rupo suplementar. Sem o `-a`, você removeria o usuário de todos os outros grupos dos quais ele faz parte!
* **`sudo gpasswd -d jdoe engenharia`**: **Remove a funcionária "jdoe"** do departamento "engenharia".

---

### <img src="https://api.iconify.design/mdi/key-master.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Parte 3: A Chave Mestra e o Acesso VIP (`root`, `su` e `sudo`)

No Linux, existe um usuário supremo, todo-poderoso.

* **Usuário `root`:**
    * **Analogia:** É o **"Zelador com a Chave Mestra"**. Ele pode abrir qualquer porta, entrar em qualquer sala, modificar qualquer coisa no prédio. Ele tem poder absoluto.
    * **<img src="https://api.iconify.design/mdi/alert-outline.svg?color=currentColor" width="16" /> O Perigo:** Com grande poder, vem grande responsabilidade. Um comando errado executado como `root` pode destruir o sistema inteiro sem aviso. Por isso, a **prática recomendada de segurança é NUNCA fazer login diretamente como `root`**. Você faz login com seu usuário normal e eleva seus privilégios apenas quando necessário.

Existem duas maneiras de "pegar a chave mestra":

| Comando | Analogia | Como Funciona? | Quando Usar? |
| :--- | :--- | :--- | :--- |
| **`su`** | **Pegar emprestado o crachá e o uniforme do Zelador.** | Você se **torna** o usuário `root`. Você precisa saber a senha do `root`. O terminal muda de `$` para `#`. | Quase nunca. Apenas quando você precisa executar uma longa sequência de tarefas administrativas. |
| **`sudo`** | **Pedir para o Zelador usar a chave dele para uma tarefa específica.** | Você executa **um único comando** com os poderes do `root`. Você digita a **SUA PRÓPRIA SENHA** para autorizar. | **SEMPRE.** É o método mais seguro e recomendado. |

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO LINUX ESSENTIALS:** A diferença entre `su` e `sudo` é um dos conceitos de segurança mais importantes e um tópico garantido na prova.
> * **`su` (Switch User):** Exige a senha do usuário de destino. Você se **transforma** no outro usuário.
> * **`sudo` (Superuser Do):** Exige a **sua** senha. Você **executa um comando como** outro usuário. É auditável (cada uso do `sudo` é registrado em `/var/log/secure`) e mais seguro.

* **O Arquivo `/etc/sudoers`:**
    * **Analogia:** É a **"Lista de Delegação de Tarefas para o Zelador"**. É neste arquivo que o administrador do sistema define quais usuários (ou grupos) podem usar o `sudo` e para quais comandos.
    * **<img src="https://api.iconify.design/mdi/alert-outline.svg?color=currentColor" width="16" /> Cuidado:** NUNCA edite este arquivo diretamente. Use sempre o comando `sudo visudo`, que trava o arquivo e verifica a sintaxe antes de salvar, evitando que você se tranque para fora do sistema.

---

### <img src="https://api.iconify.design/mdi/cloud-lock-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conectando com a Nuvem: Usuários Linux vs. AWS IAM

É fundamental não confundir os dois sistemas de identidade.

* **Analogia Final:** Pense na sua conta AWS como o **"Condomínio"** inteiro e em cada instância EC2 como um **"Apartamento"** dentro dele.
    * **<img src="https://api.iconify.design/logos/aws-iam.svg?color=currentColor" width="16" /> AWS IAM:** É o sistema de segurança **do Condomínio**. Ele controla quem pode entrar no prédio, quais elevadores pode usar e quais áreas comuns pode acessar (quais serviços AWS você pode usar).
    * **<img src="https://api.iconify.design/mdi/linux.svg?color=currentColor" width="16" /> Usuários Linux:** São os sistemas de segurança **de cada Apartamento**. Depois que o IAM te deixou entrar no prédio e pegar o elevador até o 5º andar (acessar a instância EC2), são os usuários e permissões do Linux que definem quais cômodos (pastas/arquivos) você pode acessar dentro daquele apartamento específico.

Eles trabalham juntos, em camadas, para criar um ambiente seguro.