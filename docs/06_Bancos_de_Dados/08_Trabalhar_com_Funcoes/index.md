# <img src="https://api.iconify.design/mdi/function-variant.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Caixa de Ferramentas do SQL: Guia Prático de Funções Essenciais

Já sabemos como buscar dados brutos com `SELECT`. Mas e se quisermos calcular a média de vendas, juntar o nome e o sobrenome de um cliente, ou encontrar todos os pedidos da última semana? Para isso, usamos as **Funções SQL**.

**Analogia:** Pense nas funções SQL como as **"fórmulas prontas do Excel"** (`=SOMA()`, `=MÉDIA()`, `=MAIÚSCULA()`). Elas são atalhos poderosos que executam cálculos e transformações nos seus dados diretamente no banco de dados, retornando um resultado pronto para você.

Existem dezenas de funções, mas elas se encaixam em algumas categorias principais. Vamos focar nas três mais importantes para o dia a dia.

---

### <img src="https://api.iconify.design/mdi/calculator-variant-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Arsenal do Analista (Funções de Agregação)

Estas são as funções mais poderosas para análise de dados. Elas pegam os valores de múltiplas linhas e os "agregam" em um único resultado de resumo. Quase sempre são usadas com a cláusula `GROUP BY`.

**A Dor que Resolve:** "Eu tenho uma tabela com 10 milhões de vendas. Eu não quero ver todas as linhas, quero apenas saber o faturamento total e o número de clientes únicos."

| Função | O que faz? | Exemplo de Uso |
| :--- | :--- | :--- |
| **`COUNT()`** | **Conta** o número de linhas. | `SELECT COUNT(*) FROM Pedidos;` |
| **`SUM()`** | **Soma** os valores de uma coluna numérica. | `SELECT SUM(valor_total) FROM Pedidos;` |
| **`AVG()`** | Calcula a **média** de uma coluna numérica. | `SELECT AVG(valor_total) FROM Pedidos;` |
| **`MAX()`** | Encontra o valor **máximo** em uma coluna. | `SELECT MAX(valor_total) FROM Pedidos;` |
| **`MIN()`** | Encontra o valor **mínimo** em uma coluna. | `SELECT MIN(valor_total) FROM Pedidos;` |

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO (A Palavra-Chave `DISTINCT`):**
> A função `COUNT()` tem um superpoder quando combinada com `DISTINCT`.
> * `COUNT(cliente_id)`: Conta **quantas vendas** foram feitas.
> * `COUNT(DISTINCT cliente_id)`: Conta **quantos clientes únicos** fizeram compras.

**<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> Cenário Prático na AWS:** Gerar um relatório de vendas por país.
```sql
SELECT
    pais,
    COUNT(DISTINCT id_cliente) AS numero_de_clientes,
    SUM(valor_total) AS faturamento_total,
    AVG(valor_total) AS ticket_medio
FROM
    Vendas
GROUP BY
    pais;
```
### <img src="https://api.iconify.design/mdi/format-font.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Estilista de Texto (Funções de String)

Estas funções são suas ferramentas para manipular e formatar dados de texto.

* **A Dor que Resolve:** "Os dados que recebi estão uma bagunça. Nomes em maiúsculas e minúsculas, com espaços extras, e eu preciso juntar o nome e o sobrenome."

| Função | O que faz? |
| :--- | :--- |
| **`CONCAT()`** | **Concatena** (junta) duas ou mais strings. |
| **`UPPER()` / `LOWER()`**| Converte uma string para **maiúsculas** ou **minúsculas**. |
| **`LENGTH()`** | Retorna o **comprimento** (número de caracteres) de uma string. |
| **`SUBSTRING()`** | **Extrai uma parte** de uma string. |
| **`TRIM()`** | **Remove espaços** em branco do início e do fim de uma string. |

* **<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Cenário Prático na AWS:** Limpar e padronizar nomes de clientes em uma tabela no seu Amazon RDS.
    ```sql
    -- Junta nome e sobrenome, remove espaços extras e padroniza para maiúsculas
    SELECT 
        CONCAT(UPPER(TRIM(nome)), ' ', UPPER(TRIM(sobrenome))) AS nome_completo
    FROM 
        Clientes;
    ```

---

### <img src="https://api.iconify.design/mdi/calendar-clock.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Mestre do Tempo (Funções de Data)

Estas funções permitem que você manipule e faça cálculos com datas e horas.

* **A Dor que Resolve:** "Preciso encontrar todos os clientes que se cadastraram no último mês" ou "Preciso calcular há quantos dias um pedido está pendente."

| Função (Exemplos Comuns*) | O que faz? |
| :--- | :--- |
| **`NOW()`** ou **`CURRENT_TIMESTAMP`** | Retorna a **data e hora atuais** do servidor. |
| **`DATE()`** | **Extrai apenas a parte da data** de um valor `DATETIME`. |
| **`YEAR()`**, **`MONTH()`**, **`DAY()`** | **Extraem o ano, mês ou dia** de uma data. |
| **`DATE_ADD()`**, **`DATE_SUB()`** | **Adiciona ou subtrai** um intervalo de tempo de uma data. |

_*A sintaxe exata das funções de data pode variar um pouco entre os diferentes motores de banco de dados (MySQL, PostgreSQL, etc.)._

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova Cloud Practitioner, você não precisa memorizar a sintaxe de cada função. O importante é entender o conceito de **Funções de Agregação (`COUNT`, `SUM`)** e saber que elas são usadas para resumir dados, uma tarefa comum em análise e Business Intelligence (BI). Saber que serviços como **Amazon Athena** e **Amazon Redshift** são projetados para executar essas agregações em volumes massivos de dados também é crucial.

---

### <img src="https://api.iconify.design/mdi/calculator-variant-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Análise Avançada com SQL: Guia de Funções de Data e Agregação

Já sabemos como selecionar e filtrar dados. Agora, vamos aprender a **calcular e transformar** esses dados diretamente no banco de dados. As funções são as "fórmulas" do seu SQL, permitindo que você faça perguntas muito mais inteligentes e complexas.

Vamos explorar as duas categorias de funções mais importantes para qualquer analista ou desenvolvedor.

---

### <img src="https-api.iconify.design/mdi/calendar-clock.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Mestre do Tempo (Funções de Data)

**A Dor que Resolve:** Dados de data e hora são armazenados em formatos precisos (ex: `2025-09-05 15:30:10`), mas as perguntas de negócio são mais amplas ("Vendas do último mês", "Idade do cliente"). As funções de data são a ponte entre esses dois mundos.

* **Analogia:** As **"ferramentas de calendário e cronômetro"** do gerente de vendas.

#### <img src="https://api.iconify.design/mdi/tools.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Funções Essenciais de Data:
* **`NOW()`** ou **`CURRENT_TIMESTAMP`**:
    * **O que faz?** Retorna a data e a hora exatas do servidor no momento da consulta.
* **`DATE_ADD()`** ou **`DATE_SUB()`**:
    * **O que fazem?** Adicionam ou subtraem um intervalo de tempo de uma data.
    * **Cenário Prático:** "Este cliente assinou nosso serviço por um ano. Qual a data de expiração?"
        ```sql
        SELECT DATE_ADD(data_de_inicio, INTERVAL 1 YEAR) AS data_expiracao FROM assinaturas;
        ```
* **`TIMESTAMPDIFF()`** ou **`DATEDIFF()`**:
    * **O que fazem?** Calculam a diferença entre duas datas.
    * **Cenário Prático:** "Calcular a idade de um cliente em anos."
        ```sql
        -- Exemplo de função aninhada: NOW() é usada dentro de TIMESTAMPDIFF
        SELECT TIMESTAMPDIFF(YEAR, data_nascimento, NOW()) AS idade FROM clientes;
        ```
* **`YEAR()`**, **`MONTH()`**, **`DAY()`**:
    * **O que fazem?** Extraem uma parte específica de uma data.

---

### <img src="https://api.iconify.design/mdi/chart-box-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Resumo Executivo (Funções de Agregação)

Estas funções pegam milhares de linhas e as condensam em um **único valor de resumo**. São o coração da Business Intelligence.

* **Analogia:** As **"ferramentas de resumo executivo"** do gerente de vendas.

#### <img src="https://api.iconify.design/mdi/format-list-numbered.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> As 5 Grandes Funções de Agregação:
* **`SUM()`**: **Soma** os valores de uma coluna. (*"Qual o faturamento total?"*)
* **`COUNT()`**: **Conta** o número de linhas. (*"Quantos pedidos foram feitos?"*)
* **`AVG()`**: Calcula a **média**. (*"Qual o ticket médio por venda?"*)
* **`MAX()`**: Encontra o valor **máximo**. (*"Qual foi a nossa maior venda individual?"*)
* **`MIN()`**: Encontra o valor **mínimo**. (*"Qual foi a nossa menor venda individual?"*)

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** As funções de agregação como `SUM()` e `AVG()` ignoram automaticamente os valores `NULL`. Elas não os tratam como zero, o que garante que seus cálculos não sejam distorcidos por dados ausentes.

---

### <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Workshop Prático: Resolvendo os Desafios

Vamos aplicar esses conceitos para resolver os desafios do material.

* **Desafio 1:** "Qual a quantidade total de livros vendidos no ano de 2017?"
    * **Solução:**
    ```sql
    SELECT SUM(qty) AS total_vendido_2017
    FROM pub1.sales 
    WHERE sldate LIKE '2017-%';
    ```
    * **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" /> Dica de Especialista:** Usar `LIKE` funciona, mas uma abordagem mais performática, que pode usar índices de forma mais eficiente, é usar uma função de data: `WHERE YEAR(sldate) = 2017`.

* **Desafio 2:** "Qual o custo total de todos os livros publicados no ano de 2016?"
    * **Solução:**
    ```sql
    SELECT SUM(slprice) AS custo_total_2016
    FROM pub1.titles 
    WHERE pubdate LIKE '2016-%';
    ```

---

### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Contexto AWS

Estas funções são o padrão SQL e você as usará extensivamente em qualquer serviço de banco de dados relacional na AWS.

* **Amazon RDS e Aurora:** Perfeitos para executar estas consultas em seus dados operacionais e transacionais.
* **Amazon Redshift:** Um serviço de Data Warehouse otimizado para executar agregações complexas (`SUM`, `AVG`) sobre petabytes de dados históricos.
* **Amazon Athena:** Permite que você execute estas mesmas funções de agregação e data diretamente em arquivos de log e CSV armazenados no seu Data Lake em S3.

> **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação:** Para a prova Cloud Practitioner, você não precisa escrever SQL, mas precisa entender os **casos de uso**.
> * **Funções de Agregação** são usadas para **Business Intelligence (BI) e análise**.
> * **Amazon Redshift** é o serviço otimizado para este tipo de carga de trabalho analítica em grande escala.

Com as funções, seu SQL evolui de um extrator de dados para uma poderosa calculadora analítica.

---

### <img src="https://api.iconify.design/mdi/format-font.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Estilista de Texto: Guia Prático de Funções de String em SQL

Dados do mundo real, especialmente textos inseridos por humanos, são bagunçados. Nomes vêm com espaços extras, cidades em maiúsculas e minúsculas, códigos de produtos que precisam ser quebrados... Lidar com essa bagunça é a principal tarefa de um profissional de dados.

As **funções de string** do SQL são a sua "caixa de ferramentas de restauração". Elas permitem que você limpe, padronize e transforme dados de texto diretamente em suas consultas.

**Analogia:** Pense em você como um **"restaurador de livros antigos"**. Cada função é uma ferramenta na sua mesa para consertar títulos e textos inconsistentes.

---

### <img src="https://api.iconify.design/mdi/content-cut.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Faxina (Funções de Limpeza)

A primeira etapa é sempre remover o "lixo" e os espaços desnecessários.

* **A Dor que Resolve:** "Estou tentando procurar por `cidade = 'São Paulo'`, mas a busca falha porque no banco de dados o valor está salvo como `'   São Paulo  '` com espaços no início e no fim."
* **A Ferramenta (`TRIM`):**
    * **Analogia:** A **"guilhotina e as tesouras"** para aparar as margens e os espaços em branco.
    * **`TRIM()`**: Remove espaços de **ambos** os lados.
    * `LTRIM()`: Remove espaços da **esquerda** (*Left*).
    * `RTRIM()`: Remove espaços da **direita** (*Right*).
    ```sql
    -- Retorna 'São Paulo', sem os espaços
    SELECT TRIM('   São Paulo  ');
    ```

---

### <img src="https://api.iconify.design/mdi/format-pilcrow-arrow-right.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Padronização (Funções de Formatação)

Depois de limpo, o texto precisa ser padronizado para garantir a consistência.

* **A Dor que Resolve:** Buscas por `estado = 'sp'` não encontram registros salvos como `'SP'` ou `'Sp'`.
* **As Ferramentas (`UPPER`, `LOWER`, `CONCAT`):**
    * **`UPPER()` e `LOWER()` (O Padronizador):** Convertem o texto para MAIÚSCULAS ou minúsculas.
        > **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> HACK:** Para buscas que ignoram o case, converta **ambos** os lados da comparação: `WHERE UPPER(estado) = 'SP'`.
    * **`CONCAT()` (A Cola):** Junta duas ou mais strings de texto.
        ```sql
        -- Junta o nome e o sobrenome para criar um nome completo
        SELECT CONCAT(primeiro_nome, ' ', ultimo_nome) AS nome_completo FROM clientes;
        ```

---

### <img src="https://api.iconify.design/mdi/scissors-cutting.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Corte de Precisão (Função `SUBSTRING`)

* **A Dor que Resolve:** "A coluna `codigo_pedido` tem o formato `ANO-ID-PAIS` (ex: `2025-12345-BR`). Eu preciso extrair apenas o `ID` do meio."
* **A Ferramenta (`SUBSTRING`):**
    * **Analogia:** O **"bisturi de precisão"** do restaurador.
    * **Como Funciona:** `SUBSTRING(texto, posicao_inicial, quantidade_de_caracteres)`
    * **Exemplo:**
        ```sql
        -- Extrai 5 caracteres, começando da 6ª posição
        SELECT SUBSTRING('2025-12345-BR', 6, 5); -- Retorna '12345'
        ```

---

### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Contexto AWS

Estas funções são padrão SQL e funcionam em todos os serviços de banco de dados relacional da AWS: **Amazon RDS**, **Amazon Aurora** e **Amazon Redshift**.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK DE ARQUITETURA (Limpeza em Escala):**
>
> Embora você *possa* fazer a limpeza de dados diretamente no banco de dados com estas funções, para grandes volumes de dados, a melhor prática é fazer esta "transformação" **antes** de carregar os dados.
>
> É aqui que o **AWS Glue** brilha. Você usaria o Glue para **extrair** os dados "sujos" do S3, **transformá-los** em alta velocidade usando o poder do Spark (que tem funções equivalentes a `trim`, `upper`, etc.), e **carregar** o resultado já limpo e padronizado no seu Data Warehouse (**Amazon Redshift**) ou banco de dados (**Amazon RDS**).
>
> **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" /> Dica de Certificação:** Para a prova, o importante é saber que o SQL possui **funções para manipular e limpar dados de texto**. E que, para operações de limpeza em larga escala (ETL), o serviço ideal da AWS é o **AWS Glue**.


