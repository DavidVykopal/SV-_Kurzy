# Info o Studentských Projektech - Domácí Realizace

Tento dokument obsahuje přehled všech projektů, které si děti během kurzu vytvoří v simulaci a mohou pak skutečně postavit doma.

## Hlavní Projekty podle Bloků

### **Block 2: Základní LED projekty**
- **Blikátko s tlačítkem** - 3 LED různých barev, 3 různé módy blikání
- **Semafor** - realistické časování červená/žlutá/zelená
- *Náklady: ~200-300 Kč*

### **Block 3: Inteligentní osvětlení**
- **Automatické světlo** s LDR senzorem - zapíná se při stmívání
- **Smart LED systém** s manuálním přepínáním a adaptivním jasem
- *Náklady: ~400-500 Kč*

### **Block 5: Senzorové projekty**
- **Teplotní monitor** s LCD displejem a barevnou signalizací
- **Bezpečnostní alarm** s PIR senzorem, časovačem a různými módy
- **Kombinované systémy** - teplota + světlo + pohyb
- *Náklady: ~800-1200 Kč*

### **Block 6-7: Komplexní ročníkové projekty**

**Nejčastější projekty studentů:**

#### 1. **Smart Květináč** 🌱
- Automatické zalévání podle vlhkosti půdy
- Monitoring teploty a světla
- LCD displej s informacemi
- Manuální a automatické módy
- *Náklady: ~1200-1500 Kč*

#### 2. **Domácí Bezpečnostní Systém** 🏠
- PIR detekce pohybu
- Světelný sensor (detekce rozbitého okna)
- LCD displej, bzučák, LED signalizace
- Různé módy: Doma/Pryč/Vypnuto
- *Náklady: ~1000-1300 Kč*

#### 3. **Automatické Krmítko** 🐕
- Servo motor pro dávkování
- Časovač nebo tlačítkové ovládání
- Senzor váhy (detekce prázdné misky)
- LCD s časem dalšího krmení
- *Náklady: ~800-1000 Kč*

#### 4. **Chytrý Termostat** 🌡️
- TMP36 teplotní senzor
- Ovládání topení/ventilátoru (relay)
- Nastavitelná cílová teplota
- Týdenní časový program
- *Náklady: ~600-800 Kč*

#### 5. **LED Světelná Show** 💡
- Hudební reaktivní LED pásky
- Mikrofonový senzor
- Různé vizuální efekty
- Ovládání přes tlačítka/potenciometry
- *Náklady: ~700-900 Kč*

## Přesný Seznam Součástek pro Domácí Stavbu

### **Základní Arduino Kit (nutný základ):**
```
Arduino Uno R3         ~300 Kč
Breadboard             ~100 Kč  
Jumper wires           ~100 Kč
Resistor kit           ~150 Kč
LED kit (různé barvy)  ~100 Kč
Pushbutton set         ~80 Kč
CELKEM: ~830 Kč
```

### **Senzory a Moduly (podle projektu):**
```
TMP36 teplotní senzor     ~50 Kč
LDR fotoresistor          ~30 Kč
PIR motion sensor         ~120 Kč
Soil moisture sensor      ~80 Kč
LCD displej 16x2          ~180 Kč
Servo motor SG90          ~120 Kč
Relay modul               ~100 Kč
Buzzer                    ~40 Kč
Potenciometr              ~30 Kč
```

### **Napájení a Mechanika:**
```
9V baterie + konektor     ~100 Kč
DC čerpadlo (mini)        ~150 Kč
3D tištěné díly          ~50-200 Kč
Krabička/housing         ~100-300 Kč
```

## Skutečné Možnosti Domácí Stavby

### **✅ CO FUNGUJE DOBŘE DOMA:**
- Všechny digitální senzory (PIR, tlačítka, LED)
- Teplotní a světelné senzory
- LCD displeje a jednoduché výstupy
- Servo motory pro mechanický pohyb
- Základní automation projekty

### **⚠️ CO VYŽADUJE DOSPĚLOU POMOC:**
- Připojení k síťovému napájení (230V)
- Práce s vodou (čerpadla, zalévání)
- Pájení permanentních spojů
- 3D tisk mechanických dílů

### **❌ CO JE OBTÍŽNÉ/DRAHÉ:**
- Pokročilé senzory (GPS, IMU, kamery)
- Vysokovýkonové aktuátory
- WiFi/IoT konektivita (vyžaduje ESP32)
- Profesionální PCB výroba

## Doporučený Postup pro Rodiče

### **Fáze 1: Start s Simulací (0 Kč)**
- Dítě ukáže funkční projekt v Tinkercad
- Rodiče vidí co projekt dělá
- Společné rozhodnutí o fyzické stavbě

### **Fáze 2: Základní Kit (~800 Kč)**
- Pořízení Arduino základny
- Stavba jednoduchých projektů (LED, tlačítka)
- Ověření zájmu dítěte

### **Fáze 3: Rozšíření podle Projektu (~500-800 Kč)**
- Dokoupení specifických senzorů
- Realizace ročníkového projektu
- 3D tisk nebo improvizace mechaniky

### **Fáze 4: Upgrade a Vylepšení (~1000+ Kč)**
- ESP32 pro WiFi projekty
- Pokročilejší senzory
- Vlastní PCB design
- 3D tiskárna pro mechaniku

## Praktický Příklad: Smart Květináč

**Co dítě vytvoří v simulaci:**
- Kompletní funkční kód v Pythonu
- Schéma zapojení všech komponent
- Testování různých scénářů
- Dokumentace projektu

**Co můžete stavět doma postupně:**

**Verze 1 (Basic - 800 Kč):**
- Arduino + senzor vlhkosti + LED signalizace
- Jen upozornění kdy zalít

**Verze 2 (Advanced - 1200 Kč):**
- + LCD displej + čerpadlo + automatické zalévání

**Verze 3 (Pro - 2000 Kč):**
- + 3D tištěný obal + WiFi + mobilní app

## Detailní Rozpis Nákladů podle Projektů

### **LED Blikátko (Začátečník)**
```
Arduino Uno R3        300 Kč
Breadboard            100 Kč
3× LED různé barvy     30 Kč
3× Rezistor 220Ω       15 Kč
1× Pushbutton          20 Kč
Jumper wires           50 Kč
CELKEM: ~515 Kč
```

### **Automatické Osvětlení (Pokročilý začátečník)**
```
Základní kit          515 Kč
LDR fotoresistor       30 Kč
Rezistor 10kΩ          10 Kč
Potenciometr           30 Kč
CELKEM: ~585 Kč
```

### **Bezpečnostní Alarm (Středně pokročilý)**
```
Základní kit          515 Kč
PIR motion sensor     120 Kč
LCD displej 16×2      180 Kč
Buzzer                 40 Kč
2× LED signalizační    20 Kč
CELKEM: ~875 Kč
```

### **Smart Květináč (Pokročilý)**
```
Základní kit          515 Kč
Soil moisture sensor   80 Kč
TMP36 teplotní sensor  50 Kč
LCD displej           180 Kč
Mini čerpadlo         150 Kč
Relay modul           100 Kč
Hadičky a mechanika   200 Kč
CELKEM: ~1275 Kč
```

## Kde Koupit Součástky

### **🎯 DOPORUČENO: Nákup přes učitele kurzu**
- **Na vyžádání zajistím všechny potřebné součástky**
- **Výhody nákupu přes učitele:**
  - ✅ Garantovaná kompatibilita a kvalita součástek
  - ✅ Přesně odpovídá projektům z kurzu
  - ✅ Předem otestované komponenty
  - ✅ Konkurenceschopné ceny (bez marže obchodníků)
  - ✅ Součástky připravené v sadách podle projektů
  - ✅ Možnost osobního předání + konzultace
  - ✅ Podpora při stavbě a troubleshooting
- **Kontakt:** [doplnit kontaktní údaje učitele]
- **Objednávky:** Nejlépe 1-2 týdny předem

#### **Připravené sady komponent:**

**🟢 ZÁKLADNÍ SADA "Arduino Start" (~800 Kč)**
- Arduino Uno R3 + USB kabel
- Breadboard + jumper wires
- LED kit (různé barvy) + rezistory
- Pushbutton set + pull-up rezistory
- Základní senzory (LDR, teplotní)
- *Pro projekty Bloků 1-3*

**🟡 ROZŠÍŘENÁ SADA "Smart Home" (~1200 Kč)**
- Vše z Základní sady +
- PIR motion sensor
- LCD displej 16×2
- Relay modul + buzzer
- Servo motor + potenciometry
- *Pro většinu projektů Bloků 4-5*

**🔴 PREMIUM SADA "Maker Kit" (~1800 Kč)**
- Vše z Rozšířené sady +
- Soil moisture sensor
- Mini čerpadlo + hadičky
- 3D tištěné díly (na vyžádání)
- Napájecí moduly
- Pokročilé senzory
- *Pro všechny ročníkové projekty*

**📱 UPGRADE "IoT Ready" (~500 Kč k libovolné sadě)**
- ESP32 development board
- WiFi antenna + kabel
- Breadboard adapter
- Návody na mobilní app připojení

### **Alternativní možnosti nákupu:**

**Online obchody (Česká republika):**
- **Arduino.cz** - český distributor, rychlé doručení
- **TME.cz** - profesionální elektronické komponenty
- **Santy.cz** - hobby elektronika, Arduino kity
- **GM Electronic** - tradiční český dodavatel

**Mezinárodní (levnější, pomalejší doručení):**
- **AliExpress** - nejlevnější, dodání 2-4 týdny
- **Amazon.de** - rychlé doručení, vyšší cены
- **Mouser/Digikey** - profesionální komponenty

**Fyzické obchody:**
- **GM Electronic pobočky** (Praha, Brno, Ostrava)
- **Místní hobby obchody** s elektronikou
- **Některé OKAY/Hornbach** mají Arduino sekce

## Tipy pro Rodiče

### **🛠️ Servis a podpora (při nákupu přes učitele):**
- **Bezplatná konzultace** před objednávkou sady
- **Instrukční video** specificky pro váš projekt
- **Email/telefon podpora** během stavby
- **Osobní troubleshooting** při problémech
- **Záruka funkčnosti** všech dodaných součástek
- **Výměna vadných komponent** do 30 dnů
- **Upgrade poradenství** pro rozšiřování projektů

### **Před nákupem:**
1. **Nechte dítě ukázat projekt v simulaci**
2. **Společně projděte seznam součástek**
3. **Začněte s jednodušším projektem**
4. **Připravte se na troubleshooting**

### **Během stavby:**
1. **Buďte trpěliví - debugging je součást procesu**
2. **Nechte dítě vést, vy jen pomáhejte**
3. **Fotografujte pokrok - je to skvělé portfolio**
4. **Oslavte i malé úspěchy**

### **Pokud něco nefunguje:**
1. **Zkontrolujte zapojení podle schématu**
2. **Ověřte napájení (nejčastější problém)**
3. **Zkuste jiné součástky (mohou být vadné)**
4. **Kontaktujte učitele nebo komunitu Arduino.cz**

## Dlouhodobý Potenciál

Projekty z kurzu jsou navrženy tak, aby měly růstový potenciál:

- **Jednoduché verze** mohou děti stavět samostatně
- **Pokročilé verze** vyžadují pomoc rodičů
- **Profesionální verze** jsou inspirací pro střední školu
- **Komerční potenciál** - některé projekty lze skutečně prodat

Výsledkem kurzu tak není jen vzdělání, ale konkrétní praktické dovednosti a realizovatelné projekty, které mohou být základem dlouhodobého zájmu o techniku a možná i budoucí kariéry.