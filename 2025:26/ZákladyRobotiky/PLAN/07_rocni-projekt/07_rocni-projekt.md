# Blok 7: Ročníkový projekt (28–32)

## Hodina 28: Doladění kódu

### Cíle hodiny
- Optimalizovat kód pro výkon a spolehlivost
- Implementovat pokročilé funkce
- Přidat error handling a robustnost

### Materiály
- Dokončené projekty z bloku 6
- Referenční dokumentace pro optimalizaci
- Profiling nástroje (Serial Monitor)

### Průběh hodiny (45 min)

#### 1. Code Review a analýza výkonu (15 min)

**Systematická kontrola Python kódu:**
```python
# Checklist pro Python code review:
1. □ Všechny proměnné mají smysluplné názvy (snake_case)
2. □ Funkce mají jasný účel a jsou kratší než 50 řádků  
3. □ Žádný duplicitní kód (DRY princip)
4. □ Konstanty místo "magic numbers" (VELKÝMI_PÍSMENY)
5. □ Komentáře u složitých algoritmů
6. □ Error handling s try/except pro všechny vstupy
7. □ Správné používání global proměnných
8. □ Optimalizace smyček a list comprehensions
```

**Analýza výkonu v Pythonu:**
```python
import time

# Měření času vykonávání
start_time = time.time()
# ... kód k testování
end_time = time.time()
execution_time = (end_time - start_time) * 1000  # převod na milisekundy
print(f"Execution time: {execution_time:.2f} milliseconds")

# Monitoring využití systému (simulace)
def print_system_status():
    """Výpis stavu systému pro debugging"""
    current_time = time.time()
    print(f"System uptime: {current_time:.1f}s")
    print(f"Free memory: simulated")  # V reálném Arduino by bylo jinak
    
# Profiling funkcí
def profile_function(func, *args):
    """Změří čas vykonávání funkce"""
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"{func.__name__} took {(end-start)*1000:.2f}ms")
    return result
```

#### 2. Optimalizace a vylepšení (25 min)

**Optimalizace 1: Non-blocking operations v Pythonu**
```python
# Špatně: Blocking delays
def bad_loop():
    read_sensors()
    time.sleep(1)        # Blokuje vše na 1 sekundu!
    update_display()
    time.sleep(0.5)      # Další blokování
    check_buttons()

# Dobře: Non-blocking timing
last_sensor_read = 0
last_display_update = 0
last_button_check = 0

SENSOR_INTERVAL = 1000      # ms
DISPLAY_INTERVAL = 500      # ms
BUTTON_INTERVAL = 50        # ms

def good_loop():
    global last_sensor_read, last_display_update, last_button_check
    
    now = time.time() * 1000  # převod na milisekundy
    
    if now - last_sensor_read >= SENSOR_INTERVAL:
        read_sensors()
        last_sensor_read = now
    
    if now - last_display_update >= DISPLAY_INTERVAL:
        update_display()
        last_display_update = now
        
    if now - last_button_check >= BUTTON_INTERVAL:
        check_buttons()
        last_button_check = now
  
  if (now - lastDisplayUpdate >= DISPLAY_INTERVAL) {
    updateDisplay();
    lastDisplayUpdate = now;
  }
  
  if (now - lastButtonCheck >= BUTTON_INTERVAL) {
    checkButtons();
    lastButtonCheck = now;
  }
}
```

**Optimalizace 2: Interrupt-driven input**
```cpp
// Lepší reakce na tlačítka pomocí přerušení
volatile boolean buttonPressed = false;
volatile unsigned long buttonPressTime = 0;

void setup() {
  pinMode(BUTTON_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(BUTTON_PIN), buttonISR, FALLING);
}

void buttonISR() {
  // Debouncing v přerušení
  static unsigned long lastInterruptTime = 0;
  unsigned long interruptTime = millis();
  
  if (interruptTime - lastInterruptTime > 200) {
    buttonPressed = true;
    buttonPressTime = interruptTime;
  }
  lastInterruptTime = interruptTime;
}

void loop() {
  if (buttonPressed) {
    handleButtonPress();
    buttonPressed = false;
  }
  // ... zbytek kódu běží normálně
}
```

**Optimalizace 3: Smart sensor reading**
```cpp
// Adaptivní frekvence čtení senzorů
class SmartSensor {
private:
  int pin;
  int lastValue;
  unsigned long lastRead;
  unsigned long interval;
  int changeThreshold;
  
public:
  SmartSensor(int p, int threshold = 10) : 
    pin(p), changeThreshold(threshold), interval(1000), lastRead(0), lastValue(0) {}
  
  int read() {
    unsigned long now = millis();
    
    // Čti častěji pokud se hodnoty rychle mění
    if (now - lastRead >= interval) {
      int newValue = analogRead(pin);
      
      if (abs(newValue - lastValue) > changeThreshold) {
        interval = 250; // Rychlé čtení při změnách
      } else {
        interval = 2000; // Pomalé čtení při stabilitě
      }
      
      lastValue = newValue;
      lastRead = now;
    }
    
    return lastValue;
  }
};

// Použití
SmartSensor soilSensor(A0, 20);
SmartSensor tempSensor(A1, 5);

void loop() {
  int moisture = soilSensor.read();
  int temperature = tempSensor.read();
  // ... zbytek logiky
}
```

**Optimalizace 4: State machine improvements**
```cpp
// Pokročilejší stavový automat s historií
enum SystemState {
  INIT, MONITORING, WATERING, WAITING, MANUAL_MODE, ERROR_STATE
};

struct StateInfo {
  SystemState state;
  unsigned long enterTime;
  unsigned long totalTime;
  int entryCount;
};

StateInfo stateHistory[6];
SystemState currentState = INIT;
SystemState previousState = INIT;

void changeState(SystemState newState, const char* reason = "") {
  // Update historie předchozího stavu
  int prevIndex = (int)currentState;
  stateHistory[prevIndex].totalTime += millis() - stateHistory[prevIndex].enterTime;
  
  // Log změny stavu
  Serial.print("State: ");
  Serial.print(getStateName(currentState));
  Serial.print(" -> ");
  Serial.print(getStateName(newState));
  if (strlen(reason) > 0) {
    Serial.print(" (");
    Serial.print(reason);
    Serial.print(")");
  }
  Serial.println();
  
  // Nastav nový stav
  previousState = currentState;
  currentState = newState;
  
  // Update statistiky nového stavu
  int newIndex = (int)newState;
  stateHistory[newIndex].enterTime = millis();
  stateHistory[newIndex].entryCount++;
}

void printStatistics() {
  Serial.println("=== State Statistics ===");
  for (int i = 0; i < 6; i++) {
    Serial.print(getStateName((SystemState)i));
    Serial.print(": ");
    Serial.print(stateHistory[i].entryCount);
    Serial.print(" entries, ");
    Serial.print(stateHistory[i].totalTime / 1000);
    Serial.println("s total");
  }
}
```

#### 3. Error handling a robustnost (5 min)

**Comprehensive error handling:**
```cpp
enum ErrorCode {
  NO_ERROR = 0,
  SENSOR_TIMEOUT,
  SENSOR_OUT_OF_RANGE,
  ACTUATOR_FAILURE,
  LOW_BATTERY,
  MEMORY_LOW,
  COMMUNICATION_ERROR
};

ErrorCode lastError = NO_ERROR;
unsigned long errorTime = 0;
int errorCount = 0;

boolean readSensorSafely(int pin, int* value, int minExpected, int maxExpected) {
  static int consecutiveErrors = 0;
  
  // Timeout pro čtení
  unsigned long startTime = millis();
  int reading = analogRead(pin);
  
  if (millis() - startTime > 100) { // Timeout
    setError(SENSOR_TIMEOUT);
    return false;
  }
  
  // Kontrola rozsahu
  if (reading < minExpected || reading > maxExpected) {
    consecutiveErrors++;
    if (consecutiveErrors > 5) {
      setError(SENSOR_OUT_OF_RANGE);
      return false;
    }
    // Použij poslední známou dobrou hodnotu
    return true;
  }
  
  consecutiveErrors = 0;
  *value = reading;
  return true;
}

void setError(ErrorCode error) {
  if (error != lastError) {
    lastError = error;
    errorTime = millis();
    errorCount++;
    
    Serial.print("ERROR: ");
    Serial.println(getErrorDescription(error));
    
    // Trigger error handling
    handleError(error);
  }
}

void handleError(ErrorCode error) {
  switch (error) {
    case SENSOR_TIMEOUT:
      // Zkus restartovat senzor
      reinitializeSensors();
      break;
      
    case SENSOR_OUT_OF_RANGE:
      // Přepni na záložní senzor nebo safe mode
      switchToSafeMode();
      break;
      
    case ACTUATOR_FAILURE:
      // Vypni všechny aktátory
      emergencyStop();
      break;
      
    case LOW_BATTERY:
      // Úsporný režim
      enterPowerSaveMode();
      break;
      
    default:
      // Obecné error handling
      switchToSafeMode();
      break;
  }
}
```

### Domácí úkol
Implementovat všechny optimalizace do vlastního projektu a otestovat výkon před/po optimalizaci.

---

## Hodina 29: Testování v simulátoru

### Cíle hodiny
- Provést kompletní testování všech funkcí projektu
- Simulovat reálné podmínky použití
- Identifikovat a opravit skryté chyby

### Materiály
- Optimalizované projekty z hodiny 28
- Testovací scénáře a checklists
- Performance monitoring nástroje

### Průběh hodiny (45 min)

#### 1. Systematické funkční testování (20 min)

**Test Suite pro robotický projekt:**
```cpp
// Automatizované testování funkcí
class ProjectTester {
private:
  int testsRun = 0;
  int testsPassed = 0;
  int testsFailed = 0;
  
public:
  void runAllTests() {
    Serial.println("=== Starting Test Suite ===");
    
    // Základní testy
    testSensorReadings();
    testActuatorControl();  
    testStateMachine();
    testErrorHandling();
    testUserInterface();
    testPerformance();
    
    printTestResults();
  }
  
private:
  boolean assert(boolean condition, const char* testName) {
    testsRun++;
    if (condition) {
      testsPassed++;
      Serial.print("[PASS] ");
    } else {
      testsFailed++;
      Serial.print("[FAIL] ");
    }
    Serial.println(testName);
    return condition;
  }
  
  void testSensorReadings() {
    Serial.println("\n--- Sensor Tests ---");
    
    // Test 1: Senzory vrací hodnoty v očekávaném rozsahu
    int soilValue = analogRead(SOIL_PIN);
    assert(soilValue >= 0 && soilValue <= 1023, "Soil sensor range check");
    
    // Test 2: Senzory reagují na změny
    int temp1 = readTemperature();
    delay(100);
    int temp2 = readTemperature(); 
    assert(abs(temp1 - temp2) < 100, "Temperature stability check");
    
    // Test 3: Filtrování funguje
    int filtered = getFilteredSoilMoisture();
    assert(filtered != 0, "Sensor filtering working");
  }
  
  void testActuatorControl() {
    Serial.println("\n--- Actuator Tests ---");
    
    // Test 1: LED kontrola
    digitalWrite(LED_PIN, HIGH);
    delay(100);
    assert(digitalRead(LED_PIN) == HIGH, "LED can be turned on");
    digitalWrite(LED_PIN, LOW);
    assert(digitalRead(LED_PIN) == LOW, "LED can be turned off");
    
    // Test 2: Motor/Relay kontrola
    digitalWrite(PUMP_RELAY, HIGH);
    delay(50);
    boolean pumpWorking = digitalRead(PUMP_RELAY) == HIGH;
    digitalWrite(PUMP_RELAY, LOW);
    assert(pumpWorking, "Pump relay control");
  }
  
  void testStateMachine() {
    Serial.println("\n--- State Machine Tests ---");
    
    SystemState originalState = currentState;
    
    // Test 1: State transitions
    changeState(MONITORING);
    assert(currentState == MONITORING, "State change to MONITORING");
    
    changeState(WATERING);
    assert(currentState == WATERING, "State change to WATERING");
    assert(previousState == MONITORING, "Previous state tracking");
    
    // Restore original state
    changeState(originalState);
  }
  
  void testErrorHandling() {
    Serial.println("\n--- Error Handling Tests ---");
    
    // Test 1: Error detection
    setError(SENSOR_TIMEOUT);
    assert(lastError == SENSOR_TIMEOUT, "Error code setting");
    
    // Test 2: Error recovery
    clearError();
    assert(lastError == NO_ERROR, "Error clearing");
  }
};

ProjectTester tester;

// Spustit testy při startu (pro debugging)
void runDiagnostics() {
  tester.runAllTests();
}
```

#### 2. Stress testing a edge cases (15 min)

**Stress Test Scenarios:**
```cpp
void stressTest() {
  Serial.println("=== Stress Test Starting ===");
  
  // Test 1: Rychlé změny vstupů
  for (int i = 0; i < 100; i++) {
    simulateButtonPress();
    delay(10);
  }
  Serial.println("Rapid button press test completed");
  
  // Test 2: Extrémní hodnoty senzorů
  testExtremeValues();
  
  // Test 3: Dlouhodobý běh
  longRunTest(300000); // 5 minut
  
  // Test 4: Přetížení paměti
  memoryStressTest();
}

void testExtremeValues() {
  Serial.println("Testing extreme sensor values...");
  
  // Simulace extrémních hodnot
  struct TestCase {
    int soilValue;
    float tempValue;  
    int lightValue;
    const char* description;
  };
  
  TestCase extremeCases[] = {
    {0, -20, 0, "All minimum values"},
    {1023, 60, 1023, "All maximum values"}, 
    {512, 0, 0, "Mixed extreme values"},
    {0, 25, 1023, "Conflicting conditions"},
    {1023, 25, 0, "Opposite extremes"}
  };
  
  for (int i = 0; i < 5; i++) {
    Serial.print("Testing: ");
    Serial.println(extremeCases[i].description);
    
    // Simulace hodnot (v reálném HW by se použily proměnné)
    simulateSensorValues(extremeCases[i].soilValue, 
                        extremeCases[i].tempValue,
                        extremeCases[i].lightValue);
    
    // Spusti jeden cyklus logiky
    processLogic();
    
    // Zkontroluj že systém nehavaroval
    if (currentState == ERROR_STATE) {
      Serial.println("System entered error state - investigating...");
    }
    
    delay(1000);
  }
}

void longRunTest(unsigned long duration) {
  Serial.print("Long run test for ");
  Serial.print(duration / 1000);
  Serial.println(" seconds...");
  
  unsigned long startTime = millis();
  unsigned long lastMemCheck = 0;
  int minFreeMemory = 999999;
  
  while (millis() - startTime < duration) {
    // Normální běh systému
    loop();
    
    // Každých 30 sekund kontrola paměti
    if (millis() - lastMemCheck > 30000) {
      int freeMemory = getFreeMemory();
      if (freeMemory < minFreeMemory) {
        minFreeMemory = freeMemory;
      }
      
      Serial.print("Memory check: ");
      Serial.print(freeMemory);
      Serial.println(" bytes free");
      
      lastMemCheck = millis();
    }
    
    // Kontrola že systém stále reaguje
    if (millis() % 60000 == 0) { // Každou minutu
      Serial.println("System still responsive");
    }
  }
  
  Serial.print("Long run completed. Minimum free memory: ");
  Serial.println(minFreeMemory);
}
```

#### 3. Real-world scenario testing (10 min)

**Reálné scénáře použití:**
```cpp
void realWorldScenarios() {
  Serial.println("=== Real World Scenarios ===");
  
  // Scénář 1: Týden dovolené (nikdo doma)
  weekVacationScenario();
  
  // Scénář 2: Výpadek proudu a restart
  powerOutageScenario();
  
  // Scénář 3: Zimní podmínky
  winterConditionsScenario();
  
  // Scénář 4: Letní vedra  
  summerHeatScenario();
}

void weekVacationScenario() {
  Serial.println("Scenario: Week vacation (7 days unattended)");
  
  // Simulace týdne bez zásahu uživatele
  unsigned long simulatedTime = 0;
  const unsigned long oneDay = 86400000; // 24 hodin v ms
  
  for (int day = 1; day <= 7; day++) {
    Serial.print("Day ");
    Serial.print(day);
    Serial.print(": ");
    
    // Simulace denního cyklu
    for (int hour = 0; hour < 24; hour++) {
      // Ranní světlo
      if (hour >= 6 && hour <= 8) {
        simulateLightLevel(800);
      }
      // Polední slunce  
      else if (hour >= 12 && hour <= 14) {
        simulateLightLevel(1000);
        simulateTemperature(28);
      }
      // Večer
      else if (hour >= 18 && hour <= 20) {
        simulateLightLevel(400);
      }
      // Noc
      else {
        simulateLightLevel(50);
        simulateTemperature(18);
      }
      
      // Postupné snižování vlhkosti půdy
      int soilMoisture = 800 - (day * 100) - (hour * 2);
      simulateSoilMoisture(max(soilMoisture, 100));
      
      // Spusť logiku systému
      processLogic();
      
      // Rychlá simulace (jinak by to trvalo týden!)
      simulatedTime += 3600000; // +1 hodina
    }
    
    // Denní report
    Serial.print("Watering events: ");
    Serial.print(getDayWateringCount());
    Serial.print(", System health: ");
    Serial.println(getSystemHealthScore());
    
    resetDayCounters();
  }
  
  Serial.println("Week vacation scenario completed");
}

void powerOutageScenario() {
  Serial.println("Scenario: Power outage and restart");
  
  // Uložit současný stav
  saveSystemState();
  
  // Simulace výpadku (restart Arduina)
  Serial.println("Simulating power loss...");
  initializeSystem(); // Jako při startu
  
  // Test obnovení stavu
  if (loadSystemState()) {
    Serial.println("System state successfully restored");
  } else {
    Serial.println("Failed to restore state - using defaults");
  }
  
  // Test že systém funguje normálně
  for (int i = 0; i < 10; i++) {
    processLogic();
    delay(1000);
  }
  
  Serial.println("Power outage recovery test completed");
}
```

### Testovací protokol pro odevzdání:
```
Project Testing Report
=====================
Project Name: ________________
Student: ____________________
Date: _______________________

FUNCTIONAL TESTS:          PASS/FAIL
- Sensor readings          □ / □
- Actuator control         □ / □  
- State machine           □ / □
- Error handling          □ / □
- User interface          □ / □

PERFORMANCE TESTS:         RESULT
- Memory usage            ______ bytes free
- Response time           ______ ms avg
- Long run stability      ______ hours tested

STRESS TESTS:              PASS/FAIL
- Extreme values          □ / □
- Rapid inputs           □ / □
- Memory stress          □ / □

REAL-WORLD SCENARIOS:      PASS/FAIL
- Week unattended        □ / □
- Power outage recovery  □ / □
- Environmental extremes □ / □

BUGS FOUND AND FIXED:
1. _________________________________
2. _________________________________
3. _________________________________

PERFORMANCE IMPROVEMENTS:
1. _________________________________
2. _________________________________

OVERALL SCORE: ___/10
```

### Domácí úkol
Dokončit všechny testy a opravit zjištěné chyby. Připravit testovací report.

---

## Hodina 30: Dokumentace

### Cíle hodiny
- Vytvořit kompletní dokumentaci projektu
- Naučit se profesionální způsob dokumentování
- Připravit materiály pro prezentaci a domácí stavbu

### Materiály
- Otestované a funkční projekty
- Šablony dokumentace
- Nástroje pro screenshot a diagram

### Průběh hodiny (45 min)

#### 1. Struktura projektové dokumentace (15 min)

**Profesionální dokumentace obsahuje:**

```markdown
# [NÁZEV PROJEKTU]

## 1. Přehled projektu
- Účel a cíl projektu
- Hlavní funkce
- Cílová skupina uživatelů

## 2. Technické specifikace  
- Seznam komponent
- Schéma zapojení
- Pin assignment
- Napájecí požadavky

## 3. Softwarová dokumentace
- Struktura kódu
- Stavový diagram
- API/funkce reference
- Nastavitelné parametry

## 4. Návod k použití
- Instalace a setup
- Základní ovládání
- Troubleshooting
- Maintenance

## 5. Výsledky testování
- Test reports
- Performance metriky
- Známé limity

## 6. Přílohy
- Kompletní kód
- Nákupní seznam
- Možná vylepšení
```

#### 2. Praktické vytváření dokumentace (25 min)

**Template pro projektovou dokumentaci:**

```markdown
# Smart Flower Care System
*Automatický systém péče o pokojové rostliny*

## 1. Přehled projektu

### Účel
Automatizace zalévání pokojových rostlin na základě měření vlhkosti půdy, teploty a světelných podmínek.

### Hlavní funkce
- ✅ Automatické měření vlhkosti půdy
- ✅ Teplotní monitoring
- ✅ Světelný senzor pro optimalizace
- ✅ Automatické zalévání při suchu
- ✅ LCD displej s informacemi
- ✅ Manuální ovládání tlačítkem  
- ✅ Chytrá logika podle denní doby
- ✅ Statistiky a error reporting

### Cílová skupina
Milovníci pokojových rostlin, kteří cestují nebo zapomínají zalévat.

## 2. Technické specifikace

### Seznam komponent
| Komponenta | Typ | Cena (Kč) | Účel |
|------------|-----|-----------|------|
| Arduino Uno R3 | Mikrokontrolér | 450 | Hlavní řídící jednotka |
| Soil Moisture Sensor | Analogový | 80 | Měření vlhkosti půdy |
| TMP36 | Teplotní senzor | 45 | Měření teploty |
| LDR + 10kΩ resistor | Fotorezistor | 25 | Světelný senzor |
| LCD 16×2 + I2C | Displej | 120 | Zobrazení informací |
| Relay modul 5V | Spínač | 65 | Ovládání čerpadla |
| Submersible pump 5V | Čerpadlo | 180 | Zalévání |
| Push button | Tlačítko | 15 | Manuální ovládání |
| LED (červená, zelená) | Indikace | 10 | Vizuální signalizace |
| Breadboard + vodiče | Propojení | 85 | Prototyp |
| **CELKEM** | | **1075 Kč** | |

### Schéma zapojení
```
Arduino Uno Pin Assignment:
- A0: Soil Moisture Sensor (OUT)
- A1: TMP36 Temperature Sensor (OUT)  
- A2: LDR Light Sensor (OUT)
- A4: LCD SDA (I2C)
- A5: LCD SCL (I2C)
- D2: Button Input (INPUT_PULLUP)
- D7: Relay Control (OUTPUT)
- D8: Green LED Status (OUTPUT)
- D9: Red LED Warning (OUTPUT)
- D10: Buzzer (optional)
- 5V: VCC pro všechny komponenty
- GND: Společná zem
```

### Napájecí požadavky
- Arduino Uno: 5V, 500mA (přes USB nebo DC jack)
- Čerpadlo: 5V, 200mA (přes relay)
- Ostatní komponenty: < 100mA celkem
- **Doporučeno:** 5V 2A adapter

## 3. Softwarová dokumentace

### Struktura kódu
```cpp
// Hlavní sekce kódu:
1. Configuration & Constants (řádky 1-30)
2. Global Variables (řádky 31-50)  
3. Setup Function (řádky 51-80)
4. Main Loop (řádky 81-120)
5. State Machine Handlers (řádky 121-300)
6. Sensor Functions (řádky 301-400)
7. Actuator Functions (řádky 401-450)
8. Utility Functions (řádky 451-500)
```

### Stavový diagram
```
[INIT] → [MONITORING] ↔ [MANUAL_MODE]
   ↓           ↓
[ERROR] ← [WATERING] → [WAITING]
   ↑           ↑           ↓
   └───────────┴───────────┘
```

### Klíčové funkce
```cpp
// Hlavní funkce API:
void setup()                    // Inicializace systému
void loop()                     // Hlavní smyčka
void changeState(SystemState)   // Změna stavu
boolean shouldWater()           // Rozhodovací logika
void startWatering(int duration) // Spuštění zalévání
int readFilteredSensor(int pin) // Filtrované čtení
void updateDisplay()            // Aktualizace LCD
void handleError(ErrorCode)     // Error handling
```

### Nastavitelné parametry
```cpp
// Prahové hodnoty (lze upravit):
const int DRY_THRESHOLD = 300;      // Práh suché půdy
const int WET_THRESHOLD = 600;      // Práh vlhké půdy  
const int WATERING_TIME = 5000;     // Doba zalévání (ms)
const int MIN_TEMP = 5;             // Min teplota pro zalévání
const int MAX_TEMP = 35;            // Max teplota pro zalévání
const unsigned long WAIT_TIME = 3600000; // Čekání mezi zalíváním
```

## 4. Návod k použití

### První spuštění
1. **Připojení komponent** podle schématu zapojení
2. **Upload kódu** do Arduino IDE
3. **Kalibrace senzorů:**
   - Soil sensor: ponořit do suché/mokré půdy, zapsat hodnoty
   - Light sensor: změřit minimum/maximum světla
   - Temperature sensor: zkontrolovat pokojovou teplotu
4. **Test funkcí:** spustit diagnostiku příkazem v Serial Monitor

### Základní ovládání  
- **Automatický režim:** Systém běží samostatně
- **Tlačítko krátké:** Přepnutí do manuálního režimu
- **Tlačítko v manuálu:** Zapnutí/vypnutí zalévání
- **Tlačítko dlouhé:** Návrat do automatického režimu

### LCD displej informace
```
Řádek 1: Aktuální stav systému
Řádek 2: Hodnoty sensorů / chybové hlášení

Příklady:
"AUTO: Monitoring"     "MANUAL: Watering" 
"T:23°C S:45% L:678"   "ERROR: Sensor fail"
```

### Troubleshooting

| Problém | Možná příčina | Řešení |
|---------|---------------|--------|
| LCD nezobrazuje | Špatné I2C připojení | Zkontroluj A4/A5 piny |
| Nereaguje na tlačítko | Špatný pull-up | Zkontroluj INPUT_PULLUP |
| Čerpadlo neběží | Relay problém | Zkontroluj 5V napájení |
| Špatná čtení sensorů | Špatná kalibrace | Přenastavit prahové hodnoty |
| Systém zamrzne | Memory overflow | Restartuj, zkontroluj kód |

## 5. Výsledky testování

### Performance Metriky
- **Response Time:** < 100ms na vstup uživatele
- **Memory Usage:** 1250 bytes RAM (60% využito)
- **Power Consumption:** 0.8W při monitoring, 1.4W při zalévání
- **Uptime Test:** 168 hodin bez problémů

### Test Results Summary
```
✅ Functional Tests:     10/10 passed
✅ Performance Tests:    95% rating
✅ Stress Tests:         8/10 passed  
✅ Real-world Scenarios: 9/10 passed
⚠️  Known Issues:        2 minor bugs
```

### Známé limity
1. **Zimní podmínky:** Nefunguje pod 5°C
2. **Vzdálené monitorování:** Pouze lokální LCD
3. **Množství vody:** Pevně nastavená doba zalévání
4. **Více rostlin:** Podporuje pouze jednu rostlinu

## 6. Přílohy

### A. Kompletní kód
*[Zde by byl celý kód, v reálném dokumentu]*

### B. Nákupní seznam s odkazy
- Arduino Uno: www.example.com/arduino-uno
- Soil Sensor: www.example.com/soil-sensor
- [... další komponenty]

### C. Možná vylepšení
**Verze 2.0 plány:**
- [ ] WiFi modul pro remote monitoring
- [ ] Webové rozhraní  
- [ ] Podpora více rostlin
- [ ] Kamera pro monitoring růstu
- [ ] Solární napájení
- [ ] Mobilní aplikace
- [ ] Datalogging na SD kartu
- [ ] Push notifikace

### D. 3D modely
- Krabička pro Arduino: `arduino_case.stl`
- Držák senzorů: `sensor_mount.stl`  
- Kryt čerpadla: `pump_cover.stl`

### E. Fotodokumentace
*[Screenshots z Tinkercad, fotky prototypu, atd.]*
```

#### 3. Finalizace a kontrola (5 min)

**Checklist dokončené dokumentace:**
- ✓ Všechny sekce vyplněné
- ✓ Schéma zapojení jasné a přesné
- ✓ Kód je komentovaný a čitelný  
- ✓ Testovací výsledky úplné
- ✓ Nákupní seznam s cenami
- ✓ Troubleshooting guide
- ✓ Screenshots/fotky přiloženy
- ✓ Kontaktní informace na autora

### Domácí úkol
Dokončit kompletní dokumentaci vlastního projektu podle template.

---

## Hodina 31: Prezentace návrhu

### Cíle hodiny
- Prezentovat dokončený projekt před ostatními
- Naučit se efektivní prezentaci technického projektu
- Získat zpětnou vazbu a návrhy na vylepšení

### Materiály
- Dokončené a zdokumentované projekty
- Projektory/obrazovky pro prezentace
- Hodnotící formuláře
- Časomíry pro prezentace

### Průběh hodiny (45 min)

#### 1. Příprava na prezentaci (10 min)

**Struktura 5-minutové prezentace:**
```
1. Úvod (30s)
   - Jméno, název projektu
   - Problém, který řeší
   
2. Demo (2 min)
   - Live ukázka funkčnosti
   - Hlavní features
   
3. Technické detaily (1.5 min)
   - Klíčové komponenty
   - Zajímavé řešení
   - Překonané výzvy
   
4. Výsledky (30s)
   - Co fungovalo dobře
   - Co by se dalo vylepšit
   
5. Q&A (30s)
   - Zodpovězení dotazů
```

**Prezentační tipy:**
- **Mluvit pomalu a zřetelně** - techničtí obsah je složitý
- **Ukázat, nejen říct** - demo je důležitější než teorie
- **Připravit se na dotazy** - většinou se ptají na problémy
- **Být hrdý na svou práci** - i malé projekty jsou úspěch

#### 2. Studentské prezentace (30 min)

**Příklad prezentace - Smart květináč:**

*Dobrý den, jmenuji se [Jméno] a můj projekt se jmenuje Smart Flower Care System. Řeší problém zapomínání zalévat pokojové rostliny.*

*[DEMO - spusti Tinkercad]*
*Tady vidíte můj systém v akci. Arduino načítá data ze tří senzorů - vlhkost půdy, teplotu a světlo. LCD displej ukazuje aktuální hodnoty. Když půda vyschne pod tuto úroveň* [ukáže na simulátoru]*, systém automaticky zapne čerpadlo na 5 sekund.*

*Můžu také přepnout do manuálního režimu tímto tlačítkem a ovládat zalévání ručně.*

*[TECHNICKÉ DETAILY]*
*Nejzajímavější část byla implementace stavového automatu s pěti stavy a chytré logiky, která nezalévá v noci nebo při extrémních teplotách. Největší výzva bylo filtrování signálu ze soil sensoru, který byl velmi šumový.*

*[VÝSLEDKY]*  
*Systém jsem testoval simulací týdne dovolené a zvládl to bez problémů. V budoucnu bych přidal WiFi pro remote monitoring.*

*Máte nějaké dotazy?*

**Hodnotící kritéria pro publikum:**
```
Projekt: _______________________
Presenter: ____________________

TECHNICKÁ KVALITA (1-5):
- Funkčnost projektu: ⭐⭐⭐⭐⭐
- Složitost řešení: ⭐⭐⭐⭐⭐  
- Originalita: ⭐⭐⭐⭐⭐

PREZENTACE (1-5):
- Jasnost výkladu: ⭐⭐⭐⭐⭐
- Demo kvalita: ⭐⭐⭐⭐⭐
- Zodpovězení dotazů: ⭐⭐⭐⭐⭐

PRAKTIČNOST (1-5):
- Řeší reálný problém: ⭐⭐⭐⭐⭐
- Možnost realizace: ⭐⭐⭐⭐⭐

CELKOVÝ DOJEM: ⭐⭐⭐⭐⭐

NEJLEPŠÍ ČÁSTI:
- _______________________________
- _______________________________

NÁVRHY NA ZLEPŠENÍ:
- _______________________________  
- _______________________________
```

#### 3. Zpětná vazba a diskuse (5 min)

**Po každé prezentaci:**
- 2-3 technické otázky od ostatních studentů
- 1 návrh na vylepšení
- Pozitivní komentář k nejlepší části

**Možné otázky:**
- "Jak dlouho vydrží baterie?"
- "Co se stane když selže senzor?"
- "Dalo by se to použít i venku?"
- "Kolik to stálo vyrobit?"
- "Jak dlouho ti to trvalo naprogramovat?"

**Společná diskuse na konci:**
- Který projekt byl nejoríginálnější?
- Které řešení bylo nejelegantnější?
- Co vás překvapilo?
- Která prezentace byla nejlepší?

### Hodnotící protokol pro učitele:

**Individuální hodnocení:**
```
Student: ________________________
Projekt: ________________________

TECHNICKÉ KRITÉRIA (60 bodů):
□ Funkcionalita (15b): projekt plně funguje
□ Složitost (10b): odpovídající úroveň obtížnosti  
□ Kód kvali∈ta (10b): čistý, komentovaný kód
□ Hardware (10b): správné zapojení komponentů
□ Dokumentace (15b): kompletní a jasná

SOFT SKILLS (25 bodů):
□ Prezentace (10b): jasná a strukturovaná
□ Demo (10b): funkční ukázka
□ Komunikace (5b): zodpovězení dotazů

KREATIVITA & INOVACE (15 bodů):
□ Originalita (10b): jedinečný nápad/řešení
□ Praktičnost (5b): řeší reálný problém

CELKEM: ___/100 bodů

SLOVNÍ HODNOCENÍ:
_________________________________
_________________________________
_________________________________
```

### Domácí úkol
Na základě zpětné vazby upravit dokumentaci projektu a připravit finální verzi.

---

## Hodina 32: Doporučení pro stavbu doma

### Cíle hodiny
- Převést simulační projekt na reálnou hardware stavbu
- Poskytnout praktické rady pro nákup komponentů
- Připravit studenty na případné problémy při realizaci

### Materiály  
- Katalogy elektronických součástek
- Ukázky reálných komponentů
- Nástroje a příslušenství pro stavbu
- Troubleshooting guides

### Průběh hodiny (45 min)

#### 1. Od simulace k realitě (15 min)

**Hlavní rozdíly mezi Tinkercad a reálným světem:**

| Tinkercad | Reálný svět | Řešení |
|-----------|-------------|--------|
| Perfektní signály | Šum, interference | Filtrování, shielding |
| Neomezené napájení | Omezený proud/napětí | Proper power supply |
| Okamžité připojení | Loose connections | Pájení, terminály |
| Bez fyziky | Gravitace, vibrace | Mechanická konstrukce |
| Ideální komponenty | Tolerance, degradace | Kalibrace, náhradní díly |

**Praktické přizpůsobení projektu:**
```cpp
// Tinkercad kód:
int sensorValue = analogRead(A0);

// Reálný svět - s filtrováním a validací:
int readRealSensor(int pin) {
  // Více čtení pro stability
  long sum = 0;
  int validReadings = 0;
  
  for (int i = 0; i < 10; i++) {
    int reading = analogRead(pin);
    
    // Filtr zjevně špatných hodnot
    if (reading >= 0 && reading <= 1023) {
      sum += reading;
      validReadings++;
    }
    delay(10);
  }
  
  if (validReadings == 0) {
    return -1; // Error
  }
  
  return sum / validReadings;
}
```

#### 2. Nákupní průvodce a sourcing (20 min)

**Kde nakupovat komponenty:**

**Tuzemské e-shopy:**
- **GM Electronic** (gme.cz) - široký výběr, rychlé dodání
- **Santy** (santy.cz) - Arduino a robotika focus
- **TME** (tme.eu) - profesionální komponenty
- **Laskakit** (laskakit.cz) - český Arduino shop

**Mezinárodní:**
- **AliExpress** - nejlevnější, dlouhé dodání (2-4 týdny)
- **Amazon** - rychlé dodání, dražší
- **Mouser/Digikey** - profesionální, přesné specifikace

**Nákupní strategie:**
```
Nákupní priority:
1. KVALITA: Arduino, power supply, critical sensors
   → Koupit lokálně od ověřeného prodejce
   
2. STANDARD: Rezistory, LED, basic components  
   → AliExpress kit, 10x levnější
   
3. MECHANICAL: 3D printed parts, enclosures
   → DIY nebo local 3D print service
   
4. TOOLS: Soldering iron, multimeter
   → Investice na dlouho, koupit kvalitní
```

**Cenový benchmark pro Smart květináč:**
```
TINKERCAD ESTIMATE: 1075 Kč
REAL WORLD COSTS:

Budget verze (AliExpress):
- Arduino Uno clone: 150 Kč  
- Sensor kit (10+ sensors): 200 Kč
- Relay module: 30 Kč
- LCD + I2C: 60 Kč
- Pump + tubing: 80 Kč
- Breadboard kit: 100 Kč
- Vodiče, resistory: 50 Kč
TOTAL: 670 Kč (37% úspora)

Premium verze (originál):
- Arduino Uno R3: 450 Kč
- Quality sensors: 300 Kč  
- Professional relay: 80 Kč
- Quality pump: 250 Kč
- Enclosure + mounting: 200 Kč
- Tools (soldering): 400 Kč
TOTAL: 1680 Kč (+56% náklady)
```

#### 3. Praktická realizace a troubleshooting (10 min)

**Step-by-step realizace:**

**Fáze 1: Získání komponentů (1-2 týdny)**
```
Týden 1: Objednat Arduino + základní komponenty
Týden 2: Objednat specifické sensory a aktory
Meanwhile: Připravit tools, workspace, dokumentaci
```

**Fáze 2: Prototyp na breadboard (víkend 1)**
```
1. Fyzicky zkontroluj všechny komponenty
2. Začni s Arduino + LCD - basic connection test
3. Postupně přidávej sensory jeden po jednom  
4. Testuj každý sensor samostatně před integrací
5. Nakonec přidej aktory (pump, relays)
```

**Fáze 3: Software adaptace (víkend 2)**
```
1. Upload původní Tinkercad kód
2. Upravuj prahové hodnoty podle reálných sensorů
3. Přidej více error handling pro real-world podmínky
4. Implementuj calibration routine pro uživatele
5. Extensive testing různých podmínek
```

**Fáze 4: Finální konstrukce (víkend 3)**
```
1. Design a print/build enclosure
2. Permanent connections (pájení nebo terminály)
3. Cable management, strain relief
4. Final testing a validace všech funkcí
5. Dokumentace real-world differences
```

**Časté problémy a řešení:**

| Problém | Symptom | Debug | Řešení |
|---------|---------|-------|--------|
| **Loose connections** | Intermittent readings | Wiggle test | Solder or better terminals |
| **Power issues** | Random resets | Measure voltages | Better PSU, decoupling caps |
| **Sensor drift** | Values change over time | Compare with reference | Calibration routine |
| **EMI interference** | Noisy readings | Shield/filter | Twisted pairs, ferrites |
| **Mechanical failure** | Pump stops working | Visual inspection | Redundancy, maintenance |

**Real-world troubleshooting toolkit:**
```cpp
// Debug helper functions pro reálný hardware
void systemDiagnostics() {
  Serial.println("=== SYSTEM DIAGNOSTICS ===");
  
  // Power supply check
  Serial.print("VCC voltage: ");
  Serial.println(readVCC(), 3);
  
  // Memory check
  Serial.print("Free RAM: ");
  Serial.println(getFreeRam());
  
  // Sensor sanity check
  for (int pin = A0; pin <= A5; pin++) {
    Serial.print("A");
    Serial.print(pin - A0);
    Serial.print(": ");
    int reading = analogRead(pin);
    Serial.print(reading);
    if (reading == 0 || reading == 1023) {
      Serial.print(" (CHECK CONNECTION!)");
    }
    Serial.println();
  }
  
  // Digital pins check
  for (int pin = 2; pin <= 13; pin++) {
    pinMode(pin, INPUT_PULLUP);
    Serial.print("D");
    Serial.print(pin);
    Serial.print(": ");
    Serial.println(digitalRead(pin) ? "HIGH" : "LOW");
  }
}

long readVCC() {
  // Read 1.1V reference against AVcc
  ADMUX = _BV(REFS0) | _BV(MUX3) | _BV(MUX2) | _BV(MUX1);
  delay(2);
  ADCSRA |= _BV(ADSC);
  while (bit_is_set(ADCSRA,ADSC));
  
  long result = ADCL;
  result |= ADCH<<8;
  result = 1125300L / result;
  return result;
}
```

### Závěrečné doporučení pro studenty:

**"Maker Mindset" pro domácí realizaci:**
1. **Start Simple:** Začni s minimální funkčností
2. **Test Early:** Každá změna = okamžitý test  
3. **Document Everything:** Fotky, notes, version control
4. **Plan for Failure:** Backup komponenty, alternative solutions
5. **Learn from Others:** Online communities, forums
6. **Iterate:** Verze 1.0 nebude perfektní, to je OK!

**Kontaktní informace pro podporu:**
- Školní email pro technické dotazy
- Discord/online komunita pro troubleshooting
- Recommended YouTube channels a tutorials
- Local maker spaces a fab labs

### Domácí "úkol" (volitelný):
Realizovat fyzickou verzi projektu během prázdnin a zdokumentovat proces včetně problémů a řešení.

### Shrnutí bloku 7
- Optimalizovali jsme kód pro reálné nasazení
- Naučili jsme se systematicky testovat komplexní systémy
- Vytvořili jsme profesionální dokumentaci
- Prezentovali jsme výsledky své práce
- Připravili jsme se na realizaci v reálném světě
- Získali jsme kompletní zkušenost s vývojem robotického projektu
