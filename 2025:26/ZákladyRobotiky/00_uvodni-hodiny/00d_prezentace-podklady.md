# 00d: Prezentace - Tinkercad Circuits + Arduino sada

## Struktura prezentace (15 slidů)

### Slide 1: Titulní slide
- **Název**: Tinkercad Circuits + Arduino sada
- **Podtitul**: Od simulace k fyzickým komponentám
- **Datum**: Říjen 2025
- **Lektor**: [Jméno]

### Slide 2: Cíle hodiny
- Vidět demonstraci Tinkercad Circuits simulátoru
- Sledovat tvorbu první Arduino simulace (blikající LED)
- Fyzicky si prohlédnout Arduino komponenty
- Pochopit bezpečnostní zásady při práci s elektronikou
- Získat přehled o možných projektech

### Slide 3: Co je Tinkercad Circuits?
- **Webový simulátor** obvodů
- **Bez instalace** - funguje v prohlížeči
- **Arduino simulace** s programováním
- **Multimetr** pro měření

### Slide 4: Základní komponenty
- **Arduino UNO**: Mikrokontrolér
- **Breadboard**: Nepájivé pole
- **Rezistory**: Omezují proud
- **LED**: Světelná dioda
- **Tlačítko**: Spínač
- **Kabely**: Propojení

### Slide 5: Bezpečnostní zásady
- **Arduino 5V**: Bezpečné napětí
- **Polarita LED**: + a - pól
- **Rezistory**: Vždy s LED
- **220V**: Při práci s vysokým napětím volat dospělého

### Slide 6: Demonstrace: LED + rezistor (20-25 min)
- **Lektor ukazuje**: Otevřít Tinkercad Circuits
- **Přidání komponent**: Arduino, LED, rezistor z knihovny
- **Propojení**: GND → rezistor → LED → pin 13
- **Vysvětlení**: Proč potřebujeme rezistor?
- **Spuštění simulace**: Pozorování výsledku

### Slide 7: Multimetr - teorie a demonstrace
- **Co je multimetr**: Nástroj pro měření elektrických veličin
- **Měření napětí**: Připojit paralelně (ukázat v Tinkercad)
- **Měření proudu**: Připojit sériově (ukázat v Tinkercad)
- **Měření odporu**: Odpojit od obvodu
- **Live demo**: Lektor měří napětí, proud, odpor v simulaci

### Slide 8: Programování Arduino - demonstrace (10 min)
- **Lektor ukazuje**: Přepnout do Code editoru
- **Vysvětlení struktury**: `setup()` a `loop()`
- **Blokové programování**: Postupné přidávání bloků
  - digitalWrite(13, HIGH)
  - delay(1000)
  - digitalWrite(13, LOW)
  - delay(1000)
- **Spuštění**: Pozorování blikající LED

### Slide 9: Vysvětlení kódu - řádek po řádku
```cpp
void setup() {  // Spustí se jednou na začátku
  pinMode(13, OUTPUT);  // Pin 13 jako výstup
}

void loop() {  // Opakuje se pořád dokola
  digitalWrite(13, HIGH);  // Zapnout LED
  delay(1000);  // Čekat 1 sekundu (1000ms)
  digitalWrite(13, LOW);  // Vypnout LED
  delay(1000);  // Čekat 1 sekundu
}
```
**Diskuse**: Co by se stalo když změníme delay?

### Slide 10: Fyzické Arduino komponenty - ukázka (10-15 min)
- **Lektor ukazuje každý komponent**:
  - **Arduino UNO**: Mozek projektu, počítá a řídí
  - **Breadboard**: Nepájivé pole pro prototypy
  - **Rezistory**: Různé hodnoty (čtení barevných pásků)
  - **LED**: Různé barvy, polarita +/-
  - **Tlačítko**: Spínač
  - **Kabely**: Propojovací vodiče (samec-samec, samec-samice)
- **Děti si mohou prohlédnout** (ale zatím neprogramují)

### Slide 11: Piny Arduino - orientace
- **Lektor ukazuje na fyzickém Arduino**:
  - **GND**: Společná zem (mínus, 0V)
  - **5V**: Napájecí napětí (plus)
  - **Digitální piny (0-13)**: ON/OFF signály
  - **Analogové piny (A0-A5)**: Měření hodnot (0-1023)
  - **TX/RX**: Komunikace s počítačem
- **Analogie**: Jako zásuvky v pokoji - každá má účel

### Slide 12: Bezpečnost při práci
- **Nízké napětí**: Arduino je bezpečné
- **Polarita**: LED má + a - pól
- **Rezistory**: Vždy s LED (ochrana)
- **Kontakt**: Při práci s 220V volat dospělého

### Slide 13: Inspirace - možné projekty
- **Ukázky projektů**: Lektor prezentuje možnosti
  - **Semafor**: 3 LED, tlačítko pro chodce
  - **Tlačítkový zámek**: Kombinace tlačítek jako heslo
  - **Teploměr**: Senzor teploty + displej
  - **Alarm**: Senzor pohybu + bzučák
  - **Knight Rider**: Běžící světlo
- **Diskuse**: Který projekt by vás nejvíc bavil?

### Slide 14: Domácí úkol
- **Teoretický úkol**: Nakreslit na papír Arduino projekt
  - Vybrat si projekt ze slidu 13
  - Nakreslit schéma zapojení
  - Popsat jak by měl fungovat
- **Volitelně**: Vytvořit Tinkercad účet a zkusit blikající LED
- **Přemýšlení**: Jaký projekt byste chtěli udělat?

### Slide 15: Co nás čeká příště
- **01**: Teorie a základy
- Elektrotechnické zákony
- Ohmův zákon v praxi
- Základy programování
