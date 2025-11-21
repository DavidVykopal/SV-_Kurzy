# Blok 5: Senzory (16–20)

## Hodina 16: Teplota – simulace senzoru

### Cíle hodiny
- Pochopit princip teplotních senzorů
- Naučit se číst analogové hodnoty v Arduino
- Vytvořit teplotní monitor s LCD displejem

### Materiály
- Tinkercad Circuits s Arduino
- Teplotní senzor TMP36
- LCD displej 16×2
- LED pro signalizaci

### Průběh hodiny (45 min)

#### 1. Princip teplotních senzorů (15 min)
**Jak funguje teplotní senzor?**
- **TMP36:** Analogový senzor, výstup přímo úměrný teplotě
- **Výstup:** 0°C = 0.5V, každý °C = +10mV
- **Rozsah:** -40°C až +125°C
- **Výhody:** Přesný, levný, nevyžaduje kalibraci

**Praktické použití:**
- Meteostanice
- Termostat
- Monitoring serveru
- Chytré domy

**Připojení TMP36:**
```
VCC → 5V (Arduino)
GND → GND (Arduino)  
OUT → A0 (analogový vstup)
```

#### 2. Čtení analogových hodnot (15 min)
**Analogové vs. digitální:**
- **Digitální:** pouze 0 nebo 1 (5V nebo 0V)
- **Analogový:** plynulé hodnoty (0-5V)
- **ADC (Analog-to-Digital Converter):** Převádí napětí na číslo

**Python funkce pro Arduino:**
```python
hodnota = arduino.analog_read(arduino.A0)  # Vrací 0-1023
```

**Převod na napětí:**
```python
napeti = (hodnota * 5.0) / 1024.0
```

**Převod na teplotu (TMP36):**
```python
teplota = (napeti - 0.5) * 100.0
```

#### 3. Praktický projekt - Teplotní monitor (15 min)

**Obvod:**
- Arduino + TMP36 senzor + LCD displej + 2× LED

**Kompletní Python kód:**
```python
import arduino
import time

# LCD připojení (RS, E, D4, D5, D6, D7) - simulace v Tinkercadu
# V reálném projektu by se použila knihovna pro LCD

TEMP_PIN = arduino.A0
LED_COLD = 8    # Modrá LED
LED_HOT = 9     # Červená LED

def setup():
    # LCD inicializace (simulováno printy)
    arduino.pin_mode(LED_COLD, arduino.OUTPUT)
    arduino.pin_mode(LED_HOT, arduino.OUTPUT)
    
    print("Teplotni mereni")
    time.sleep(2)
    print("System ready")

def loop():
    # Čtení teploty
    analog_value = arduino.analog_read(TEMP_PIN)
    voltage = (analog_value * 5.0) / 1024.0
    temperature = (voltage - 0.5) * 100.0
    
    # Zobrazení na "LCD" (print simuluje LCD displej)
    print(f"Teplota: {temperature:.1f}C")
    
    if temperature < 20:
        print("Je zima!")
        arduino.digital_write(LED_COLD, arduino.HIGH)
        arduino.digital_write(LED_HOT, arduino.LOW)
    elif temperature > 25:
        print("Je teplo!")
        arduino.digital_write(LED_COLD, arduino.LOW)
        arduino.digital_write(LED_HOT, arduino.HIGH)
    else:
        print("Prijemne")
        arduino.digital_write(LED_COLD, arduino.LOW)
        arduino.digital_write(LED_HOT, arduino.LOW)
    
    # Debug informace
    print(f"ADC: {analog_value}, Napeti: {voltage:.2f}V, Teplota: {temperature:.1f}C")
    
    time.sleep(1)

# Spuštění programu
setup()
while True:
    loop()
```

### Domácí úkol
Upravit kód tak, aby LED blikaly při extrémních teplotách (< 15°C nebo > 30°C).

---

## Hodina 17: Světelný senzor – simulace

### Cíle hodiny
- Pochopit fungování fotoresistoru (LDR)
- Vytvořit automatické osvětlení
- Naučit se kalibrovat senzor

### Materiály
- Tinkercad Circuits s Arduino
- Fotoresistor (LDR)
- Rezistor 10kΩ (pull-down)
- LED pro osvětlení
- Serial Monitor pro ladění

### Průběh hodiny (45 min)

#### 1. Princip světelného senzoru (15 min)
**Fotoresistor (LDR - Light Dependent Resistor):**
- **Princip:** Odpor se mění podle intenzity světla
- **Světlo:** Malý odpor (~100Ω)
- **Tma:** Velký odpor (~10MΩ)
- **Citlivost:** Viditelné světlo, pomalá reakce

**Zapojení děliče napětí:**
```
5V → LDR → A0 → Rezistor 10kΩ → GND
```

**Proč potřebujeme rezistor?**
- Vytvoří dělič napětí
- Bez něj bychom neměřili napětí, ale odpor

#### 2. Kalibrace a čtení hodnot (15 min)

**Základní čtení:**
```python
light_value = arduino.analog_read(arduino.A0)  # 0-1023
```

**Kalibrace - zjištění rozsahu:**
```python
import arduino
import time

def setup():
    print("Kalibrace svetelneho senzoru:")
    print("Nejprv zakryj senzor, pak jej osvet...")

def loop():
    light_value = arduino.analog_read(arduino.A0)
    print(light_value)
    time.sleep(0.5)

# Spuštění
setup()
while True:
    loop()
```

**Typické hodnoty:**
- Přímé světlo: 800-1023
- Pokojové osvětlení: 300-600  
- Tma: 0-200

#### 3. Praktický projekt - Automatické osvětlení (15 min)

**Zadání:** LED se automaticky rozsvítí při snížení osvětlení

```python
import arduino
import time

LIGHT_SENSOR = arduino.A0
LED_PIN = 9
BUTTON_PIN = 2

# Kalibrace - je třeba změřit!
LIGHT_THRESHOLD = 400
HYSTERESIS = 50        # Proti blikání

light_level = 0
led_state = False
manual_override = False
last_button_state = True

def map_value(value, from_low, from_high, to_low, to_high):
    """Mapuje hodnotu z jednoho rozsahu na druhý"""
    return int((value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low)

def constrain(value, min_val, max_val):
    """Omezí hodnotu na daný rozsah"""
    return max(min_val, min(max_val, value))

def setup():
    arduino.pin_mode(LED_PIN, arduino.OUTPUT)
    arduino.pin_mode(BUTTON_PIN, arduino.INPUT_PULLUP)
    
    print("Automaticke osvetleni")
    print("Tlacitko pro rucni ovladani")

def loop():
    global light_level, led_state, manual_override, last_button_state
    
    light_level = arduino.analog_read(LIGHT_SENSOR)
    current_button_state = arduino.digital_read(BUTTON_PIN) == arduino.LOW
    
    # Detekce stisku tlačítka (změna ze False na True)
    if current_button_state and not last_button_state:
        manual_override = not manual_override
        print("Rucni rezim" if manual_override else "Automaticky rezim")
        time.sleep(0.3)  # Debounce
    
    last_button_state = current_button_state
    
    if not manual_override:
        # Automatický režim s hysterezí
        if light_level < (LIGHT_THRESHOLD - HYSTERESIS) and not led_state:
            led_state = True
            print("LED zapnuta - je tma")
        elif light_level > (LIGHT_THRESHOLD + HYSTERESIS) and led_state:
            led_state = False
            print("LED vypnuta - je svetlo")
    else:
        # Manuální režim - tlačítko ovládá LED
        led_state = current_button_state
    
    # Nastavení jasu podle osvětlení
    if led_state:
        brightness = map_value(light_level, 0, 1023, 255, 50)
        brightness = constrain(brightness, 50, 255)
        arduino.analog_write(LED_PIN, brightness)
    else:
        arduino.analog_write(LED_PIN, 0)
    
    # Debug informace
    led_status = "ON" if led_state else "OFF"
    mode_status = "Rucni" if manual_override else "Auto"
    print(f"Svetlo: {light_level}, LED: {led_status}, Rezim: {mode_status}")
    
    time.sleep(0.2)

# Spuštění programu
setup()
while True:
    loop()
```

### Pokročilé funkce
- **Hystereze:** Zamezení blikání při hraničních hodnotách
- **Map funkce:** Převod rozsahu hodnot
- **Adaptivní jas:** LED svítí silněji v větší tmě

### Domácí úkol
Vytvořit "chytrý detektor úsvitu" - LED bliká když se rozednívá (světlo pomalu stoupá).

---

## Hodina 18: Pohybový senzor – ukázka v Tinkercad

### Cíle hodiny
- Pochopit princip PIR senzoru
- Vytvořit systém detekce pohybu
- Kombinovat senzor s časovačem

### Materiály
- Tinkercad Circuits s Arduino
- PIR senzor (Passive Infrared)
- LED a buzzer pro alarm
- LCD displej pro informace

### Průběh hodiny (45 min)

#### 1. Princip PIR senzoru (15 min)
**PIR (Passive Infrared) senzor:**
- **Detekuje:** Tepelné záření (infrared) od lidí a zvířat
- **Dosah:** 3-7 metrů, úhel ~120°
- **Výstup:** Digitální (HIGH/LOW)
- **Kalibrace:** 10-60 sekund po zapnutí

**Jak funguje:**
- Dva čidla měří infračervené záření
- Rozdíl mezi čidly = pohyb
- **Pasivní:** Nevysílá nic, jen přijímá

**Praktické použití:**
- Bezpečnostní systémy
- Automatické světla
- Úspora energie
- Monitoring domácích mazlíčků

#### 2. Připojení a programování (15 min)

**Zapojení PIR senzoru:**
```
VCC → 5V
GND → GND
OUT → Digital pin 2
```

**Základní Python kód:**
```python
import arduino
import time

PIR_PIN = 2
LED_PIN = 13

def setup():
    arduino.pin_mode(PIR_PIN, arduino.INPUT)
    arduino.pin_mode(LED_PIN, arduino.OUTPUT)
    
    print("PIR senzor - kalibrace 30s")
    time.sleep(30)  # Kalibrace PIR senzoru
    print("PIR pripraven!")

def loop():
    motion = arduino.digital_read(PIR_PIN)
    
    if motion:
        arduino.digital_write(LED_PIN, arduino.HIGH)
        print("POHYB DETEKOVAN!")
    else:
        arduino.digital_write(LED_PIN, arduino.LOW)
    
    time.sleep(0.1)

# Spuštění programu
setup()
while True:
    loop()
```

#### 3. Praktický projekt - Bezpečnostní alarm (15 min)

**Zadání:** Komplexní bezpečnostní systém s časovačem a různými módy

```cpp
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

const int PIR_PIN = 7;
const int BUZZER_PIN = 8;
const int LED_RED = 9;
const int LED_GREEN = 10;
const int BUTTON_ARM = 6;
const int BUTTON_DISARM = 13;

boolean systemArmed = false;
boolean alarmActive = false;
unsigned long motionTime = 0;
unsigned long alarmDelay = 10000;  // 10 sekund prodleva

void setup() {
  pinMode(PIR_PIN, INPUT);
  pinMode(BUZZER_PIN, OUTPUT);
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(BUTTON_ARM, INPUT_PULLUP);
  pinMode(BUTTON_DISARM, INPUT_PULLUP);
  
  lcd.begin(16, 2);
  Serial.begin(9600);
  
  lcd.print("Bezpecnostni");
  lcd.setCursor(0, 1);
  lcd.print("system READY");
  
  digitalWrite(LED_GREEN, HIGH);
  
  // Kalibrace PIR
  delay(30000);
  Serial.println("PIR kalibrovan");
}

void loop() {
  // Ovládání tlačítky
  if (digitalRead(BUTTON_ARM) == LOW) {
    armSystem();
    delay(300);
  }
  
  if (digitalRead(BUTTON_DISARM) == LOW) {
    disarmSystem();
    delay(300);
  }
  
  // Detekce pohybu
  boolean motion = digitalRead(PIR_PIN);
  
  if (systemArmed && motion && !alarmActive) {
    motionDetected();
  }
  
  // Kontrola alarmu
  if (alarmActive && (millis() - motionTime > alarmDelay)) {
    triggerAlarm();
  }
  
  updateDisplay();
  delay(100);
}

void armSystem() {
  systemArmed = true;
  digitalWrite(LED_GREEN, LOW);
  digitalWrite(LED_RED, HIGH);
  
  lcd.clear();
  lcd.print("SYSTEM ARMED");
  Serial.println("System zastaven");
}

void disarmSystem() {
  systemArmed = false;
  alarmActive = false;
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_GREEN, HIGH);
  noTone(BUZZER_PIN);
  
  lcd.clear();
  lcd.print("System DISARMED");
  Serial.println("System odstaven");
}

void motionDetected() {
  motionTime = millis();
  alarmActive = true;
  
  lcd.clear();
  lcd.print("POHYB! Alarm za");
  lcd.setCursor(0, 1);
  lcd.print("10 sekund...");
  
  Serial.println("POHYB DETEKOVAN - Alarm za 10s");
}

void triggerAlarm() {
  // Alarm sound
  tone(BUZZER_PIN, 1000, 500);
  delay(500);
  tone(BUZZER_PIN, 1500, 500);
  delay(500);
  
  Serial.println("!!! ALARM AKTIVNI !!!");
}

void updateDisplay() {
  if (!alarmActive) {
    lcd.setCursor(0, 1);
    lcd.print("Status: ");
    lcd.print(systemArmed ? "ARMED  " : "DISARMED");
  }
}
```

**Funkce systému:**
- **Zastaven/Odstaven:** Tlačítka pro ovládání
- **Časová prodleva:** 10 sekund na opuštění místnosti
- **Vizuální a zvukové signály:** LED + bzučák
- **LCD informace:** Stav systému

### Rozšíření projektu
- Přidání více PIR senzorů (různé místnosti)
- SMS notifikace (GSM modul)
- Webové rozhraní
- Kamera při detekci

### Domácí úkol
Upravit alarm tak, aby po detekci pohybu počítal osoby (každá detekce = +1 osoba).

---

## Hodina 19: Kombinace senzorů

### Cíle hodiny
- Naučit se kombinovat více senzorů současně
- Vytvořit inteligentní rozhodovací logiku
- Pochopit koncepty fuzzy logiky

### Materiály
- Tinkercad Circuits s Arduino
- Kombinace senzorů: TMP36 + LDR + PIR
- LCD displej pro zobrazení stavu
- Více LED pro různé indikace

### Průběh hodiny (45 min)

#### 1. Principy kombinování senzorů (15 min)

**Proč kombinovat senzory?**
- **Vyšší přesnost:** Více informací = lepší rozhodnutí
- **Redundance:** Záložní systém při selhání
- **Komplexní logika:** Kombinace podmínek

**Typy kombinace:**
1. **AND logika:** Všechny podmínky musí být splněny
2. **OR logika:** Stačí jedna splněná podmínka
3. **Prioritní logika:** Jeden senzor má přednost
4. **Fuzzy logika:** Částečné splnění podmínek

**Praktické příklady:**
- **Chytrý termostat:** Teplota + čas + přítomnost osob
- **Bezpečnost auta:** Rychlost + vzdálenost + počasí
- **Chytrý dům:** Světlo + pohyb + čas

#### 2. Praktická implementace (20 min)

**Projekt: Chytrá místnost**
- Teplotní senzor: Komfort
- Světelný senzor: Automatické osvětlení  
- PIR senzor: Přítomnost osob
- Kombinace: Inteligentní ovládání

```cpp
#include <LiquidCrystal.h>

LiquidCrystal lcd(12, 11, 5, 4, 3, 2);

// Senzory
const int TEMP_PIN = A0;      // TMP36
const int LIGHT_PIN = A1;     // LDR
const int PIR_PIN = 7;        // PIR

// Výstupy
const int LED_LIGHT = 3;      // Osvětlení (PWM)
const int LED_HEATING = 8;    // Topení
const int LED_COOLING = 9;    // Chlazení
const int FAN_PIN = 10;       // Ventilátor (PWM)

// Prahové hodnoty
const float TEMP_COLD = 18.0;
const float TEMP_WARM = 25.0;
const int LIGHT_DARK = 300;
const int LIGHT_BRIGHT = 700;

// Stav systému
boolean personPresent = false;
unsigned long lastMotion = 0;
const unsigned long PRESENCE_TIMEOUT = 300000; // 5 minut

void setup() {
  // Nastavení pinů
  pinMode(PIR_PIN, INPUT);
  pinMode(LED_HEATING, OUTPUT);
  pinMode(LED_COOLING, OUTPUT);
  pinMode(LED_LIGHT, OUTPUT);
  pinMode(FAN_PIN, OUTPUT);
  
  lcd.begin(16, 2);
  Serial.begin(9600);
  
  lcd.print("Chytra mistnost");
  lcd.setCursor(0, 1);
  lcd.print("Inicializace...");
  
  delay(30000); // PIR kalibrace
  lcd.clear();
}

void loop() {
  // Čtení všech senzorů
  float temperature = readTemperature();
  int lightLevel = analogRead(LIGHT_PIN);
  boolean motionDetected = digitalRead(PIR_PIN);
  
  // Detekce přítomnosti
  updatePresence(motionDetected);
  
  // Rozhodovací logika
  if (personPresent) {
    controlLighting(lightLevel);
    controlHeating(temperature);
    controlCooling(temperature);
  } else {
    // Úsporný režim - všechno vypnuto
    energySaveMode();
  }
  
  // Zobrazení informací
  updateDisplay(temperature, lightLevel, personPresent);
  
  delay(500);
}

float readTemperature() {
  int analogValue = analogRead(TEMP_PIN);
  float voltage = (analogValue * 5.0) / 1024.0;
  return (voltage - 0.5) * 100.0;
}

void updatePresence(boolean motion) {
  if (motion) {
    personPresent = true;
    lastMotion = millis();
  } else {
    // Kontrola timeout
    if (millis() - lastMotion > PRESENCE_TIMEOUT) {
      personPresent = false;
    }
  }
}

void controlLighting(int lightLevel) {
  int brightness = 0;
  
  if (lightLevel < LIGHT_DARK) {
    // Tma - plné osvětlení
    brightness = 255;
  } else if (lightLevel < LIGHT_BRIGHT) {
    // Polostín - částečné osvětlení
    brightness = map(lightLevel, LIGHT_DARK, LIGHT_BRIGHT, 255, 50);
  } else {
    // Dostatek světla - minimální osvětlení
    brightness = 0;
  }
  
  analogWrite(LED_LIGHT, brightness);
}

void controlHeating(float temperature) {
  if (temperature < TEMP_COLD) {
    digitalWrite(LED_HEATING, HIGH);
    Serial.println("Topeni zapnuto");
  } else {
    digitalWrite(LED_HEATING, LOW);
  }
}

void controlCooling(float temperature) {
  if (temperature > TEMP_WARM) {
    digitalWrite(LED_COOLING, HIGH);
    // Ventilátor podle teploty
    int fanSpeed = map(constrain(temperature, TEMP_WARM, 35), 
                       TEMP_WARM, 35, 100, 255);
    analogWrite(FAN_PIN, fanSpeed);
    Serial.println("Chlazeni zapnuto");
  } else {
    digitalWrite(LED_COOLING, LOW);
    analogWrite(FAN_PIN, 0);
  }
}

void energySaveMode() {
  digitalWrite(LED_HEATING, LOW);
  digitalWrite(LED_COOLING, LOW);
  analogWrite(LED_LIGHT, 0);
  analogWrite(FAN_PIN, 0);
}

void updateDisplay(float temp, int light, boolean present) {
  lcd.setCursor(0, 0);
  lcd.print("T:");
  lcd.print(temp, 1);
  lcd.print("C L:");
  lcd.print(light);
  lcd.print("   ");
  
  lcd.setCursor(0, 1);
  lcd.print("Osoba: ");
  lcd.print(present ? "ANO" : "NE ");
  
  // Stav systémů
  lcd.print(" ");
  if (digitalRead(LED_HEATING)) lcd.print("H");
  else if (digitalRead(LED_COOLING)) lcd.print("C");
  else lcd.print("-");
}
```

#### 3. Pokročilá rozhodovací logika (10 min)

**Prioritní systém:**
```cpp
void smartDecision(float temp, int light, boolean motion) {
  // 1. Bezpečnost má nejvyšší prioritu
  if (temp > 40) {
    emergencyShutdown();
    return;
  }
  
  // 2. Přítomnost osob
  if (!motion) {
    energySaveMode();
    return;
  }
  
  // 3. Kombinované podmínky
  if (temp < 18 && light < 300) {
    // Zima a tma - topení + světlo
    digitalWrite(HEATING, HIGH);
    analogWrite(LIGHT, 255);
  } else if (temp > 25 && light > 700) {
    // Teplo a světlo - chlazení, bez umělého osvětlení
    digitalWrite(COOLING, HIGH);
    analogWrite(LIGHT, 0);
  }
  // ... další kombinace
}
```

**Váhovaný systém (fuzzy logika):**
```cpp
int calculateComfort(float temp, int light, boolean motion) {
  int comfort = 50; // Základní úroveň
  
  // Teplota (30% váha)
  if (temp >= 20 && temp <= 24) comfort += 30;
  else comfort -= abs(22 - temp) * 5;
  
  // Osvětlení (20% váha)  
  if (light >= 400 && light <= 600) comfort += 20;
  else comfort -= 10;
  
  // Přítomnost (50% váha)
  if (motion) comfort += 50;
  else comfort -= 25;
  
  return constrain(comfort, 0, 100);
}
```

### Domácí úkol
Navrhnout "chytrou skleník" kombinující teplotu, světlo a vlhkost půdy pro automatické zavlažování.

---

## Hodina 20: Mini projekt – alarm

### Cíle hodiny
- Aplikovat všechny dosud naučené znalosti o senzorech
- Vytvořit komplexní bezpečnostní systém
- Dokumentovat projekt pro domácí stavbu

### Materiály
- Tinkercad Circuits s Arduino
- Všechny dosud použité senzory
- LCD displej, klávesnice (simulace)
- Bzučák, LED, servo motor

### Průběh hodiny (45 min)

#### 1. Specifikace projektu (10 min)

**"Domácí bezpečnostní systém"**

**Funkce:**
1. **Detekce vniknutí:** PIR + světelný senzor
2. **Požární ochrana:** Teplotní senzor
3. **Uživatelské rozhraní:** LCD + tlačítka
4. **Alarm:** Vizuální + zvukový
5. **Záložní napájení:** Simulace battery backup

**Módy systému:**
- **DISARMED:** Vypnutý, monitoruje pouze teplotu
- **HOME:** Ochrana oken/dveří, ignoruje vnitřní pohyb
- **AWAY:** Plná ochrana všech senzorů
- **ALARM:** Aktivní poplach

#### 2. Implementace kompletního systému (30 min)

```cpp
#include <LiquidCrystal.h>
#include <Servo.h>

// Hardware setup
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
Servo lockServo;

// Senzory
const int PIR_INDOOR = 6;
const int PIR_DOOR = 7;
const int TEMP_SENSOR = A0;
const int LIGHT_SENSOR = A1;
const int SMOKE_SENSOR = A2;

// Ovládání
const int BUTTON_ARM = 8;
const int BUTTON_DISARM = 9;
const int BUTTON_HOME = 10;
const int BUZZER = 13;

// Indikace
const int LED_STATUS = A3;
const int LED_FIRE = A4;
const int LED_INTRUSION = A5;

// Systémové proměnné
enum SystemMode { DISARMED, HOME, AWAY, ALARM, FIRE_ALARM };
SystemMode currentMode = DISARMED;

unsigned long alarmStartTime = 0;
unsigned long lastDisplayUpdate = 0;
boolean sirenState = false;

// Bezpečnostní nastavení
const float FIRE_TEMP = 45.0;        // °C
const int SMOKE_THRESHOLD = 600;     // ADC hodnota
const int ENTRY_DELAY = 15000;       // 15 sekund na odstaven
const int EXIT_DELAY = 30000;        // 30 sekund na opuštění
const char* MASTER_CODE = "1234";

// Statistiky
unsigned long systemUptime = 0;
int falseAlarms = 0;
int validAlarms = 0;

void setup() {
  // Inicializace hardware
  pinMode(PIR_INDOOR, INPUT);
  pinMode(PIR_DOOR, INPUT);
  pinMode(BUTTON_ARM, INPUT_PULLUP);
  pinMode(BUTTON_DISARM, INPUT_PULLUP);
  pinMode(BUTTON_HOME, INPUT_PULLUP);
  
  pinMode(BUZZER, OUTPUT);
  pinMode(LED_STATUS, OUTPUT);
  pinMode(LED_FIRE, OUTPUT);
  pinMode(LED_INTRUSION, OUTPUT);
  
  lockServo.attach(A4);
  lockServo.write(0); // Unlocked position
  
  lcd.begin(16, 2);
  Serial.begin(9600);
  
  // Uvítací obrazovka
  lcd.print("SECURITY SYSTEM");
  lcd.setCursor(0, 1);
  lcd.print("Starting up...");
  
  // Inicializace senzorů (kalibrace PIR)
  for (int i = 30; i > 0; i--) {
    lcd.setCursor(14, 1);
    lcd.print(i);
    if (i < 10) lcd.print(" ");
    delay(1000);
  }
  
  lcd.clear();
  currentMode = DISARMED;
  updateDisplay();
  
  Serial.println("Security System Ready");
}

void loop() {
  // Čtení senzorů
  SensorReadings sensors = readAllSensors();
  
  // Kontrola požární ochrany (aktivní vždy!)
  if (checkFireHazard(sensors)) {
    if (currentMode != FIRE_ALARM) {
      triggerFireAlarm();
    }
  }
  
  // Hlavní logika podle módu
  switch (currentMode) {
    case DISARMED:
      handleDisarmedMode();
      break;
      
    case HOME:
      handleHomeMode(sensors);
      break;
      
    case AWAY:
      handleAwayMode(sensors);
      break;
      
    case ALARM:
      handleAlarmMode();
      break;
      
    case FIRE_ALARM:
      handleFireAlarmMode();
      break;
  }
  
  // Aktualizace displeje a indikace
  if (millis() - lastDisplayUpdate > 500) {
    updateDisplay();
    updateLEDs();
    lastDisplayUpdate = millis();
  }
  
  systemUptime = millis();
  delay(100);
}

struct SensorReadings {
  boolean pirIndoor;
  boolean pirDoor;
  float temperature;
  int lightLevel;
  int smokeLevel;
};

SensorReadings readAllSensors() {
  SensorReadings readings;
  
  readings.pirIndoor = digitalRead(PIR_INDOOR);
  readings.pirDoor = digitalRead(PIR_DOOR);
  
  // Teplota
  int tempRaw = analogRead(TEMP_SENSOR);
  float voltage = (tempRaw * 5.0) / 1024.0;
  readings.temperature = (voltage - 0.5) * 100.0;
  
  readings.lightLevel = analogRead(LIGHT_SENSOR);
  readings.smokeLevel = analogRead(SMOKE_SENSOR);
  
  return readings;
}

boolean checkFireHazard(SensorReadings sensors) {
  return (sensors.temperature > FIRE_TEMP || 
          sensors.smokeLevel > SMOKE_THRESHOLD);
}

void handleDisarmedMode() {
  // Kontrola ovládacích tlačítek
  if (digitalRead(BUTTON_ARM) == LOW) {
    setMode(AWAY);
    delay(300);
  } else if (digitalRead(BUTTON_HOME) == LOW) {
    setMode(HOME);
    delay(300);
  }
  
  // Pouze monitoring bez akcí
  digitalWrite(LED_STATUS, LOW);
  noTone(BUZZER);
}

void handleHomeMode(SensorReadings sensors) {
  // Home mode: pouze vnější senzory (dveře/okna)
  if (sensors.pirDoor) {
    triggerAlarm("Door/Window");
  }
  
  // Kontrola odstaven
  if (digitalRead(BUTTON_DISARM) == LOW) {
    setMode(DISARMED);
    delay(300);
  }
}

void handleAwayMode(SensorReadings sensors) {
  // Away mode: všechny senzory aktivní
  if (sensors.pirIndoor || sensors.pirDoor) {
    triggerAlarm("Motion detected");
  }
  
  // Kontrola odstaven s prodlevou
  if (digitalRead(BUTTON_DISARM) == LOW) {
    entryDelayCountdown();
  }
}

void handleAlarmMode() {
  // Alarm siren
  sirenState = !sirenState;
  if (sirenState) {
    tone(BUZZER, 1000, 250);
  } else {
    tone(BUZZER, 1500, 250);
  }
  
  // Kontrola odstaven
  if (digitalRead(BUTTON_DISARM) == LOW) {
    if (verifyMasterCode()) {
      setMode(DISARMED);
      validAlarms++;
      Serial.println("Alarm deactivated with valid code");
    } else {
      falseAlarms++;
      Serial.println("Invalid disarm attempt!");
    }
    delay(300);
  }
  
  // Auto-reset po 5 minutách
  if (millis() - alarmStartTime > 300000) {
    setMode(HOME); // Návrat do home mode
    falseAlarms++;
  }
}

void handleFireAlarmMode() {
  // Požární alarm - nelze vypnout, jen reset
  tone(BUZZER, 2000, 100);
  delay(100);
  tone(BUZZER, 2500, 100);
  delay(100);
  
  // Automatické odemčení dveří pro evakuaci
  lockServo.write(90);
  
  if (digitalRead(BUTTON_DISARM) == LOW) {
    // Reset pouze po potvrzení
    lcd.clear();
    lcd.print("Fire alarm reset");
    lcd.setCursor(0, 1);
    lcd.print("Check sensors!");
    delay(3000);
    setMode(DISARMED);
  }
}

void triggerAlarm(const char* reason) {
  currentMode = ALARM;
  alarmStartTime = millis();
  
  lcd.clear();
  lcd.print("!!! ALARM !!!");
  lcd.setCursor(0, 1);
  lcd.print(reason);
  
  Serial.print("ALARM TRIGGERED: ");
  Serial.println(reason);
}

void triggerFireAlarm() {
  currentMode = FIRE_ALARM;
  alarmStartTime = millis();
  
  lcd.clear();
  lcd.print("!!! FIRE !!!");
  lcd.setCursor(0, 1);
  lcd.print("EVACUATE NOW!");
  
  Serial.println("FIRE ALARM TRIGGERED!");
}

void entryDelayCountdown() {
  for (int i = ENTRY_DELAY/1000; i > 0; i--) {
    lcd.clear();
    lcd.print("Entry delay:");
    lcd.setCursor(0, 1);
    lcd.print(i);
    lcd.print(" seconds");
    
    tone(BUZZER, 800, 100);
    delay(1000);
    
    if (digitalRead(BUTTON_DISARM) == LOW) {
      if (verifyMasterCode()) {
        setMode(DISARMED);
        return;
      }
    }
  }
  
  // Timeout - spustit alarm
  triggerAlarm("Entry timeout");
}

boolean verifyMasterCode() {
  // Simulace zadání kódu
  lcd.clear();
  lcd.print("Enter code:");
  lcd.setCursor(0, 1);
  lcd.print("****");
  delay(2000);
  
  // V reálném systému by zde byla klávesnice
  return true; // Pro simulaci vždy úspěšné
}

void setMode(SystemMode newMode) {
  currentMode = newMode;
  
  switch (newMode) {
    case DISARMED:
      lockServo.write(0); // Unlock
      noTone(BUZZER);
      break;
      
    case HOME:
    case AWAY:
      lockServo.write(90); // Lock
      // Exit delay countdown
      for (int i = EXIT_DELAY/1000; i > 0; i--) {
        lcd.clear();
        lcd.print("Exit delay:");
        lcd.setCursor(0, 1);
        lcd.print(i);
        lcd.print(" seconds");
        tone(BUZZER, 500, 100);
        delay(1000);
      }
      break;
  }
}

void updateDisplay() {
  static int displayPage = 0;
  
  // Střídání stránek displeje
  displayPage = (displayPage + 1) % 3;
  
  lcd.setCursor(0, 0);
  
  switch (displayPage) {
    case 0: // Status
      lcd.print("Mode: ");
      switch (currentMode) {
        case DISARMED: lcd.print("OFF    "); break;
        case HOME: lcd.print("HOME   "); break;
        case AWAY: lcd.print("AWAY   "); break;
        case ALARM: lcd.print("ALARM  "); break;
        case FIRE_ALARM: lcd.print("FIRE!! "); break;
      }
      
      lcd.setCursor(0, 1);
      lcd.print("Up: ");
      lcd.print(systemUptime / 3600000);
      lcd.print("h");
      break;
      
    case 1: // Senzory
      SensorReadings current = readAllSensors();
      lcd.print("T:");
      lcd.print(current.temperature, 1);
      lcd.print("C L:");
      lcd.print(current.lightLevel);
      
      lcd.setCursor(0, 1);
      lcd.print("PIR:");
      lcd.print(current.pirIndoor ? "I" : "-");
      lcd.print(current.pirDoor ? "D" : "-");
      lcd.print(" S:");
      lcd.print(current.smokeLevel);
      break;
      
    case 2: // Statistiky
      lcd.print("Alarms V:");
      lcd.print(validAlarms);
      lcd.print(" F:");
      lcd.print(falseAlarms);
      
      lcd.setCursor(0, 1);
      lcd.print("Battery: 87%"); // Simulace
      break;
  }
}

void updateLEDs() {
  // Status LED
  switch (currentMode) {
    case DISARMED:
      digitalWrite(LED_STATUS, LOW);
      break;
    case HOME:
    case AWAY:
      digitalWrite(LED_STATUS, (millis() / 1000) % 2);
      break;
    case ALARM:
      digitalWrite(LED_STATUS, (millis() / 250) % 2);
      break;
  }
  
  // Požární LED
  digitalWrite(LED_FIRE, currentMode == FIRE_ALARM);
  
  // Intrusion LED  
  digitalWrite(LED_INTRUSION, currentMode == ALARM);
}
```

#### 3. Dokumentace projektu (5 min)

**Odevzdání obsahuje:**
1. **Funkční Tinkercad projekt** s komentovaným kódem
2. **Schéma zapojení** s popisem všech komponent
3. **Uživatelský manuál** - jak systém ovládat
4. **Seznam součástek** s cenami (odhad nákladů)
5. **Možná vylepšení** pro budoucí verze

### Projekt k odevzdání
Kompletní domácí bezpečnostní systém s dokumentací připravenou pro skutečnou stavbu.

### Shrnutí bloku 5
- Ovládáme všechny základní typy senzorů
- Umíme kombinovat více senzorů současně  
- Vytváříme komplexní rozhodovací logiku
- Aplikujeme znalosti v praktickém projektu
- Jsme připraveni na vlastní kreativní projekty
