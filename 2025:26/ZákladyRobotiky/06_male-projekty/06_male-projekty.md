# Blok 6: Malé projekty (21–27)

## Hodina 21: Návrh ročníkového projektu – brainstorming

### Cíle hodiny
- Identifikovat vlastní zájmy a potřeby pro projekt
- Naučit se systematický přístup k návrhu projektu
- Vytvořit koncept ročníkového projektu

### Materiály
- Papír a tužky pro skicování
- Flipchart nebo tabule pro skupinové brainstorming
- Inspirační obrázky robotických projektů
- Formuláře pro projektové plány

### Průběh hodiny (45 min)

#### 1. Úvod - Co je projektové myšlení? (10 min)
**Design Thinking proces:**
1. **Empathize** - Pochop problém
2. **Define** - Definuj výzvu  
3. **Ideate** - Vymysli řešení
4. **Prototype** - Vytvoř prototyp
5. **Test** - Otestuj a vylepši

**Otázky k zamyšlení:**
- Co vás doma nebo ve škole obtěžuje?
- Jaký problém byste rádi vyřešili?
- Co vás na robotice nejvíc baví?

#### 2. Brainstorming - Hledání nápadů (20 min)

**Kategorien projektů:**

| Kategorie | Příklady | Obtížnost |
|-----------|----------|-----------|
| **Domácí pomocníci** | Automatické krmítko, zavlažování květin | ⭐⭐ |
| **Bezpečnostní systémy** | Alarm, detektor kouře, kamera | ⭐⭐⭐ |
| **Zábavní projekty** | LED světelné show, hudební nástroj | ⭐⭐ |
| **Smart Home** | Chytrý termostat, automatické žaluzie | ⭐⭐⭐ |
| **Zdraví a fitness** | Krokoměr, připomínač léků | ⭐⭐ |
| **Vzdělávací hry** | Quiz, reakcní hry | ⭐⭐ |
| **Ekologické projekty** | Měřič kvality vzduchu, úspora energie | ⭐⭐⭐ |

**Brainstorming pravidla:**
- Žádná kritika během brainstormingu
- Kvantita nad kvalitou
- Stavějte na nápadech ostatních
- Buďte kreativní a bláznivý

**Techniky brainstormingu:**
1. **Myšlenkové mapy:** Napište problém doprostřed, kolem něj nápady
2. **6-3-5 metoda:** 6 lidí, 3 nápady, 5 minut
3. **SCAMPER:** Substitute, Combine, Adapt, Modify, Put to other uses, Eliminate, Reverse

#### 3. Hodnocení a výběr nápadu (10 min)

**Kritéria pro hodnocení:**
- **Užitečnost:** Vyřeší skutečný problém? (1-5 bodů)
- **Realizovatelnost:** Dokážeme to s našimi znalostmi? (1-5)
- **Originalita:** Je to něco nového/zajímavého? (1-5)
- **Složitost komponent:** Máme potřebné části? (1-5)

**Hodnotící matice:**
```
Nápad: _______________________
Užitečnost:     ⭐⭐⭐⭐⭐
Realizovatelnost: ⭐⭐⭐⭐⭐
Originalita:    ⭐⭐⭐⭐⭐
Komponenty:     ⭐⭐⭐⭐⭐
Celkem:         __/20 bodů
```

#### 4. První náčrt projektu (5 min)

**Projektový formulář:**
- **Název projektu:** 
- **Problém, který řeší:**
- **Hlavní funkce (3-5 bodů):**
- **Potřebné komponenty:**
- **Očekávané výsledky:**

### Domácí úkol
Dopracovat projektový nápad - najít podobné projekty na internetu, inspirovat se, ale nevybírat hotové řešení.

---

## Hodina 22: Tvorba schématu

### Cíle hodiny
- Převést nápad do technického schématu
- Naučit se plánovat elektrické zapojení
- Identifikovat potřebné komponenty

### Materiály
- Tinkercad Circuits
- Katalogy komponent
- Papír pro rucni skicování
- Kalkulačka pro výpočty

### Průběh hodiny (45 min)

#### 1. Od nápadu ke schématu (15 min)

**Postup návrhu:**
1. **Funkcní bloky:** Rozdělení na logické celky
2. **Vstupy a výstupy:** Co projekt přijímá/odesílá
3. **Propojení:** Jak bloky komunikují
4. **Napájení:** Energie pro celý systém

**Příklad - Automatické krmítko:**
```
[Časovač] → [Arduino] → [Servo motor]
             ↑    ↓
        [Tlačítko] [LCD displej]
             ↑    ↓  
        [Senzor váhy] [Bzučák]
```

#### 2. Výběr komponent (20 min)

**Systematický přístup:**

| Funkce | Možné komponenty | Výběr | Důvod |
|--------|------------------|-------|--------|
| Mikrokontrolér | Arduino Uno, Nano | Uno | Více pinů, snadné připojení |
| Zobrazení | LCD 16×2, OLED | LCD | Levnější, dostatečné |
| Pohyb | Servo, DC motor | Servo | Přesná pozice |
| Čas | RTC modul, millis() | millis() | Jednodušší |
| Zvuk | Buzzer, speaker | Buzzer | Méně pinů |

**Kontrolní seznam:**
- ✓ Arduino má dostatek pinů?
- ✓ Napájení stačí pro všechny komponenty?
- ✓ Žádné konflikty pinů?
- ✓ Všechny komponenty jsou v Tinkercad?

#### 3. Kreslení schématu (10 min)

**V Tinkercad Circuits:**
1. Přidej Arduino jako základ
2. Přidej všechny komponenty
3. Propoj podle plánu
4. **Pojmenuj vodiče** (pravý klik → Label)
5. Přidaj komentáře k složitějším částem

**Standardní zapojení:**
- **Napájení:** Červené vodiče (5V, VCC)
- **Zem:** Černé vodiče (GND)  
- **Signály:** Barevné podle funkce
- **Analogové:** Žluté
- **Digitální:** Zelené
- **PWM:** Modré

### Praktický příklad - Smart květináč

**Specifikace:**
- Měří vlhkost půdy
- Automaticky zalije při suchu
- Měří teplotu a světlo
- LCD displej s informacemi
- Tlačítko pro manuální zalévání

**Komponenty:**
- Arduino Uno
- Soil moisture sensor
- Water pump (DC motor)
- TMP36 teplotní senzor
- LDR světelný senzor
- LCD 16×2
- Tlačítko + pull-up rezistor
- LED indikace
- Relay modul pro pumpu

**Schéma zapojení v Pythonu:**
```python
# Pin Assignment
SOIL_PIN = arduino.A0      # Vlhkost půdy
TEMP_PIN = arduino.A1      # Teplota
LIGHT_PIN = arduino.A2     # Světlo
PUMP_RELAY = 8             # Čerpadlo
BUTTON_PIN = 2             # Tlačítko
LED_WATER = 9              # LED zalévání
LED_STATUS = 10            # Status LED
# LCD: simulováno pomocí print() funkcí
```

### Domácí úkol
Dokončit schéma vlastního projektu v Tinkercad s popisky a komentáři.

---

## Hodina 23: Programování logiky

### Cíle hodiny
- Implementovat základní logiku projektu
- Naučit se strukturovat složitější kód
- Otestovat funkčnost v simulátoru

### Materiály
- Hotová schémata z minulé hodiny
- Tinkercad Circuits s code editorem
- Referenční dokumentace Arduino funkcí

### Průběh hodiny (45 min)

#### 1. Struktura složitějšího kódu (15 min)

**Organizace Python kódu:**
```python
# ============= KONFIGURACE =============
import arduino
import time

# Konstanty pinů
SENSOR_PIN = arduino.A0
LED_PIN = 13

# Globální proměnné
sensor_value = 0
last_update = 0

# ============= SETUP =============
def setup():
    # Inicializace
    initialize_pins()
    initialize_lcd()
    print("System started")

# ============= MAIN LOOP =============
def loop():
    # Hlavní logika
    read_sensors()
    process_data()
    update_outputs()
    update_display()
    
    time.sleep(0.1)

# ============= FUNKCE =============
def initialize_pins():
    # Nastavení všech pinů
    arduino.pin_mode(LED_PIN, arduino.OUTPUT)

def read_sensors():
    # Čtení ze senzorů
    global sensor_value
    sensor_value = arduino.analog_read(SENSOR_PIN)

# Spuštění hlavního programu
setup()
while True:
    loop()
```

**Výhody strukturovaného kódu:**
- Lepší čitelnost
- Snadnější ladění
- Možnost znovupoužití
- Týmová spolupráce

#### 2. Implementace stavového automatu (20 min)

**Koncept stavů:**
Mnoho robotických projektů má různé stavy (módy):
- Inicializace → Monitoring → Akce → Čekání

**Příklad - Smart květináč v Pythonu:**
```python
# Stavy systému - používáme stringy místo enum
INIT = "init"
MONITORING = "monitoring" 
WATERING = "watering"
WAITING = "waiting"
MANUAL_MODE = "manual_mode"
ERROR_STATE = "error_state"

current_state = INIT
state_start_time = 0

# Globální proměnné
soil_moisture = 0
temperature = 0.0
light_level = 0
button_pressed = False

# Prahové hodnoty
DRY_THRESHOLD = 300
WET_THRESHOLD = 600
WATERING_TIME = 5000    # 5 sekund (v ms)
WAIT_TIME = 3600000     # 1 hodina (v ms)

def loop():
    global current_state
    
    # Čtení vstupů
    read_all_sensors()
    
    # Stavový automat
    if current_state == INIT:
        handle_init_state()
    elif current_state == MONITORING:
        handle_monitoring_state()
    elif current_state == WATERING:
        handle_watering_state()
    elif current_state == WAITING:
        handle_waiting_state()
    elif current_state == MANUAL_MODE:
        handle_manual_state()
    elif current_state == ERROR_STATE:
        handle_error_state()
    
    update_display()
    time.sleep(0.1)

void handleInitState() {
  Serial.println("Initializing system...");
  digitalWrite(LED_STATUS, HIGH);
  
  // Test všech komponent
  if (testAllComponents()) {
    changeState(MONITORING);
  } else {
    changeState(ERROR_STATE);
  }
}

void handleMonitoringState() {
  // Kontrola tlačítka pro manuální režim
  if (buttonPressed) {
    changeState(MANUAL_MODE);
    return;
  }
  
  // Kontrola vlhkosti půdy
  if (soilMoisture < DRY_THRESHOLD) {
    Serial.println("Soil is dry - starting watering");
    changeState(WATERING);
  }
  
  // Blikání status LED
  digitalWrite(LED_STATUS, (millis() / 1000) % 2);
}

void handleWateringState() {
  // Zapni čerpadlo a LED
  digitalWrite(PUMP_RELAY, HIGH);
  digitalWrite(LED_WATER, HIGH);
  
  Serial.println("Watering plants...");
  
  // Kontrola času nebo vlhkosti
  if (millis() - stateStartTime > WATERING_TIME || 
      soilMoisture > WET_THRESHOLD) {
    
    Serial.println("Watering complete");
    digitalWrite(PUMP_RELAY, LOW);
    digitalWrite(LED_WATER, LOW);
    
    changeState(WAITING);
  }
}

void handleWaitingState() {
  // Čekání mezi zalévání
  if (millis() - stateStartTime > WAIT_TIME) {
    changeState(MONITORING);
  }
  
  // Pomalé blikání LED
  digitalWrite(LED_STATUS, (millis() / 2000) % 2);
}

void handleManualState() {
  Serial.println("Manual mode");
  
  if (buttonPressed) {
    // Toggle watering
    boolean pumpState = digitalRead(PUMP_RELAY);
    digitalWrite(PUMP_RELAY, !pumpState);
    digitalWrite(LED_WATER, !pumpState);
  }
  
  // Dlouhé stisknutí pro návrat do auto módu
  if (longButtonPress()) {
    digitalWrite(PUMP_RELAY, LOW);
    digitalWrite(LED_WATER, LOW);
    changeState(MONITORING);
  }
}

void handleErrorState() {
  Serial.println("ERROR: System malfunction!");
  
  // Rychlé blikání error LED
  digitalWrite(LED_STATUS, (millis() / 200) % 2);
  
  // Reset po stisku tlačítka
  if (buttonPressed) {
    changeState(INIT);
  }
}

void changeState(SystemState newState) {
  Serial.print("State change: ");
  Serial.print(currentState);
  Serial.print(" -> ");
  Serial.println(newState);
  
  currentState = newState;
  stateStartTime = millis();
}
```

#### 3. Testování a ladění (10 min)

**Debugovací techniky:**
1. **Serial Monitor:** Výpisy stavu programu
2. **LED indikace:** Vizuální feedback
3. **Postupné testování:** Po malých krocích
4. **Simulace extrémních hodnot:** Co se stane při...?

**Serial debugging:**
```cpp
void printDebugInfo() {
  Serial.print("State: ");
  Serial.print(currentState);
  Serial.print(", Soil: ");
  Serial.print(soilMoisture);
  Serial.print(", Temp: ");
  Serial.print(temperature);
  Serial.print(", Light: ");
  Serial.println(lightLevel);
}
```

### Domácí úkol
Implementovat základní stavový automat pro vlastní projekt s alespoň 3 stavy.

---

## Hodina 24: Přidání senzorů

### Cíle hodiny
- Integrovat senzory do existujícího projektu
- Vyřešit problémy s čtením a kalibrací
- Implementovat filtrování a zpracování dat

### Materiály
- Rozpracované projekty s implementovanou logikou
- Všechny typy senzorů dostupné v Tinkercad
- Kalkulačka pro statistické výpočty

### Průběh hodiny (45 min)

#### 1. Integrace senzorů do stavového automatu (15 min)

**Přidání funkcí pro senzory:**
```cpp
// Globální proměnné pro senzory
struct SensorData {
  int soilMoisture;
  float temperature;
  int lightLevel;
  boolean motionDetected;
  unsigned long lastUpdate;
};

SensorData sensors;

void readAllSensors() {
  sensors.soilMoisture = readSoilMoisture();
  sensors.temperature = readTemperature();
  sensors.lightLevel = analogRead(LIGHT_PIN);
  sensors.motionDetected = digitalRead(PIR_PIN);
  sensors.lastUpdate = millis();
  
  // Debug výstup
  if (millis() % 5000 == 0) { // Každých 5 sekund
    printSensorData();
  }
}

int readSoilMoisture() {
  // Čtení vlhkosti půdy s filtrováním
  int reading = analogRead(SOIL_PIN);
  
  // Mapování na procenta (kalibrace podle senzoru)
  int moisture = map(reading, 200, 1000, 100, 0);
  moisture = constrain(moisture, 0, 100);
  
  return moisture;
}

float readTemperature() {
  int analogValue = analogRead(TEMP_PIN);
  float voltage = (analogValue * 5.0) / 1024.0;
  float temperature = (voltage - 0.5) * 100.0;
  
  // Kontrola rozumných hodnot
  if (temperature < -10 || temperature > 50) {
    Serial.println("Warning: Temperature reading out of range");
    return sensors.temperature; // Vrátit předchozí hodnotu
  }
  
  return temperature;
}
```

#### 2. Filtrování a zpracování dat (20 min)

**Problém šumu v datech:**
Senzory často dávají "skákavé" hodnoty kvůli elektrickému šumu.

**Řešení - Moving Average (klouzavý průměr):**
```cpp
const int FILTER_SIZE = 5;

// Filtry pro každý senzor
int soilReadings[FILTER_SIZE];
int tempReadings[FILTER_SIZE];
int lightReadings[FILTER_SIZE];

int filterIndex = 0;
boolean filtersInitialized = false;

int getFilteredSoilMoisture() {
  // Přidej nové čtení
  soilReadings[filterIndex] = analogRead(SOIL_PIN);
  
  // Vypočítej průměr
  long sum = 0;
  for (int i = 0; i < FILTER_SIZE; i++) {
    sum += soilReadings[i];
  }
  
  filterIndex = (filterIndex + 1) % FILTER_SIZE;
  
  return sum / FILTER_SIZE;
}

// Alternativa - exponenciální filtr (jednodušší)
int exponentialFilter(int newValue, int oldValue, float alpha) {
  // alpha = 0.1 to 0.9 (vyšší = více reaguje na změny)
  return (alpha * newValue) + ((1.0 - alpha) * oldValue);
}
```

**Detekce změn (edge detection):**
```cpp
boolean detectSignificantChange(int currentValue, int previousValue, int threshold) {
  return abs(currentValue - previousValue) > threshold;
}

// Použití
if (detectSignificantChange(sensors.lightLevel, previousLightLevel, 50)) {
  Serial.println("Significant light change detected");
  // Nějaká akce...
}
```

#### 3. Adaptivní rozhodování (10 min)

**Dynamické prahové hodnoty:**
```cpp
// Místo pevných hodnot použít adaptivní
int calculateDryThreshold() {
  // Podle teploty - v horku potřebujeme více vody
  if (sensors.temperature > 25) {
    return 400; // Vyšší vlhkost
  } else if (sensors.temperature < 15) {
    return 250; // Nižší vlhkost stačí
  } else {
    return 300; // Standardní
  }
}

// Podle světla - ve stínu méně vody
int adjustForLight() {
  int threshold = calculateDryThreshold();
  
  if (sensors.lightLevel < 200) { // Stín
    threshold *= 0.8; // 20% méně vody
  }
  
  return threshold;
}
```

**Multi-kriteriální rozhodování:**
```cpp
boolean shouldWater() {
  int threshold = adjustForLight();
  
  // Hlavní podmínka
  if (sensors.soilMoisture > threshold) {
    return false; // Dostatečně vlhko
  }
  
  // Doplňkové kontroly
  if (sensors.temperature > 35) {
    Serial.println("Too hot to water - risk of burning plants");
    return false;
  }
  
  if (sensors.lightLevel < 100 && hour() > 20) {
    Serial.println("Too dark and late - wait for morning");
    return false;
  }
  
  // Kontrola historie - nezalévat příliš často
  if (millis() - lastWateringTime < MIN_WATERING_INTERVAL) {
    return false;
  }
  
  return true;
}
```

**Příklad komplexní logiky:**
```cpp
void smartWateringLogic() {
  static unsigned long lastWatering = 0;
  static int wateringCount = 0;
  
  // Pouze během vhodných hodin (simulace - podle millis)
  boolean dayTime = ((millis() / 3600000) % 24) >= 6 && 
                   ((millis() / 3600000) % 24) <= 20;
  
  if (!dayTime) {
    Serial.println("Night time - no watering");
    return;
  }
  
  // Hlavní rozhodovací logika
  if (shouldWater()) {
    // Různé režimy zalévání podle podmínek
    int wateringDuration = calculateWateringDuration();
    
    startWatering(wateringDuration);
    
    lastWatering = millis();
    wateringCount++;
    
    // Log pro statistiky
    Serial.print("Watering #");
    Serial.print(wateringCount);
    Serial.print(" for ");
    Serial.print(wateringDuration);
    Serial.println("ms");
  }
}

int calculateWateringDuration() {
  int baseDuration = 3000; // 3 sekundy
  
  // Podle sucha půdy
  if (sensors.soilMoisture < 20) {
    baseDuration *= 1.5; // Déle pro velmi suchou půdu
  }
  
  // Podle teploty
  if (sensors.temperature > 28) {
    baseDuration *= 1.2; // Více vody v horku
  }
  
  // Podle velikosti rostliny (simulace - den v cyklu)
  int dayOfCycle = (millis() / 86400000) % 30; // 30 denní cyklus
  if (dayOfCycle > 15) { // "Větší" rostlina
    baseDuration *= 1.3;
  }
  
  return constrain(baseDuration, 1000, 10000); // 1-10 sekund
}
```

### Domácí úkol
Implementovat alespoň 2 senzory do vlastního projektu s filtrováním dat a inteligentním rozhodováním.

---

## Hodina 25: Případné 3D díly

### Cíle hodiny
- Navrhnout 3D díly pro vlastní projekt
- Vyřešit mechanické problémy v projektu
- Připravit díly k tisku nebo alternativní řešení

### Materiály
- Tinkercad 3D (online)
- Rozměry Arduino a komponent
- Kalkulačka pro výpočty rozměrů
- Ukázky hotových 3D dílů

### Průběh hodiny (45 min)

#### 1. Identifikace potřebných dílů (15 min)

**Typické potřeby 3D dílů v robotice:**

| Problém | 3D řešení | Alternativa |
|---------|-----------|-------------|
| Ochrana Arduino | Krabička | Plastový box |
| Držák senzorů | Custom držák | Lepicí páska |
| Mechanické spojení | Spojky, závěsy | Šrouby, drát |
| Ozubená kola | Převody | Hotová kola |
| Díly na míru | Specifický tvar | Úprava hotového |

**Analýza vlastního projektu:**
1. **Co potřebuje ochranu?** (elektronika, senzory)
2. **Co potřebuje držák?** (kamery, senzory, motory)
3. **Co potřebuje mechaniku?** (pohyb, otáčení)
4. **Co chce vypadat hezky?** (kryt, logo)

**Příklad - Smart květináč:**
```
Potřebné díly:
✓ Kryt pro Arduino a elektroniku
✓ Držák pro čerpadlo
✓ Kryt pro soil senzor (nepromokavý)
✓ Násypka pro vodu
✓ Dekorativní kryt LCD displeje
```

#### 2. Návrh v Tinkercad 3D (25 min)

**Projekt 1 - Krabička pro Arduino Uno:**
```
Rozměry Arduino Uno:
- Délka: 68.6mm
- Šířka: 53.4mm  
- Výška komponent: ~15mm
- Pozice šroubů: 4 díry 3.2mm

Krabička rozměry:
- Vnitřní: 70×55×18mm
- Vnější: 74×59×22mm (2mm stěny)
- Víko: separátní díl
```

**Kroky v Tinkercad:**
1. **Základní box:** 74×59×22mm
2. **Vnitřní díra:** 70×55×18mm, posunutá 2mm nahoru
3. **Díry pro USB a napájení:**
   - USB: 12×5mm na krátké straně
   - Power jack: 9×9mm na krátké straně
4. **Díry pro šrouby:** 4× válec 1.5mm průměr
5. **Víko:** Tenký box 74×59×4mm s okrajem

**Projekt 2 - Držák senzoru:**
```cpp
// Přizpůsobený držák PIR senzoru
Základní válec: průměr 30mm, výška 40mm
Díra pro senzor: průměr 24mm, hloubka 35mm
Příruby pro šrouby: 4× díry 3mm
Otvor pro kabel: 6×3mm obdélník
```

**Projekt 3 - Ozubené kolo:**
```cpp
// Jednoduché ozubené kolo
Základ: válec průměr 40mm, výška 8mm
Díra středu: průměr 6mm (pro servo horn)
Zuby: 20× malý obdélník na obvodu
```

#### 3. Praktické tipy pro 3D tisk (5 min)

**Design pravidla:**
- **Minimální tloušťka stěn:** 0.8mm (2× šířka trysky)
- **Převisy:** max 45° bez podpěr
- **Mezery:** minimum 0.2mm mezi pohyblivými díly  
- **První vrstva:** dobré přilnutí k podložce

**Orientace pro tisk:**
- Největší plocha dolů
- Minimalizovat podpěry
- Funkční plochy nahoru

**Alternativy k 3D tisku:**
- **Laser cut:** Plexisklo, dřevo (2D díly)
- **Ready-made:** Koupit hotové díly
- **DIY řešení:** Karton, plastové krabičky
- **Kovové díly:** Alu profily, L-úhelníky

### Praktické workshopy (podle dostupného času):

**Workshop A - Parametrické díly:**
```cpp
// Krabička s proměnnými rozměry
width = 50;    // Šířka
length = 70;   // Délka  
height = 20;   // Výška
thickness = 2; // Tloušťka stěn

// V Tinkercad nelze programovat, ale můžeme
// připravit několik velikostí předem
```

**Workshop B - Mechanické spoje:**
```cpp
// Připojení servo k ozubenému kolu
servo_horn_holes = 4;  // 4 díry pro šrouby
gear_center_diameter = 6; // Díra pro servo horn
```

**Workshop C - Vícekomponentní díly:**
```cpp
// Díl ze dvou částí
bottom_part();    // Spodní díl
top_part();       // Horní díl s 0.1mm mezerou
```

### Domácí úkol
Navrhnout a exportovat alespoň jeden 3D díl pro vlastní projekt (STL soubor).

---

## Hodina 26: Dokončení návrhu

### Cíle hodiny
- Dokončit všechny komponenty projektu
- Vyřešit zbývající technické problémy
- Připravit projekt k finálnímu testování

### Materiály
- Všechny rozpracované projekty
- Kompletní Tinkercad workspace
- Kontrolní seznamy projektů

### Průběh hodiny (45 min)

#### 1. Kontrola kompletnosti projektu (15 min)

**Kontrolní seznam:**

| Komponent | ✓ | Poznámky |
|-----------|---|----------|
| **Hardware schéma** | | Všechny komponenty připojené |
| **Základní kód** | | Setup() a loop() funkční |
| **Stavový automat** | | Minimálně 3 stavy |
| **Senzory** | | Alespoň 2 různé typy |
| **Výstupy** | | LED, motor, nebo displej |
| **Uživatelské rozhraní** | | Tlačítka nebo LCD |
| **Error handling** | | Co když něco selže? |
| **Dokumentace** | | Komentáře v kódu |
| **3D díly (volitelné)** | | STL soubory |
| **Testování** | | Funguje v simulátoru |

**Společná kontrola:**
Každý student prezentuje svůj projekt 2 minuty:
- Co projekt dělá?
- Jaké má hlavní funkce?
- Co bylo nejtěžší vyřešit?

#### 2. Řešení technických problémů (20 min)

**Časté problémy a řešení:**

**Problém 1: Nedostatek pinů**
```cpp
// Řešení A: Multiplexing
void selectPin(int pinNumber) {
  digitalWrite(2, pinNumber & 1);
  digitalWrite(3, (pinNumber >> 1) & 1);
  digitalWrite(4, (pinNumber >> 2) & 1);
  // Nyní můžeme vybrat 1 z 8 pinů
}

// Řešení B: Shift register (74HC595)
// Řešení C: I2C expander
// Řešení D: Přehodnotit design - je vše potřeba?
```

**Problém 2: Nestabilní čtení senzorů**
```cpp
// Řešení: Lepší filtrování
int stableRead(int pin, int samples = 10) {
  long sum = 0;
  for (int i = 0; i < samples; i++) {
    sum += analogRead(pin);
    delay(10);
  }
  return sum / samples;
}
```

**Problém 3: Pomalá odezva**
```cpp
// Špatně: všechno v loop()
void loop() {
  delay(1000);  // Blokuje všechno!
  readSensor();
  delay(500);
  updateDisplay();
}

// Dobře: non-blocking timing
unsigned long lastSensorRead = 0;
unsigned long lastDisplayUpdate = 0;

void loop() {
  if (millis() - lastSensorRead > 1000) {
    readSensor();
    lastSensorRead = millis();
  }
  
  if (millis() - lastDisplayUpdate > 500) {
    updateDisplay();
    lastDisplayUpdate = millis();
  }
}
```

**Problém 4: Vysoká spotřeba**
```cpp
// Power management
void enterSleepMode() {
  // Vypni nepotřebné periferie
  digitalWrite(LED_PIN, LOW);
  // V reálném Arduino: sleep_mode();
  delay(5000); // Simulace sleep
}

void wakUp() {
  // Zapni systémy
  Serial.println("System wake up");
}
```

#### 3. Finální optimalizace (10 min)

**Code review checklist:**
- ✓ Všechny proměnné mají smysluplné názvy
- ✓ Kód je rozdělený do funkcí (max 50 řádků/funkce)
- ✓ Komentáře u složitých částí
- ✓ Konstanty jsou #define nebo const
- ✓ Žádné "magic numbers" (vysvětlit co znamená 1023)
- ✓ Error handling (co když senzor neodpovídá?)

**Optimization tips:**
```cpp
// Místo:
if (analogRead(A0) > 500 && analogRead(A0) < 800) {

// Použij:
int sensorValue = analogRead(A0);
if (sensorValue > 500 && sensorValue < 800) {

// Nebo ještě lépe:
const int SENSOR_MIN = 500;
const int SENSOR_MAX = 800;
int sensorValue = analogRead(SENSOR_PIN);
if (sensorValue > SENSOR_MIN && sensorValue < SENSOR_MAX) {
```

**Memory optimization:**
```cpp
// Šetření RAM
// Místo: String message = "Hello World";
// Použij: const char* message = "Hello World";

// Místo globálních proměnných pro dočasné výpočty
// použij lokální proměnné ve funkcích
```

### Individuální konzultace:
Zbývající čas věnovat individuální pomoci studentům s jejich specifickými problémy.

**Typické dotazy:**
- "Proč mi nefunguje tenhle kód?"
- "Jak přidat další funkci?"
- "Můžu změnit koncept projektu?"
- "Co když nemám dost komponent?"

### Domácí úkol
Dokončit projekt do finální verze připravené k prezentaci a testování.

---

## Hodina 27: Kontrola a simulace

### Cíle hodiny
- Provést kompletní testování všech projektů
- Identifikovat a opravit chyby
- Připravit projekty na prezentaci

### Materiály
- Dokončené projekty v Tinkercad
- Testovací scénáře
- Formuláře pro peer review

### Průběh hodiny (45 min)

#### 1. Systematické testování (20 min)

**Testovací protokol:**

**Fáze 1: Základní funkčnost (5 min/projekt)**
```cpp
// Test checklist
1. Spustí se bez chyb? □
2. Reaguje na vstupy? □  
3. Ovládají se výstupy? □
4. LCD/Serial výstupy fungují? □
5. Všechny stavy systému dostupné? □
```

**Fáze 2: Boundary testing (extrémní hodnoty)**
```cpp
// Co se stane když:
- Senzor vrací 0? □
- Senzor vrací maximum (1023)? □
- Tlačítko držíme dlouho? □
- Rychle přepínáme stavy? □
- Simulujeme poruchu senzoru? □
```

**Fáze 3: User experience testing**
```cpp
// Z pohledu uživatele:
- Je jasné co projekt dělá? □
- Dá se ovládat bez instrukcí? □
- Poskytuje zpětnou vazbu? □
- Chová se předvídatelně? □
- Má užitečnou funkci? □
```

**Testovací scénáře podle projektu:**

**Smart květináč:**
```
Scénář 1: Normální provoz
1. Spusti projekt
2. Nastav vlhkost půdy na 200 (sucho)
3. Čekej - má se spustit zalévání
4. Zkontroluj že se spustilo čerpadlo
5. Nastav vlhkost na 700 (mokro)  
6. Čerpadlo se má vypnout

Scénář 2: Manuální režim
1. Stiskni tlačítko → přepnout do manuálu
2. Stiskni znovu → zapnout/vypnout zalévání
3. Dlouhé stisknutí → návrat do auto

Scénář 3: Extrémní podmínky  
1. Teplota 40°C → má přestat zalévat
2. Světlo 0 + pozdní hodina → nočních režim
```

#### 2. Peer review (15 min)

**Párové testování:**
Studenti si vymění projekty a testují navzájem podle formuláře.

**Review formulář:**
```
Projekt: ______________________
Autor: ________________________
Reviewer: ____________________

FUNKČNOST (1-5 bodů):
- Projekt se spustí bez problémů: ___
- Všechny funkce fungují: ___
- Reaguje na vstupy správně: ___

POUŽITELNOST (1-5 bodů):
- Je jasné co projekt dělá: ___
- Dá se snadno ovládat: ___
- Poskytuje jasnou zpětnou vazbu: ___

KÓD (1-5 bodů):
- Kód je čitelný a komentovaný: ___
- Logická struktura: ___
- Dobrá práce s chybami: ___

ORIGINALITA (1-5 bodů):
- Kreativní nápad: ___
- Zajímavé řešení problému: ___

CELKEM: ___/20 bodů

POZITIVNÍ:
- _________________________________
- _________________________________

NÁVRHY NA ZLEPŠENÍ:
- _________________________________
- _________________________________
```

#### 3. Finalizace a příprava na prezentaci (10 min)

**Prezentační checklist:**
- ✓ Funkční demo v Tinkercad
- ✓ Stručný popis projektu (2-3 věty)
- ✓ Hlavní funkce vypsané
- ✓ Seznam potřebných součástek
- ✓ Odhad nákladů na stavbu
- ✓ Možná vylepšení do budoucna

**Formát prezentace (3 minuty/student):**
1. **Název a účel** (30s)
   - "Můj projekt se jmenuje... a řeší problém..."
2. **Demonstrace** (90s)
   - Live ukázka funkčnosti
3. **Technické detaily** (30s)
   - Klíčové komponenty a funkce
4. **Budoucnost projektu** (30s)
   - Jak by se dal projekt rozšířit/vylepšit

**Příprava materiálů k odevzdání:**
```
Pro každý projekt připravit:
1. Tinkercad link (sdílený)
2. Komentovaný screenshot schématu
3. Výpis kódu s komentáři
4. Krátký popis (1 strana A4):
   - Účel projektu
   - Hlavní funkce  
   - Seznam součástek + ceny
   - Návod na použití
   - Možná vylepšení
```

**Troubleshooting session:**
Zbývající čas na řešení posledních problémů a dotazů před prezentací.

### Typické problémy před prezentací:

**"Projekt nefunguje!"**
- Zkontroluj všechna připojení
- Restartuj simulátor
- Zkontroluj kód na syntaktické chyby

**"Nevím co říct na prezentaci"**
- Začni proč jsi si vybral tento projekt
- Ukaž hlavní funkci
- Řekni co tě překvapilo při vývoji

**"Můj projekt je příliš jednoduchý"**
- Vysvětli proč je tvoje řešení elegantní
- Ukaž jak by se dal rozšířit
- Porovnej s podobnými řešeními

### Domácí úkol
Připravit 3-minutovou prezentaci projektu a všechny potřebné materiály k odevzdání.

### Shrnutí bloku 6
- Naučili jsme se systematický přístup k návrhu projektu
- Dokážeme převést nápad do funkčního prototypu
- Umíme integrovat více komponent do celku
- Testujeme a dokumentujeme vlastní práci
- Jsme připraveni prezentovat výsledky
