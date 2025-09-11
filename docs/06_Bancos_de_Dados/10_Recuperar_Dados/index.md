# <img src="https://api.iconify.design/mdi/table-multiple.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Unindo Mundos: Guia Prático de `UNION` e `JOIN`s em SQL

No mundo real, seus dados não vivem em uma única tabela gigante. Eles estão organizados e "normalizados" em tabelas separadas e relacionadas (Clientes, Pedidos, Produtos, etc.). Mas como juntamos tudo isso para criar um relatório útil?

Existem duas maneiras de combinar dados de múltiplas tabelas, e elas são fundamentalmente diferentes.

**Analogia:** Pense que você tem **planilhas do Excel**.
* **`UNION`** é o ato de **"empilhar"** uma planilha embaixo da outra.
* **`JOIN`** é o ato de usar o **"PROCV (VLOOKUP)"** para enriquecer uma planilha com dados de outra.

---

### <img src="https://api.iconify.design/mdi/table-row.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. Empilhando os Dados (O Operador `UNION`)

* **O que faz?** O `UNION` combina o resultado de duas ou mais instruções `SELECT` em um único conjunto de resultados, colocando as linhas umas sobre as outras.
* **Analogia:** "Copiar todas as linhas da planilha `Vendas_2025` e colar no final da planilha `Vendas_2024` para criar uma lista mestra."
* **A Dor que Resolve:** "Eu tenho uma tabela de `clientes_ativos` e uma de `clientes_inativos`. Como eu consigo uma lista de e-mails de **todos** os clientes para um comunicado geral?"

#### <img src="https://api.iconify.design/mdi/format-list-checks.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> As Regras de Ouro do `UNION`:
1.  O número de colunas em todas as instruções `SELECT` deve ser o mesmo.
2.  Os tipos de dados em cada coluna correspondente devem ser compatíveis.

**Exemplo:**
```sql
SELECT nome, email FROM clientes_ativos
UNION
SELECT nome, email FROM clientes_inativos;
```
> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO (`UNION` vs. `UNION ALL`):** Por padrão, o `UNION` **remove automaticamente as linhas duplicadas** do resultado final. Se você tem certeza de que não há duplicatas ou não se importa com elas, use o `UNION ALL`. Ele é muito mais rápido porque não gasta tempo verificando por duplicatas.

---

### <img src="https://api.iconify.design/mdi/vector-link.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. Costurando os Dados (A Cláusula `JOIN`)

O `JOIN` é a operação mais importante em um banco de dados relacional. É como damos vida às "relações" entre as tabelas.

* **O que faz?** Combina colunas de duas ou mais tabelas em um único resultado, com base em uma coluna relacionada entre elas (geralmente a chave primária e a estrangeira).
* **Analogia:** É o **"PROCV (VLOOKUP) do SQL"**.
* **A Dor que Resolve:** O problema central da normalização. "Minha tabela `Pedidos` só tem o `ID_do_Cliente`. Como eu mostro o **nome** do cliente no meu relatório de vendas?"

#### <img src="https://api.iconify.design/mdi/code-tags.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> A Anatomia de um `JOIN`:
```sql
SELECT 
    c.nome_cliente,  -- Nome Qualificado: coluna "nome_cliente" da tabela "c"
    p.data_pedido
FROM 
    Clientes AS c
JOIN 
    Pedidos AS p ON c.ID_Cliente = p.ID_Cliente;
```
* **`JOIN Pedidos AS p`**: "Junte com a tabela Pedidos, que terá o apelido `p`."
* **`ON c.ID_Cliente = p.ID_Cliente`**: A **condição de junção**. "A conexão entre as tabelas é onde o `ID_Cliente` da tabela de Clientes for igual ao `ID_Cliente` da tabela de Pedidos."

---

### <img src="https://api.iconify.design/mdi/compare-horizontal.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. Os Tipos de Costura (Tipos de `JOIN`)

#### <img src="https://api.iconify.design/mdi/set-center.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> `INNER JOIN` (O Casamento Perfeito)
* **O que faz?** Retorna apenas as linhas onde há uma **correspondência em AMBAS as tabelas**.
* **Analogia:** O PROCV padrão. Se um pedido tem um `ID_Cliente` que não existe na tabela `Clientes`, essa linha do pedido é **ignorada** no resultado final.

#### <img src="https://api.iconify.design/mdi/set-left.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> `LEFT JOIN` (O Lado Esquerdo é o que Manda)
* **O que faz?** Retorna **TODAS as linhas da tabela da esquerda** (`FROM`) e as linhas correspondentes da tabela da direita (`JOIN`). Se não houver correspondência na direita, as colunas da direita virão como `NULL`.
* **A Dor que Resolve:** "Eu quero uma lista de **TODOS** os meus clientes e, *se eles tiverem feito um pedido*, quero ver a data do pedido. Se não, ainda quero ver o cliente na lista."

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Insight:** Existem outros tipos de `JOIN` (`RIGHT`, `FULL OUTER`), mas no dia a dia, 95% das suas necessidades serão resolvidas com `INNER JOIN` e `LEFT JOIN`.

---

### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Contexto AWS

* **Amazon RDS e Aurora:** Os `JOIN`s são o coração das consultas em bancos de dados relacionais. Otimizar `JOIN`s com **índices** nas chaves estrangeiras é a principal tarefa de um DBA para garantir a performance destes serviços.
* **Amazon Athena:** O poder do Athena é que ele também permite executar `JOIN`s complexos entre múltiplos arquivos (ex: um `clientes.csv` e um `pedidos.json`) no seu Data Lake em S3, tratando-os como se fossem tabelas.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova Cloud Practitioner:
> 1.  Você não precisa escrever `JOIN`s, mas precisa entender que eles são a forma como bancos de dados **Relacionais (RDS/Aurora)** conectam dados entre tabelas.
> 2.  Entenda a diferença conceitual: **`UNION` empilha dados (verticalmente)**, **`JOIN` combina dados (horizontalmente)**.

---

### <img src="https://api.iconify.design/mdi/table-multiple.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Construindo Relatórios Completos: Guia Definitivo de `UNION` e `JOIN`s

No mundo real dos dados, a informação que você precisa raramente está em um único lugar. Graças a um bom design (Normalização), seus dados estão organizados em tabelas separadas e especializadas: uma para clientes, uma para produtos, uma para vendas.

Mas como juntamos tudo isso? O SQL nos oferece duas ferramentas poderosas, mas com propósitos muito diferentes: `UNION` e `JOIN`.

**Analogia:** Pense que seus dados estão em **planilhas do Excel**.
* **`UNION`** é o ato de **"empilhar"** uma planilha embaixo da outra para criar uma lista única.
* **`JOIN`** é o ato de usar o **"PROCV (VLOOKUP)"** para enriquecer uma planilha com colunas de outra.

---

### <img src="https://api.iconify.design/mdi/table-row.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. Empilhando as Planilhas (O Operador `UNION`)

* **O que faz?** Combina os resultados de duas ou mais consultas `SELECT` em um único conjunto de resultados, colocando as linhas umas sobre as outras.
* **A Dor que Resolve:** "Eu tenho uma tabela de `Vendas_2024` e outra de `Vendas_2025`. Como eu crio um relatório com as vendas de **todos os anos** juntos?"

#### <img src="https://api.iconify.design/mdi/format-list-checks.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> As Regras de Ouro do `UNION`:
1.  O **número de colunas** em todas as consultas `SELECT` deve ser o mesmo.
2.  Os **tipos de dados** em cada coluna correspondente devem ser compatíveis (ex: texto com texto, número com número).

**Exemplo:**
```sql
SELECT nome_cliente, cidade FROM clientes_sp
UNION ALL
SELECT nome_cliente, cidade FROM clientes_rj;
```
> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO (`UNION` vs. `UNION ALL`):**
> * **`UNION`**: Por padrão, ele **remove as linhas duplicadas**. É mais lento porque precisa verificar cada linha.
> * **`UNION ALL`**: Inclui **todas as linhas**, mesmo que sejam duplicadas. É muito mais rápido e eficiente. Use-o sempre que souber que não há duplicatas ou se elas não importarem para o seu resultado.

---

### <img src="https://api.iconify.design/mdi/vector-link.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O PROCV do SQL (A Cláusula `JOIN`)

O `JOIN` é a operação que dá vida ao modelo relacional. Ele "costura" tabelas diferentes.

* **O que faz?** Combina colunas de duas ou mais tabelas em um único resultado, com base em uma coluna de ligação entre elas.
* **A Dor que Resolve:** "Minha tabela `Vendas` tem a coluna `ID_Cliente`, mas eu preciso mostrar o **nome** do cliente no meu relatório."

#### <img src="https://api.iconify.design/mdi/code-tags.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> A Anatomia de um `JOIN`:
Para evitar ambiguidade quando duas tabelas têm uma coluna com o mesmo nome (como `id`), usamos nomes qualificados (`tabela.coluna`) e aliases (apelidos para as tabelas).

```sql
SELECT
    c.nome_cliente,         -- A coluna "nome_cliente" da tabela Clientes (apelido "c")
    p.data_pedido,
    t.nome_produto
FROM
    Clientes AS c
JOIN
    Pedidos AS p ON c.ID_Cliente = p.ID_Cliente -- Condição de ligação
JOIN
    Titulos AS t ON p.ID_Produto = t.ID_Produto; -- Outra condição de ligação* **`JOIN Pedidos AS p`**: "Junte com a tabela Pedidos, que terá o apelido `p`."
```
#### <img src="https://api.iconify.design/mdi/compare-horizontal.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Os Tipos de Junção Mais Comuns:
* **`INNER JOIN` (O Encontro Perfeito):**
    * **O que faz?** Retorna apenas as linhas onde há uma correspondência em **AMBAS** as tabelas.
    * **Analogia:** "Mostre-me apenas os clientes **que fizeram pedidos**."
* **`LEFT JOIN` (O Relatório Inclusivo):**
    * **O que faz?** Retorna **TODAS** as linhas da tabela da esquerda (a do `FROM`) e os dados correspondentes da tabela da direita. Se não houver correspondência, as colunas da direita virão como `NULL`.
    * **A Dor que Resolve:** "Mostre-me **TODOS** os clientes, e, *se eles tiverem feito um pedido*, mostre a data do pedido."

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Insight:** Existem outros tipos de `JOIN` (`RIGHT`, `FULL OUTER`), mas no dia a dia, 95% das suas necessidades serão resolvidas com `INNER JOIN` e `LEFT JOIN`.

---

### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Contexto AWS

* **Amazon RDS e Aurora:** Os `JOIN`s são o coração das consultas em bancos de dados relacionais. A performance dos seus `JOIN`s no **RDS** ou **Aurora** depende diretamente de uma boa modelagem de dados e do uso de **índices** nas suas chaves.
* **Amazon Athena:** O poder do Athena é que ele permite executar `JOIN`s complexos não apenas entre tabelas, mas entre **diferentes arquivos e formatos** no seu Data Lake em S3. Você pode juntar um arquivo `clientes.csv` com um `pedidos.parquet` em uma única consulta.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova Cloud Practitioner:
> 
> * Você não precisa escrever `JOIN`s.
> * Você precisa entender a diferença conceitual: **`UNION` empilha dados (verticalmente)**. **`JOIN` combina dados (horizontalmente)**.
> * Saiba que os `JOIN`s são a principal característica que

---

### <img src="https://api.iconify.design/mdi/vector-link.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Arte da Conexão: Guia Prático dos Tipos de `JOIN` em SQL

Já sabemos que o `JOIN` é o "PROCV" do SQL, a ferramenta para enriquecer uma tabela com dados de outra. Agora, vamos aprender as diferentes "técnicas de costura" que um especialista usa para obter resultados precisos.

Cada tipo de `JOIN` responde a uma pergunta de negócio diferente.

---

### <img src="https://api.iconify.design/mdi/table-large.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Cenário: Nossos Dados da Empresa

Para todos os exemplos, vamos usar estas duas tabelas simples:

**Tabela `Departamentos`:**
| id | nome_depto |
| :--: | :--- |
| 1 | Vendas |
| 2 | Engenharia |

**Tabela `Funcionarios`:**
| id | nome | id_departamento | id_gerente |
| :--: | :--- | :---: | :---: |
| 101 | Ana | 1 | 103 |
| 102 | Bruno | 2 | 104 |
| 103 | Carlos | 1 | NULL |
| 104 | Diana | 2 | NULL |
| 105 | Eva | NULL | 104 |

---

### <img src="https://api.iconify.design/mdi/compare-horizontal.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. Os Tipos de Junção na Prática

#### <img src="https://api.iconify.design/mdi/set-center.svg?color=currentColor" width="20" /> `INNER JOIN` (O Encontro Perfeito)
* **Pergunta de Negócio:** "Mostre-me uma lista de todos os funcionários **que estão em um departamento válido**."
* **Como Funciona:** Retorna apenas as linhas onde há uma correspondência em **AMBAS** as tabelas. A funcionária "Eva", que não tem `id_departamento`, será **excluída** do resultado.
* **O Código:**
    ```sql
    SELECT f.nome, d.nome_depto
    FROM Funcionarios AS f
    INNER JOIN Departamentos AS d ON f.id_departamento = d.id;
    ```
* **O Resultado:**
    | nome | nome_depto |
    | :--- | :--- |
    | Ana | Vendas |
    | Bruno | Engenharia |
    | Carlos | Vendas |
    | Diana | Engenharia |

#### <img src="https://api.iconify.design/mdi/set-left.svg?color=currentColor" width="20" /> `LEFT OUTER JOIN` (O Relatório Inclusivo)
* **Pergunta de Negócio:** "Mostre-me uma lista de **TODOS** os funcionários e, *se eles tiverem um departamento*, mostre o nome do departamento."
* **Como Funciona:** Retorna **TODAS as linhas da tabela da esquerda** (a do `FROM`, neste caso `Funcionarios`) e os dados correspondentes da tabela da direita. Se não houver correspondência, a coluna da direita virá como `NULL`.
* **O Código:**
    ```sql
    SELECT f.nome, d.nome_depto
    FROM Funcionarios AS f
    LEFT JOIN Departamentos AS d ON f.id_departamento = d.id;
    ```
* **O Resultado:**
    | nome | nome_depto |
    | :--- | :--- |
    | Ana | Vendas |
    | Bruno | Engenharia |
    | Carlos | Vendas |
    | Diana | Engenharia |
    | **Eva** | **NULL** |

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** O `LEFT JOIN` é a ferramenta perfeita para encontrar "órfãos". Para descobrir quais funcionários **não têm** um departamento, você usaria um `LEFT JOIN` e adicionaria `WHERE d.id IS NULL`.

#### <img src="https://api.iconify.design/mdi/mirror-rectangle.svg?color=currentColor" width="20" /> `Self JOIN` (O Espelho da Tabela)
* **Pergunta de Negócio:** "Crie um organograma, mostrando cada funcionário e o nome do seu respectivo gerente."
* **Como Funciona:** Esta é uma técnica especial onde você junta uma tabela **com ela mesma**. O segredo é usar **aliases de tabela** para tratá-la como se fossem duas tabelas diferentes.
* **O Código:**
    ```sql
    SELECT
        f.nome AS "Nome do Funcionário",
        g.nome AS "Nome do Gerente"
    FROM
        Funcionarios AS f -- A tabela "f" representa o funcionário
    INNER JOIN
        Funcionarios AS g -- A tabela "g" representa o gerente
    ON
        f.id_gerente = g.id; -- A ligação é onde o "id_gerente" do funcionário é igual ao "id" do gerente
    ```
* **O Resultado:**
    | Nome do Funcionário | Nome do Gerente |
    | :--- | :--- |
    | Ana | Carlos |
    | Bruno | Diana |
    | Eva | Diana |

---

### <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO E BOAS PRÁTICAS

* **Nomes Qualificados:** Como vimos nos exemplos (`f.nome`, `d.nome_depto`), usar o alias da tabela antes do nome da coluna (`alias.coluna`) não é opcional quando se usa `JOIN`s; é uma **necessidade** para evitar erros de ambiguidade.
* **Performance:** `JOIN`s podem ser operações "caras" para o banco de dados. A performance dos seus `JOIN`s em **Amazon RDS** ou **Aurora** depende 100% da criação de **índices** nas colunas usadas na cláusula `ON` (as chaves primárias e estrangeiras).
* **Para a Prova:** Entenda a diferença conceitual:
    * **`INNER JOIN`** retorna apenas os dados que **combinam** nas duas tabelas.
    * **`LEFT JOIN`** retorna **todos** os dados da primeira tabela, mais os que combinam da segunda.

Dominar os diferentes tipos de `JOIN` é a chave para desbloquear o verdadeiro poder relacional do seu banco de dados e responder a praticamente qualquer pergunta de negócio.