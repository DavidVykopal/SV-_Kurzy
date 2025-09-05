# Blok 1: Teorie a základy (1–5)

## Hodina 1: Co je elektřina, napětí, proud, odpor

### Cíle hodiny
- Porozumět základním pojmům elektřiny
- Pochopit rozdíl mezi napětím, proudem a odporem
- Naučit se základní jednotky (V, A, Ω)

### Materiály
- Falstad Circuit Simulator (https://falstad.com/circuit/)
- Ukázkové obrázky z reálného světa
- Pracovní list s úkoly

### Průběh hodiny (45 min)

#### 1. Úvod - Co je elektřina? (10 min)
**Otázka pro děti:** "Co všechno doma potřebuje elektřinu?"
- Rozsvícení lampy, počítač, lednička, mobil
- Elektřina = tok elektronů vodičem
- **Analogie s vodou:** Elektřina je jako voda v hadici

#### 2. Napětí (U) - "tlak" elektřiny (10 min)
- **Analogie:** Napětí = tlak vody v hadici
- Měří se ve voltech (V)
- **Praktický příklad:** 
  - Baterie AA = 1.5V
  - Mobil = 3.7V
  - Zásuvka = 230V (POZOR - nebezpečné!)
- **Falstad ukázka:** Ukázat baterii s různým napětím

#### 3. Proud (I) - "množství" elektřiny (10 min)
- **Analogie:** Proud = množství vody protékající hadicí za sekundu
- Měří se v ampérech (A)
- **Praktický příklad:**
  - LED = 0.02A (20mA)
  - Mobil při nabíjení = 1A
  - Mikrovlnka = 10A
- **Falstad ukázka:** Ukázat měření proudu v obvodu

#### 4. Odpor (R) - "překážka" pro elektřinu (10 min)
- **Analogie:** Odpor = zúžení v hadici
- Měří se v ohmech (Ω)
- **Praktický příklad:**
  - Krátký tlustý drát = malý odpor
  - Dlouhý tenký drát = větší odpor
  - Rezistor = komponenta s přesným odporem
- **Falstad ukázka:** Ukázat rezistor a jak ovlivňuje proud

#### 5. Ohmův zákon (5 min)
- **Jednoduchá verze:** Větší napětí = větší proud
- **Vzorec pro starší děti:** U = R × I
- **Praktická ukázka:** Ve Falstadu změnit napětí a sledovat proud

### Domácí úkol
Najdi doma 3 věci, které používají elektřinu, a zkus odhadnout, jestli potřebují velké nebo malé napětí.

---

## Hodina 2: Bezpečnost při práci s elektřinou

### Cíle hodiny
- Pochopit nebezpečí elektřiny
- Naučit se základní bezpečnostní pravidla
- Rozpoznat bezpečné a nebezpečné napětí

### Materiály
- Obrázky bezpečnostních symbolů
- Ukázky různých zdrojů napětí
- Bezpečnostní plakát pro třídu

### Průběh hodiny (45 min)

#### 1. Proč je elektřina nebezpečná? (10 min)
- **Základní pravidlo:** Elektřina hledá nejkratší cestu
- Lidské tělo je vodivé (díky vodě v těle)
- **Nebezpečí:**
  - Popálení
  - Zásah srdce
  - Úraz svalů

#### 2. Bezpečná vs. nebezpečná napětí (15 min)
- **BEZPEČNÁ (pro naše účely):**
  - 1.5V baterie AA
  - 3V baterie (2×AA)
  - 5V USB napájení
  - 9V blok baterie
- **NEBEZPEČNÁ - NIKDY SE NEDOTÝKAT:**
  - 230V zásuvka
  - Autobaterie 12V (velký proud!)
  - Jakékoli poškozené kabely

#### 3. Bezpečnostní pravidla (15 min)
1. **Vždy vypni obvod** před změnami
2. **Nikdy nepracuj s mokrýma rukama**
3. **Nepoužívaj poškozené komponenty**
4. **Zeptej se dospělého** před připojením k zásuvce
5. **V simulátoru můžeme zkoušet cokoliv** - je bezpečný!

#### 4. Rozpoznávání nebezpečí (5 min)
- Bezpečnostní symboly (blesk, lebka)
- Poškozené kabely
- Voda + elektřina = NIKDY!

### Praktická část
Vytvoření třídy "Bezpečnostních pravidel" - každé dítě navrhne jedno pravidlo.

---

## Hodina 3: Schémata obvodů, základní symboly

### Cíle hodiny
- Naučit se číst schémata obvodů
- Poznat základní elektronické symboly
- Nakreslit první jednoduché schéma

### Materiály
- Tabulka symbolů
- Falstad Circuit Simulator
- Papír a tužka pro kreslení

### Průběh hodiny (45 min)

#### 1. Co je schéma obvodu? (10 min)
- **Analogie:** Schéma = mapa elektrického obvodu
- Proč nekreslíme fotografie komponent?
- Mezinárodní symboly - rozumí jim každý na světě

#### 2. Základní symboly (20 min)

| Symbol | Komponenta | Význam |
|--------|------------|--------|
| ─── | Vodič | Drát, spojení |
| ⊥ | Zem | Referenční bod (0V) |
| ─\|─ | Baterie | Zdroj napětí |
| ─\/\/\/─ | Rezistor | Odpor |
| ─\|>──  | LED | Světelná dioda |
| ─\|\|─ | Kondenzátor | Ukládá elektřinu |
| ○ | Spoj | Místo spojení drátů |

#### 3. Čtení schémat (10 min)
- **Ukázka jednoduchého obvodu:** Baterie + LED + Rezistor
- Jak sledovat cestu proudu
- **Falstad ukázka:** Stejné schéma v simulátoru

#### 4. Kreslení schémat (5 min)
- Pravidla: čisté čáry, správné symboly, popisky
- **Cvičení:** Nakreslit obvod baterka + LED

### Domácí úkol
Nakreslit schéma svítilny (baterie, spínač, žárovka).

---

## Hodina 4: Baterie, rezistory, LED – vysvětlení ve Falstad

### Cíle hodiny
- Prakticky pochopit funkci základních komponent
- Naučit se používat Falstad simulátor
- Vytvořit první fungující obvody

### Materiály
- Počítače s internetem
- Falstad Circuit Simulator
- Pracovní list s úkoly

### Průběh hodiny (45 min)

#### 1. Úvod do Falstad simulátoru (10 min)
- Otevření stránky: https://falstad.com/circuit/
- Základní ovládání:
  - Pravé tlačítko = menu
  - Draw = kreslení komponent
  - Levé tlačítko = informace o komponentě

#### 2. Baterie ve Falstadu (10 min)
- **Vytvoření baterie:** Draw → Passive Components → Voltage Source (2-terminal)
- **Nastavení napětí:** Pravé tlačítko na baterii → Edit
- **Ukázka:** Baterie 3V vs. 9V
- **Pozorování:** Zelená = kladný pól, červená = záporný pól

#### 3. Rezistory ve Falstadu (10 min)
- **Vytvoření rezistoru:** Draw → Passive Components → Resistor
- **Nastavení odporu:** Pravé tlačítko → Edit → Resistance
- **Ukázky různých odporů:** 100Ω, 1kΩ, 10kΩ
- **Pozorování barvy:** Světlejší = méně proudu

#### 4. LED ve Falstadu (10 min)
- **Vytvoření LED:** Draw → Passive Components → LED
- **Pozorování:** LED svítí pouze v jednom směru!
- **Proč potřebujeme rezistor?** Ochrana před vysokým proudem
- **Vytvoření obvodu:** Baterie 5V → Rezistor 220Ω → LED → zpět k baterii

#### 5. Praktické cvičení (5 min)
Každé dítě si vytvoří obvod: Baterie 3V + Rezistor 150Ω + LED

### Domácí úkol
Ve Falstadu vytvořit obvod se 2 LED (paralelně).

---

## Hodina 5: Přehled součástek, ukázka Arduina

### Cíle hodiny
- Poznat Arduino a jeho možnosti
- Porozumět rozdílu mezi analogovými a digitálními signály
- Přehled komponent, které budeme používat

### Materiály
- Fyzické Arduino Uno (ukázka)
- Tinkercad Circuits účet
- Obrázky různých součástek

### Průběh hodiny (45 min)

#### 1. Co je Arduino? (15 min)
- **Mikrokontrolér** = malý počítač pro ovládání elektroniky
- **Ukázka fyzického Arduina:**
  - USB konektor pro napájení a programování
  - Digitální piny (0-13)
  - Analogové piny (A0-A5)
  - Napájecí piny (5V, 3.3V, GND)

#### 2. Digitální vs. analogové signály (10 min)
- **Digitální:** Pouze 0 nebo 1 (vypnuto/zapnuto)
  - Příklad: LED on/off, tlačítko stisknuto/nestisknuto
  - V Pythonu: `True`/`False` nebo `1`/`0`
- **Analogové:** Plynulé hodnoty (0-255, 0-1023)
  - Příklad: jas LED, teplota, pozice potenciometru
  - V Pythonu: čísla jako `127`, `512`, `850`

#### 3. Přehled součástek pro kurz (15 min)

| Součástka | Použití | Typ |
|-----------|---------|-----|
| LED | Světlo | Digitální výstup |
| Rezistor | Ochrana, dělič napětí | Pasivní |
| Tlačítko | Vstup od uživatele | Digitální vstup |
| Potenciometr | Nastavitelná hodnota | Analogový vstup |
| Teploměr | Měření teploty | Analogový vstup |
| Fotoresistor | Světelný senzor | Analogový vstup |
| PIR senzor | Pohybový senzor | Digitální vstup |
| Servo motor | Pohyb | Digitální výstup |
| Bzučák | Zvuk | Digitální výstup |

#### 4. První seznámení s programováním (5 min)
- **Python** - jednoduchý programovací jazyk
- **Příklad základní logiky:**
  ```python
  if svetlo_je_zapnute:
      print("LED svítí")
  else:
      print("LED nesvítí")
  ```
- **Tinkercad** - můžeme programovat v blokách nebo textu (Python-like)
- Registrace na tinkercad.com → "Circuits"

### Příprava na další hodiny
- Každý má účet na Tinkercad
- Domácí úkol: Prohlédnout si komponenty v Tinkercad → Components → All

### Shrnutí bloku 1
- Pochopili jsme základy elektřiny (U, I, R)
- Víme, jak pracovat bezpečně
- Umíme číst schémata
- Známe základní komponenty
- Jsme připraveni na simulace!
