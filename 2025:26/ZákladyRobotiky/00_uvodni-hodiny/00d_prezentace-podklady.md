# 00d: Prezentace - Tinkercad Circuits + Arduino sada

## Struktura prezentace (15 slidů)

### Slide 1: Titulní slide
- **Název**: Tinkercad Circuits + Arduino sada
- **Podtitul**: Od simulace k fyzickým komponentám
- **Datum**: Říjen 2025
- **Lektor**: [Jméno]

### Slide 2: Cíle hodiny
- Seznámit se s Tinkercad Circuits
- Vytvořit první simulaci
- Fyzicky si osahat Arduino sadu
- Projít bezpečnostní zásady

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

### Slide 6: Tinkercad: LED + rezistor (20-25 min)
- **Otevřít Tinkercad Circuits**
- **Přidat komponenty**: Arduino, LED, rezistor
- **Propojit**: GND → rezistor → LED → pin 13
- **Praktická část**: První obvod

### Slide 7: Multimetr v Tinkercad
- **Měření napětí**: Paralelně s komponentou
- **Měření proudu**: Sériově s komponentou
- **Měření odporu**: Mezi dvěma body
- **Praktická část**: Změřit hodnoty

### Slide 8: Blokové programování: blikání LED (10 min)
- **Otevřít Arduino editor**
- **Přidat blok**: "digital write pin 13 HIGH"
- **Přidat blok**: "delay 1000ms"
- **Přidat blok**: "digital write pin 13 LOW"
- **Praktická část**: Programovat blikání

### Slide 9: Blokové programování - kód
```cpp
void setup() {
  pinMode(13, OUTPUT);
}

void loop() {
  digitalWrite(13, HIGH);
  delay(1000);
  digitalWrite(13, LOW);
  delay(1000);
}
```

### Slide 10: Ukázka Arduino sady (10-15 min)
- **Arduino UNO**: Hlavní deska
- **Breadboard**: Nepájivé pole
- **Rezistory**: Různé hodnoty
- **LED**: Různé barvy
- **Tlačítko**: Spínač
- **Kabely**: Propojovací vodiče

### Slide 11: Fyzické propojení
- **GND**: Společná zem
- **5V**: Napájecí napětí
- **Digitální piny**: 0-13
- **Analogové piny**: A0-A5
- **Praktická část**: Osahat komponenty

### Slide 12: Bezpečnost při práci
- **Nízké napětí**: Arduino je bezpečné
- **Polarita**: LED má + a - pól
- **Rezistory**: Vždy s LED (ochrana)
- **Kontakt**: Při práci s 220V volat dospělého

### Slide 13: Mini-projekty na listopad
- **Semafor**: 3 LED, tlačítko
- **Tlačítkový zámek**: Kombinace tlačítek
- **Teploměr**: Senzor teploty
- **Alarm**: Senzor pohybu
- **Praktická část**: Vybrat si projekt

### Slide 14: Domácí úkol
- Uložit a sdílet odkaz na Tinkercad obvod
- Vybrat si mini-projekt na listopad
- **Tip**: Začít s jednoduchým blikáním

### Slide 15: Co nás čeká příště
- **01**: Teorie a základy
- Elektrotechnické zákony
- Ohmův zákon v praxi
- Základy programování
