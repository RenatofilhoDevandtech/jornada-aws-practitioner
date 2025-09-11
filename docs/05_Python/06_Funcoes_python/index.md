# <img src="https://api.iconify.design/mdi/function-variant.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Poder da Reutilização: Um Guia Prático sobre Funções em Python

Imagine que, toda vez que você quisesse um sanduíche, precisasse dar ao seu robô-assistente a mesma sequência de 10 ordens: "1. Pegue duas fatias de pão. 2. Abra o pote de maionese...". Seria tedioso, repetitivo e propenso a erros.

E se, em vez disso, você pudesse ensinar essa sequência de 10 passos ao robô uma única vez e dar a ela um nome, como `fazer_sanduiche`? A partir daí, bastaria uma única ordem para que ele executasse a tarefa completa.

Isso é uma **Função**. É um bloco de código nomeado e reutilizável que executa uma tarefa específica. Elas são a base do princípio de programação mais importante: **DRY (Don't Repeat Yourself - Não se Repita)**.

---

### <img src="https://api.iconify.design/mdi/robot-happy-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> As Duas Missões de uma Função

Uma função pode ter duas missões principais:

1.  **Funções que *Fazem* Algo (Procedimentos)**
    * **Analogia:** O robô **"prepara o sanduíche e o deixa na mesa"**. Ele executou uma ação, mas não te entregou nada diretamente na mão.
    * **O que fazem?** Executam uma série de passos, como imprimir algo na tela, modificar um arquivo ou enviar um e-mail. Elas não usam a palavra-chave `return`.
    * **Exemplo:**
        ```python
        def saudar_usuario():
            print("Olá! Bem-vindo ao sistema.")
        ```

2.  **Funções que *Calculam* Algo (Retornando um Valor)**
    * **Analogia:** O robô **"calcula o preço do sanduíche e te entrega a etiqueta com o valor"**. Ele não apenas fez algo, ele te deu um resultado para você usar.
    * **O que fazem?** Processam informações e usam a palavra-chave `return` para enviar um valor de volta para quem a chamou.
    * **Exemplo:**
        ```python
        def somar(a, b):
            resultado = a + b
            return resultado
        
        preco_total = somar(5, 3) # a variável preco_total agora guarda o valor 8
        ```

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Anatomia de uma Habilidade (Criando suas Funções)

Vamos quebrar a sintaxe para "ensinar" o robô.

* **A Definição (`def`):** Você começa com a palavra `def`, seguida pelo nome que você quer dar à função e parênteses `()`.
    ```python
    def nome_da_funcao():
        # O código indentado aqui dentro pertence a esta função
        print("Esta função foi chamada!")
    ```

* **Os Ingredientes (Parâmetros e Argumentos):** Para tornar a função flexível, você pode definir "espaços reservados" (parâmetros) dentro dos parênteses.
    ```python
    # 'recheio' e 'pao' são os PARÂMETROS
    def fazer_sanduiche(recheio, pao):
        print(f"Fazendo um sanduíche de {recheio} no pão {pao}.")

    # "frango" e "integral" são os ARGUMENTOS que você passa ao chamar a função
    fazer_sanduiche("frango", "integral") 
    ```
    > **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" /> Insight:** **Parâmetro** é a variável na definição da função. **Argumento** é o valor real que você passa quando a chama.

* **O Resultado (`return`):** A palavra-chave `return` envia um valor de volta e **encerra a função imediatamente**.

---

### <img src="https://api.iconify.design/mdi/library-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Biblioteca de Habilidades do Python (Funções Embutidas)

O Python já vem com uma vasta biblioteca de "habilidades" pré-ensinadas que você pode usar a qualquer momento. Algumas das mais famosas são:
* `print()`: Imprime um valor na tela.
* `input()`: Pede uma entrada ao usuário.
* `len()`: Retorna o **len**gimento (comprimento) de uma lista ou string.
* `int()`, `str()`: Converte um valor para inteiro ou string.
* `sum()`: Soma os itens de uma lista de números.

---

### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Contexto AWS: Funções para Automação Inteligente

**A Dor:** "Eu preciso verificar o status de várias instâncias EC2. O código para verificar uma instância é um pouco complexo, e eu não quero copiá-lo e colá-lo para cada instância."

**A Solução Profissional:** Crie uma **função-ferramenta** reutilizável.

```python
import boto3 # Importa o "skill pack" da AWS

# --- Definição da Ferramenta ---
# Esta função tem uma única responsabilidade: verificar o status de uma instância.
def verificar_status_ec2(id_da_instancia):
    """Verifica o status de uma instância EC2 e retorna uma string."""
    try:
        ec2 = boto3.client('ec2')
        resposta = ec2.describe_instances(InstanceIds=[id_da_instancia])
        status = resposta['Reservations'][0]['Instances'][0]['State']['Name']
        return status # Retorna o resultado
    except Exception as e:
        # Se der erro, retorna uma mensagem de erro
        return "Nao_Encontrada"

# --- Execução Principal do Script ---
# Esta é a nossa lista de tarefas do dia.
instancias_para_checar = ["i-0123abcd", "i-8910efgh", "i-instanciaquenaoexiste"]

print("--- Iniciando Relatório de Status de Instâncias Críticas ---")

# Para cada item na nossa lista...
for instancia_id in instancias_para_checar:
    # ...chamamos nossa ferramenta reutilizável.
    status_atual = verificar_status_ec2(instancia_id)
    print(f"A instância {instancia_id} está no estado: {status_atual}")
```
><img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO E CARREIRA: Esta estrutura é o padrão da indústria para um bom script de automação. A lógica complexa fica isolada dentro de funções bem nomeadas. A parte principal do script apenas orquestra a chamada dessas funções. Isso torna o código incrivelmente organizado, fácil de ler, fácil de testar e fácil de dar manutenção.