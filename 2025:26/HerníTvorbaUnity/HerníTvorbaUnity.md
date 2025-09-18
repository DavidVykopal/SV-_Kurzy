# Příprava počítačové učebny pro kroužek herního vývoje v Unity

Vážený pane správce, vážená paní správkyně,

obracím se na Vás s prosbou o přípravu počítačové učebny pro potřeby nového kroužku "Herní Tvorba s Unity". Cílem tohoto dokumentu je přehledně shrnout veškeré technické požadavky na software, síťový přístup a uživatelská oprávnění, abychom zajistili hladký průběh výuky.

Děkuji předem za Vaši spolupráci.

---

### 1. Software k instalaci (vyžaduje administrátorská oprávnění)

Následující software je potřeba nainstalovat na všechny počítače v učebně.

| Software | Účel a poznámka |
| :--- | :--- |
| **Unity Hub** | Správce verzí enginu Unity a projektů. Základní nástroj, přes který se vše spravuje. |
| **Unity Editor (LTS)**| Hlavní herní engine. Prosíme o instalaci nejnovější **LTS (Long-Term Support)** verze přes Unity Hub pro zajištění maximální stability. |
| **Visual Studio Code** | Primární editor kódu. Je lehký a vhodný pro začátečníky. |
| &nbsp;&nbsp;↳ *Doplňky pro VS Code*| Je nutné doinstalovat rozšíření: `C# Dev Kit` a `Unity` od Microsoftu. |
| **JetBrains Rider** | Profesionální IDE pro C# a Unity. Jde o náročnější alternativu k VS Code. Pro školy je dostupná bezplatná licence v rámci "Educational Packu". |
| **Git** | Verzovací systém nezbytný pro spolupráci na projektech a zálohování kódu na platformě GitHub. |
| **Blender** (Volitelně)| Open-source software pro tvorbu 3D modelů. |
| **Audacity** (Volitelně)| Open-source software pro nahrávání a úpravu zvukových souborů. |

---

### 2. Přístup k online službám a doménám

Pro plnohodnotnou výuku je nutné zajistit, aby školní síť a firewall neblokovaly přístup k následujícím online službám a doménám, které jsou klíčové pro stahování nástrojů, assetů, verzování a komunikaci.

**Seznam klíčových domén k povolení:**
- `*.unity.com`, `*.unity3d.com` (přihlašování, dokumentace, Asset Store)
- `*.github.com` (verzování kódu)
- `*.visualstudio.com` (stahování doplňků pro editor)
- `*.jetbrains.com` (licence a doplňky pro Rider)
- `*.notion.so` (týmová dokumentace)
- `*.figma.com` (návrh UI/UX)
- `*.itch.io` (herní assety a publikace)
- `*.google.com` (pro přístup ke Google Drive, Docs, Slides)
- `*.discord.com` (komunikace v týmu)

---

### 3. Hardwarové požadavky na PC

Vývoj her je hardwarově náročná disciplína. Pro plynulý chod jsou klíčové následující parametry:

- **Operační systém:** Windows 10/11 (64-bit)
- **RAM:** Minimum **8 GB**, doporučeno **16 GB**.
- **Pevný disk:** **SSD disk je naprosto klíčový.** Práce na klasickém HDD je kvůli pomalému načítání projektů a dat prakticky nemožná. Je potřeba alespoň **50 GB volného místa** na systémovém disku pro software a další prostor pro studentské projekty.
- **Grafická karta:** Karta s podporou DirectX 11. Pro 3D grafiku je doporučena dedikovaná grafická karta (NVIDIA GeForce / AMD Radeon).

---

### 4. Požadovaná uživatelská oprávnění

Pro bezproblémový chod kroužku potřebují studenti následující oprávnění:

1.  **Instalace a aktualizace:** Počáteční instalaci softwaru provedete Vy. Je však možné, že v průběhu roku bude potřeba doinstalovat doplňkové moduly do Unity (např. pro export na Android). Bylo by ideální najít řešení, jak tyto moduly instalovat bez nutnosti opakovaného zásahu z Vaší strany.
2.  **Právo stahovat soubory:** Studenti si musí moci stahovat grafické a zvukové materiály (assety) z internetu.
3.  **Právo zápisu na disk:** Studenti musí mít neomezené právo zápisu do svých uživatelských složek, kam si budou ukládat své projekty. Projekty v Unity mohou snadno dosáhnout velikosti několika gigabytů.

---

V případě jakýchkoliv dotazů či nejasností jsem plně k dispozici ke konzultaci.

S pozdravem a poděkováním,

David Vykopal
