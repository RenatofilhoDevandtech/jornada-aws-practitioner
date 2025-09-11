## <img src="https://api.iconify.design/mdi/school-outline.svg" width="20"> 2. Principais Pontos da Lição

Neste módulo, você aprenderá os fundamentos essenciais para começar a programar em Python:

### 🧠 Você vai aprender a:
- Instalar o Python em um computador Linux
- Definir a terminologia básica da linguagem
- Declarar variáveis e realizar operações com elas
- Compreender declarações, funções e exceções

> Este é o ponto de partida para dominar Python com confiança e clareza.

---

## <img src="https://api.iconify.design/mdi/laptop.svg" width="20"> 3. Requisitos de Sistema para o Python

Python é compatível com os principais sistemas operacionais:

- 🪟 **Microsoft Windows**
- 🍎 **macOS**
- 🐧 **Linux**

> A instalação pode variar conforme o sistema, mas o funcionamento da linguagem é consistente em todos eles.

---

## <img src="https://api.iconify.design/mdi/terminal.svg" width="20"> 4. Demonstração: Instalando o Python no Linux (CentOS)

Por padrão, o CentOS inclui o Python 2.7. Para este curso, usaremos o Python 3.7. Abaixo estão os passos para instalar:

### 🔧 Etapas de instalação:
1. Verifique a versão atual:
   ```bash
   python --version
   ```
2. Baixe o instalador:Instale os pacotes necessários:

```bash
yum install gcc openssl-devel bzip2-devel libffi-devel
```
3. Baixe o Python 3.7.2:

```bash
cd /usr/src
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
```
4. Extraia o arquivo:

```bash
tar xzf Python-3.7.2.tgz
```
5. Compile e instale:

```bash
cd Python-3.7.2
./configure --enable-optimizations
make altinstall
```
6. Remova o arquivo baixado:

```bash
rm /usr/src/Python-3.7.2.tgz
```

7. Verifique a nova instalação:

```bash
python3.7 -V
```
Após esses passos, você terá o Python 3.7 pronto para uso no seu sistema Linux.

---

## <img src="https://api.iconify.design/mdi/code-tags-check.svg" width="20"> 5. Noções Básicas de Sintaxe do Python

O Python utiliza **recuo e espaçamento** para organizar blocos de código — diferente de linguagens como C ou Java que usam `{}`.

### ⚠️ Atenção:
- Erros comuns vêm de **espaçamento incorreto**
- O recuo deve ser **consistente** (geralmente 4 espaços)
- Pontuação como `:` é essencial após estruturas como `if`, `for`, `def`
- Python diferencia **maiúsculas de minúsculas** (`Variavel` ≠ `variavel`)

> A clareza da sintaxe é uma das razões pelas quais Python é tão acessível e popular.

---

## <img src="https://api.iconify.design/mdi/identifier.svg" width="20"> 6. Identificadores em Python

Um **identificador** é o nome dado a variáveis, funções, classes e outros elementos no código.

### 📌 Regras para nomear identificadores:
- Não podem começar com números (`1variavel` é inválido)
- Não podem usar **palavras reservadas** (`def`, `class`, `if`, etc.)
- Não podem conter **símbolos especiais** como `!`, `@`, `#`, `$`, `%`
- Podem ter qualquer tamanho e usar letras, números e sublinhados (`_`)

> Bons identificadores tornam o código mais legível, organizado e fácil de manter.

---

## <img src="https://api.iconify.design/mdi/file-code-outline.svg" width="20"> 7. Extensões de Arquivos: `.py`

Arquivos Python usam a extensão **`.py`**, que indica que o conteúdo é um script da linguagem.

### 📝 Características:
- Podem ser criados em qualquer editor de texto
- Precisam do **intérprete Python** para serem executados
- São usados para armazenar **funções, classes, variáveis e lógica de programas**

> Um arquivo `.py` é como uma receita: contém os passos que o computador deve seguir para executar uma tarefa.

---

## <img src="https://api.iconify.design/mdi/function-variant.svg" width="20"> 8. Funções em Python

Funções são blocos de código que realizam **tarefas específicas** e podem ser reutilizados ao longo do programa.

### 🧠 Conceitos-chave:
- Toda função tem um **nome** e é chamada com parênteses: `print()`
- Pode receber **argumentos**: dados que a função usa para operar
- Pode ser **nativa** (como `print`) ou **definida pelo usuário**

### 📌 Exemplo:
```python
def saudacao(nome):
    print("Olá,", nome)

saudacao("Renato")
```
## <img src="https://api.iconify.design/mdi/function-variant.svg" width="20"> 8. Funções em Python

Funções são blocos de código que dizem ao computador para realizar uma **tarefa específica**. Elas ajudam a organizar o programa e evitar repetição.

### 🧠 Conceitos-chave:
- Toda função tem um **nome** e é chamada com parênteses: `print()`
- Pode receber **argumentos**: dados que a função usa para operar
- Pode ser **nativa** (como `print`) ou **definida pelo usuário**

### 📌 Exemplos:
```python
print()        # Exibe uma linha em branco
print(10)      # Exibe o número 10
print("Olá")  # Exibe a string "Olá"
```

# Introdução ao Python e ao Editor Vim

Este guia é voltado para quem está começando a programar com Python e usar o editor Vim no Linux. Vamos abordar variáveis, operadores, funções, exceções, strings, e muito mais — com exemplos práticos e explicações claras.

---

## Variáveis em Python

### O que são?

Variáveis são nomes que armazenam valores. Elas permitem que você guarde dados para usar mais tarde no programa.

### Regras para nomear variáveis:

- ✅ Podem conter letras, números e sublinhados (`_`)
- ❌ Não podem começar com números
- ❌ Não podem ser palavras reservadas do Python (como `for`, `if`, `print`, etc.)

### Exemplos:

```python
maçãs = 2             # Armazena o número 2 na variável 'maçãs'
laranjas = 3          # Armazena o número 3
maçãs = laranjas      # Agora 'maçãs' vale 3
cor_carro = "vermelho"  # Armazena uma string
```
# <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O DNA do Código: Guia Profissional de Variáveis e Operadores em Python

Para construir automações poderosas, primeiro precisamos dominar a "gramática" da linguagem. Este guia é um mergulho profundo nos blocos de construção fundamentais do Python: como ele armazena informações (variáveis e tipos) e como ele opera sobre essas informações (operadores).

Dominar estes conceitos é o que permite que você escreva scripts que não apenas executam tarefas, mas que pensam, comparam e decidem.

---

### <img src="https://api.iconify.design/mdi/variable-box.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. As Unidades de Memória (Variáveis e Tipos de Dados)

* **Analogia:** Uma variável é uma **"caixa com uma etiqueta"**. Você usa a etiqueta (`nome_da_variavel`) para guardar e recuperar um "objeto" (o valor).

#### <img src="https://api.iconify.design/mdi/label-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> As Regras de Etiquetagem (Nomenclatura de Variáveis)
Seu "robô-assistente" é muito rigoroso com as etiquetas:
* Só pode conter letras, números e `_` (underscore).
* **Não** pode começar com um número. (`1_nome` é inválido, mas `nome_1` é válido).
* **Não** pode ser uma palavra-chave reservada do Python (como `if`, `for`, `while`).

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK (A Convenção Pythônica):** A comunidade Python prefere o estilo `snake_case` para variáveis (letras minúsculas separadas por underscore).
> * **Prefira:** `cor_do_carro = "azul"`
> * **Evite:** `corCarro = "azul"` ou `CorDoCarro = "azul"`

#### <img src="https://api.iconify.design/mdi/toy-brick-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Os 4 Tipos de "Objetos" Fundamentais
* **`int` (Inteiro):** Números inteiros (`10`, `-50`, `2025`).
* **`float` (Ponto Flutuante):** Números com casas decimais (`3.14`, `9.99`).
* **`str` (String):** Texto, sempre entre aspas (`"Olá, mundo!"`, `'Amazon Web Services'`).
* **`bool` (Booleano):** Representa verdade ou falsidade. Só pode ter dois valores: `True` ou `False`. É a base de toda a lógica.

---

### <img src="https://api.iconify.design/mdi/gamepad-variant-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Painel de Controle do Robô (O Mundo dos Operadores)

Operadores são os "botões" que dizem ao robô o que fazer com os valores nas caixas.

| Categoria | O que faz? (Analogia) | Exemplos |
| :--- | :--- | :--- |
| **Aritméticos** | A **"calculadora"** do robô. | `+`, `-`, `*`, `/` (divisão), `**` (potência), `%` (resto da divisão), `//` (divisão inteira) |
| **Atribuição** | **"Guardar ou atualizar"** o valor em uma caixa. | `=`, `+=`, `-=` |
| **Comparação** | Os **"sensores"** que comparam duas caixas e respondem `True` ou `False`. | `==` (igual a), `!=` (diferente de), `>` (maior que), `<` (menor que) |
| **Lógicos** | O **"circuito lógico"** para combinar respostas `True`/`False`. | `and`, `or`, `not` |
| **Associação** | A função de **"verificar se um item está numa lista"**. | `in`, `not in` |
| **Identidade** | O **"scanner de DNA"** que verifica se duas etiquetas apontam para o mesmo objeto. | `is`, `is not` |

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO (A Confusão Clássica):**
> * **`=`** é para **atribuir** um valor. (`idade = 25`) -> "Guarde o valor 25 na caixa 'idade'".
> * **`==`** é para **comparar** um valor. (`idade == 25`) -> "O valor na caixa 'idade' é igual a 25?". A resposta será `True` ou `False`.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. A Ordem das Coisas: BODMAS e Exceções

* **BODMAS (Ordem das Operações):**
    * **O que é?** A sequência de prioridades que o Python usa para resolver expressões matemáticas: **B**rackets (Parênteses), **O**rders (Potências), **D**ivision/**M**ultiplication, **A**ddition/**S**ubtraction.
    * **A Dor que Resolve:** Garante que `2 + 3 * 4` seja sempre `14` (3*4 primeiro) e não `20`.

* **Exceções (Quando o Robô Trava):**
    * **O que é?** Um erro que interrompe o programa.
    * **Analogia:** É o robô parando e te entregando um relatório de erro (*stack trace*) porque não conseguiu cumprir uma ordem.
    * **Exemplos:** Tentar usar uma variável que não existe (`NameError`), dividir por zero (`ZeroDivisionError`), tentar somar um número com um texto (`TypeError`).

---

### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Propósito Final: O Contexto da Nuvem

Como usamos essa "gramática" para resolver um problema real na AWS?

**Missão:** Escrever um script que verifica a política de um bucket S3 para ver se ele está público.

**O "Pensamento" do Script:**

```python
# A política do bucket (um dicionário Python retornado pelo Boto3)
politica_bucket = {
    "Version": "2012-10-17",
    "Statement": [{
        "Sid": "PublicReadGetObject",
        "Effect": "Allow",
        "Principal": "*",
        "Action": "s3:GetObject",
        "Resource": "arn:aws:s3:::meu-bucket-exposto/*"
    }]
}

# Variável para controlar o estado
esta_publico = False

# Operador de associação "in" para checar se a chave existe
if "Statement" in politica_bucket:
    
    # Acessa a lista e pega o primeiro item (índice 0)
    primeira_regra = politica_bucket["Statement"][0]

    # Operadores lógicos "and" e de comparação "=="
    if (primeira_regra["Effect"] == "Allow") and (primeira_regra["Principal"] == "*"):
        esta_publico = True

# Verificação final
if esta_publico:
    print("ALERTA DE SEGURANÇA: Bucket está público!")
else:
    print("Bucket está configurado de forma privada. Tudo certo.")

```
> <img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK DE AUTOMAÇÃO: Este exemplo simples é a base da automação de segurança na nuvem. Um script como este pode rodar em uma AWS Lambda a cada hora, verificando todos os seus buckets e te alertando sobre configurações perigosas, fazendo o trabalho de um analista de segurança de forma automática e incansável.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Python em Ação: Automação Prática na AWS

No último guia, equipamos nosso "robô-assistente" com a gramática básica (variáveis e operadores). Agora, vamos colocá-lo para trabalhar na "fábrica" da AWS, dando a ele suas primeiras missões reais.

Para isso, ele precisa aprender a lidar com múltiplas informações ao mesmo tempo e a tomar decisões. Vamos ensinar nosso robô a usar **Listas**, **Dicionários** e a pensar com **Lógica Condicional**.

---

### <img src="https://api.iconify.design/mdi/clipboard-list-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Missão 1: O Inventário (Trabalhando com Listas)

**O Cenário:** Você precisa verificar o status de um grupo específico de instâncias EC2 críticas.

**O Conceito (Listas):** Quando você lida com mais de um item, você os organiza em uma **lista**.
* **Analogia:** Uma **"Lista de Tarefas"** ou um **"Inventário"**. É uma coleção ordenada de itens.
* **Por que é importante na AWS?** Quando você pede à AWS: "me dê todas as suas instâncias EC2", ela não te devolve uma única coisa. Ela te devolve uma **lista** de instâncias.

**Na Prática:**

```python
# Uma lista simples com os IDs das instâncias que precisamos verificar
instancias_criticas = ["i-0123abcd4567", "i-8910efgh1234", "i-5678ijkl9101"]

# Como acessar um item? Pelo seu índice (posição na lista), que começa em 0.
primeira_instancia = instancias_criticas[0]

print(f"Iniciando verificação da primeira instância: {primeira_instancia}")
# Resultado: Iniciando verificação da primeira instância: i-0123abcd4567
```

---
### <img src="https://api.iconify.design/mdi/card-text-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Missão 2: A Ficha Técnica (Trabalhando com Dicionários)

**O Cenário:** Uma lista de IDs é útil, mas precisamos dos **detalhes** de cada instância: qual o seu tipo? Qual o seu IP? Em que estado ela está?

**O Conceito (Dicionários):** Para armazenar dados estruturados, usamos **dicionários**.

* **Analogia:** Uma **"Ficha Técnica"** ou um **"Cartão de Visita"**. É uma coleção de pares `chave: valor`.
* **Por que é importante na AWS?** Cada recurso na AWS (uma instância EC2, um bucket S3, um usuário IAM) é representado como um **dicionário** cheio de informações.

**Na Prática:**

```python
# Exemplo simplificado da "ficha técnica" de uma única instância EC2
instancia_info = {
  "InstanceId": "i-0123abcd4567",
  "InstanceType": "t2.micro",
  "State": "running",
  "PrivateIpAddress": "172.31.10.5",
  "Tags": ["WebServer", "Producao"]
}

# Como acessar um detalhe? Pela sua chave!
tipo = instancia_info["InstanceType"]
status = instancia_info["State"]

print(f"A instância {instancia_info['InstanceId']} é do tipo {tipo} e está no estado '{status}'.")
# Resultado: A instância i-0123abcd4567 é do tipo t2.micro e está no estado 'running'.
```
### <img src="https://api.iconify.design/mdi/call-split.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Missão 3: A Tomada de Decisão (Lógica com `if`)

**O Cenário:** Agora que temos os detalhes, nosso script precisa **agir** com base neles. Se uma instância crítica estiver parada, precisamos soar um alarme!

**O Conceito (`if/else`):** É a estrutura que permite ao nosso "robô" tomar decisões.

* **Analogia:** O **"Fluxograma de Decisão"**: **SE** uma condição for verdadeira, **ENTÃO** faça a Ação A, **SENÃO**, faça a Ação B.

**Na Prática:**

```python
# A resposta da AWS é sempre uma LISTA de DICIONÁRIOS
lista_de_instancias_da_aws = [
  { "InstanceId": "i-aaaabbbb", "State": "running", "Env": "Prod" },
  { "InstanceId": "i-ccccdddd", "State": "stopped", "Env": "Dev" },
  { "InstanceId": "i-eeeeffff", "State": "running", "Env": "Prod" }
]

print("--- Iniciando Relatório de Status da Frota EC2 ---")

# Para cada "ficha técnica" (dicionário) na nossa lista de inventário...
for instancia in lista_de_instancias_da_aws:
    
    # ...pegue o ID e o Status...
    instance_id = instancia["InstanceId"]
    status = instancia["State"]
    
    # ...e tome uma decisão!
    if status == "running":
        print(f"[OK] Instância {instance_id} está online.")
    else:
        print(f"[ALERTA] Instância {instance_id} está offline (status: {status}). Ação necessária!")

print("--- Fim do Relatório ---")
```
> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO E CARREIRA:** Este último exemplo é a **essência da automação na nuvem**. Praticamente todo script que você escrever para a AWS seguirá este padrão:
> 1.  Pedir uma lista de recursos à AWS.
> 2.  Receber uma **lista de dicionários**.
> 3.  Usar um loop **`for`** para inspecionar cada dicionário da lista.
> 4.  Usar condicionais **`if`** para tomar decisões com base nos valores encontrados nas chaves.
> 
> Dominar este fluxo é dominar a automação com Python na AWS.