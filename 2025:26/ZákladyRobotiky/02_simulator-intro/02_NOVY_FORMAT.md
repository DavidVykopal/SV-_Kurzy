# Blok 2: Simulátor obvodů - Tinkercad hands-on (5 hodin)

## Přehled bloku
**Formát:** David staví obvody live v Tinkercad, děti sledují a navrhují
**Cíl:** Od teorie k praxi - tvorba funkčních obvodů
**Cool faktor:** Virtuální hardware který FUNGUJE jako reálný!

---

## Hodina 6: Tinkercad Circuits tour - první obvody (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Tinkercad interface walkthrough (10 min)
**COOL MOMENT:** "Tohle je vaše elektronická dílna!"

**Live tour po projekci:**
- **Přihlášení:** tinkercad.com → Circuits
- **Create New Circuit:** prázdná workspace
- **Components panel:** "Supermarket s elektronikou!"
- **Simulation controls:** Play = zapne obvod, Stop = vypne

**Základní ovládání:**
- Drag & drop komponent
- Propojování (klik na pin → tažení)
- Rotace (R key)
- Zoom (scroll)
- Delete (Del nebo koš)

"Jako Minecraft creative mode, ale pro elektroniku!"

#### 2. Breadboard - základ všeho (10 min)
**COOL MOMENT:** Rentgen pohled na breadboard!

**Ukaž breadboard a vysvětli:**
```
     Power Rails (+ a -)
     │││││││││││││││
┌────┤├─────────────┐
│ +  ├─── všechny propojeny
│ -  ├─── všechny propojeny
│    │
│    ├──  řádky propojeny (a-e, f-j)
│    ├──  ale NENÍ propojení přes střed!
└────────────────────┘
```

**Live demo:**
- Umísti breadboard
- Ukaž color coding (červená = +, modrá/černá = -)
- "Breadboard = chytré propojení bez pájení!"

#### 3. První obvod - battery + LED (15 min)
**COOL MOMENT:** První světlo!

**Krok za krokem (David dělá, děti sledují):**

**Komponenty:**
1. Small Breadboard
2. Battery (9V)
3. LED (červená)
4. Resistor (220Ω)

**Zapojení live:**
```
[Battery +] → breadboard + rail
[Battery -] → breadboard - rail

[+ rail] → [Resistor] → [LED long leg]
[LED short leg] → [- rail]
```

**Zmáčkni "Start Simulation"**
→ LED SVÍTÍ! 🎉

**"První obvod úspěšně sestaven!"**

**Troubleshooting live (záměrně udělej chybu):**
- Zapoij LED obráceně → nesvítí
- "Aha! LED má polaritu!"
- Otoč → svítí! ✅

#### 4. Experimenty s hodnotami (10 min)
**Děti navrhují, David testuje:**

**Změna rezistoru:**
- Klikni na rezistor → Properties
- 100Ω → jasnější
- 1000Ω → tlumenější
- 10kΩ → sotva svítí

"Rezistor = stmívač pro LED!"

**Změna baterie:**
- 3V → slabé světlo
- 9V → normální
- 12V → velmi jasné

### 👥 ZAPOJENÍ
- "Jakou barvu LED chcete?" → hlasování
- "Tipni si: bude svítit jasněji nebo slaběji?" → predictions
- "Co se stane když smažu rezistor?" → nebezpečné, ale v simulaci OK!

### 💻 CO BY DĚTI MOHLY DĚLAT
- Replicate stejný obvod v Tinkercad
- Experimentovat s různými hodnotami
- Přidat více LED
- Vyzkoušet různé barvy

---

## Hodina 7: LED série a paralelní zapojení (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Série - za sebou (15 min)
**COOL MOMENT:** Světelný řetězec!

**Série obvod live:**
```
[Battery +] → [R] → [LED1 +/-] → [LED2 +/-] → [LED3 +/-] → [Battery -]
```

**Postavím před dětmi:**
- 3× LED za sebou
- 1× rezistor 220Ω
- Battery 9V

**Simulation → všechny svítí!**

**Experiment: "Co se stane když jedna LED vypadne?"**
- Odpoj jednu LED → VŠECHNY zhasnou!
- "Jako vánoční řetěz - jedna vypadne, všechny nesvítí!"

**Napětí v sérii:**
- Multimeter mezi každou LED
- "9V se rozdělí: 3V + 3V + 3V = 9V"
- "Každá LED dostane kousek energie"

#### 2. Paralelní - vedle sebe (15 min)
**COOL MOMENT:** Nezávislé kontroly!

**Paralelní obvod live:**
```
[Battery +] ┬─ [R1] → [LED1] ┬─ [Battery -]
            ├─ [R2] → [LED2] ┤
            └─ [R3] → [LED3] ┘
```

**Postavím a zapnu:**
- 3× LED paralelně, každá svůj rezistor
- Battery 9V

**Experiment: "Co se stane když jedna LED vypadne?"**
- Odpoj LED1 → LED2 a LED3 svítí dál!
- "Nezávislé! Jako světla v domě"

**Napětí v paralelním:**
- Multimeter na každou LED
- "Všechny mají 9V! Každá dostává plnou energii"

#### 3. Porovnání série vs paralelní (10 min)
**Side-by-side ukázka:**

**Série:**
- ✅ Šetří komponenty (1 rezistor)
- ❌ Všechny závisí na sobě
- ❌ Nižší napětí na každou LED
- Použití: Dekorace, displayery

**Paralelní:**
- ✅ Nezávislé - jedna vypadne, ostatní fungují
- ✅ Plné napětí pro každou
- ❌ Více rezistorů potřeba
- Použití: Domácí instalace, důležité systémy

**"Ve hře: Series = chain quest, Parallel = side quests!"**

#### 4. Challenge (5 min)
**Děti navrhují, David staví:**

"Udělejte semafor:"
- 3× LED (červená, žlutá, zelená)
- Paralelně aby mohly svítit nezávisle
- S tlačítky (preview příští hodiny)

### 👥 ZAPOJENÍ
- "Série nebo paralelní - co je lepší?" → diskuze
- "Kde doma máte serie? Kde paralelní?" → real-world examples
- Challenge návrhy od dětí

### 💻 CO BY DĚTI MOHLY DĚLAT
- Postavit série i paralelní obvod
- Experimentovat s počty LED
- Vytvořit světelnou show (různé kombinace)
- Měřit napětí multimetrem

---

## Hodina 8: Tlačítka a spínače - ovládání (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Pushbutton - dočasný kontakt (10 min)
**COOL MOMENT:** Interaktivní ovládání!

**Jednoduchý obvod s tlačítkem:**
```
[Battery +] → [Button] → [Resistor] → [LED] → [Battery -]
```

**Live build a test:**
- Simulation → LED nesvítí
- Klikni na tlačítko (v simulaci) → LED svítí!
- Pusť → zhasne
- "To je tlačítko! Jako spacebar ve hře"

**Aplikace:**
- Zvonek
- Gamepad buttons
- Klávesnice

#### 2. Switch - trvalý kontakt (10 min)

**Obvod se spínačem:**
```
[Battery +] → [Slide Switch] → [Resistor] → [LED] → [Battery -]
```

**Test:**
- Přepni switch → LED svítí TRVALE
- Přepni zpět → zhasne
- "Switch = light switch doma"

**Aplikace:**
- Vypínače světel
- On/Off button na zařízeních
- Power switch

#### 3. Více tlačítek - logika (15 min)
**COOL MOMENT:** AND a OR gates fyzicky!

**AND logika (série):**
```
[Battery] → [Button1] → [Button2] → [LED] → [Battery -]
```
- LED svítí JEN když OBĚ tlačítka zmáčknuta
- "To je AND - OBOJE musí být true"
- **Real world:** "Bezpečnostní systém - dvě klíče"

**OR logika (paralelní):**
```
            ┌─ [Button1] ─┐
[Battery] ──┤             ├─ [LED] ─ [Battery -]
            └─ [Button2] ─┘
```
- LED svítí když JAKÉKOLI tlačítko zmáčknuto
- "To je OR - stačí jedno"
- **Real world:** "Světlo ovládané ze dvou míst"

**Interactive test:**
Děti volají kombinace:
- "Button1 ON, Button2 OFF" → David testuje
- "Both ON!" → co se stane?

#### 4. Pull-up/pull-down rezistory (10 min)
**Vysvětlení floating pins:**

**Problém:**
```
[Button] → [Arduino Pin]
```
"Když tlačítko není stisknuto, pin je 'floating' - neví jestli HIGH nebo LOW!"

**Řešení: Pull-up rezistor**
```
        ┌─ [10kΩ Resistor] ─ [+5V]
        │
[Arduino Pin] ─ [Button] ─ [GND]
```

**Jak funguje:**
- Bez stisku: Pin = HIGH (tahán nahoru rezistorem)
- Se stiskem: Pin = LOW (připojen k zemi)
- "Pull-up = default hodnota"

"Jako gumička co táhne nahoru!"

### 👥 ZAPOJENÍ
- "Navrhněte bezpečnostní systém!" → 2+ tlačítka musí být zmáčknutá
- "Kde doma máte tlačítka vs. spínače?"
- Test různých kombinací AND/OR

### 💻 CO BY DĚTI MOHLY DĚLAT
- Sestavit quiz button system (kdo zmáčkne první?)
- Bezpečnostní systém (musí zmáčknout ve správném pořadí)
- Light controller s více spínači
- Kombinovat série a paralelní tlačítka

---

## Hodina 9: Potenciometr a analogové vstupy (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Co je potenciometr? (10 min)
**COOL MOMENT:** "Volume knob pro obvody!"

**Ukázka physical potenciometru:**
- "Je to proměnný rezistor"
- Točíš → mění se odpor (0Ω až 10kΩ)
- **Jako:** Volume, brightness, speed control

**Tinkercad potenciometr:**
```
[5V] → [Potentiometer] → [Arduino A0]
                        ↓
                      [GND]
```

**Multimeter ukázka:**
- Točím doleva → 0Ω
- Uprostřed → 5kΩ  
- Doprava → 10kΩ
- "Plynulá změna!"

#### 2. LED dimmer - První aplikace (15 min)
**COOL MOMENT:** Stmívatelná LED!

**Obvod:**
```
[Arduino] → [Pot na A0]
          → [LED na pin 9 (PWM)]
```

**Arduino kód (simplified):**
```cpp
void loop() {
  int sensorValue = analogRead(A0);  // Čti pot (0-1023)
  int brightness = sensorValue / 4;   // Převeď na 0-255
  analogWrite(9, brightness);         // Nastav jas LED
}
```

**Live demo:**
- Simulation → točím potenciometrem
- LED mění jas plynule!
- "Tohle je PWM - Pulse Width Modulation"

**Vysvětlení PWM jednoduše:**
```
Nízký jas:  █░░░█░░░█░░░  (rychlé blikání = slabé)
Střední:    ██░██░██░  
Vysoký:     ███████████  (skoro pořád ON = jasné)
```
"Bliká tak rychle že oko nevidí!"

#### 3. RGB LED control - Barevný mix (15 min)
**COOL MOMENT:** Vytvoř si vlastní barvu!

**Obvod:**
```
[Arduino] → [Pot1 na A0] → Červená hodnota
          → [Pot2 na A1] → Zelená hodnota
          → [Pot3 na A2] → Modrá hodnota
          → [RGB LED]
```

**Kód koncept:**
```cpp
int red = analogRead(A0) / 4;
int green = analogRead(A1) / 4;
int blue = analogRead(A2) / 4;

analogWrite(redPin, red);
analogWrite(greenPin, green);
analogWrite(bluePin, blue);
```

**Interactive test:**
- Všechny poty na 0 → černá (off)
- Red max → červená
- Red + Green → žlutá!
- All max → bílá!

"Jako color picker ve hře nebo Photoshop!"

#### 4. Serial Monitor - vidění hodnot (5 min)
```cpp
void loop() {
  int val = analogRead(A0);
  Serial.println(val);  // Vypíše do konzole
  delay(100);
}
```

**V Tinkercadu:**
- Code → Serial Monitor
- Vidíš čísla 0-1023 jak točíš
- "Debugging! Vidíš co Arduino 'cítí'"

### 👥 ZAPOJENÍ
- "Jakou barvu chcete vytvořit?" → děti navrhují, David točí poty
- "Tipni si jaká hodnota je to" → učí se rozsahy
- "Co byste ovládali potenciometrem?" → brainstorm

### 💻 CO BY DĚTI MOHLY DĚLAT
- LED dimmer
- RGB color mixer
- Servo motor control (rychlost/pozice)
- Speed control pro blikání
- "Volume" pro piezo bzučák

---

## Hodina 10: Mini projekt - chytré blikátko (45 min)

### 🎮 CO DAVID UKAZUJE

**Komplexní projekt od A do Z před dětmi!**

#### Specifikace projektu (5 min)
**"Chytré interaktivní blikátko":**

**Features:**
- 3× LED (červená, žlutá, zelená)
- 1× tlačítko pro změnu módu
- 1× potenciometr pro rychlost
- 3 různé módy blikání:
  1. Postupné (traffic light)
  2. Všechny najednou
  3. Náhodné

#### Hardware setup - live build (15 min)
**David staví před dětmi:**

**Komponenty:**
- Arduino Uno
- Breadboard
- 3× LED (R, Y, G)
- 3× Rezistor 220Ω (pro LED)
- 1× Pushbutton
- 1× Rezistor 10kΩ (pull-up)
- 1× Potenciometr 10kΩ
- Dráty

**Zapojení:**
```
LED Red   → Pin 11 → Resistor → GND
LED Yellow→ Pin 12 → Resistor → GND
LED Green → Pin 13 → Resistor → GND

Button → Pin 2 (s pull-up na 5V)
Potentiometer → A0
```

**"Jako stavění LEGO - krok po kroku!"**

#### Software - live coding (20 min)
**David píše kód live, vysvětluje:**

```cpp
// === SETUP ===
const int ledPins[] = {11, 12, 13};
const int buttonPin = 2;
const int potPin = A0;

int mode = 1;  // Aktuální mód
int lastButtonState = HIGH;

void setup() {
  for(int i = 0; i < 3; i++) {
    pinMode(ledPins[i], OUTPUT);
  }
  pinMode(buttonPin, INPUT_PULLUP);
  Serial.begin(9600);
}

// === HLAVNÍ SMYČKA ===
void loop() {
  // Čtení tlačítka
  int buttonState = digitalRead(buttonPin);
  
  if(buttonState == LOW && lastButtonState == HIGH) {
    mode++;
    if(mode > 3) mode = 1;
    Serial.print("Mód: ");
    Serial.println(mode);
    delay(200);  // Debounce
  }
  lastButtonState = buttonState;
  
  // Čtení potenciometru pro rychlost
  int speed = analogRead(potPin);
  int delayTime = map(speed, 0, 1023, 50, 1000);
  
  // Spuštění módu
  switch(mode) {
    case 1: modeTrafficLight(delayTime); break;
    case 2: modeAllBlink(delayTime); break;
    case 3: modeRandom(delayTime); break;
  }
}

// === MÓDY ===
void modeTrafficLight(int del) {
  for(int i = 0; i < 3; i++) {
    digitalWrite(ledPins[i], HIGH);
    delay(del);
    digitalWrite(ledPins[i], LOW);
  }
}

void modeAllBlink(int del) {
  for(int i = 0; i < 3; i++) {
    digitalWrite(ledPins[i], HIGH);
  }
  delay(del);
  for(int i = 0; i < 3; i++) {
    digitalWrite(ledPins[i], LOW);
  }
  delay(del);
}

void modeRandom(int del) {
  int randomLED = random(0, 3);
  digitalWrite(ledPins[randomLED], HIGH);
  delay(del);
  digitalWrite(ledPins[randomLED], LOW);
}
```

**Průběžné testování:**
- Po každé funkci → "Start Simulation" → test
- "Funguje mód 1? ✅"
- "Přepíná tlačítko? ✅"
- "Rychlost se mění? ✅"

#### Testing a demo (5 min)
**COOL MOMENT:** Kompletní funkční projekt!

**David demonstruje:**
- Zmáčkne tlačítko → mód 2 → všechny blikají
- Točí potenciometr → rychleji/pomaleji
- Zmáčkne znovu → mód 3 → náhodné
- "Hotovo! Funkční interaktivní zařízení!"

### 👥 ZAPOJENÍ
- Děti navrhují 4. mód → David přidá live!
- "Rychleji nebo pomaleji?" → děti řídí
- "Jakou barvu první?" → design decisions
- Debuging společně pokud něco nefunguje

### 💻 CO BY DĚTI MOHLY DĚLAT
- Replicate projekt v Tinkercad
- Přidat vlastní 4. a 5. mód
- Přidat bzučák (audio feedback)
- Přidat LCD display (zobrazení módu)
- Experimentovat s timing a vzory

---

## Shrnutí bloku 2

### Co děti viděly:
✅ Tinkercad Circuits hands-on workflow
✅ Breadboard a propojování
✅ První funkční obvody (LED + button)
✅ Série vs. paralelní zapojení
✅ Tlačítka, spínače a logika
✅ Potenciometr a analogové vstupy
✅ RGB LED control
✅ Kompletní projekt od nuly po hotovo!

### Key takeaways:
- **Tinkercad = bezpečný playground** pro experimenty
- **Breadboard = chytré propojení** bez pájení
- **Serie vs Parallel = závislost vs nezávislost**
- **Digital vs Analog = ON/OFF vs plynulé hodnoty**
- **PWM = iluze dimming** pomocí rychlého blikání
- **Od simple k complex** - každý projekt je jen kombinace základů!

### Připraveno pro:
- Další blok: Programování s Arduino (proměnné, smyčky, podmínky)
- Práce se senzory (světlo, teplota, vzdálenost)
- Složitější projekty (roboti, alarmy, weatherstanice)

---

## Poznámky pro Davida

### Tech setup:
- **Tinkercad account ready** a přihlášený
- **Projektor/share screen** - všichni musí vidět components panel
- **Backup projekty** - připravené obvody pokud live build selže
- **Internet connection** - Tinkercad je online only

### Presentation tips:
- **Mluv co děláš:** "Teď beru LED, zapojuji do řady 5..."
- **Test často:** Každých 5-10 min "Start Simulation"
- **Celebrate errors:** "Aha! Chyba! Jak to opravím?"
- **Speed:** Stavěj POMALU - děti musí stíhat sledovat

### Common issues:
- **Obvod nefunguje:** Zkontroluj polaritu LED, spojení na breadboard
- **Tinkercad laguje:** Refresh page, nebo přejdi na backup projekt
- **Děti se nudí:** Dej jim rozhodnout (barva LED, rychlost, mód)
- **Čas dochází:** Měj prepared projekt ready to show

### Engagement tricks:
- Nech děti hlasovat o decisions
- "Co se stane když..." predictions
- Real-world examples ("Kde doma máte potenciometr?")
- Gaming analogies ("Jako health bar, jako mana bar")

### Energy management:
- Hodina 6-7: Základy (může být slower)
- Hodina 8-9: Interactive (tlačítka/poty = fun)
- Hodina 10: Projekt (climax! highest energy)

