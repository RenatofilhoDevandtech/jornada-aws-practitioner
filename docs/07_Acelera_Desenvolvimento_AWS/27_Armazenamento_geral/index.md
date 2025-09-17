# <img src="https://api.iconify.design/mdi/archive-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> A Despensa da Nuvem: Guia do Arquiteto para os Serviços de Armazenamento da AWS

Toda aplicação precisa armazenar dados. Mas, assim como em uma casa, você não guarda tudo no mesmo lugar. Ingredientes frescos ficam na geladeira, pratos ficam no armário e itens raramente usados vão para o sótão.

**A Dor:** Usar o tipo de armazenamento errado para seus dados leva a baixa performance, altos custos e complexidade desnecessária.
**A Filosofia da AWS:** Oferecer **armazenamento construído para fins específicos (`purpose-built`)**. Um arquiteto de nuvem é como um mestre organizador: ele sabe exatamente qual "cômodo" usar para cada tipo de "coisa".

---

### <img src="https://api.iconify.design/mdi/compare-horizontal.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 1. A Tríade do Armazenamento (Bloco, Arquivo e Objeto)

Esta é a diferença mais fundamental que você precisa dominar.

| Tipo | Analogia | Unidade Mínima | Acesso | Caso de Uso Principal | Serviço AWS Chave |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Bloco** | Uma **"Tábua de Cortar"** na sua cozinha. | **Bloco**. Permite modificar pequenos pedaços de um arquivo. | Direto (como um HD local). | Instalar um SO, rodar um banco de dados de alta performance. | **Amazon EBS** |
| **Arquivo**| A **"Despensa Comunitária"** da casa. | **Arquivo**. Acessado em uma hierarquia de pastas. | Compartilhado via rede (protocolo NFS/SMB). | Servidores de arquivos, diretórios compartilhados. | **Amazon EFS** |
| **Objeto** | O **"Sótão com Caixas Etiquetadas"**. | **Objeto** (o arquivo inteiro). | Via API web (HTTP/S). | Backups, imagens, vídeos, sites estáticos, Data Lakes. | **Amazon S3** |

---

### <img src="https://api.iconify.design/mdi/toolbox-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 2. O Catálogo de Serviços de Armazenamento da AWS

* **<img src="https://api.iconify.design/mdi/dots-grid.svg?color=currentColor" width="18" /> Armazenamento em Bloco:**
    * **Amazon EBS:** A "tábua de cortar" persistente e de alta performance para suas instâncias EC2.
    * **Instance Store:** A "tábua de cortar" temporária e ultrarrápida, mas seus dados são apagados se a instância for parada.

* **<img src="https://api.iconify.design/mdi/file-cabinet.svg?color=currentColor" width="18" /> Armazenamento de Arquivos:**
    * **Amazon EFS:** A "despensa" elástica e gerenciada para cargas de trabalho **Linux**.
    * **Amazon FSx:** "Despensas" especializadas e de alta performance, com opções para **Windows File Server** e **Lustre** (para computação de alto desempenho).

* **<img src="https://api.iconify.design/mdi/package-variant-closed-box.svg?color=currentColor" width="18" /> Armazenamento de Objetos:**
    * **Amazon S3:** O "sótão" infinitamente escalável para praticamente qualquer tipo de dado.
    * **Amazon S3 Glacier:** O **"cofre de segurança no fundo do sótão"**, para arquivamento de longo prazo com o menor custo possível.

* **<img src="https://api.iconify.design/mdi/truck-delivery-outline.svg?color=currentColor" width="18" /> Armazenamento Híbrido:**
    * **AWS Storage Gateway:** O **"serviço de delivery"** que conecta sua "casa" (data center on-premises) com os "armazéns" da AWS (S3, EBS) de forma transparente.

---

### <img src="https://api.iconify.design/mdi/comment-question-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> 3. O Guia de Seleção do Arquiteto (Cenários)

* **Se você precisa de...** um "HD" persistente e de alta performance para sua instância EC2 rodar um banco de dados.
    * **<img src="https://api.iconify.design/mdi/arrow-right-thin-circle-outline.svg" /> A Recomendação:** **Amazon EBS**.

* **Se você precisa de...** um local para guardar backups, imagens e vídeos, e hospedar um site estático, com acesso de qualquer lugar da internet.
    * **<img src="https://api.iconify.design/mdi/arrow-right-thin-circle-outline.svg" /> A Recomendação:** **Amazon S3**.

* **Se você precisa de...** arquivar dados por anos com o menor custo possível, para fins de conformidade.
    * **<img src="https://api.iconify.design/mdi/arrow-right-thin-circle-outline.svg" /> A Recomendação:** **Amazon S3 Glacier**.

* **Se você precisa de...** um servidor de arquivos compartilhado para que múltiplas instâncias EC2 **Linux** possam acessar os mesmos dados ao mesmo tempo.
    * **<img src="https://api.iconify.design/mdi/arrow-right-thin-circle-outline.svg" /> A Recomendação:** **Amazon EFS**.

* **Se você precisa de...** uma forma de integrar seu ambiente local com o armazenamento da AWS para backups ou recuperação de desastres.
    * **<img src="https://api.iconify.design/mdi/arrow-right-thin-circle-outline.svg" /> A Recomendação:** **AWS Storage Gateway**.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** A prova **adora** a diferença entre os três tipos de armazenamento. É um dos tópicos mais importantes.
> * **S3 -> Objeto** (acesso via API, internet, escalabilidade infinita).
> * **EBS -> Bloco** (HD virtual de alta performance, para **uma única** EC2).
> * **EFS -> Arquivo** (servidor de arquivos compartilhado, para **múltiplas** EC2s).

--- 

### <img src="https://api.iconify.design/mdi/archive-search-outline.svg?color=currentColor" width="26" style="vertical-align:middle; margin-right:8px;" /> O Guia de Seleção do Arquiteto: Resolvendo Desafios de Armazenamento na AWS

Você é o arquiteto. Um cliente chega com um desafio de armazenamento. Sua missão é ouvir a necessidade e escolher a ferramenta perfeita na "caixa de ferramentas" da AWS. Este guia é o seu manual de seleção rápida para os cenários mais comuns.

---

### <img src="https://api.iconify.design/mdi/creation.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Playbook de Cenários de Armazenamento

#### <img src="https://api.iconify.design/logos/aws-ebs.svg?color=currentColor" width="20" /> Se você precisa de...
* Armazenamento em bloco persistente para o Amazon EC2.
* Armazenamento que funciona bem para bancos de dados e aplicações.
> **A Recomendação:** **Amazon EBS (Elastic Block Store)**
>
> **O "Porquê":** O EBS funciona como o **"HD ou SSD"** da sua instância EC2. É um armazenamento em bloco de alta performance e baixa latência, ideal para rodar o sistema operacional e bancos de dados que precisam de acesso rápido e persistente a partir de **uma única instância**.

---
#### <img src="https://api.iconify.design/logos/aws-s3.svg?color=currentColor" width="20" /> Se você precisa de...
* Uma plataforma escalável e durável que torna os dados acessíveis de qualquer local da Internet.
* Armazenamento para conteúdo gerado pelo usuário, arquivamento ativo, computação sem servidor, armazenamento de big data ou backup e recuperação.
> **A Recomendação:** **Amazon S3 (Simple Storage Service)**
>
> **O "Porquê":** O S3 é o seu **"sótão infinito com caixas etiquetadas"**. É um serviço de armazenamento de objetos projetado para durabilidade e escala massiva. Por ser acessível via HTTP, é perfeito para guardar qualquer tipo de arquivo (imagens, vídeos, backups) e servi-los para aplicações web e móveis.

---
#### <img src="https://api.iconify.design/logos/aws-s3-glacier.svg?color=currentColor" width="20" /> Se você precisa de...
* Um serviço de armazenamento na nuvem seguro, durável e de custo extremamente baixo para o arquivamento de dados e backup de longo prazo.
> **A Recomendação:** **Amazon S3 Glacier**
>
> **O "Porquê":** O Glacier é o **"cofre de segurança no fundo do sótão"**. Ele oferece o menor custo de armazenamento na AWS, ideal para dados que você precisa guardar por anos (para fins de conformidade ou legais) mas que raramente acessa.

---
#### <img src="https://api.iconify.design/logos/aws-efs.svg?color=currentColor" width="20" /> Se você precisa de...
* Um sistema de arquivos NFS simples e escalável para cargas de trabalho do **Linux** que usam serviços de nuvem da AWS e recursos locais.
> **A Recomendação:** **Amazon EFS (Elastic File System)**
>
> **O "Porquê":** O EFS é a sua **"despensa comunitária"**. É um servidor de arquivos totalmente gerenciado que pode ser acessado por **múltiplas instâncias EC2 Linux ao mesmo tempo**. Ele cresce e encolhe automaticamente, sendo ideal para sistemas de gerenciamento de conteúdo e diretórios compartilhados.

---
#### <img src="https://api.iconify.design/logos/aws-storage-gateway.svg?color=currentColor" width="20" /> Se você precisa de...
* Armazenamento híbrido que amplia seu ambiente local com o armazenamento na nuvem da AWS, para recuperação de desastres (DR) ou migração.
> **A Recomendação:** **AWS Storage Gateway**
>
> **O "Porquê":** O Storage Gateway é o **"serviço de delivery"** que conecta sua "casa" (data center on-premises) com os "armazéns" da AWS. Ele permite que suas aplicações locais usem o armazenamento da nuvem (como S3 e EBS) de forma transparente.

---
#### <img src="https://api.iconify.design/logos/aws-fsx.svg?color=currentColor" width="20" /> Se você precisa de...
* Um sistema de arquivos para cargas de trabalho específicas, como aplicações **Windows** ou computação de alto desempenho (HPC).
> **A Recomendação:** **Amazon FSx**
>
> **O "Porquê":** O FSx oferece "despensas" especializadas. O **Amazon FSx for Windows File Server** fornece um servidor de arquivos totalmente gerenciado e nativo do Windows. O **Amazon FSx for Lustre** é otimizado para cargas de trabalho de computação de alta performance que precisam de acesso extremamente rápido a grandes conjuntos de dados.

> **<img src="https://api.iconify.design/mdi/star-four-points.svg?color=currentColor" width="18" style="vertical-align:middle; margin-right:8px;" /> HACK PARA CERTIFICAÇÃO:** A prova é cheia de perguntas de cenário sobre armazenamento. Esta página é a sua "cola". As associações mais importantes são:
> * **`HD` para UMA EC2** -> **EBS** (Bloco).
> * **Backups, Imagens, Site Estático** -> **S3** (Objeto).
> * **Arquivo Morto / Longo Prazo** -> **S3 Glacier** (Objeto/Arquivo).
> * **Servidor de Arquivos Compartilhado (Linux)** -> **EFS** (Arquivo).

