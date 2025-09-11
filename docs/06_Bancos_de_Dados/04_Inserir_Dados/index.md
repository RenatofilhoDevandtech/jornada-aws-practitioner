# <img src="https://api.iconify.design/mdi/database-import-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Povoando a Biblioteca: Guia de Inserção e Importação de Dados

Já projetamos nossas tabelas ("as prateleiras da biblioteca") com as colunas e os tipos de dados corretos. Agora, como colocamos os "livros" (os dados) nelas?

Existem duas formas principais: a inserção manual, um por um, e a importação em massa a partir de um arquivo. Mas antes de importar, precisamos falar sobre o segredo sujo do mundo dos dados: eles quase nunca chegam limpos.

---

### <img src="https://api.iconify.design/mdi/database-plus-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Inserção Manual: `INSERT INTO`

* **O que é?** O comando SQL para adicionar **uma única linha (registro)** a uma tabela.
* **Analogia:** O bibliotecário **"catalogando um único livro novo e colocando-o na prateleira no lugar exato"**.
* **A Dor que Resolve:** A necessidade de adicionar novos registros individuais à medida que eles acontecem no dia a dia: um novo cliente se cadastra, uma nova venda é realizada, um novo post é criado.
* **A Sintaxe:**
    ```sql
    INSERT INTO Clientes (Nome, Email, Cidade, ClienteAtivo)
    VALUES ('Maria Silva', 'maria.s@email.com', 'São Paulo', TRUE);
    ```

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO (O Valor `NULL`):** E se não soubermos a cidade da Maria? Se a coluna `Cidade` não for obrigatória, podemos inserir um valor `NULL`.
> * **O que é `NULL`?** Não é zero nem um texto vazio. `NULL` significa **"a ausência de um valor"** ou "informação desconhecida". É um "campo em branco" na ficha de cadastro.

---

### <img src="https://api.iconify.design/mdi/file-delimited-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Inserção em Massa: O Desafio do Arquivo CSV

No mundo real, você raramente insere milhares de registros manualmente. Em vez disso, você recebe os dados em um arquivo, como um **CSV (Comma-Separated Values - Valores Separados por Vírgula)**.

* **Analogia:** Um arquivo CSV é como uma **"caixa de doações de livros"** que chega à sua biblioteca.

#### <img src="https://api.iconify.design/mdi/broom.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> A Etapa Crucial: Limpeza e Preparação dos Dados
**A Dor:** Você não pode simplesmente pegar a caixa de doações e jogar os livros nas prateleiras. O mundo real é bagunçado, e os dados também. Antes de importar, o "bibliotecário" (você) precisa fazer uma **triagem**.

**Checklist de Problemas Comuns em Dados "Sujos":**
* **<img src="https://api.iconify.design/mdi/file-question-outline.svg?color=currentColor" width="16" /> Dados Faltando:** Valores `NULL` em colunas obrigatórias.
* **<img src="https://api.iconify.design/mdi/file-cancel-outline.svg?color=currentColor" width="16" /> Tipos de Dados Incorretos:** Um texto como `"N/A"` em uma coluna de números (`INT`).
* **<img src="https://api.iconify.design/mdi/format-letter-case.svg?color=currentColor" width="16" /> Formato Inconsistente:** Datas como `01/10/2025` e `Oct-01-2025` na mesma coluna. Nomes de cidade como "São Paulo" e "sao paulo".
* **<img src="https://api.iconify.design/mdi/content-copy.svg?color=currentColor" width="16" /> Dados Duplicados:** O mesmo cliente ou venda listado múltiplas vezes.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> A REGRA 80/20 DOS DADOS:** 80% do trabalho de um analista de dados é gasto **limpando e preparando** os dados. Apenas 20% é gasto na análise em si. A qualidade da sua análise depende 100% da qualidade da sua limpeza.

#### <img src="https://api.iconify.design/mdi/database-import-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Importando o CSV Limpo
Depois que os dados no arquivo CSV estão limpos e padronizados, a maioria das ferramentas de banco de dados (como o DBeaver ou o próprio query editor do **Amazon RDS**) oferece uma opção de "Importar de CSV" com uma interface gráfica. O comando SQL por trás disso geralmente é `LOAD DATA INFILE` (MySQL) ou `\copy` (PostgreSQL).

---

### <img src="https://api.iconify.design/logos/aws-glue.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Contexto AWS: Ingestão de Dados em Escala

**A Dor:** Limpar e importar um arquivo CSV de 10GB ou 1TB manualmente é inviável. Como automatizar e escalar esse processo?

**A Solução da AWS:** **AWS Glue**.
* **Analogia:** O AWS Glue é o seu **"robô de triagem e catalogação industrial"**.
* **O que é?** Um serviço de **ETL (Extract, Transform, Load - Extrair, Transformar, Carregar)** totalmente gerenciado.
* **Como Funciona:**
    1.  **Extract (Extrair):** O Glue se conecta à sua fonte de dados "sujos" (ex: um bucket S3 onde os CSVs chegam).
    2.  **Transform (Transformar):** Ele executa um script (que ele pode até gerar para você) para **limpar, validar, normalizar e transformar** os dados automaticamente, com base nas suas regras.
    3.  **Load (Carregar):** Ele carrega os dados já limpos e estruturados no seu destino final, como um banco de dados **Amazon RDS** ou um data warehouse **Amazon Redshift**.

> **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação:** Para a prova:
> 1.  Conheça a sintaxe e a finalidade do comando `INSERT INTO`.
> 2.  Entenda o conceito de **limpeza de dados** como uma etapa crucial antes da importação.
> 3.  Saiba que o **AWS Glue** é o serviço de **ETL** principal da AWS, usado para preparar e mover dados em larga escala.

--- 

### <img src="https://api-iconify.design/mdi/table-plus.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Preenchendo as Prateleiras: Guia Prático do Comando `INSERT`

Já projetamos a estrutura da nossa biblioteca com tabelas e colunas perfeitas. Mas prateleiras vazias não contam histórias. A instrução `INSERT INTO` é o comando SQL que nos permite popular nosso banco de dados, adicionando novas linhas de informação às nossas tabelas.

Este comando pertence a uma categoria de comandos SQL chamada **DML (Data Manipulation Language - Linguagem de Manipulação de Dados)**, pois ele, de fato, manipula os dados dentro das tabelas.

---

### <img src="https://api.iconify.design/mdi/file-eye-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Primeiro Passo: Inspecionando a Ficha (`DESCRIBE`)

Antes de tentar inserir um novo "livro", um bom bibliotecário primeiro olha a "ficha de cadastro" em branco para entender quais informações são necessárias.

* **A Dor que Resolve:** "Vou inserir um novo cliente, mas não tenho certeza dos nomes exatos das colunas, da ordem delas ou do tipo de dado que cada uma espera."
* **O Comando:** `DESCRIBE nome_da_tabela;` (ou a abreviação `DESC nome_da_tabela;`).
* **Analogia:** É o ato de **"pegar a ficha de cadastro em branco e ler os nomes dos campos"** antes de começar a preencher. Ele te mostra a estrutura exata da sua tabela.

---

### <img src="https://api.iconify.design/mdi/file-document-edit-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. As Duas Formas de Preencher a Ficha

Existem duas sintaxes para o comando `INSERT`. Uma é segura e profissional, a outra é um atalho que pode ser perigoso.

#### <img src="https://api.iconify.design/mdi/check-decagram-outline.svg?color=currentColor" width="20" /> O Jeito Seguro e Recomendado (Sintaxe Explícita)
Neste método, você especifica exatamente em quais colunas (`campos`) você está inserindo os dados.

* **Analogia:** O bibliotecário preenche a ficha de forma **"cuidadosa e organizada"**, dizendo: "No campo `Título`, escrevo 'A Revolução dos Bichos'. No campo `Autor`, escrevo 'George Orwell'."
* **A Sintaxe:**
    ```sql
    INSERT INTO tabela (coluna1, coluna2, coluna3)
    VALUES (valor1, valor2, valor3);
    ```
* **Por que é o Melhor?** Este método é **robusto a mudanças**. Se amanhã um novo DBA adicionar uma nova coluna opcional à sua tabela, seu código **não quebra**, porque você está especificando exatamente quais colunas está preenchendo.

#### <img src="https://api.iconify.design/mdi/run-fast.svg?color=currentColor" width="20" /> O Atalho Arriscado (Sintaxe Implícita)
Neste método, você omite os nomes das colunas. Isso **exige** que você forneça um valor para **TODAS** as colunas, na **ORDEM EXATA** em que elas foram criadas na tabela.

* **Analogia:** O bibliotecário **"preenchendo a ficha de memória, sem olhar os campos"**.
* **A Sintaxe:**
    ```sql
    INSERT INTO tabela
    VALUES (valor1, valor2, valor3);
    ```
* **<img src="https://api.iconify.design/mdi/alert-outline.svg?color=currentColor" width="18" /> O Risco:** Se alguém alterar a estrutura da tabela (adicionar, remover ou reordenar uma coluna), este comando **vai quebrar** ou, pior, **inserir dados nos lugares errados** (ex: colocar o ano de publicação no campo do autor). **Evite este método em código de produção.**

---

### <img src="https://api.iconify.design/mdi/plus-box-multiple-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. Adicionando Múltiplos Livros de uma Vez

**A Dor que Resolve:** Inserir 100 novos registros com 100 comandos `INSERT` separados é ineficiente e lento.

**A Solução:** Você pode inserir múltiplas linhas em um único comando `INSERT`, separando os conjuntos de valores por vírgulas.

```sql
INSERT INTO funcionarios (id, nome, sobrenome)
VALUES 
('EN1-10', 'Xiulan', 'Wang'),
('EN1-12', 'Diego', 'Ramirez'),
('EN1-19', 'Mary', 'Major');
```

--- 
> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** Este método é muito mais performático porque o banco de dados processa a inserção como uma única transação, em vez de múltiplas transações pequenas, reduzindo o overhead.

---

### <img src="https://api.iconify.design/logos/aws-rds.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Contexto AWS

* **Onde Usar?** Você executará comandos `INSERT INTO` no seu dia a dia em qualquer banco de dados relacional da AWS, seja através do **Query Editor** no console do **Amazon RDS**, ou conectado a uma instância **Amazon Aurora** ou a um cluster **Amazon Redshift** a partir de uma ferramenta cliente SQL.
* **Inserção vs. Ingestão:** Lembre-se que `INSERT` é ideal para adicionar algumas linhas de cada vez (operações transacionais). Para carregar milhões de registros de um arquivo CSV de um bucket S3, você usaria comandos de ingestão em massa otimizados, como `COPY` no Redshift ou `LOAD DATA FROM S3` no Aurora, que são ordens de magnitude mais rápidos.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova, você não precisa escrever SQL, mas deve entender a finalidade dos comandos **DML (Data Manipulation Language)**. O `INSERT` é o comando usado para **adicionar novos dados** a uma tabela.

---
### <img src="https://api.iconify.design/mdi/broom.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Restaurador de Dados: Guia de Limpeza e Importação de Dados

Já projetamos e criamos nossas tabelas ("as prateleiras da biblioteca"). Agora, precisamos populá-las. Raramente faremos isso inserindo uma linha de cada vez. No mundo real, recebemos grandes volumes de dados de fontes externas, geralmente em arquivos **CSV**.

**Analogia:** Pense em um arquivo CSV como uma **"caixa de doações de livros"** que chega à sua biblioteca. Ela contém centenas de livros que precisam ser catalogados.

O problema? As doações quase nunca chegam em perfeito estado.

---

### <img src="https://api.iconify.design/mdi/alert-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Diagnóstico (Identificando Dados "Sujos")

O princípio mais importante em análise de dados é **"Garbage In, Garbage Out" (Lixo Entra, Lixo Sai)**. Se você carregar dados de baixa qualidade no seu banco de dados, seus relatórios e análises serão inúteis e enganosos.

Por isso, o primeiro passo de qualquer importação é a **triagem** ou **limpeza de dados**.

#### <img src="https://api.iconify.design/mdi/playlist-check.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Checklist de Problemas Comuns na "Caixa de Doações":
* **<img src="https://api.iconify.design/mdi/file-question-outline.svg?color=currentColor" width="16" /> Dados Ausentes:** Livros sem título ou autor (valores `NULL` em colunas obrigatórias).
* **<img src="https://api.iconify.design/mdi/file-cancel-outline.svg?color=currentColor" width="16" /> Tipos de Dados Incorretos:** No campo "Ano de Publicação", alguém escreveu "século dezenove" em vez de um número.
* **<img src="https://api.iconify.design/mdi/format-letter-case.svg?color=currentColor" width="16" /> Representação Inconsistente:** Alguns autores estão como "Machado de Assis", outros como "Assis, M.".
* **<img src="https://api.iconify.design/mdi/content-copy.svg?color=currentColor" width="16" /> Dados Duplicados:** O mesmo livro aparece duas vezes na caixa.
* **<img src="https://api.iconify.design/mdi/emoticon-poop-outline.svg?color=currentColor" width="16" /> Caracteres Inaceitáveis:** Títulos com rabiscos, manchas ou caracteres estranhos que podem quebrar a importação.

---

### <img src="https://api.iconify.design/mdi/toolbox-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. A Caixa de Ferramentas do Restaurador (Funções SQL para Limpeza)

O SQL oferece um conjunto de funções de texto que são as "ferramentas de restauração" do bibliotecário para limpar os dados.

| Ferramenta (Função) | O que faz? (Analogia) | Exemplo de Uso |
| :--- | :--- | :--- |
| **`TRIM()`** | A **"Tesoura"** que apara espaços em branco desnecessários no início e no fim de um texto. | `SELECT TRIM('   São Paulo  ');` |
| **`UPPER()` / `LOWER()`**| O **"Padronizador"** que converte todo o texto para maiúsculas ou minúsculas, garantindo consistência. | `SELECT UPPER('Brasil');` |
| **`CONCAT()`** | A **"Cola"** que junta duas ou more strings de texto. | `SELECT CONCAT(nome, ' ', sobrenome);`|
| **`REPLACE()`** | O **"Corretor"** que substitui uma parte do texto por outra. | `SELECT REPLACE('BR,SP', ',', '-');` |
| **`LEFT()` / `RIGHT()`**| A **"Faca de Precisão"** que extrai um número de caracteres do início (esquerda) ou do fim (direita) de um texto. | `SELECT LEFT('AWSCloud', 3);` (retorna `AWS`) |

---

### <img src="https://api.iconify.design/mdi/database-import-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. A Importação em Massa (Levando os Livros para a Prateleira)

Depois que o arquivo CSV está limpo, podemos carregá-lo em massa para a nossa tabela.

* **O Comando:** Cada motor de banco de dados tem seu próprio comando otimizado para isso. O exemplo do seu material, `LOAD DATA INFILE`, é específico do MySQL.
* **A Sintaxe (Exemplo MySQL):**
    ```sql
    LOAD DATA INFILE 'c:/tmp/loyalty.csv' 
    INTO TABLE loyalty
    FIELDS TERMINATED BY ',' 
    ENCLOSED BY '"' 
    LINES TERMINATED BY '\n' 
    IGNORE 1 ROWS;
    ```
* **Decodificando a Ordem:**
    * `LOAD DATA INFILE ...`: "Carregue os dados deste arquivo..."
    * `INTO TABLE loyalty`: "...para dentro da tabela `loyalty`."
    * `FIELDS TERMINATED BY ','`: "Entenda que cada coluna é separada por uma vírgula."
    * `IGNORE 1 ROWS`: "Pule a primeira linha, pois ela é o cabeçalho e não dados reais."

---

### <img src="https://api.iconify.design/logos/aws-glue.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Contexto AWS: Limpeza e Ingestão em Escala

**A Dor:** Limpar e importar um arquivo CSV de 100GB usando funções SQL dentro do banco de dados é lento e ineficiente. Como as grandes empresas fazem?

**A Solução da AWS:** **AWS Glue**.
* **Analogia:** O AWS Glue é a sua **"oficina de restauração industrial e automatizada"**.
* **O que é?** Um serviço de **ETL (Extract, Transform, Load - Extrair, Transformar, Carregar)** totalmente gerenciado.
* **Como Funciona:**
    1.  **Extract (Extrair):** O Glue lê os dados "sujos" diretamente do seu Data Lake no **Amazon S3**.
    2.  **Transform (Transformar):** Ele executa um script poderoso (em Python ou Spark) para fazer toda a limpeza, validação e transformação dos dados em alta velocidade e em paralelo.
    3.  **Load (Carregar):** Ele carrega os dados já limpos e perfeitos no seu destino final, seja um banco de dados **Amazon RDS** ou um data warehouse **Amazon Redshift**.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> 1.  Entenda que a **limpeza de dados** é uma etapa crucial do processo de ingestão ("Garbage In, Garbage Out").
> 2.  Saiba que o **AWS Glue** é o principal serviço de **ETL** da AWS, usado para **transformar** e limpar dados em larga escala.
> 3.  Lembre-se que o **Amazon S3** é frequentemente usado como a área de preparação (*staging area*) para receber os dados brutos antes que eles sejam limpos e carregados em um banco de dados.