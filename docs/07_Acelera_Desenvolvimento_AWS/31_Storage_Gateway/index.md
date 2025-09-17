# <img src="https://api.iconify.design/mdi/server-network-outline.svg?color=currentColor" width="28" style="vertical-align:middle; margin-right:8px;" /> AWS Storage Gateway — Ponte entre Local e Nuvem  

O **AWS Storage Gateway** é um serviço híbrido que conecta aplicações locais ao armazenamento em nuvem da AWS. Ele combina protocolos familiares (NFS, SMB, iSCSI) com os serviços de armazenamento da AWS (S3, Glacier, EBS).  

---

## <img src="https://api.iconify.design/mdi/school-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Que Você Aprenderá  

- Definir o **Storage Gateway**  
- Entender conceitos do **modelo de dados** do serviço  
- Explorar as **três soluções** disponíveis (arquivo, volume e fita)  
- Identificar **casos de uso práticos**  

**Principais termos:**  
- Storage Gateway  
- Interface de arquivos  
- Interface de volume  
- Interface de fita  

---

## <img src="https://api.iconify.design/mdi/bridge.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> O Conceito de Ponte  

O Storage Gateway funciona como uma **ponte** entre o ambiente local e a nuvem.  
- Se uma aplicação **não puder migrar totalmente** (por performance, compliance ou complexidade), o Storage Gateway conecta o local ao S3, EBS ou Glacier.  
- Ele fornece **cache local** para baixa latência e mecanismos de **transferência eficiente** com resiliência de rede.  

---

## <img src="https://api.iconify.design/mdi/database.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Conceitos de Modelo de Dados  

- Os aplicativos se conectam ao Storage Gateway via:  
  - **VM** (VMware ESXi, Hyper-V, Linux KVM)  
  - **Dispositivo físico dedicado** (appliance)  
- Protocolos suportados: **NFS**, **SMB** e **iSCSI**  
- Integra com:  
  - **Amazon S3**  
  - **Amazon EBS (Snapshots)**  
  - **Glacier e Glacier Deep Archive**  
- Oferece suporte a:  
  - **Arquivos**  
  - **Volumes**  
  - **Fitas Virtuais**  

---

## <img src="https://api.iconify.design/mdi/layer-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Três Soluções do Storage Gateway  

| Tipo de Gateway | Objetivo | Serviços da AWS | Protocolos |
|-----------------|----------|-----------------|------------|
| **File Gateway** | Armazenamento de arquivos como objetos no S3 com cache local | Amazon S3 / Glacier | NFS, SMB |
| **Volume Gateway** | Volumes de armazenamento em blocos (snapshots no Amazon EBS e S3) | Amazon S3 / EBS Snapshots | iSCSI |
| **Tape Gateway** | Substitui bibliotecas de fitas físicas por fitas virtuais, armazenadas no S3 e Glacier | Amazon S3 / Glacier / Glacier Deep Archive | iSCSI |

---

## <img src="https://api.iconify.design/mdi/briefcase-variant-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Casos de Uso  

- **Backup e Arquivamento** → Tape Gateway substitui fitas físicas.  
- **Recuperação de Desastres (DR)** → Volume Gateway com snapshots no S3/EBS.  
- **Processamento de Dados na Nuvem** → mover workloads gradualmente.  
- **Armazenamento em Camadas** → File Gateway envia arquivos ao S3, mantendo cache local.  
- **Migração Híbrida** → quando aplicações não podem ou não devem ser movidas completamente para a nuvem.  

---

## <img src="https://api.iconify.design/mdi/star-four-points-outline.svg?color=currentColor" width="22" style="vertical-align:middle; margin-right:8px;" /> Hacks para Certificação  

1. **File Gateway** → usa NFS/SMB, armazena no **S3 como objetos**.  
2. **Volume Gateway** → expõe volumes via iSCSI, snapshots salvos no **EBS/S3**.  
3. **Tape Gateway** → emula fitas físicas, salva no **S3/Glacier**.  
4. Sempre lembrar da **analogia da ponte** → conecta local à nuvem.  
5. Cache local = **baixa latência** para dados mais acessados.  

---
# <img src="https://api.iconify.design/mdi/server-network-outline.svg?color=currentColor" width="28" style="vertical-align:middle; margin-right:8px;" /> Como Funciona o AWS Storage Gateway  

O Storage Gateway cria uma **ponte híbrida** entre seu ambiente local e a Nuvem AWS, usando protocolos familiares e cache local para agilizar o acesso aos dados.  

---

## <img src="https://api.iconify.design/mdi/network-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Protocolos e Implantação  

- Protocolos suportados:  
  - **NFS / SMB** para File Gateway  
  - **iSCSI** para Volume Gateway e Tape Gateway  
- Implantação:  
  - Máquina Virtual (VM) em VMware, Hyper-V, KVM  
  - Dispositivo físico (hardware appliance)  
- Segurança:  
  - Criptografia em trânsito via HTTPS (Internet ou AWS Direct Connect)  
- Ponto de extremidade do serviço:  
  - Internet, Amazon VPC, FIPS  

---

## <img src="https://api.iconify.design/mdi/cloud-upload-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Visão Geral do Fluxo e Serviços AWS  

| On-Premises    | Storage Gateway                 | AWS Cloud Storage                  |
|----------------|--------------------------------|----------------------------------|
| Aplicativo de  | Gateway de Arquivo / Volume /  | Amazon S3 (Objetos)               |
| Backup / App / | Fita (VM ou Hardware Appliance)| Amazon S3 Glacier                 |
| Servidor       |                                | Amazon S3 Glacier Deep Archive   |

---

## <img src="https://api.iconify.design/mdi/folder-multiple-outline.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Gateway de Arquivo (File Gateway)  

- Usa protocolos **NFS ou SMB** para permitir que aplicações locais armazenem arquivos no **Amazon S3** como objetos.  
- Fornece **cache local** para acesso rápido aos dados mais usados.  
- Arquivos são armazenados e recuperados via ponto de montagem NFS/SMB.  
- Arquivos no S3 aproveitam recursos como **versionamento**, **ciclo de vida**, **replicação entre regiões** e **arquivamento** no Glacier.  

---

## <img src="https://api.iconify.design/mdi/harddisk.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Gateway de Volume (Volume Gateway)  

- Apresenta volumes de disco em bloco para aplicações via **iSCSI**.  
- Os dados são armazenados em cache localmente, enquanto os backups são feitos por meio de **snapshots no Amazon EBS/S3**.  
- Dois modos:  
  - **Armazenado em cache:** dados principais no S3, cache local para dados acessados frequentemente → reduz custo e mantém baixa latência.  
  - **Armazenado:** todo o conjunto de dados local, com backups assíncronos para o S3 → rápido acesso local e durabilidade na nuvem.  

---

## <img src="https://api.iconify.design/mdi/tape.svg?color=currentColor" width="24" style="vertical-align:middle; margin-right:8px;" /> Gateway de Fita (Tape Gateway)  

- Emula bibliotecas de fita físicas para aplicativos de backup via **iSCSI**.  
- Grava dados em fitas virtuais armazenadas no **Amazon S3**.  
- Fitas podem ser arquivadas posteriormente no **Amazon S3 Glacier / Glacier Deep Archive** para redução de custos.  
- Permite continuidade no uso dos softwares de backup já existentes enquanto migra o backend para a nuvem.  

---

# <img src="https://api.iconify.design/mdi/cloud-refresh-outline.svg?color=currentColor" width="28" style="vertical-align:middle; margin-right:8px;" /> Casos de Uso do AWS Storage Gateway  

O Storage Gateway conecta o armazenamento local ao da nuvem AWS, permitindo cenários híbridos eficientes.  

---

## Três Principais Casos de Uso de Nuvem Híbrida  

1. **Mover backups e arquivos para a nuvem:**  
   Transfira dados locais para armazenamento durável e escalável da AWS, reduzindo custos e complexidade de manutenção de hardware local.  

2. **Reduzir armazenamento local com compartilhamentos de arquivos em nuvem:**  
   Use o Storage Gateway para fornecer compartilhamento de arquivo com suporte na nuvem, aliviando o espaço no armazenamento on-premises.  

3. **Fornecer acesso de baixa latência a dados armazenados na AWS para aplicações locais:**  
   O cache local do gateway mantém dados acessados frequentemente no ambiente local para desempenho rápido, enquanto guarda o restante na nuvem.  

---

## Principais Conclusões  

- O Storage Gateway atua no local, **fazendo a ponte entre o ambiente local e a nuvem AWS**.  
- Ele é ideal para cenários híbridos em que há necessidade de armazenamento local limitado, mas que complementa com armazenamento cloud (S3, Glacier, EBS).  
- Oferece três interfaces principais para diferentes necessidades: **gateway de arquivo, gateway de volume e gateway de fita**.  

---


