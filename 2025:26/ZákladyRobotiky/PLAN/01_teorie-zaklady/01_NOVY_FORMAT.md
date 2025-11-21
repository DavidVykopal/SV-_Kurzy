# Blok 1: Teorie a základy elektrotechniky - Demonstrační formát (5 hodin)

## Přehled bloku
**Formát:** David experimentuje s elektronikou live, děti sledují + přemýšlejí
**Cíl:** Ukázat že elektřina není magie, ale logika  
**Cool faktor:** Světla, zvuky, pohyb - okamžitá fyzická odezva!

---

## Hodina 1: Co je elektřina - živé experimenty (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Elektřina jako tok vody (10 min)
**COOL MOMENT:** Analogie s hadicí!

**David s props:**
- Ukaž hadici s vodou
- "Elektřina = tok elektronů, jako voda v hadici"
- **Napětí (V)** = Tlak vody (kolik silně tlačí)
- **Proud (A)** = Množství vody (kolik jí teče)
- **Odpor (Ω)** = Zúžení hadice (co brzdí tok)

"Čím větší tlak (napětí), tím více vody (proud) poteče!"

#### 2. Falstad Circuit Simulator - live demo (20 min)
**Otevři Falstad na projekci:**

**Experiment 1: Baterie + LED**
```
[Battery 9V] → [LED] → [Ground]
```
*Naklikej v real-time*
- "Vidíte? LED svítí!"
- "Proud teče v kruhu - z baterie a zpět"

**Změn napětí 3V → 9V:**
- 3V: Slabé světlo
- 9V: Jasné světlo
- "Více napětí = více energie = jasnější!"

**Experiment 2: Přidej rezistor**
```
[Battery 9V] → [Resistor 220Ω] → [LED] → [Ground]
```
- "Rezistor = ochrana. LED by bez něj shořela!"
- Ukaž simulaci: změň odpor → mění se jas

**Experiment 3: Co se stane bez rezistoru?**
*Smaž rezistor → příliš velký proud*
- "Vidíte to červené? Příliš! LED by zemřela!"
- "Proto VŽDY potřebujeme rezistor s LED!"

#### 3. Praktická ukázka - Minecraft Redstone? (15 min)
**COOL MOMENT:** "Elektřina je jako redstone!"

Pusti Minecraft nebo ukaž:
- Redstone = drát (vodič)
- Redstone torch = baterie/zapínač
- Redstone lamp = LED
- Repeater = zesilovač signálu

"Vidíte? Redstone je elektřina ve hře! Stejné principy!"

### 👥 ZAPOJENÍ DĚTÍ

#### Predictions:
- "Co se stane když dám větší baterii?"
- "Bude LED svítit silněji nebo slaběji?"
- "Potřebujeme rezistor? Proč?"

#### Analogie z her:
- "Hráli jste Minecraft redstone?" → diskuze
- "Kde jste viděli elektřinu v jiných hrách?"

#### Kreslení:
- Děti můžou nakreslit obvod na papír
- "Nakreslete baterii → drát → LED → zpět"

### 💻 CO BY DĚTI MOHLY DĚLAT

**Falstad Simulator (online, zdarma):**
- Otevřít falstad.com/circuit
- Vytvořit obvod: Baterie + LED + Resistor
- Experimentovat s hodnotami
- Sledovat proud a napětí (klik na komponenty)

**Minecraft (pokud dostupný):**
- Postavit redstone obvod
- Lampa co se rozsvítí tlačítkem
- Experimenty s repeaters a comparators

**Roblox - Circuit Maker 2:**
- Hra kde stavíš elektrické obvody!
- Puzzle levels s logikou

---

## Hodina 2: Bezpečnost - co ANO a co NE (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Ukázka bezpečných napětí (15 min)
**COOL MOMENT:** David se dotýká 5V - nic se neděje!

**Show real batteries:**
- **1.5V AA baterie** → "Bezpečné! Klidně se dotkni"
- **9V blok** → "Taky OK, maximálně cítíš mírné brnění na jazyku" (NEUKAZUJ!)
- **5V USB** → "Mobily, Arduino - všechno bezpečné"
- **230V zásuvka** → "NEBEZPEČNÉ! NIKDY!"

**Vizuální pomůcka:**
```
✅ SAFE ZONE (můžeme použít):
1.5V, 3V, 5V, 9V - baterie a USB

⚠️ CAUTION:
12V autobaterie - bezpečné napětí, ale VELKÝ proud!

❌ DANGER ZONE (nikdy!):
230V zásuvka, poškozené kabely, mokré ruce
```

#### 2. Bezpečnostní pravidla - story time (15 min)
**Příběhy (fiktivní ale poučné):**

**Příběh 1: "Kabel v kaluži"**
"Jednou jeden kluk viděl kabel u bazénu..."
→ Poučení: Voda + elektřina = NIKDY!

**Příběh 2: "Experimenty s zásuvkou"**
"Jiný kluk si myslel že zkusí..."
→ Poučení: Zásuvky nejsou na experimenty!

**Pravidla (na plakát):**
1. ✅ **Baterie do 9V jsou OK**
2. ✅ **USB 5V je safe**  
3. ❌ **Zásuvky = NE!**
4. ❌ **Mokré ruce = NE!**
5. ✅ **V simulátoru můžeme všechno!**
6. ✅ **Vždy se zeptej dospělého před real hardware**

#### 3. Co dělat když... (10 min)
**Scénáře:**

"**Vidím kouř z obvodu** → Co dělám?"
→ Odpověď: Odpoj baterii! Nehas vodou!

"**Poškozený kabel** → Co dělám?"
→ Odpověď: Nepoužívat! Říct dospělému!

"**Chci větší napětí** → Co dělám?"
→ Odpověď: Zeptám se! Nespojuji baterie náhodně!

#### 4. Simulator = bezpečný playground (5 min)
**COOL MOMENT:** "Tady můžete zničit cokoliv!"

**Falstad demo:**
- Připoj 1000V na LED → *BOOM* v simulaci
- "Vidíte? V simulátoru nic špatného! Proto je skvělý!"
- "Můžete experimentovat bez rizika!"

### 👥 ZAPOJENÍ
- "Kdo viděl nějaký elektrický úraz?" → diskuze opatrně
- "Kde doma máte nejvíc elektřiny?" → awareness
- Kvíz: "Bezpečné nebo nebezpečné?" (ukazuješ obrázky)

### 💻 CO BY DĚTI MOHLY DĚLAT
- Vytvořit vlastní "safety poster" s pravidly
- Simulator experimenty bez omezení
- Najít doma co je na baterie a co na zásuvku

---

## Hodina 3: Schémata obvodů - jazyk elektroniků (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Proč schémata? (5 min)
**COOL MOMENT:** Porovnání fotky vs. schématu

**Ukaž dva obrázky:**
- **Foto breadboardu** → "Chaotické! Těžko čitelné!"
- **Schéma** → "Čisté! Každý na světě rozumí!"

"Schéma = mapa obvodu. Mezinárodní jazyk!"

#### 2. Základní symboly - learn by doing (25 min)
**David kreslí symboly na tabuli, děti opisují:**

**Symbol by symbol live:**

```
─── = Vodič (drát)
"Spojuje komponenty"

─|─ = Baterie
"Zdroj napětí, dlouhá čárka = plus"

─/\/\/─ = Rezistor
"Zpomaluje proud, zig-zag tvar"

─|>──  = LED
"Svítí! Šipka ukazuje směr světla"
```

**Falstad side-by-side:**
- Naklikej symbol v simulátoru
- Ukaž jak vypadá v real life (fotka)
- "Vidíte? Stejný symbol, různé zobrazení!"

**Praktické cvičení:**
David nakreslí schéma → děti tápou co to je → odkryje!
```
  ─|─ → ─/\/\/─ → ─|>── → ─⊥
(Battery → Resistor → LED → Ground)
```

#### 3. Čtení schémat - detective work (10 min)
**COOL MOMENT:** "Najděte chybu ve schématu!"

**Schéma 1 (správné):**
```
[Battery +] → [Resistor] → [LED +] → [LED -] → [Battery -]
```
"Proud teče v kruhu → funguje!"

**Schéma 2 (chyba - LED otočená):**
```
[Battery +] → [Resistor] → [LED -] → [LED +] → [Battery -]
```
"LED otočená! Nebude svítit!"

**Schéma 3 (chyba - chybí rezistor):**
```
[Battery +] → [LED] → [Battery -]
```
"Chybí rezistor! LED shoří!"

Děti hledají chyby jako detektivové!

#### 4. Nakresli svůj obvod (5 min)
**Zadání:** "Nakreslete obvod: Baterie + 2 LED série"
- Děti kreslí na papír
- David chodí kolem, pomáhá
- Nejlepší návrhy na tabuli!

### 👥 ZAPOJENÍ
- "Hádejte co je tohle za symbol?" → hra
- "Nakreslete baterii z paměti" → všichni zkoušejí
- "Najděte chybu!" → competition

### 💻 CO BY DĚTI MOHLY DĚLAT
- Nakreslit schémata na papír
- Použít Falstad a zkusit replicate nakreslen obvod
- Vytvořit vlastní symboly pro fantasy komponenty

---

## Hodina 4: Komponenty v Falstad - hands-on (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Baterie - zdroj energie (10 min)
**Live v Falstad:**

**Experiment sequence:**
- 1.5V → LED nesvítí (málo)
- 3V → LED slabě svítí
- 5V → LED svítí normálně  
- 9V → LED svítí jasně
- 12V → LED velmi jasně!

"Baterie = tlak co žene proud. Více voltů = více tlaku!"

**Series vs Parallel:**
- 2× baterie série (3V + 3V = 6V) → více napětí
- 2× baterie paralel (3V + 3V = 3V) → více výdrž

#### 2. Rezistory - regulátoři proudu (10 min)

**Experiment: Jas LED s různými rezistory:**
- 100Ω → velmi jasná
- 220Ω → normální (doporučeno)
- 1kΩ → slabá
- 10kΩ → sotva viditelná

**Live calculation (jednoduše):**
```
Ohmův zákon: U = R × I
"Více odpor = méně proud = slabší světlo"
```

**Vizualizace v Falstad:**
- Klikni na rezistor → zobrazí se proud
- Změň hodnotu → sleduj jak se mění proud
- "Vidíte? Matematika v akci!"

#### 3. LED - světelné diody (15 min)
**COOL MOMENT:** Barevné LED!

**Různé barvy LED v Falstad:**
- Červená LED → forward voltage ~2V
- Modrá LED → forward voltage ~3V
- "Různé barvy = různé napětí potřebují!"

**Polarita:**
```
Správně:  + → [LED →] → -  ✅ Svítí
Špatně:   + → [← LED] → -  ❌ Nesvítí
```
"LED má směr! Jako jednosměrka!"

**Experiment:**
- Otoč LED v obvodu → přestane svítit
- Otoč zpět → svítí!
- "Tohle je důležité pamatovat!"

#### 4. Challenge obvody (10 min)
**David zadává, děti navrhují:**

**Challenge 1:** "Udělej 2 LED série"
**Challenge 2:** "Udělej 3 LED různých barev"
**Challenge 3:** "LED bliká (použij switch)"

Děti radí, David staví v Falstad live!

### 👥 ZAPOJENÍ
- "Jakou barvu LED chcete vidět?"
- "Tipněte si correct resistor hodnotu"
- "Navrh svůj vlastní obvod!"

### 💻 CO BY DĚTI MOHLY DĚLAT
- Replicate ukázky v Falstad
- Experimentovat s kombinacemi
- Vytvořit "light show" s několika LED
- Měřit proud a napětí (multimeter v Falstad)

---

## Hodina 5: Arduino úvod - mozek projektů (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Co je Arduino? (10 min)
**COOL MOMENT:** Ukázka physical Arduino!

**Ukaž real Arduino Uno:**
- "Tohle je miniaturní počítač!"
- "Má procesor, paměť, vstupy, výstupy"
- "Stojí ~200 Kč, ale zvládne neuvěřitelné věci!"

**Piny overview:**
- **Digital (0-13):** ON/OFF signály
- **Analog (A0-A5):** Hodnoty 0-1023
- **Power:** 5V, 3.3V, GND
- **USB:** Napájení + nahrávání kódu

**Analogie:**
"Arduino = mozek, senzory = smysly, motory = svaly"

#### 2. Tinkercad Circuits + Arduino (15 min)
**Live demo: První Arduino obvod**

**Otevři Tinkercad před dětmi:**

**Krok za krokem:**
1. Components → Arduino Uno R3
2. Components → LED
3. Components → Resistor 220Ω
4. Zapoj: Pin 13 → Resistor → LED → GND

**Kód (v Tinkercad text mode):**
```cpp
void setup() {
  pinMode(13, OUTPUT);  // Pin 13 = výstup
}

void loop() {
  digitalWrite(13, HIGH);  // Zapni
  delay(1000);             // Čekej 1s
  digitalWrite(13, LOW);   // Vypni
  delay(1000);             // Čekej 1s
}
```

**Zmáčkni "Start Simulation"**
→ LED bliká!

**COOL MOMENT:** "Napsali jsme program pro hardware!"

#### 3. Změny v real-time (15 min)
**Experiment sequence:**

**Rychlost blikání:**
- `delay(1000)` → pomalé (1s)
- `delay(500)` → střední
- `delay(100)` → rychlé!
- `delay(50)` → velmi rychlé!

**Morse kód:**
```cpp
// S O S v Morse
// S: . . .  (krátké)
// O: - - -  (dlouhé)

blink(200); blink(200); blink(200); // S
delay(500);
blink(600); blink(600); blink(600); // O
delay(500);
blink(200); blink(200); blink(200); // S
```

"Vidíte? Arduino mluví!"

**Multiple LEDs:**
- Přidej 3 LED na piny 11, 12, 13
- Blikej postupně → efekt "scanner"
- "Jako KITT z Knight Rider!"

#### 4. Input - tlačítko (5 min)
**Quick preview příští hodiny:**

Přidej pushbutton:
```cpp
void loop() {
  if (digitalRead(2) == HIGH) {
    digitalWrite(13, HIGH);  // Tlačítko stisknuto → LED svítí
  } else {
    digitalWrite(13, LOW);
  }
}
```

"Arduino poslouchá tlačítko! To je INPUT!"

### 👥 ZAPOJENÍ
- "Jak rychle má blikat?"
- "Vymyslete vlastní blikací pattern!"
- "Co by Arduino mohlo ovládat?" → brainstorm

### 💻 CO BY DĚTI MOHLY DĚLAT
**Tinkercad Circuits:**
- Vytvořit Arduino + LED blikátko
- Experimentovat s delay časováním
- Přidat více LED
- Zkusit různé patterns (semafor, rytmus)

**Roblox Circuit Maker 2:**
- Arduino-like puzzle levels

---

## Shrnutí bloku 1 (5 hodin)

### Co děti viděly:
✅ Elektřina jako tok (analogie s vodou)
✅ Bezpečnostní pravidla (co ano, co ne)
✅ Schémata obvodů (mezinárodní jazyk)
✅ Komponenty (baterie, rezistor, LED) v simulaci
✅ Arduino jako "brain" projektů
✅ První kód a blikající LED!

### Key takeaways:
- Elektřina není magie - je to logika!
- Simulátory = bezpečný playground
- Arduino = powerful nástroj
- Každý projekt začíná simple (blikátko)

### Co dál:
Příští blok = Tinkercad深入, programování, senzory!

---

## Poznámky pro Davida

### Presentation tips:
- **Používej VELKÉ symboly** - aby všichni viděli
- **Barevně** - zvýrazni komponenty
- **Srovnávej** - real vs simulace vs schéma
- **Chyby jsou OK** - ukaž troubleshooting

### Tech setup:
- Falstad otevřený v jednom tabu
- Tinkercad v druhém
- Minecraft/Roblox ready pokud čas
- Physical Arduino na ukázku (nemusí být zapojené)

### Energy management:
- První 2 hodiny = teorie (může být suché)
- Hodina 3 = interaktivní (symboly)
- Hodina 4-5 = hands-on simulace (nejzábavnější!)
- Plánuj breaky s cool videi pokud vidíš únavu

