# <img src="https://api.iconify.design/mdi/compass-rose.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Lab 01: O Mapa do Tesouro - Navegando com Maestria no Console da AWS

### O Cenário (A "User Story")

> **Como** um novo entusiasta da nuvem, **EU QUERO** aprender a navegar no Console de Gerenciamento da AWS de forma eficiente, **PARA QUE** eu possa encontrar os serviços que preciso rapidamente, organizar meu espaço de trabalho e evitar os erros mais comuns de iniciantes.

### A Dor que o Lab Resolve

O Console da AWS é incrivelmente poderoso, com centenas de serviços. Para um iniciante, isso pode ser intimidante. É como abrir um mapa de uma megalópole pela primeira vez. Esta "sobrecarga de informação" pode levar a erros simples, como criar um recurso na região errada e depois não conseguir encontrá-lo. Este laboratório te dará a confiança para se tornar um explorador experiente.

### Objetivos de Aprendizado
Ao final deste laboratório, você será capaz de:

* [ ] Encontrar qualquer serviço da AWS usando a barra de busca.
* [ ] Criar uma barra de atalhos personalizada para seus serviços mais usados.
* [ ] Entender e navegar entre as diferentes Regiões da AWS.
* [ ] Usar o Editor de Tags para encontrar recursos específicos.

### Pré-requisitos
* Uma conta AWS e um usuário IAM com permissões de administrador.

---

### <img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Passo a Passo: Um Tour Guiado

#### Passo 1: Encontrando seus Destinos (A Barra de Serviços)
A primeira tarefa em qualquer mapa é saber como encontrar um endereço.

1.  **O Método Rápido (A Barra de Pesquisa Universal):**
    * No topo do console, você verá uma barra de busca. Este é seu melhor amigo.
    * Digite `VPC` nela. Observe como ela já te mostra o link para o serviço, a documentação e outros recursos.
    * Digite `EC2` e pressione Enter. Você será levado diretamente para o painel do EC2.

2.  **O Método Exploratório (O Menu "Services"):**
    * No canto superior esquerdo, clique em **Services** (Serviços).
    * Observe como os serviços são organizados por categoria (`Compute`, `Storage`, `Database`, etc.). É uma ótima maneira de descobrir novos serviços e entender o ecossistema.

#### Passo 2: Criando seu "Acesso Rápido" (A Barra de Atalhos)
**A Dor:** Ter que procurar por `EC2` e `S3` toda vez que você faz login é ineficiente.

1.  No menu **Services**, você verá uma seção **Recently visited** (Visitados recentemente).
2.  Ao lado de cada nome de serviço (ex: `EC2`), você verá um ícone de **alfinete (pin) <img src="https://api.iconify.design/mdi/pin-outline.svg?color=currentColor" width="16" />**.
3.  **Sua Missão:** Encontre os "Quatro Fantásticos" e clique no alfinete ao lado de cada um:
    * **EC2**
    * **S3**
    * **VPC**
    * **IAM**
4.  Observe como eles agora aparecem fixados na barra de navegação superior. Você acabou de criar seu menu de acesso rápido personalizado!

#### Passo 3: A Regra Geográfica (O Seletor de Região)
Este é o conceito mais importante e a causa da maior confusão para iniciantes.

**A Dor:** "Eu tenho certeza de que criei uma instância EC2, mas agora a lista está vazia! A AWS deletou meu servidor?"

1.  Olhe para o canto superior direito do console. Você verá o nome de uma cidade, como **N. Virginia** (`us-east-1`) ou **São Paulo** (`sa-east-1`). Esta é a **Região** em que você está operando.
2.  Clique no nome da Região para abrir a lista de todas as Regiões disponíveis.
3.  Selecione uma Região **diferente** da sua atual. Por exemplo, se você estava em `N. Virginia`, mude para `Ohio` (`us-east-2`).
4.  **Observe o que acontece:** O console se atualiza. Se você navegar para o painel do EC2, verá que sua lista de instâncias (se você tinha alguma) está vazia.
5.  **Agora, mude de volta** para a sua Região original. Suas instâncias "reaparecerão".

> **`!!! note "Conceito Fundamental (Governança)"`**
> A maioria dos recursos da AWS (como instâncias EC2 e VPCs) são **regionais**. Eles vivem **apenas** na Região onde você os criou. Isso é uma feature de segurança e conformidade (garante a soberania dos dados), mas pode ser confuso. Se um recurso "sumiu", a primeira coisa a verificar é o seletor de Região. (Serviços como o IAM e o S3 são exceções e têm um escopo Global, mas a regra geral é ser regional).

#### Passo 4: O Inventário Central (Resource Groups & Tag Editor)
**A Dor:** "Minha conta tem centenas de recursos espalhados por vários serviços. Como eu encontro todos os recursos que pertencem ao 'Projeto-X'?"

1.  Na barra de busca de serviços, procure por **Resource Groups & Tag Editor**.
2.  No painel esquerdo, clique em **Tag Editor** (Editor de tags).
3.  Em **Regions**, selecione a sua região.
4.  Em **Resource types** (Tipos de recurso), você pode deixar `All supported resource types`.
5.  Em **Tags**, digite a `Chave` da tag que você quer procurar (ex: `Name`) e o `Valor` (ex: `ServidorWeb`, do nosso lab anterior).
6.  Clique em **Search resources** (Buscar recursos). O resultado mostrará todos os recursos (EC2, Volumes EBS, etc.) que correspondem àquela tag.

---

### <img src="https://api.iconify.design/mdi/check-all.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Verificação
Você agora sabe encontrar serviços, customizar sua barra de atalhos, entende a importância crucial das Regiões e como usar tags para encontrar seus recursos. Você tem o mapa da megalópole digital.

---

### <img src="https://api.iconify.design/mdi/delete-sweep-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Limpeza de Recursos
* [x] **Não há nada para limpar!** Este laboratório foi focado em navegação e não criou nenhum recurso com custo.

---

### <img src="https://api.iconify.design/mdi/comment-quote-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conclusão
Parabéns! Você dominou a habilidade mais fundamental para trabalhar na AWS: navegar no console com confiança.

Agora que você tem o mapa, está pronto para começar a construir nos territórios. No nosso próximo laboratório, vamos mergulhar fundo no serviço de computação mais importante: **Amazon EC2**.