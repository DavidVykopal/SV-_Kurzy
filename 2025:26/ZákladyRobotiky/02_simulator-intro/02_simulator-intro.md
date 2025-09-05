# Blok 2: Simulátor obvodů (6–10)

## Hodina 6: Úvod do Tinkercad Circuits

### Cíle hodiny
- Seznámit se s Tinkercad Circuits rozhraním
- Vytvořit první jednoduchý obvod
- Porozumět základním nástrojům pro simulaci

### Materiály
- Počítače s internetem
- Tinkercad účty (založené v hodině 5)
- Instrukční karty s kroky

### Průběh hodiny (45 min)

#### 1. Přihlášení a orientace (10 min)
- Přihlášení na tinkercad.com
- **Circuits → Create new Circuit**
- **Rozhraní Tinkercad:**
  - Components panel (vpravo)
  - Workspace (střed)
  - Simulator controls (nahoře)

#### 2. Základní komponenty (15 min)
- **Breadboard (nepájivé pole):** Základ pro všechny obvody
- **Baterie 9V:** Components → Basic → Battery
- **LED:** Components → Basic → LED
- **Rezistor:** Components → Basic → Resistor

#### 3. Připojování komponent (15 min)
- **Drag & Drop** komponent do workspace
- **Propojování:** Klik na pin → tažení na druhý pin
- **Barvy drátů:** 
  - Červená = kladné napětí (+)
  - Černá = záporné napětí (-, GND)
  - Jiné barvy = signálové vodiče

#### 4. První obvod - test (5 min)
**Jednoduchý obvod:** Baterie 9V + LED + Rezistor 220Ω

**Kroky:**
1. Umísti baterie na breadboard
2. Připoj LED (delší nožička = kladný pól)
3. Přidej rezistor mezi LED a baterii
4. **Spuštění simulace:** Tlačítko "Start Simulation"

### Domácí úkol
Vytvoř obvod se 2 LED různých barev (série).

---

## Hodina 7: První obvod (LED + rezistor)

### Cíle hodiny
- Pochopit funkci rezistoru v LED obvodu
- Experimentovat s různými hodnotami rezistorů
- Naučit se měřit napětí a proud

### Materiály
- Tinkercad Circuits
- Kalkulačka pro výpočty
- Tabulka barev rezistorů

### Průběh hodiny (45 min)

#### 1. Opakování z minulé hodiny (5 min)
- Proč potřebuje LED rezistor?
- **Odpověď:** Ochrana před vysokým proudem (LED by shořela)

#### 2. Experimentování s rezistory (20 min)

**Obvod:** Baterie 9V + LED + Rezistor

**Test různých rezistorů:**
- 100Ω - LED svítí velmi jasně
- 220Ω - LED svítí normálně (doporučeno)
- 1kΩ - LED svítí slabě
- 10kΩ - LED téměř nesvítí

**Pozorování:** Větší odpor = menší proud = slabší světlo

#### 3. Měření v simulátoru (15 min)
- **Multimetr:** Components → Basic → Multimeter
- **Měření proudu:** Multimetr v sérii s LED
- **Měření napětí:** Multimetr paralelně k LED

**Příklad měření (LED + 220Ω + 9V):**
- Napětí na LED: ~2V
- Napětí na rezistoru: ~7V
- Proud obvodem: ~32mA

#### 4. Jednoduchý výpočet (5 min)
**Ohmův zákon v praxi:**
- Napětí rezistoru: 9V - 2V = 7V
- Odpor: 220Ω
- **Proud = U/R = 7V/220Ω ≈ 0.032A = 32mA**

### Domácí úkol
Vytvoř obvod s 3 LED různých barev a změř proud u každé.

---

## Hodina 8: Logické obvody v Tinkercad

### Cíle hodiny
- Porozumět logickým hradlům
- Vytvořit obvody s tlačítky a spínači
- Pochopit koncept logických stavů (0/1)

### Materiály
- Tinkercad Circuits
- Pracovní list s logickými tabulkami

### Průběh hodiny (45 min)

#### 1. Co jsou logické obvody? (10 min)
- **Logický stav:**
  - 0 = NEPRAVDA = 0V = vypnuto
  - 1 = PRAVDA = 5V = zapnuto
- **Příklady v reálném světě:**
  - Spínač světla (on/off)
  - Dveře otevřené/zavřené

#### 2. Tlačítko a spínač (15 min)
**Obvod s tlačítkem:**
- Components → Basic → Pushbutton
- **Zapojení:** Baterie → Tlačítko → LED → Rezistor → zpět

**Obvod se spínačem:**
- Components → Basic → Switch
- **Rozdíl:** Spínač zůstává zapnutý, tlačítko pouze při stisku

#### 3. Pull-up a pull-down rezistory (15 min)
**Proč potřebujeme pull-up rezistor?**
- Bez něj má nevstup neurčitou hodnotu (floating)
- **Pull-up:** Drží vstup na 1 když není tlačeno
- **Pull-down:** Drží vstup na 0 když není tlačeno

**Praktický obvod:**
- Arduino pin + Pull-up rezistor (10kΩ) + Tlačítko na GND

#### 4. Kombinace více tlačítek (5 min)
**Sériové spojení:** Obě tlačítka musí být stisknuta (AND)
**Paralelní spojení:** Stačí jedno tlačítko (OR)

### Domácí úkol
Vytvoř "bezpečnostní systém" - LED svítí pouze když jsou stisknuta 2 tlačítka současně.

---

## Hodina 9: Programování Arduina v Pythonu

### Cíle hodiny
- První kroky s Arduino programováním v Pythonu
- Porozumět základní struktuře Python Arduino kódu  
- Ovládat LED pomocí Python kódu

### Materiály
- Tinkercad Circuits s Arduino
- Referenční karty Arduino funkcí

### Průběh hodiny (45 min)

#### 1. Arduino v Tinkercad s Pythonem (10 min)
- **Přidání Arduina:** Components → Microcontrollers → Arduino Uno R3
- **Breadboard + Arduino:** Automatické propojení napájení
- **Code Editor:** Tlačítko "Code" → změnit na "Text" místo "Blocks"
- **Python mode:** V Tinkercad můžeme psát kód podobný Pythonu

#### 2. Struktura Python Arduino kódu (15 min)

```python
# Import knihovny pro Arduino
import arduino
import time

# Nastavení - spustí se pouze jednou
def setup():
    # Nastavení pinů, komunikace, atd.
    arduino.pin_mode(13, arduino.OUTPUT)

# Hlavní smyčka - opakuje se nekonečně  
def loop():
    # Hlavní logika programu
    pass

# Spuštění programu
setup()
while True:
    loop()
```

**Základní Python funkce:**
- `arduino.pin_mode(pin, arduino.OUTPUT)` - Nastavení pinu jako výstup
- `arduino.digital_write(pin, arduino.HIGH)` - Zapnutí pinu (5V)
- `arduino.digital_write(pin, arduino.LOW)` - Vypnutí pinu (0V) 
- `time.sleep(1)` - Čekání 1 sekunda

#### 3. První program - blikání LED (15 min)

**Obvod:** Arduino + LED (pin 13) + Rezistor 220Ω

```python
import arduino
import time

def setup():
    arduino.pin_mode(13, arduino.OUTPUT)  # Pin 13 jako výstup

def loop():
    arduino.digital_write(13, arduino.HIGH)  # Zapni LED
    time.sleep(1)                           # Čekej 1 sekundu
    arduino.digital_write(13, arduino.LOW)   # Vypni LED  
    time.sleep(1)                           # Čekej 1 sekundu

# Spuštění
setup()
while True:
    loop()
```

**Vysvětlení:**
- LED se zapne na 1 sekundu
- Pak se vypne na 1 sekundu  
- A opakuje se to nekonečně díky `while True:`

#### 4. Úpravy programu (5 min)
**Experimenty:**
- Změn `time.sleep(1)` na `time.sleep(0.2)` - rychlé blikání
- Změn na `time.sleep(0.1)` a `time.sleep(2)` - různé rytmy

### Domácí úkol
Vytvoř "semafor" - 3 LED (červená, žlutá, zelená) s realistickými časováními.

---

## Hodina 10: Mini projekt – blikátko

### Cíle hodiny
- Aplikovat získané znalosti v komplexním projektu
- Vytvořit interaktivní blikátko s tlačítkem
- Dokumentovat vlastní projekt

### Materiály
- Tinkercad Circuits
- Projektová šablona
- Popisné kartičky

### Průběh hodiny (45 min)

#### 1. Specifikace projektu (5 min)
**"Chytré blikátko":**
- 2-3 LED různých barev
- 1 tlačítko pro změnu módu
- 3 různé módy blikání
- Potenciometr pro rychlost (bonus)

#### 2. Plánování obvodu (10 min)
**Komponenty:**
- Arduino Uno
- 3× LED (červená, zelená, modrá)
- 3× Rezistor 220Ω
- 1× Pushbutton
- 1× Rezistor 10kΩ (pull-up)
- Potenciometr (volitelný)

**Pin assignment:**
- LED: piny 11, 12, 13
- Tlačítko: pin 2
- Potenciometr: pin A0

#### 3. Implementace (25 min)

**Python kód:**

```python
import arduino
import time
import random

# Nastavení pinů
led_red = 11
led_green = 12  
led_blue = 13
button_pin = 2

# Proměnné
mode = 1
last_button_state = False

def setup():
    arduino.pin_mode(led_red, arduino.OUTPUT)
    arduino.pin_mode(led_green, arduino.OUTPUT) 
    arduino.pin_mode(led_blue, arduino.OUTPUT)
    arduino.pin_mode(button_pin, arduino.INPUT_PULLUP)

def loop():
    global mode, last_button_state
    
    # Čtení tlačítka (inverted kvůli pullup)
    button_state = not arduino.digital_read(button_pin)
    
    # Detekce stisku tlačítka
    if button_state and not last_button_state:
        mode += 1
        if mode > 3:
            mode = 1
        time.sleep(0.2)  # debounce
    
    last_button_state = button_state
    
    # Módy blikání
    if mode == 1:
        blink_sequential()
    elif mode == 2: 
        blink_all()
    elif mode == 3:
        blink_random()

def blink_sequential():
    # Postupné blikání
    arduino.digital_write(led_red, arduino.HIGH)
    time.sleep(0.3)
    arduino.digital_write(led_red, arduino.LOW)
    
    arduino.digital_write(led_green, arduino.HIGH) 
    time.sleep(0.3)
    arduino.digital_write(led_green, arduino.LOW)
    
    arduino.digital_write(led_blue, arduino.HIGH)
    time.sleep(0.3)
    arduino.digital_write(led_blue, arduino.LOW)

def blink_all():
    # Všechny LED současně
    arduino.digital_write(led_red, arduino.HIGH)
    arduino.digital_write(led_green, arduino.HIGH)
    arduino.digital_write(led_blue, arduino.HIGH)
    time.sleep(0.5)
    
    arduino.digital_write(led_red, arduino.LOW)
    arduino.digital_write(led_green, arduino.LOW) 
    arduino.digital_write(led_blue, arduino.LOW)
    time.sleep(0.5)

def blink_random():
    # Náhodné blikání
    led_pins = [led_red, led_green, led_blue]
    random_led = random.choice(led_pins)
    
    arduino.digital_write(random_led, arduino.HIGH)
    time.sleep(0.2)
    arduino.digital_write(random_led, arduino.LOW)
    time.sleep(0.1)

# Spuštění programu
setup()
while True:
    loop()
```

#### 4. Testování a dokumentace (5 min)
- Test všech módů
- Ověření funkcí tlačítka
- **Dokumentace:** Popis funkce, schéma zapojení, seznam součástek

### Projekt k odevzdání
- Funkční Tinkercad projekt
- Komentovaný Python kód
- Krátký popis funkce (3-4 věty)

### Shrnutí bloku 2
- Umíme pracovat s Tinkercad Circuits
- Vytváříme obvody s LED, rezistory, tlačítky
- Programujeme Arduino v Pythonu
- Dokážeme vytvořit jednoduché interaktivní projekty
- Rozumíme základním programovacím konstrukcím v Pythonu
