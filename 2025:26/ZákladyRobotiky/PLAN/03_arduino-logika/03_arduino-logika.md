# Blok 3: Arduino logika a kód (11–13)

## Hodina 11: Úvod do programování (proměnné, podmínky)

### Cíle hodiny
- Pochopit koncept proměnných v programování
- Naučit se používat podmínky (if-else)
- Aplikovat logiku v Arduino kódu

### Materiály
- Tinkercad Circuits s Arduino projektem
- Pracovní listy s příklady kódu
- Referenční karta Arduino funkcí

### Průběh hodiny (45 min)

#### 1. Co jsou proměnné? (15 min)
**Analogie:** Proměnná = šuplík s nálepkou
- **Příklad z reálného života:**
  - "věk" = 10
  - "jméno" = "Tomáš"
  - "teplota" = 25

**Typy proměnných v Pythonu:**
```python
cislo = 42              # Celé číslo (integer)
stav = True             # Pravda/nepravda (boolean)
teplota = 23.5          # Desetinné číslo (float)
pismeno = 'A'           # Jeden znak (string)
```

**Praktický příklad:**
```python
import arduino
import time

# Nastavení proměnných
led_pin = 13             # Pin s LED
delay_time = 1.0         # Doba čekání v sekundách
led_state = False        # Stav LED (zapnuto/vypnuto)

def setup():
    arduino.pin_mode(led_pin, arduino.OUTPUT)

def loop():
    global led_state
    arduino.digital_write(led_pin, arduino.HIGH if led_state else arduino.LOW)
    led_state = not led_state  # Překlopení stavu
    time.sleep(delay_time)

# Spuštění
setup()
while True:
    loop()
```

#### 2. Podmínky - if/else (20 min)
**Analogie:** "JESTLIŽE... PAK... JINAK..."

**Základní struktura:**
```python
if podminka:
    # Co se má stát, když je podmínka pravdivá
    pass
else:
    # Co se má stát, když je podmínka nepravdivá
    pass
```

**Operátory porovnání v Pythonu:**
- `==` je rovno
- `!=` není rovno  
- `>` větší než
- `<` menší než
- `>=` větší nebo rovno
- `<=` menší nebo rovno

**Praktický příklad - inteligentní LED:**
```python
import arduino
import time

button_pin = 2
led_pin = 13

def setup():
    arduino.pin_mode(button_pin, arduino.INPUT_PULLUP)
    arduino.pin_mode(led_pin, arduino.OUTPUT)

def loop():
    # Invertujeme kvůli pull-up rezistoru
    button_pressed = not arduino.digital_read(button_pin)
    
    if button_pressed:
        arduino.digital_write(led_pin, arduino.HIGH)  # Zapni LED
    else:
        arduino.digital_write(led_pin, arduino.LOW)   # Vypni LED

# Spuštění
setup()
while True:
    loop()
```

#### 3. Logické operátory (10 min)
**Kombinování podmínek v Pythonu:**
- `and` AND (oba musí být pravda)
- `or` OR (alespoň jeden musí být pravda)  
- `not` NOT (opak)

**Příklad:**
```python
if button_pressed and led_state:
    # LED je zapnutá A tlačítko je stisknuto
    pass

if teplota > 30 or vlhkost < 20:
    # Teplota je vysoká NEBO vlhkost je nízká
    pass
```

### Domácí úkol
Vytvoř program pro LED, která bliká rychle když je tlačítko stisknuto, a pomalu když není.

---

## Hodina 12: Blokové programování v Tinkercad

### Cíle hodiny
- Porozumět blokovému programování jako alternativě k textovému kódu
- Vytvořit komplexnější logiku pomocí bloků
- Porovnat blokový a textový kód

### Materiály
- Tinkercad Circuits s Arduino
- Pracovní listy s úkoly
- Převodní tabulka bloky ↔ kód

### Průběh hodiny (45 min)

#### 1. Přepnutí na blokové programování (10 min)
- V Tinkercad Code editoru: **Blocks + Text**
- **Výhody bloků:**
  - Vizuální představa logiky
  - Nelze udělat syntaktické chyby
  - Rychlejší pro začátečníky
- **Nevýhody:**
  - Omezené možnosti
  - Pomalejší pro pokročilé

#### 2. Základní blokové konstrukce (20 min)

**Nastavení pinů:**
- Blok: `set pin 13 to OUTPUT`
- Kód: `pinMode(13, OUTPUT);`

**Digitální výstup:**
- Blok: `set digital pin 13 to HIGH`
- Kód: `digitalWrite(13, HIGH);`

**Čekání:**
- Blok: `wait 1000 milliseconds`
- Kód: `delay(1000);`

**Proměnné:**
- Blok: `set ledState to true`
- Kód: `boolean ledState = true;`

**Podmínky:**
```
if digitalRead pin 2 = HIGH
  set digital pin 13 to HIGH
else
  set digital pin 13 to LOW
```

#### 3. Praktický projekt - Semafor (15 min)

**Zadání:** Vytvoř semafor s 3 LED (červená, žlutá, zelená)

**Blokový program:**
```
forever:
  set digital pin 11 to HIGH  (červená)
  wait 3000 milliseconds
  set digital pin 11 to LOW
  
  set digital pin 12 to HIGH  (žlutá)
  wait 1000 milliseconds
  set digital pin 12 to LOW
  
  set digital pin 13 to HIGH  (zelená)  
  wait 2000 milliseconds
  set digital pin 13 to LOW
```

**Převod na Python kód:**
```python
import arduino
import time

# Piny pro LED
red_pin = 11     # Červená
yellow_pin = 12  # Žlutá  
green_pin = 13   # Zelená

def setup():
    arduino.pin_mode(red_pin, arduino.OUTPUT)
    arduino.pin_mode(yellow_pin, arduino.OUTPUT)
    arduino.pin_mode(green_pin, arduino.OUTPUT)

def loop():
    # Červená
    arduino.digital_write(red_pin, arduino.HIGH)
    time.sleep(3)
    arduino.digital_write(red_pin, arduino.LOW)
    
    # Žlutá
    arduino.digital_write(yellow_pin, arduino.HIGH)
    time.sleep(1)
    arduino.digital_write(yellow_pin, arduino.LOW)
    
    # Zelená
    arduino.digital_write(green_pin, arduino.HIGH)
    time.sleep(2)
    arduino.digital_write(green_pin, arduino.LOW)

# Spuštění
setup()
while True:
    loop()
```

### Domácí úkol
Vytvořit v blokové i textové verzi: "Noční světlo" - LED svítí pouze když je stisknuto tlačítko a současně je tma (hodnota analogového vstupu < 500).

---

## Hodina 13: Pokročilé Python programování pro Arduino

### Cíle hodiny
- Porozumět struktuře pokročilejšího Python kódu pro Arduino
- Seznámit se s pokročilejšími funkcemi
- Vytvořit vlastní funkce

### Materiály
- Tinkercad Circuits (pouze textový editor)
- Referenční manuál Arduino funkcí
- Příklady pokročilejších projektů

### Průběh hodiny (45 min)

#### 1. Struktura pokročilého Python Arduino programu (15 min)

**Kompletní struktura:**
```python
# 1. Komentáře a dokumentace
"""
Název: LED Controller
Autor: [jméno studenta]
Datum: [datum]
Popis: Ovládání LED pomocí tlačítek
"""

# 2. Import knihoven
import arduino
import time

# 3. Globální proměnné a konstanty
LED_PIN = 13        # Konstanta pro pin LED
BUTTON_PIN = 2      # Konstanta pro pin tlačítka
brightness = 0      # Globální proměnná

# 4. Setup funkce - spustí se jednou
def setup():
    arduino.pin_mode(LED_PIN, arduino.OUTPUT)
    arduino.pin_mode(BUTTON_PIN, arduino.INPUT_PULLUP)
    # Pro komunikaci s počítačem (Serial v Pythonu)
    print("Arduino started")

# 5. Loop funkce - opakuje se nekonečně
def loop():
    if arduino.digital_read(BUTTON_PIN) == arduino.LOW:
        fade_led()

# 6. Vlastní funkce
def fade_led():
    for i in range(256):  # 0 až 255
        arduino.analog_write(LED_PIN, i)
        time.sleep(0.01)  # 10ms

# 7. Hlavní program
setup()
while True:
    loop()
```

#### 2. Pokročilejší funkce Arduino (20 min)

**Komunikace s počítačem:**
```python
# V Pythonu používáme print() funkci
print("Hello!")           # Odeslání textu
print(f"Teplota: {teplota}")  # Odeslání čísla s textem
print(teplota)            # Jen číslo
```

**Analogové vstupy a výstupy:**
```python
hodnota = arduino.analog_read(arduino.A0)  # Čtení (0-1023)
arduino.analog_write(9, 128)              # PWM výstup (0-255)
```

**For smyčky:**
```python
for i in range(10):  # 0 až 9 (10 cyklů)
    arduino.digital_write(13, arduino.HIGH)
    time.sleep(0.1)
    arduino.digital_write(13, arduino.LOW)
    time.sleep(0.1)
# LED blikne 10×
```

**While smyčky:**
```python
while arduino.digital_read(2) == arduino.HIGH:
    arduino.digital_write(13, arduino.HIGH)
    time.sleep(0.1)
# LED svítí dokud je tlačítko stisknuto
```

#### 3. Praktický projekt - Inteligentní osvětlení (10 min)

**Zadání:** LED se automaticky rozsvěcí při snížené osvětlenosti a lze ji přepínat tlačítkem

```python
import arduino
import time

# Nastavení pinů
LIGHT_SENSOR = arduino.A0
LED_PIN = 9
BUTTON_PIN = 2

# Globální proměnné
light_threshold = 300
manual_mode = False
led_state = False
last_button_state = True  # Pro detekci změny

def setup():
    arduino.pin_mode(LED_PIN, arduino.OUTPUT)
    arduino.pin_mode(BUTTON_PIN, arduino.INPUT_PULLUP)
    print("Inteligentní osvětlení spuštěno")

def map_value(value, from_low, from_high, to_low, to_high):
    """Převede hodnotu z jednoho rozsahu na druhý"""
    return int((value - from_low) * (to_high - to_low) / (from_high - from_low) + to_low)

def constrain(value, min_val, max_val):
    """Omezí hodnotu na daný rozsah"""
    return max(min_val, min(max_val, value))

def loop():
    global manual_mode, led_state, last_button_state
    
    light_level = arduino.analog_read(LIGHT_SENSOR)
    current_button_state = arduino.digital_read(BUTTON_PIN) == arduino.LOW
    
    # Detekce stisku tlačítka (změna stavu)
    if current_button_state and not last_button_state:
        manual_mode = not manual_mode
        time.sleep(0.2)  # Debounce
        print(f"Režim změněn na: {'Ruční' if manual_mode else 'Automatický'}")
    
    last_button_state = current_button_state
    
    if manual_mode:
        # Ruční režim - LED ovládána tlačítkem
        led_state = current_button_state
    else:
        # Automatický režim - podle světla
        led_state = light_level < light_threshold
    
    # Nastavení jasu podle osvětlení
    brightness = map_value(light_level, 0, 1023, 255, 0)
    brightness = constrain(brightness, 0, 255)
    
    if led_state:
        arduino.analog_write(LED_PIN, brightness)
    else:
        arduino.analog_write(LED_PIN, 0)
    
    # Debug informace
    mode_text = "Ruční" if manual_mode else "Auto"
    print(f"Světlo: {light_level}, Režim: {mode_text}, Jas: {brightness}")
    
    time.sleep(0.1)

# Spuštění programu
setup()
while True:
    loop()
```

**Vysvětlení pokročilých funkcí v Pythonu:**
- `map_value()` - vlastní funkce pro převod hodnot mezi rozsahy
- `constrain()` - vlastní funkce pro omezení hodnot
- `global` - klíčové slovo pro práci s globálními proměnnými
- `f""` - formátované řetězce pro snadné výpisy

### Projekt k odevzdání
Vytvořit vlastní "chytrý" projekt kombinující:
- Alespoň 2 vstupy (tlačítko, senzor)
- Alespoň 2 výstupy (LED, brzučák)
- Vlastní funkci
- Komentovaný Python kód s vysvětlením

### Shrnutí bloku 3
- Rozumíme proměnným a podmínkám v Pythonu
- Ovládáme blokové i textové Python programování
- Vytváříme vlastní funkce
- Kombinujeme více vstupů a výstupů
- Používáme pokročilé Python konstrukce (range, f-strings, global)
- Jsme připraveni na pokročilejší projekty
