# <img src="https://api.iconify.design/mdi/bug-check-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Médico do Código: Guia Prático de Depuração e Testes em Python

Um fato universal da programação: **todo código tem bugs**. A habilidade de um desenvolvedor sênior não está em escrever código perfeito na primeira tentativa, mas sim em ser um mestre na arte de **diagnosticar (depurar) e curar (corrigir)** os problemas de forma rápida e eficiente.

Pense no seu código como um **paciente**. A depuração é o processo de diagnóstico para descobrir a causa da "doença" (o bug). Existem duas grandes abordagens para este diagnóstico.

---

### <img src="https://api.iconify.design/mdi/file-eye-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Exame Visual (Análise Estática)

* **O que é?** A análise do seu código-fonte **sem executá-lo**.
* **Analogia:** O médico fazendo um **"exame visual"** e lendo o **"prontuário do paciente"**. Ele consegue encontrar problemas óbvios apenas olhando e lendo, sem que o paciente precise fazer qualquer esforço.
* **A Dor que Resolve:** Encontrar erros de "gramática" (sintaxe), erros de digitação e desvios de boas práticas antes mesmo de rodar o programa.

#### <img src="https://api.iconify.design/mdi/tools.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Suas Ferramentas de Análise Estática:
* **O Intérprete Python:** Se você digitar `printt("Olá")` (com dois 't'), o Python nem vai começar a executar; ele já te dará um `SyntaxError`.
* **IDEs (como o VS Code):** Seu editor de código moderno age como um assistente, sublinhando erros de sintaxe em tempo real enquanto você digita.
* **Linters (ex: `Pylint`, `Flake8`):**
    * **Analogia:** O **"assistente robótico do médico"** que escaneia sua "receita" (código) e aponta não apenas erros, mas também "caligrafia ruim" (problemas de estilo) e "dosagens perigosas" (padrões de código que podem levar a bugs).

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** Configurar um **Linter** no seu editor de código é uma das práticas mais importantes para um desenvolvedor. Ele te força a escrever um código mais limpo, padronizado (seguindo o guia de estilo oficial, o **PEP 8**) e menos propenso a erros.

---

### <img src="https://api.iconify.design/mdi/run-fast.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Teste de Esforço (Análise Dinâmica)

* **O que é?** A análise do seu código **enquanto ele está em execução**.
* **Analogia:** O médico colocando o paciente em uma **"esteira para um teste de esforço"** ou fazendo um **"exame de sangue"**. Ele precisa que o corpo do paciente esteja em funcionamento para observar seu comportamento e encontrar problemas que não são visíveis em repouso.
* **A Dor que Resolve:** Encontrar erros de **lógica**, que só aparecem quando o programa interage com dados reais ou diferentes cenários.

#### <img src="https://api.iconify.design/mdi/tools.svg?color=currentColor" width="20" style="vertical-align:middle; margin-right:8px;" /> Suas Ferramentas de Análise Dinâmica:
* **<img src="https://api.iconify.design/mdi/stethoscope.svg?color=currentColor" width="18" /> Depuração com `print()` (O Estetoscópio):**
    * **Como Funciona:** É a técnica mais simples e, muitas vezes, a mais rápida. Você espalha `print()`s pelo seu código para "ouvir" o valor das variáveis em diferentes pontos e entender o fluxo de execução.
    * **Uso:** `print(f"DEBUG: O valor da variável X é: {x}")`.

* **<img src="https://api.iconify.design/mdi/ultrasound.svg?color=currentColor" width="18" /> O Depurador Python (`pdb` - A Ressonância Magnética):**
    * **O que é?** Uma ferramenta interativa que te permite **pausar** a execução do seu programa em um ponto específico (um *breakpoint*), inspecionar o valor de todas as variáveis, e depois executar o código linha por linha.
    * **Como Usar:** Você pode iniciar seu script com `python -m pdb meu_script.py`.
    * **Comandos Básicos no `(Pdb)`:** `n` (próxima linha), `c` (continuar até o próximo breakpoint), `p nome_da_variavel` (imprimir o valor da variável), `q` (sair).

* **<img src="https://api.iconify.design/mdi/test-tube.svg?color=currentColor" width="18" /> Testes Unitários (`unittest`, `pytest`):**
    * **O que é?** O ato de escrever código para testar seu código.
    * **A Dor que Resolve:** "Eu corrigi um bug, mas como posso ter certeza de que não quebrei outras cinco coisas no processo?" Testes automatizados criam uma "rede de segurança" que garante que as funcionalidades existentes continuem funcionando após uma alteração (evita *regressões*).

---

### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Depurando na Nuvem AWS

Como você depura uma função **Lambda**, que roda sem um servidor para você acessar?

* **<img src="https://api.iconify.design/logos/aws-cloudwatch-logs.svg?color=currentColor" width="18" /> Amazon CloudWatch Logs:**
    * Esta é a sua ferramenta **número um**. Toda e qualquer instrução `print()` dentro da sua função Lambda envia sua saída diretamente para o CloudWatch Logs. É a sua principal forma de "ouvir" o que sua função está fazendo e quais erros ela encontrou.

* **<img src="https://api.iconify.design/logos/aws-x-ray.svg?color=currentColor" width="18" /> AWS X-Ray:**
    * **A Dor que Resolve:** "Minha aplicação é composta por múltiplos serviços (API Gateway -> Lambda -> DynamoDB). Uma requisição está lenta ou dando erro, mas não sei em qual etapa está o problema."
    * **O que faz?** O X-Ray atua como um **"GPS"** que rastreia uma única requisição através de todos os serviços da AWS pelos quais ela passa, te dando um mapa visual de onde estão os gargalos de performance e os erros.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** A prova Cloud Practitioner não vai te perguntar sobre o `pdb`. Mas ela espera que você conheça os serviços de visibilidade:
> * **CloudWatch Logs:** É a ferramenta fundamental para **depurar** e ver a saída de serviços de computação como **Lambda** e **EC2**.
> * **AWS X-Ray:** É a ferramenta para **rastrear e analisar** requisições em aplicações **distribuídas** (microsserviços).

---

### <img src="https://api.iconify.design/mdi/bug-check-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Médico do Código: Guia Definitivo de Depuração e Testes em Python

Um fato universal da programação: **todo código tem bugs**. A habilidade de um desenvolvedor sênior não está em escrever código perfeito na primeira tentativa, mas sim em ser um mestre na arte de **diagnosticar (depurar) e curar (corrigir)** os problemas de forma rápida e eficiente.

Pense no seu código como um **paciente**. A depuração é o processo de diagnóstico para descobrir a causa da "doença" (o bug). Existem duas grandes abordagens para este diagnóstico: a análise estática e a dinâmica.

---

### <img src="https://api.iconify.design/mdi/file-eye-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. O Exame Visual (Análise Estática)

* **O que é?** A análise do seu código-fonte **sem executá-lo**.
* **Analogia:** O médico fazendo um **"exame visual"** e lendo o **"prontuário do paciente"**. Ele consegue encontrar problemas óbvios apenas olhando, sem que o paciente precise fazer qualquer esforço.
* **A Dor que Resolve:** Encontrar erros de "gramática" (sintaxe), erros de digitação e desvios de boas práticas antes mesmo de rodar o programa, economizando tempo.
* **Suas Ferramentas:**
    * **IDEs (como o VS Code):** Sublinham erros de sintaxe em tempo real.
    * **Linters (ex: `Pylint`, `Flake8`):** O **"assistente robótico do médico"** que analisa seu código em busca de erros lógicos, problemas de estilo e "código suspeito".

---

### <img src="https://api.iconify.design/mdi/run-fast.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Teste de Esforço (Análise Dinâmica)

* **O que é?** A análise do seu código **enquanto ele está em execução**.
* **Analogia:** O médico colocando o paciente em uma **"esteira para um teste de esforço"**. É aqui que os problemas de lógica e de tempo de execução aparecem.
* **A Dor que Resolve:** Encontrar bugs que só se manifestam com dados específicos ou em certas condições de execução.

#### <img src="https://api.iconify.design/mdi/stethoscope.svg?color=currentColor" width="20" /> A Técnica do `print()` (O Estetoscópio)
A forma mais simples de depuração dinâmica. Você insere `print()`s em seu código para "ouvir" o valor das variáveis em pontos-chave.

#### <img src="https://api.iconify.design/mdi/target-account.svg?color=currentColor" width="20" /> `assert` (O Monitor de Sinais Vitais)
* **O que é?** Uma declaração que verifica se uma condição é verdadeira. Se for falsa, o programa para imediatamente com um erro (`AssertionError`).
* **Analogia:** O **"monitor de sinais vitais"** que para o teste na esteira se o coração do paciente sair de um ritmo seguro.
* **A Dor que Resolve:** Validar suposições no seu código. Garante que os dados estejam no formato esperado antes de prosseguir, evitando erros complexos mais tarde.
* **Exemplo:**
    ```python
    def calcular_preco_com_desconto(preco, desconto):
        # Garante que o desconto seja um valor lógico (entre 0 e 1)
        assert 0 <= desconto <= 1, "O desconto deve ser entre 0 e 1"
        return preco * (1 - desconto)
    ```

#### <img src="https://api.iconify.design/mdi/notebook-text-outline.svg?color=currentColor" width="20" /> Logging Profissional (O Prontuário Eletrônico)
**A Dor:** `print()`s poluem a saída do seu programa e precisam ser removidos manualmente em produção.
**A Solução:** Use a biblioteca `logging`, a forma profissional de registrar eventos.

* **Analogia:** É o **"prontuário eletrônico"** que o médico preenche durante o exame. Ele anota tudo com diferentes níveis de severidade.
* **Níveis de Log:**
    * `DEBUG`: Anotações super detalhadas para o desenvolvedor.
    * `INFO`: Eventos normais ("Paciente iniciou o teste").
    * `WARNING`: Avisos ("Batimentos cardíacos elevados").
    * `ERROR`: Erros que não quebram o programa ("Equipamento de medição falhou").
    * `CRITICAL`: Erros que quebram o programa ("Paciente caiu da esteira").

* **Exemplo Prático:**
    ```python
    import logging

    # Configuração básica: salva logs de nível DEBUG e acima no arquivo 'app.log'
    logging.basicConfig(filename='app.log', level=logging.DEBUG, 
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info("O programa foi iniciado.")
    try:
        resultado = 10 / 0
    except ZeroDivisionError:
        # Em vez de print, usamos logging.error para registrar o erro
        logging.error("Ocorreu um erro de divisão por zero!")
    logging.info("O programa foi finalizado.")
    ```

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO:** A grande vantagem do `logging` é que você pode mudar o `level` para `logging.INFO` ou `logging.WARNING` em produção. As mensagens de `DEBUG` ainda estarão no seu código, mas não serão mais exibidas ou salvas, sem que você precise apagar nenhuma linha!

---

### <img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Depurando na Nuvem AWS

* **<img src="https://api.iconify.design/logos/aws-cloudwatch-logs.svg?color=currentColor" width="18" /> Amazon CloudWatch Logs:**
    * A função **AWS Lambda** é **pré-configurada para usar a biblioteca `logging` do Python**. Qualquer `logging.info()`, `logging.warning()`, etc., que você escreve no seu código Lambda aparece **automaticamente e de forma estruturada** no CloudWatch Logs. É a forma profissional de depurar em um ambiente serverless.

* **<img src="https://api.iconify.design/logos/aws-x-ray.svg?color=currentColor" width="18" /> AWS X-Ray:**
    * Para aplicações complexas (microsserviços), o X-Ray é a sua "ressonância magnética". Ele rastreia uma requisição através de múltiplos serviços (API Gateway -> Lambda -> DynamoDB) e te mostra um mapa de onde estão os erros e os gargalos de performance.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova:
> * **CloudWatch Logs:** É a ferramenta fundamental para **depuração** e ver a saída de serviços como Lambda e EC2 (**Análise Dinâmica**).
> * **AWS X-Ray:** É para **rastrear e analisar** requisições em aplicações **distribuídas**.
> * **Amazon CodeGuru:** É o serviço de **Análise Estática** da AWS, que revisa seu código em busca de bugs e otimizações.

---


### <img src="https://api.iconify.design/mdi/pyramid-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Parte 2: A Pirâmide da Qualidade (Entendendo os Níveis de Teste)

Testar um software não é uma única ação, mas uma estratégia com múltiplos níveis, conhecida como a **Pirâmide de Testes**.

**Analogia:** Pense na **construção de um carro de LEGO Technic**. Você não constrói o carro inteiro para só no final ver se ele funciona. Você testa em cada etapa.

<p style="text-align: center;">
  <img src="https://i.imgur.com/83U243v.png" alt="Pirâmide de Testes" width="450">
</p>

---


### <img src="https://api.iconify.design/mdi/toy-brick-outline.svg?color=currentColor" width="22" /> 1. Testes de Unidade (A Base da Pirâmide)
* **O que é?** O teste da **menor parte funcional** do seu código, geralmente uma única função, de forma totalmente isolada.
* **Analogia:** "Testar cada **peça de LEGO individualmente**". Antes de montar o motor, você verifica: "Esta engrenagem gira livremente? Este pino tem o tamanho certo?".
* **Quem Faz?** O próprio desenvolvedor.
* **A Dor que Resolve:** Encontrar erros de lógica em uma função específica de forma rápida e precisa, sem a complexidade do resto do sistema.

### <img src="https://api.iconify.design/mdi/cogs.svg?color=currentColor" width="22" /> 2. Testes de Integração (Conectando as Peças)
* **O que é?** O teste da **interação entre duas ou mais unidades** que já foram testadas individualmente.
* **Analogia:** "Montar e testar os **subsistemas**". Você monta o motor e a caixa de câmbio. Agora, você os conecta e testa: "Quando eu giro o eixo do motor, a caixa de câmbio troca as marchas corretamente?".
* **Quem Faz?** Desenvolvedores ou testadores de QA.
* **<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> **Na Prática na AWS:** Você testa se sua **função Lambda** (unidade 1) consegue realmente gravar e ler dados em sua tabela **DynamoDB** (unidade 2).

### <img src="https://api.iconify.design/mdi/car-outline.svg?color=currentColor" width="22" /> 3. Testes de Sistema (O Teste do Carro Completo)
* **O que é?** O teste da aplicação **completa e integrada**, do início ao fim, para verificar se ela atende aos requisitos funcionais.
* **Analogia:** "Testar o **carro de LEGO totalmente montado**". O carro está pronto. Agora você o empurra no chão e verifica: "Ele anda para frente? As portas abrem? A suspensão funciona como descrito na caixa?".
* **Quem Faz?** Principalmente testadores de QA.
* **<img src="https://api.iconify.design/logos/aws.svg?color=currentColor" width="18" /> **Na Prática na AWS:** Você simula a ação de um usuário: clica em um botão no site, que chama uma **API Gateway**, que aciona uma **Lambda**, que grava no **DynamoDB**, e verifica se o resultado esperado aparece na tela.

### <img src="https://api.iconify.design/mdi/account-check-outline.svg?color=currentColor" width="22" /> 4. Testes de Aceitação (A Prova Final)
* **O que é?** Um teste formal, geralmente realizado pelo cliente ou por donos de produto, para validar se o software atende às **necessidades do negócio**.
* **Analogia:** "Entregar o **carro de LEGO para a criança (o cliente) brincar**". A criança não se importa com os requisitos técnicos da caixa; ela vai testar se o carro é **divertido**, se ele é o que ela **esperava**.
* **Quem Faz?** O cliente, usuários finais, Product Owner.
* **A Pergunta que Responde:** "Este software resolve o problema de negócio para o qual foi construído?"

> **<img src="https://api.iconify.design/mdi/lightbulb-on-outline.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> INSIGHT PODEROSO (A Lógica da Pirâmide):** A pirâmide nos ensina que você deve ter **MUITOS** testes de unidade (que são rápidos e baratos de rodar) e **POUCOS** testes de sistema/aceitação (que são lentos e caros). A base sólida de testes de unidade garante que a maioria dos bugs seja pega antes mesmo da integração.

---

### <img src="https://api.iconify.design/logos/aws-codepipeline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Automatizando a Qualidade na AWS (CI/CD)

**A Dor:** Rodar todos esses testes manualmente a cada pequena mudança no código é inviável.

**A Solução:** Automatize a pirâmide de testes em uma esteira de **Integração e Entrega Contínua (CI/CD)**.
* **Como Funciona:**
    1.  Um desenvolvedor envia código novo para o **AWS CodeCommit**.
    2.  Isso aciona o **AWS CodePipeline** (a "esteira").
    3.  Uma etapa do **AWS CodeBuild** é executada. O CodeBuild é um "robô de montagem" que, entre outras coisas, **roda automaticamente todos os seus testes de unidade e integração**.
    4.  **SE** qualquer teste falhar, a esteira **PARA** e notifica a equipe. O código defeituoso é barrado.
    5.  **SE** todos os testes passarem, a esteira continua para as próximas etapas, como a implantação em um ambiente de testes de sistema.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:5px;" /> HACK PARA CERTIFICAÇÃO:** Para a prova, entenda a finalidade de cada nível de teste. Eles adoram perguntas que comparam **Testes de Unidade** (foco no desenvolvedor, testa a menor parte) vs. **Testes de Integração** (testa a comunicação entre as partes). Saiba que o **AWS CodeBuild** é o serviço usado para rodar testes automatizados em um pipeline de CI/CD.