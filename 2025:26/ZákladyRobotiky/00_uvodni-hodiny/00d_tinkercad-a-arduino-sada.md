# 00d: Arduino Uno v praxi – základní projekty (říjen)

## Cíle hodiny
- Fyzicky si osahat Arduino Uno a základní komponenty.
- Ukázat základní zapojení a skripty v praxi.
- Pochopit vztah mezi kódem a hardwarem.
- Naučit se pracovat s výstupy (LED, LCD, relé, servo, buzzer).
- Naučit se pracovat se vstupy (tlačítko, IR senzor).
- Vytvořit praktické projekty kombinující více komponent.

## Popis hodiny
Hodina je zaměřená na praktické ukázky Arduino projektů od nejjednodušších po pokročilejší. Začínáme s vestavěnou LED (bez zapojení), postupně přidáváme externí komponenty a končíme kombinovanými projekty (např. měřič vzdálenosti s IR senzorem a LCD). 

**Základní projekty (povinné):**
1. Vestavěná LED - první kontakt s Arduinem
2. Externí LED s rezistorem - správné zapojení
3. Semafor - práce s více výstupy
4. Tlačítko - první vstup
5. PWM stmívání - analogový výstup
6. LCD displej - zobrazení textu

**Bonus projekty (podle dostupnosti komponent):**
7. Relé - ovládání vyššího napětí
8. Servomotor - přesné ovládání pohybu
9. Buzzer - generování zvuků
10. Měřič vzdálenosti - kombinace senzoru a LCD

## Materiály
- Arduino Uno + USB kabel
- Breadboard (nepájivé pole)
- LED diody (červená, žlutá, zelená)
- Rezistory 220Ω (červená-červená-hnědá-zlatá)
- Rezistor 10kΩ (pro tlačítko - volitelně)
- Tlačítko (push button)
- LCD displej 16x2 s I2C modulem (volitelně)
- IR senzor vzdálenosti (např. Sharp GP2Y0A21YK0F) - volitelně
- Relé modul (volitelně)
- Baterka 9V + žárovka nebo malý ventilátor (pro relé - volitelně)
- Servomotor (volitelně)
- Piezo buzzer (volitelně)
- Propojovací kabely (jumper wires)
- Arduino IDE nebo online editor

---

## 🎯 PROJEKTY PRO UKÁZKU

### Projekt 1: Vestavěná LED (nejjednodušší - žádné zapojení!)

**Cíl:** Ukázat, že Arduino má vestavěnou LED, která funguje bez jakéhokoliv zapojení.

**Zapojení:** 
- ŽÁDNÉ! Pouze připoj Arduino přes USB k počítači.

**Kód:**
```cpp
// Projekt 1: Blikání vestavěné LED
// LED_BUILTIN je vestavěná LED na Arduinu (obvykle pin 13)

void setup() {
  pinMode(LED_BUILTIN, OUTPUT);  // Nastav pin jako výstup
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);  // Zapni LED
  delay(500);                        // Počkej 500ms (půl sekundy)
  digitalWrite(LED_BUILTIN, LOW);   // Vypni LED
  delay(500);                        // Počkej 500ms
}
```

**Co ukázat:**
- "Vidíte tu malou LED na desce? Ta je připojená na pin 13."
- "Stačí nahrát kód a LED začne blikat."
- "delay(500) znamená počkat půl sekundy."

---

### Projekt 2: Externí LED s rezistorem

**Cíl:** Ukázat správné zapojení LED s ochranným rezistorem.

**Zapojení:**
```
Arduino Pin 13 → Rezistor 220Ω → LED (dlouhá nožička = anoda +) → GND
```

**Schéma:**
- Pin 13 → jeden konec rezistoru
- Druhý konec rezistoru → dlouhá nožička LED (anoda, +)
- Krátká nožička LED (katoda, -) → GND

**Kód:**
```cpp
// Projekt 2: Externí LED s rezistorem
// Pin 13 → Rezistor 220Ω → LED → GND

void setup() {
  pinMode(13, OUTPUT);  // Pin 13 jako výstup
}

void loop() {
  digitalWrite(13, HIGH);  // Zapni LED
  delay(1000);             // Počkej 1 sekundu
  digitalWrite(13, LOW);   // Vypni LED
  delay(1000);             // Počkej 1 sekundu
}
```

**Co ukázat:**
- "Proč potřebujeme rezistor? Bez něj by LED shořela!"
- "Dlouhá nožička = plus, krátká = mínus (GND)"
- "220Ω je standardní hodnota pro LED s Arduinem"

---

### Projekt 3: Semafor (3 LED)

**Cíl:** Ukázat práci s více výstupy najednou.

**Zapojení:**
```
Arduino Pin 13 → Rezistor 220Ω → Červená LED → GND
Arduino Pin 12 → Rezistor 220Ω → Žlutá LED → GND
Arduino Pin 11 → Rezistor 220Ω → Zelená LED → GND
```

**Kód:**
```cpp
// Projekt 3: Semafor (3 LED)
// Pin 13 = červená, Pin 12 = žlutá, Pin 11 = zelená

void setup() {
  pinMode(13, OUTPUT);  // Červená
  pinMode(12, OUTPUT);  // Žlutá
  pinMode(11, OUTPUT);  // Zelená
}

void loop() {
  // Červená svítí
  digitalWrite(13, HIGH);
  digitalWrite(12, LOW);
  digitalWrite(11, LOW);
  delay(3000);  // 3 sekundy
  
  // Žlutá svítí
  digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
  digitalWrite(11, LOW);
  delay(1000);  // 1 sekunda
  
  // Zelená svítí
  digitalWrite(13, LOW);
  digitalWrite(12, LOW);
  digitalWrite(11, HIGH);
  delay(3000);  // 3 sekundy
  
  // Žlutá svítí (před červenou)
  digitalWrite(13, LOW);
  digitalWrite(12, HIGH);
  digitalWrite(11, LOW);
  delay(1000);  // 1 sekunda
}
```

**Co ukázat:**
- "Každá LED má svůj vlastní pin"
- "Můžeme ovládat více věcí najednou"
- "Sekvence: červená → žlutá → zelená → žlutá → opakovat"

---

### Projekt 4: LED ovládaná tlačítkem

**Cíl:** Ukázat vstup (tlačítko) a výstup (LED).

**Zapojení:**
```
LED:
Arduino Pin 13 → Rezistor 220Ω → LED → GND

Tlačítko:
Arduino Pin 2 → jeden kontakt tlačítka
Druhý kontakt tlačítka → GND
Pin 2 → Rezistor 10kΩ → 5V (pull-up rezistor)
```

**Kód:**
```cpp
// Projekt 4: LED ovládaná tlačítkem
// Pin 13 = LED výstup
// Pin 2 = tlačítko vstup

void setup() {
  pinMode(13, OUTPUT);  // LED jako výstup
  pinMode(2, INPUT_PULLUP);  // Tlačítko jako vstup s pull-up rezistorem
}

void loop() {
  // INPUT_PULLUP znamená, že když není stisknuto = HIGH
  // Když je stisknuto = LOW (spojeno s GND)
  
  if (digitalRead(2) == LOW) {  // Tlačítko stisknuto
    digitalWrite(13, HIGH);     // Zapni LED
  } else {                      // Tlačítko není stisknuto
    digitalWrite(13, LOW);      // Vypni LED
  }
}
```

**Co ukázat:**
- "INPUT_PULLUP = Arduino má vestavěný rezistor"
- "Když stisknu tlačítko, spojím pin s GND = LOW"
- "Když pustím, pin je přes rezistor na 5V = HIGH"

---

### Projekt 5: Blikání s různou rychlostí (PWM)

**Cíl:** Ukázat PWM (pulse width modulation) pro stmívání LED.

**Zapojení:**
```
Arduino Pin 9 → Rezistor 220Ω → LED → GND
(Pin 9 má PWM - označené ~ na desce)
```

**Kód:**
```cpp
// Projekt 5: Stmívání LED pomocí PWM
// Pin 9 má PWM (označen ~ na desce)
// analogWrite() používá hodnoty 0-255

void setup() {
  pinMode(9, OUTPUT);  // Pin 9 jako výstup (PWM)
}

void loop() {
  // Postupné rozsvícení (0 = vypnuto, 255 = plný jas)
  for (int jas = 0; jas <= 255; jas++) {
    analogWrite(9, jas);
    delay(10);  // Malé zpoždění pro plynulý efekt
  }
  
  // Postupné zhasnutí
  for (int jas = 255; jas >= 0; jas--) {
    analogWrite(9, jas);
    delay(10);
  }
}
```

**Co ukázat:**
- "PWM = rychlé zapínání a vypínání, které vytváří efekt stmívání"
- "analogWrite() používá hodnoty 0-255"
- "Piny s ~ mají PWM schopnost"

---

### Projekt 6: LCD displej (16x2 s I2C modulem)

**Cíl:** Ukázat práci s LCD displejem pro zobrazení textu.

**Zapojení:**
```
LCD s I2C modulem:
- VCC → Arduino 5V
- GND → Arduino GND
- SDA → Arduino Pin A4 (SDA)
- SCL → Arduino Pin A5 (SCL)
```

**Poznámka:** I2C modul zjednodušuje zapojení z 12 pinů na pouze 4 kabely!

**Kód:**
```cpp
// Projekt 6: LCD displej s I2C modulem
// Potřebuje knihovnu LiquidCrystal_I2C
// V Arduino IDE: Sketch → Include Library → Manage Libraries → vyhledat "LiquidCrystal I2C"

#include <LiquidCrystal_I2C.h>

// Vytvoříme objekt pro LCD (adresa I2C je obvykle 0x27 nebo 0x3F)
// Parametry: (adresa, počet sloupců, počet řádků)
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();           // Inicializace LCD
  lcd.backlight();      // Zapnutí podsvícení
  
  // Zobrazení úvodní zprávy
  lcd.setCursor(0, 0);  // Pozice: sloupec 0, řádek 0 (první řádek)
  lcd.print("Ahoj Arduino!");  // Text na prvním řádku
  
  lcd.setCursor(0, 1);  // Pozice: sloupec 0, řádek 1 (druhý řádek)
  lcd.print("LCD funguje!");   // Text na druhém řádku
}

void loop() {
  // Počítadlo sekund
  static unsigned long posledniCas = 0;
  static int sekundy = 0;
  
  if (millis() - posledniCas >= 1000) {  // Každou sekundu
    sekundy++;
    posledniCas = millis();
    
    // Vymazat druhý řádek a zobrazit nový čas
    lcd.setCursor(0, 1);
    lcd.print("Cas: ");
    lcd.print(sekundy);
    lcd.print(" sekund  ");  // Mezery pro vymazání zbytku řádku
  }
}
```

**Alternativní jednodušší verze (bez počítadla):**
```cpp
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();
  
  lcd.setCursor(0, 0);
  lcd.print("Robotika je");
  lcd.setCursor(0, 1);
  lcd.print("super!");
}

void loop() {
  // Text se zobrazí a zůstane
}
```

**Co ukázat:**
- "I2C = komunikace přes pouze 2 piny (SDA a SCL)"
- "LCD má 16 sloupců a 2 řádky = 32 znaků celkem"
- "setCursor() určuje, kde začne text"
- "První řádek = 0, druhý řádek = 1"
- "Pokud I2C adresa není 0x27, zkus 0x3F"

**Tip pro instalaci knihovny:**
- Arduino IDE → Sketch → Include Library → Manage Libraries
- Vyhledat: "LiquidCrystal I2C" (autor: Frank de Brabander)
- Nainstalovat knihovnu

---

### Projekt 7: Relé s baterkou/žárovkou

**Cíl:** Ukázat, jak Arduino může ovládat zařízení s vyšším napětím pomocí relé.

**Zapojení:**
```
Arduino strana:
- Arduino Pin 7 → IN pin relé modulu
- Arduino GND → GND relé modulu
- Arduino 5V → VCC relé modulu

Vysokonapěťová strana (IZOLOVANÁ od Arduina!):
- Baterka 9V (+) → jeden kontakt žárovky/spotřebiče
- Druhý kontakt žárovky → COM (Common) na relé
- NO (Normally Open) na relé → Baterka 9V (-)
```

**⚠️ DŮLEŽITÉ BEZPEČNOSTNÍ UPOZORNĚNÍ:**
- Relé modul **IZOLUJE** Arduino od vyššího napětí
- Používej pouze **baterky** (9V, AA baterky) - NIKDY síťové napětí!
- Před zapojením vždy odpoj USB z Arduina
- Kontroluj polaritu baterky

**Kód:**
```cpp
// Projekt 7: Relé s baterkou a žárovkou
// Pin 7 ovládá relé, které spíná obvod s baterkou

void setup() {
  pinMode(7, OUTPUT);  // Pin 7 jako výstup pro relé
  digitalWrite(7, LOW); // Na začátku relé vypnuto
}

void loop() {
  digitalWrite(7, HIGH);  // Zapni relé → žárovka svítí
  delay(2000);             // Počkej 2 sekundy
  
  digitalWrite(7, LOW);   // Vypni relé → žárovka zhasne
  delay(2000);             // Počkej 2 sekundy
}
```

**Alternativní verze s tlačítkem:**
```cpp
// Relé ovládané tlačítkem
// Pin 2 = tlačítko, Pin 7 = relé

void setup() {
  pinMode(2, INPUT_PULLUP);  // Tlačítko
  pinMode(7, OUTPUT);        // Relé
}

void loop() {
  if (digitalRead(2) == LOW) {  // Tlačítko stisknuto
    digitalWrite(7, HIGH);      // Zapni relé
  } else {
    digitalWrite(7, LOW);       // Vypni relé
  }
}
```

**Co ukázat:**
- "Relé = elektromagnetický spínač"
- "Arduino ovládá relé malým proudem (5V)"
- "Relé pak může spínat větší napětí (9V baterka)"
- "Relé modul má optočlen = izolace mezi Arduinem a baterkou"
- "COM = společný kontakt, NO = otevřený když relé vypnuto"

**Možné využití:**
- Ovládání žárovky
- Ovládání malého ventilátoru
- Ovládání motoru (s diodou pro ochranu)

---

### Projekt 8: Servomotor (pohyb!)

**Cíl:** Ukázat přesné ovládání pohybu pomocí servomotoru.

**Zapojení:**
```
Servomotor:
- Červený kabel (VCC) → Arduino 5V (nebo externí napájení)
- Černý/Hnědý kabel (GND) → Arduino GND
- Žlutý/Bílý/Orange kabel (Signal) → Arduino Pin 9
```

**⚠️ POZNÁMKA:** Pro větší servomotory použij externí napájení (např. baterka 6V), protože Arduino nemusí mít dostatek proudu.

**Kód:**
```cpp
// Projekt 8: Servomotor
// Potřebuje knihovnu Servo
// Sketch → Include Library → Servo (vestavěná knihovna)

#include <Servo.h>

Servo mojeServo;  // Vytvoříme objekt serva

void setup() {
  mojeServo.attach(9);  // Servo připojeno na pin 9
}

void loop() {
  // Otočit servo na 0° (vlevo)
  mojeServo.write(0);
  delay(1000);
  
  // Otočit servo na 90° (uprostřed)
  mojeServo.write(90);
  delay(1000);
  
  // Otočit servo na 180° (vpravo)
  mojeServo.write(180);
  delay(1000);
  
  // Vrátit zpět na 90°
  mojeServo.write(90);
  delay(1000);
}
```

**Alternativní verze - plynulý pohyb:**
```cpp
#include <Servo.h>

Servo mojeServo;

void setup() {
  mojeServo.attach(9);
}

void loop() {
  // Plynulý pohyb z 0° na 180°
  for (int uhel = 0; uhel <= 180; uhel++) {
    mojeServo.write(uhel);
    delay(15);  // Malé zpoždění pro plynulý pohyb
  }
  
  // Plynulý pohyb zpět z 180° na 0°
  for (int uhel = 180; uhel >= 0; uhel--) {
    mojeServo.write(uhel);
    delay(15);
  }
}
```

**Co ukázat:**
- "Servomotor = motor s přesným ovládáním úhlu"
- "Rozsah je obvykle 0-180°"
- "PWM signál řídí pozici serva"
- "Použití: robotické ruce, kamery, dveře, atd."

---

### Projekt 9: Buzzer (zvuky!)

**Cíl:** Ukázat generování zvuků pomocí piezo buzzeru.

**Zapojení:**
```
Buzzer:
- Pozitivní pin (+) → Arduino Pin 8
- Negativní pin (-) → Arduino GND
```

**Kód - jednoduché pípání:**
```cpp
// Projekt 9: Buzzer - jednoduché pípání
// Pin 8 = buzzer

void setup() {
  pinMode(8, OUTPUT);
}

void loop() {
  tone(8, 1000);    // Zapni tón 1000 Hz na pinu 8
  delay(500);       // Počkej 500ms
  noTone(8);        // Vypni tón
  delay(500);       // Počkej 500ms
}
```

**Kód - melodie (příklad):**
```cpp
// Projekt 9: Buzzer - jednoduchá melodie
// Pin 8 = buzzer

// Frekvence tónů (v Hz)
#define NOTE_C4  262
#define NOTE_D4  294
#define NOTE_E4  330
#define NOTE_F4  349
#define NOTE_G4  392
#define NOTE_A4  440
#define NOTE_B4  494
#define NOTE_C5  523

void setup() {
  pinMode(8, OUTPUT);
}

void loop() {
  // Hraj tóny postupně
  tone(8, NOTE_C4);
  delay(300);
  noTone(8);
  delay(50);
  
  tone(8, NOTE_E4);
  delay(300);
  noTone(8);
  delay(50);
  
  tone(8, NOTE_G4);
  delay(300);
  noTone(8);
  delay(50);
  
  tone(8, NOTE_C5);
  delay(500);
  noTone(8);
  
  delay(1000);  // Pauza před opakováním
}
```

**Kód - siréna (stoupající a klesající tón):**
```cpp
// Projekt 9: Buzzer - siréna efekt
// Pin 8 = buzzer

void setup() {
  pinMode(8, OUTPUT);
}

void loop() {
  // Stoupající tón (siréna nahoru)
  for (int frekvence = 200; frekvence <= 2000; frekvence += 10) {
    tone(8, frekvence);
    delay(5);
  }
  
  // Klesající tón (siréna dolů)
  for (int frekvence = 2000; frekvence >= 200; frekvence -= 10) {
    tone(8, frekvence);
    delay(5);
  }
  
  noTone(8);
  delay(500);
}
```

**Co ukázat:**
- "Buzzer = piezo reproduktor pro jednoduché zvuky"
- "tone() generuje tón na určité frekvenci"
- "Frekvence v Hz určuje výšku tónu"
- "noTone() vypne zvuk"
- "Můžeme vytvářet melodie, sirény, alarmy"

---

### Projekt 10: Měřič vzdálenosti (IR senzor + LCD)

**Cíl:** Vytvořit praktický měřič vzdálenosti kombinující IR senzor a LCD displej.

**Zapojení:**
```
IR senzor vzdálenosti (např. Sharp GP2Y0A21YK0F):
- VCC → Arduino 5V
- GND → Arduino GND
- OUT → Arduino Pin A0 (analogový vstup)

LCD displej s I2C modulem:
- VCC → Arduino 5V
- GND → Arduino GND
- SDA → Arduino Pin A4
- SCL → Arduino Pin A5
```

**Kód:**
```cpp
// Projekt 10: Měřič vzdálenosti s IR senzorem a LCD
// Kombinuje analogový senzor (A0) s LCD displejem

#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);  // LCD na I2C adrese 0x27

const int irSensorPin = A0;  // IR senzor na analogovém pinu A0

void setup() {
  // Inicializace LCD
  lcd.init();
  lcd.backlight();
  
  // Úvodní zpráva
  lcd.setCursor(0, 0);
  lcd.print("Merič vzdalenosti");
  delay(2000);
  lcd.clear();
}

void loop() {
  // Přečti hodnotu ze senzoru (0-1023)
  int sensorValue = analogRead(irSensorPin);
  
  // Převod na napětí (0-5V)
  float voltage = sensorValue * (5.0 / 1023.0);
  
  // Převod na vzdálenost v cm
  // Pro Sharp GP2Y0A21YK0F: vzdálenost = (6787 / (napětí - 3)) - 4
  // Pro jiné senzory může být vzorec jiný - zkontroluj datasheet!
  float vzdalenost = 0;
  
  if (voltage > 0.4) {  // Minimální spolehlivá hodnota
    vzdalenost = (6787.0 / (voltage - 3.0)) - 4.0;
    
    // Omezení rozsahu (senzor měří cca 10-80 cm)
    if (vzdalenost < 10) vzdalenost = 10;
    if (vzdalenost > 80) vzdalenost = 80;
  } else {
    vzdalenost = 999;  // Příliš daleko nebo mimo rozsah
  }
  
  // Zobrazení na LCD
  lcd.setCursor(0, 0);
  lcd.print("Vzdalenost:");
  
  lcd.setCursor(0, 1);
  if (vzdalenost == 999) {
    lcd.print("Mimo rozsah  ");
  } else {
    lcd.print(vzdalenost, 1);  // Zobraz s 1 desetinným místem
    lcd.print(" cm      ");     // Mezery pro vymazání zbytku
  }
  
  delay(100);  // Aktualizace každých 100ms
}
```

**Zjednodušená verze (bez přesného převodu):**
```cpp
// Jednodušší verze - zobrazuje pouze surovou hodnotu a napětí
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
  lcd.init();
  lcd.backlight();
  lcd.setCursor(0, 0);
  lcd.print("IR Sensor:");
}

void loop() {
  int hodnota = analogRead(A0);
  float napeti = hodnota * (5.0 / 1023.0);
  
  lcd.setCursor(0, 1);
  lcd.print("Val: ");
  lcd.print(hodnota);
  lcd.print(" V:");
  lcd.print(napeti, 2);
  lcd.print("V  ");
  
  delay(200);
}
```

**Verze s LED indikací (blízko = červená, daleko = zelená):**
```cpp
// Měřič vzdálenosti s LED indikací
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

const int irSensorPin = A0;
const int ledCervena = 13;  // Červená LED = blízko
const int ledZelena = 12;  // Zelená LED = daleko

void setup() {
  lcd.init();
  lcd.backlight();
  
  pinMode(ledCervena, OUTPUT);
  pinMode(ledZelena, OUTPUT);
  
  lcd.setCursor(0, 0);
  lcd.print("Merič vzdalenosti");
  delay(2000);
  lcd.clear();
}

void loop() {
  int sensorValue = analogRead(irSensorPin);
  float voltage = sensorValue * (5.0 / 1023.0);
  float vzdalenost = 0;
  
  if (voltage > 0.4) {
    vzdalenost = (6787.0 / (voltage - 3.0)) - 4.0;
    if (vzdalenost < 10) vzdalenost = 10;
    if (vzdalenost > 80) vzdalenost = 80;
  } else {
    vzdalenost = 999;
  }
  
  // Zobrazení na LCD
  lcd.setCursor(0, 0);
  lcd.print("Vzdalenost:");
  lcd.setCursor(0, 1);
  
  if (vzdalenost == 999) {
    lcd.print("Mimo rozsah  ");
    digitalWrite(ledCervena, LOW);
    digitalWrite(ledZelena, LOW);
  } else {
    lcd.print(vzdalenost, 1);
    lcd.print(" cm      ");
    
    // LED indikace
    if (vzdalenost < 30) {
      // Blízko = červená
      digitalWrite(ledCervena, HIGH);
      digitalWrite(ledZelena, LOW);
    } else {
      // Daleko = zelená
      digitalWrite(ledCervena, LOW);
      digitalWrite(ledZelena, HIGH);
    }
  }
  
  delay(100);
}
```

**Co ukázat:**
- "IR senzor = infračervený senzor vzdálenosti"
- "analogRead() čte hodnotu 0-1023 (10-bitový převodník)"
- "Převod na napětí: hodnota × (5V / 1023)"
- "Vzorec pro vzdálenost závisí na typu senzoru - zkontroluj datasheet!"
- "Kombinujeme senzor (vstup) s LCD (výstup) = praktický projekt"
- "Měření probíhá kontinuálně každých 100ms"

**Tipy:**
- Různé IR senzory mají různé vzorce převodu - zkontroluj datasheet svého senzoru
- Pro kalibraci: změř známou vzdálenost a uprav vzorec podle potřeby
- Senzor může být ovlivněn světlem a povrchem předmětu
- Pro přesnější měření použij ultrazvukový senzor HC-SR04 (ale ten není IR)

**Možná vylepšení:**
- Přidat buzzer, který pípá když je objekt blízko
- Zobrazovat graf na LCD (pokud má větší rozlišení)
- Kombinovat s servomotorem pro automatické sledování objektu

---

## 📋 PRŮBĚH HODINY (60–90 min)

**Poznámka:** Časování je flexibilní podle dostupnosti komponent. Základní projekty (1-6) zaberou cca 45-50 minut. Bonus projekty (7-10) lze přidat podle času a zájmu dětí.

### 1. Úvod a bezpečnost (5 min)
- **Bezpečnostní zásady:**
  - Nikdy nepřipojuj napětí vyšší než 5V přímo na piny!
  - Vždy používej rezistor s LED!
  - Před zapojením odpoj USB!
  - Kontroluj polaritu LED (dlouhá nožička = +)

### 2. Projekt 1: Vestavěná LED (5 min)
- Ukázat Arduino, najít vestavěnou LED
- Nahrát první kód
- Ukázat, že funguje bez zapojení

### 3. Projekt 2: Externí LED (10 min)
- Ukázat správné zapojení na breadboardu
- Vysvětlit proč rezistor
- Nahrát kód a ukázat blikání

### 4. Projekt 3: Semafor (15 min)
- Zapojit 3 LED
- Nahrát kód semaforu
- Ukázat sekvenční ovládání

### 5. Projekt 4: Tlačítko (10 min)
- Přidat tlačítko do obvodu
- Vysvětlit INPUT_PULLUP
- Ukázat interaktivní ovládání

### 6. Projekt 5: PWM stmívání (5 min)
- Ukázat PWM efekt
- Vysvětlit rozdíl mezi digitalWrite() a analogWrite()

### 7. Projekt 6: LCD displej (10 min)
- Zapojit LCD s I2C modulem (4 kabely)
- Nainstalovat knihovnu LiquidCrystal_I2C
- Nahrát kód a ukázat zobrazení textu
- Vysvětlit I2C komunikaci

### 8. Bonus projekty (podle času a dostupnosti):
- **Projekt 7: Relé** - pokud máš relé modul a baterku (10 min)
- **Projekt 8: Servomotor** - pokud máš servo (10 min)
- **Projekt 9: Buzzer** - pokud máš buzzer (5 min)
- **Projekt 10: Měřič vzdálenosti** - pokud máš IR senzor + LCD (15 min)
  - Kombinuje senzor (vstup) s LCD (výstup)
  - Praktický projekt, který děti zaujme

### 9. Shrnutí a otázky (5–10 min)
- Co jsme se naučili?
- Jaký projekt by děti chtěly zkusit příště?
- Který projekt se jim líbil nejvíc?

---

## 🎓 KLÍČOVÉ POJMY PRO DĚTI

- **Pin:** Kontakt na Arduinu, kam připojujeme komponenty
- **INPUT/OUTPUT:** Vstup (čteme hodnotu) vs. výstup (posíláme signál)
- **HIGH/LOW:** Logická 1 (5V) vs. logická 0 (0V/GND)
- **Rezistor:** Chrání LED před přepálením
- **GND (Ground):** Mínus, společný vodič
- **PWM:** Rychlé zapínání/vypínání pro stmívání
- **I2C:** Komunikační protokol přes 2 piny (SDA, SCL) - zjednodušuje zapojení
- **LCD:** Tekutokrystalový displej pro zobrazení textu
- **Relé:** Elektromagnetický spínač - umožňuje ovládat vyšší napětí pomocí Arduina
- **Servomotor:** Motor s přesným ovládáním úhlu (obvykle 0-180°)
- **Buzzer:** Piezo reproduktor pro generování zvuků a melodií
- **IR senzor:** Infračervený senzor vzdálenosti - měří vzdálenost pomocí odraženého světla
- **Analogový vstup:** Čte hodnoty 0-1023 (10-bitový převodník) - pro senzory s plynulou změnou

---

## 🏠 DOMÁCÍ ÚKOL (dobrovolný)

- Vymyslet vlastní kombinaci LED efektů
- Nakreslit schéma zapojení pro vlastní nápad
- Zkusit změnit rychlost blikání nebo barvy v semaforu
- Pokud máš Arduino doma: zkusit jeden z bonus projektů (servo, buzzer, relé)
- Vymyslet vlastní projekt kombinující více komponent (např. servo + buzzer, LED + tlačítko + LCD)

---

## 📝 POZNÁMKY PRO DAVIDA

### Příprava před hodinou:
- [ ] Otestovat všechny skripty předem
- [ ] Připravit zapojení na breadboardu předem (nebo ukázat živě)
- [ ] Mít připravené Arduino IDE nebo online editor
- [ ] Připravit několik Arduino sad pro případ, že by děti chtěly zkusit
- [ ] **Pro IR senzor:** Zkontrolovat typ senzoru a případně upravit vzorec převodu vzdálenosti v kódu
- [ ] **Pro IR senzor:** Otestovat kalibraci - změř známou vzdálenost a ověř přesnost

### Během hodiny:
- **Ukazuj kód a hardware současně:** "Tady v kódu je pin 13, a tady na desce je pin 13"
- **Vysvětluj proč:** Nejen jak, ale i proč potřebujeme rezistor, proč GND, atd.
- **Nech děti tipovat:** "Co myslíte, co se stane když změním delay na 100?"

### Bezpečnost:
- Vždy zdůrazni bezpečnostní zásady na začátku
- Ukaž správné a špatné zapojení (bez rezistoru = špatně!)
- **Při práci s relé:** Vždy používej pouze baterky, NIKDY síťové napětí!
- Před zapojením relé vždy odpoj USB z Arduina

---

## ✅ CHECKLIST DOBŘE PROVEDENÉ HODINY

- [ ] Děti viděly alespoň základní projekty (1-6) v akci
- [ ] Rozumí základnímu zapojení LED s rezistorem
- [ ] Vidí souvislost mezi kódem a hardwarem
- [ ] Rozumí rozdílu mezi vstupem (tlačítko, senzor) a výstupem (LED, LCD)
- [ ] Viděly alespoň jeden bonus projekt (pokud byly komponenty k dispozici)
- [ ] Kladou otázky o další možnosti a kombinace
- [ ] Chtěly by to zkusit samy nebo mají nápady na vlastní projekty

