# <img src="https://api.iconify.design/mdi/robot-industrial-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> Construindo Ferramentas: Guia Prático de um Script de Automação

Chegou a hora de juntar tudo. Já aprendemos os comandos do Linux (`usermod`, `groups`) e os fundamentos do Python (funções, loops, `subprocess`). Agora, vamos combinar esses dois mundos para construir uma ferramenta que automatiza uma tarefa comum e crítica: adicionar um usuário a múltiplos grupos.

**A Dor que Vamos Resolver:** Adicionar um novo desenvolvedor a 5 grupos diferentes (`developers`, `docker`, `aws-cli-users`, `vpn-access`, `testing`) usando o comando `usermod` manualmente é lento, repetitivo e muito propenso a erros de digitação.

**Nossa Solução:** Um script Python interativo que guia o administrador, valida as informações e executa o comando complexo de forma segura.

**Analogia:** Vamos construir um **"Assistente de RH Automatizado"** que cuida do processo de dar os crachás de acesso corretos (grupos) para um novo funcionário (usuário).

---

### <img src="https://api.iconify.design/mdi/code-braces.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Ferramenta Completa (O Código-Fonte Comentado)

Antes de "destrinchar", veja a receita completa. Este é o nosso script final, ligeiramente aprimorado para maior clareza.

```python
import os
import subprocess

def adicionar_usuario_ao_grupo():
    """
    Script interativo para adicionar um usuário existente a um ou mais grupos no Linux.
    """
    # --- Bloco 1: Coleta de Dados ---
    username = input("Insira o nome do usuário a ser modificado: ")
    
    print("\n--- Grupos Disponíveis no Sistema ---")
    # Usamos subprocess.run para uma forma mais moderna e segura de capturar a saída
    resultado_groups = subprocess.run(['groups'], capture_output=True, text=True)
    grupos_existentes = resultado_groups.stdout.strip().split()
    print(' '.join(grupos_existentes))
    
    print("\nInsira os grupos para adicionar o usuário (separados por espaço):")
    grupos_escolhidos_str = input("Grupos: ")

    # --- Bloco 2: Processamento dos Dados ---
    grupos_para_adicionar = grupos_escolhidos_str.strip().split()
    string_de_grupos = ""

    # --- Bloco 3: Lógica de Verificação ---
    print("\n--- Análise dos Grupos ---")
    for grupo in grupos_para_adicionar:
        if grupo in grupos_existentes:
            print(f"- Grupo Existente: {grupo}")
        else:
            print(f"- Aviso: O grupo '{grupo}' não existe e será criado.")
        
        # Constrói a string de grupos para o comando final
        string_de_grupos += grupo + ","

    # --- Bloco 4: Confirmação e Execução ---
    if not string_de_grupos:
        print("\nNenhum grupo foi selecionado. Operação cancelada.")
        return # Sai da função

    # Remove a última vírgula da string
    string_de_grupos = string_de_grupos[:-1]

    confirmacao = ""
    while confirmacao not in ["S", "N"]:
        confirmacao = input(f"\nAdicionar o usuário '{username}' aos grupos '{string_de_grupos}'? (S/N): ").upper()

    if confirmacao == "S":
        comando_final = f"sudo usermod -aG {string_de_grupos} {username}"
        print(f"\nExecutando o comando: {comando_final}")
        os.system(comando_final)
        print(f"\nUsuário '{username}' atualizado com sucesso!")
    else:
        print("\nOperação cancelada pelo usuário.")

# --- Ponto de Entrada do Script ---
if __name__ == "__main__":
    adicionar_usuario_ao_grupo()

```
### <img src="https://api.iconify.design/mdi/magnify-scan.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> A Anatomia da Ferramenta (O Código Explicado)

#### <img src="https://api.iconify.design/mdi/clipboard-text-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Bloco 1: A Coleta de Dados
* **O que faz?** Interage com o administrador. Pede o nome do usuário e a lista de grupos desejados.
* **A Mágica:** `subprocess.run(['groups'], ...)` executa o comando `groups` do Linux e captura a saída para que nosso script saiba quais "departamentos" já existem na empresa.

#### <img src="https://api.iconify.design/mdi/puzzle-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Bloco 2 & 3: Processamento e Verificação
* **O que fazem?** Usam o método `.split()` para transformar as strings de texto (ex: "grupo1 grupo2") em listas Python (`['grupo1', 'grupo2']`).
* **A Lógica:** O loop `for` percorre cada grupo que o administrador pediu. O `if grupo in grupos_existentes:` verifica se o "departamento" solicitado já existe ou se precisa ser criado.

#### <img src="https://api.iconify.design/mdi/check-decagram-outline.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Bloco 4: Confirmação e Execução
* **O que faz?** Monta o comando final `usermod -aG ...` e, crucialmente, pede uma **confirmação** final ao administrador antes de executar uma ação com `sudo`.
* **A Execução:** `os.system(comando_final)` é o momento em que o nosso robô Python pega o "walkie-talkie" e dá a ordem final para o Shell Linux.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO (E VIDA REAL):** Este script é um exemplo perfeito da sinergia entre Python e Linux:
> 1.  O **Python** é usado para a lógica, interação com o usuário e processamento de dados (a parte "inteligente").
> 2.  O **Shell Linux** é invocado para executar as tarefas de sistema operacional (`groups`, `usermod`).
>
> Entender como usar uma linguagem de script para orquestrar comandos do sistema é um conceito fundamental para as certificações Linux Essentials e para a prática de DevOps/Cloud.

Este script transforma um processo manual, propenso a erros e que exige conhecimento de sintaxe complexa em um fluxo de trabalho guiado, seguro e eficiente — a essência da automação.

--- 

# <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Canivete Suíço do Admin: Criando Ferramentas de Automação com Python

Chegamos ao ápice da nossa jornada em Python: a construção de ferramentas. Um script de automação é a sua solução para transformar tarefas manuais, repetitivas e propensas a erro em um processo rápido, confiável e consistente.

**A Missão:** Vamos construir um "Canivete Suíço" para um administrador de sistemas: um script em Python que funciona como um painel de controle simplificado para gerenciar pacotes `apt` em um sistema Debian/Ubuntu.

---

### <img src="https://api.iconify.design/mdi/code-braces-box.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Ferramenta Completa (O Código-Fonte Comentado)

Antes de analisarmos, veja a ferramenta completa. Note que refatoramos o código para usar `subprocess.run`, a prática moderna e segura.

```python
import subprocess
import sys

# --- Funções do nosso "Canivete Suíço" ---

def atualizar_ambiente():
    """Executa os comandos para atualizar o sistema (apt update, upgrade)."""
    print("\n--- Atualizando a lista de pacotes (apt update)... ---")
    subprocess.run(["sudo", "apt", "update"], check=True)
    
    print("\n--- Atualizando os pacotes instalados (apt upgrade)... ---")
    subprocess.run(["sudo", "apt", "upgrade", "-y"], check=True)
    
    print("\n--- Atualização do ambiente concluída! ---")

def limpar_ambiente():
    """Executa os comandos para limpar pacotes desnecessários."""
    print("\n--- Removendo dependências órfãs (autoremove)... ---")
    subprocess.run(["sudo", "apt", "autoremove", "-y"], check=True)
    
    print("\n--- Limpando o cache de pacotes antigos (autoclean)... ---")
    subprocess.run(["sudo", "apt", "autoclean"], check=True)
    
    print("\n--- Limpeza do ambiente concluída! ---")

def gerenciar_pacotes():
    """Função principal que lida com a instalação ou remoção de pacotes."""
    acao = input("Você deseja [instalar] ou [remover] pacotes?: ").lower()
    
    if acao not in ["instalar", "remover"]:
        print("Opção inválida. Saindo.")
        return

    pacotes = input(f"Insira o(s) nome(s) do(s) pacote(s) para {acao} (separados por espaço): ")

    if acao == "remover":
        while True:
            escolha = input("Deseja limpar os arquivos de configuração (--purge)? (S/N): ").upper()
            if escolha in ["S", "N"]:
                break
        
        if escolha == "S":
            # Constrói o comando com a opção --purge
            comando = ["sudo", "apt", "remove", "--purge", "-y"] + pacotes.split()
        else:
            comando = ["sudo", "apt", "remove", "-y"] + pacotes.split()
    else: # Ação é "instalar"
        comando = ["sudo", "apt", "install", "-y"] + pacotes.split()
        
    print(f"\nExecutando: {' '.join(comando)}")
    subprocess.run(comando, check=True)
    print(f"\nOperação '{acao}' concluída com sucesso!")


# --- Menu Principal ---
if __name__ == "__main__":
    print("Bem-vindo ao Canivete Suíço de Gerenciamento de Pacotes!")
    # ... (Aqui poderia ter um menu mais elaborado) ...
    gerenciar_pacotes()

```

---
### <img src="https://api.iconify.design/mdi/security.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Upgrade de Segurança: `os.system` vs. `subprocess.run`

O material original usava `os.system()`. Por que nós o substituímos por `subprocess.run()`?

* **A Dor que `subprocess.run` Resolve:** Uma vulnerabilidade de segurança grave chamada **Injeção de Comando (Command Injection)**.

* **Analogia:**
    * `os.system()` é um **"Campo de Texto Aberto"** no seu painel. Você passa uma única string de texto, e o shell a executa.
    * `subprocess.run()` é um **"Formulário Estruturado"**. Você passa uma lista, onde o primeiro item é o comando e os seguintes são os argumentos.

* **O Ataque:**
    Imagine que um usuário mal-intencionado consegue inserir o seguinte nome de pacote no nosso script antigo: `meu-pacote; sudo rm -rf /`
    * Com `os.system("sudo apt install " + pacotes)`: O shell veria isso como **dois comandos separados**: primeiro, `sudo apt install meu-pacote`, e depois, o catastrófico `sudo rm -rf /`.
    * Com `subprocess.run(["sudo", "apt", "install", pacotes])`: O programa tentaria procurar por um pacote com o nome literal e bizarro `meu-pacote; sudo rm -rf /`. Ele não o encontraria e daria um erro seguro, **sem executar o comando malicioso**.

| Característica | `os.system` (O Jeito Antigo e Inseguro) | `subprocess.run` (O Jeito Moderno e Seguro) |
| :--- | :--- | :--- |
| **Argumentos** | Uma única string de texto. | Uma **lista** de strings. |
| **Segurança**| Vulnerável a *Command Injection*. | **Seguro.** Trata os argumentos como dados, não como comandos. |
| **Flexibilidade**| Limitado. Não captura a saída facilmente. | Muito flexível. Permite capturar saída, erros e o código de retorno. |

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK DE ESPECIALISTA:** Em qualquer código Python moderno, **sempre prefira `subprocess.run`** em vez de `os.system`. É mais seguro, mais poderoso e a prática recomendada pela comunidade.

---

### <img src="https://api.iconify.design/logos/aws-systems-manager.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Contexto AWS: De um Script a uma Ferramenta de Frota

Como um script como este é usado em um ambiente de nuvem real?

* **A Dor:** "Eu preciso garantir que o pacote `nginx` seja instalado e o pacote `telnet` seja removido em todas as minhas 100 instâncias EC2." Fazer isso manualmente via SSH seria um pesadelo.
* **A Solução:** Você usa um serviço como o **AWS Systems Manager Run Command**. Ele permite que você execute um script (como o nosso "Canivete Suíço") em toda a sua frota de instâncias de uma só vez. Você pode passar parâmetros (ex: `ação=instalar`, `pacotes=nginx`) para o script em cada máquina.

Isso transforma sua ferramenta de um "canivete" para um único servidor em uma "fábrica de configuração" para toda a sua infraestrutura, garantindo consistência e automação em escala.

> **<img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> Dica de Certificação:** Entender o conceito de usar scripts (Python, Shell) para automatizar tarefas de administração de sistemas é chave. Para a prova, saiba que o **AWS Systems Manager** é o serviço principal para orquestrar e executar essas automações em sua frota de instâncias EC2.