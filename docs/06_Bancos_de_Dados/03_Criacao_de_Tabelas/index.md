# <img src="https://api.iconify.design/mdi/table-edit.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Primeiro Desafio: Guia Prático de Criação de Tabelas e Tipos de Dados

Bem-vindo ao seu primeiro dia na QualquerEmpresa Global! Como vimos, sua gerente de projetos, Ana, te deu uma missão crucial: analisar a tabela de dados da cafeteria e propor uma estrutura melhor.

Esta não é uma tarefa trivial. Uma tabela mal projetada é como um guarda-roupa com gavetas do tamanho errado: as roupas não cabem direito, fica uma bagunça, e você nunca encontra o que precisa. No mundo dos dados, isso prejudica a integridade, a performance e a capacidade de extrair informações valiosas.

Vamos arregaçar as mangas e resolver este desafio.

---

### <img src="https://api.iconify.design/mdi/ruler-square.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O "Porquê": A Importância Crítica dos Tipos de Dados

Antes de corrigir a tabela, vamos entender por que a Ana está tão preocupada com os "tipos de dados".

* **Analogia:** Escolher o tipo de dado para uma coluna é como **decidir o formato de cada divisória** em uma gaveta nova. "Esta divisória será para anéis, esta para relógios, esta para lenços."

Escolher o tipo de dado correto é vital por três motivos:

1.  **<img src="https://api.iconify.design/mdi/check-decagram-outline.svg?color=currentColor" width="16" /> Integridade dos Dados:** Garante que apenas "meias" entrem na gaveta de meias. Se você definir uma coluna como `DATE` (data), o banco de dados vai rejeitar qualquer tentativa de inserir um texto como "ontem", forçando a consistência.
2.  **<img src="https://api.iconify.design/mdi/arrow-collapse.svg?color=currentColor" width="16" /> Otimização de Espaço:** Uma divisória para anéis (`INT`) ocupa muito menos espaço no guarda-roupa do que uma para casacos de inverno (`TEXT`). Usar o tipo certo economiza custos de armazenamento.
3.  **<img src="https://api.iconify.design/mdi/rocket-launch-outline.svg?color=currentColor" width="16" /> Performance:** É muito mais rápido para o "mordomo" (o DBMS) encontrar um relógio em uma gaveta de relógios do que procurar em uma caixa bagunçada. O banco de dados otimiza as buscas com base nos tipos de dados.

---

### <img src="https://api.iconify.design/mdi/format-list-bulleted-square.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O "O Quê": O Cardápio de Tipos de Dados SQL

Aqui estão os tipos de dados mais comuns que você encontrará.

| Tipo de Dado | O que Armazena? | Exemplo de Uso |
| :--- | :--- | :--- |
| **`VARCHAR(n)`**| Texto de tamanho **variável** (até `n` caracteres). | `nome_cliente`, `cidade` |
| **`CHAR(n)`** | Texto de tamanho **fixo** (exatamente `n` caracteres).| `codigo_pais` (ex: 'BRA'), `sigla_estado` (ex: 'SP')|
| **`INT`** ou **`INTEGER`** | Números **inteiros**. | `quantidade_estoque`, `vendas_unidades` |
| **`DECIMAL(p, s)`**| Números com **precisão decimal** exata. | `preco_produto`, `salario` (ideal para dinheiro) |
| **`DATE`** | Apenas **datas** (ano, mês, dia). | `data_nascimento` |
| **`DATETIME`** ou **`TIMESTAMP`**| **Data e hora**. | `data_do_pedido` |
| **`BOOLEAN`** | Apenas valores de **verdadeiro (`true`) ou falso (`false`)**. | `cliente_ativo`, `pedido_pago` |

---

### <img src="https://api.iconify.design/mdi/wrench-cog-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. Mão na Massa: Corrigindo a Tabela da Cafeteria

Vamos analisar a tabela de dados da Ana e responder às perguntas da atividade.

<img src="https://i.imgur.com/KqW4lI0.png" alt="Tabela de Vendas" />

* **Pergunta 1:** Qual tipo de dados é representado na coluna `date`?
    * **Resposta:** **`DATE`**.
    * **Por quê?** Armazenar como texto te impediria de fazer perguntas como "Mostre-me todas as vendas de Dezembro" ou "Qual foi o crescimento de vendas entre 2021 e 2022?". Como `DATE`, o banco de dados entende o calendário.

* **Pergunta 2:** Qual tipo de dados é representado na coluna `unit_sales`?
    * **Resposta:** **`INT`** (ou `INTEGER`).
    * **Por quê?** A coluna representa a venda de *unidades*, que são números inteiros. Usar `INT` é mais eficiente em espaço e performance do que usar um tipo decimal.

* **Pergunta 3:** Quais são as duas colunas que podem ser combinadas?
    * **Resposta:** Nenhuma das opções é ideal para combinar na mesma tabela.
    * **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> Insight de Especialista (Normalização):** A pergunta é uma "pegadinha". Um bom analista de dados não combinaria essas colunas. Em vez disso, ele perceberia que `food_category` e `food_subcategory` se repetem muito. A prática profissional (chamada de **normalização**) seria criar uma **tabela separada** chamada `Categorias` e usar um `ID` numérico para se referir a elas na tabela de vendas. Isso economiza espaço e evita erros de digitação.

---

### <img src="https://api.iconify.design/logos/aws-rds.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 4. Construindo o Guarda-Roupa na AWS (`CREATE TABLE`)

Com base na nossa análise, aqui está o comando SQL que você, como analista júnior, apresentaria para a Ana para criar a nova tabela corrigida.

```sql
CREATE TABLE VendasGlobais (
    data_venda DATE,
    categoria_comida VARCHAR(50),
    subcategoria_comida VARCHAR(100),
    pais VARCHAR(50),
    codigo_pais CHAR(3),
    continente VARCHAR(50),
    cidade VARCHAR(50),
    vendas_unidades INT
);

```
* **Como Fazer na AWS?** Em um banco de dados **Amazon RDS**, você se conectaria a ele usando um cliente SQL (como o DBeaver ou o query editor do próprio RDS) e executaria este comando `CREATE TABLE` para construir sua tabela perfeitamente projetada.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova, você não precisa escrever SQL, mas precisa entender os **conceitos**: o que é uma **tabela**, uma **coluna**, uma **linha**, e por que a escolha do tipo de dado correto é importante para a **integridade** e a **performance** do banco de dados.

# <img src="https://api.iconify.design/mdi/vector-square.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Arquiteto de Dados: Guia de Modelagem para SQL e NoSQL na AWS

Criar uma tabela é fácil. Criar a *tabela certa* para o problema certo é uma arte. A forma como você estrutura suas tabelas em um banco de dados relacional (SQL) é fundamentalmente **diferente** da forma como você estrutura seus dados em um banco não relacional (NoSQL).

Entender essas duas filosofias de design é o que separa um iniciante de um arquiteto de dados profissional.

---

### <img src="https://api.iconify.design/mdi/wardrobe-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Filosofia SQL: Normalização (Evite a Repetição)

* **O Objetivo:** Garantir que cada pedaço de informação seja armazenado **uma única vez** no banco de dados.
* **Analogia:** O design de um **"closet de luxo, modular e interconectado"**.
* **A Dor que Resolve:** **Inconsistência e desperdício.** Imagine uma tabela de `Pedidos` onde, para cada pedido, você digita o nome e o endereço completo do cliente.
    * **Problema 1 (Desperdício):** Se um cliente faz 500 pedidos, você armazenou o endereço dele 500 vezes.
    * **Problema 2 (Inconsistência):** Se esse cliente se muda, você precisa encontrar e atualizar o endereço nos 500 registros, correndo o risco de esquecer algum.
* **A Solução (Normalização):** Você quebra os dados em tabelas separadas e as conecta com chaves.
    1.  Crie uma tabela `Clientes` (o "módulo de clientes") com `ID_Cliente`, `Nome`, `Endereço`.
    2.  Na sua tabela `Pedidos`, em vez de repetir o endereço, você apenas insere uma pequena "etiqueta" de referência: o `ID_Cliente`.
* **<img src="https://api.iconify.design/logos/aws-rds.svg?color=currentColor" width="18" /> **Quando Usar na AWS?** Use este modelo com **Amazon RDS** e **Amazon Aurora** para aplicações transacionais (e-commerce, sistemas financeiros, ERPs) onde a **consistência e a integridade** dos dados são a prioridade máxima.

---

### <img src="https://api.iconify.design/mdi/treasure-chest-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Filosofia NoSQL: Denormalização (Otimize para a Leitura)

* **O Objetivo:** Estruturar os dados de forma que sua aplicação possa obter todas as informações que precisa para uma tela específica em **uma única e rápida operação de leitura**.
* **Analogia:** O design de uma **"mala de viagem otimizada para rapidez"**.
* **A Dor que Resolve:** Em escala massiva, a operação de juntar (`JOIN`) múltiplas tabelas, que é o superpoder do SQL, pode se tornar lenta.
* **A Solução (Denormalização):** A **duplicação de dados é uma ferramenta, não um inimigo**.
    * **Analogia:** Para uma viagem, você não leva seu closet inteiro e seu arquivo de endereços. Você pega sua camisa e **costura uma etiqueta com seu nome e o endereço do hotel diretamente nela**.
    * **Na Prática:** Em vez de ter uma coleção `Pedidos` e uma `Clientes`, você pode ter um único "documento" de pedido que já contém uma cópia das informações do cliente.
* **O Trade-Off:** A leitura é incrivelmente rápida. A escrita é mais complexa: se o cliente mudar de endereço, sua aplicação é responsável por encontrar todos os "pedidos" dele e atualizar a "etiqueta" copiada.
* **<img src="https://api.iconify.design/logos/aws-dynamodb.svg?color=currentColor" width="18" /> **Quando Usar na AWS?** Use este modelo com **Amazon DynamoDB** para aplicações que precisam de latência de milissegundos em altíssima escala (redes sociais, games, IoT). Você projeta sua estrutura de dados pensando nos **padrões de acesso** da sua aplicação.

---

### <img src="https://api.iconify.design/mdi/book-search-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O "Algo Mais": Índices, a Arma Secreta da Performance

* **O que é?** Um índice de banco de dados é uma estrutura de dados especial que melhora a velocidade das operações de busca.
* **Analogia:** É o **"índice remissivo no final de um livro de 1000 páginas"**.
* **A Dor que Resolve:** "Minha consulta `SELECT * FROM clientes WHERE cidade = 'São Paulo'` está demorando muito!"
* **Como Funciona:** Sem um índice, o banco de dados precisa ler a lista de clientes **inteira, linha por linha**, para encontrar quem é de São Paulo (um *Full Table Scan*). Com um índice na coluna `cidade`, o banco de dados vai direto para a letra 'S' do índice, encontra 'São Paulo', e vê que os clientes que ele precisa estão nas linhas 5, 87 e 1034. A busca é quase instantânea.

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT DE ESPECIALISTA:** Índices são um trade-off. Eles aceleram drasticamente as **leituras (`SELECT`)**, mas deixam as **escritas (`INSERT`, `UPDATE`)** um pouco mais lentas, pois o "índice remissivo" também precisa ser atualizado. Use-os com sabedoria nas colunas que você mais usa em cláusulas `WHERE`.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Associe **SQL/RDS** com **Normalização** (dados separados em múltiplas tabelas) e consistência.
> 2.  Associe **NoSQL/DynamoDB** com **Denormalização** (dados duplicados/aninhados), flexibilidade e performance em escala.
> 3.  Saiba que **Índices** são a principal ferramenta para **otimizar a performance de consultas** (leituras) em ambos os tipos de banco de dados.