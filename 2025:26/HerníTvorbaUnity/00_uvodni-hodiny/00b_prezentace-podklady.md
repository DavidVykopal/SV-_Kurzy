# 00b: Prezentace - Vibe coded – terminálové mini-hry

## Struktura prezentace (15 slidů)

### Slide 1: Titulní slide
- **Název**: Vibe coded – terminálové mini-hry
- **Podtitul**: Programování her v C# konzoli
- **Datum**: Říjen 2025
- **Lektor**: [Jméno]

### Slide 2: Cíle hodiny
- **Pochopit úplné základy programování**: proměnné, podmínky, cykly
- Vidět živou demonstraci programování mini-her v konzoli
- Porozumět herní smyčce a základním programovacím konceptům
- Sledovat tvorbu 2 mini-her (hádej číslo, reakční trenažér)
- Získat teoretický základ pro budoucí praktické programování

### Slide 3: Základy programování - Proměnné
- **Co je proměnná**: "Krabička" pro uložení hodnoty
- **Datové typy**: čísla, text, boolean (pravda/nepravda)
- **Příklady**:
  - `vek = 15` (číslo)
  - `jmeno = "David"` (text)
  - `je_student = True` (boolean)

### Slide 4: Podmínky (if, else, elif)
- **Podmínky**: Rozhodování v programu
- **Syntaxe**:
  ```python
  if vek >= 18:
      print("Jsi dospělý")
  elif vek >= 13:
      print("Jsi teenager")
  else:
      print("Jsi dítě")
  ```
- **Operátory**: ==, !=, <, >, <=, >=

### Slide 5: Cykly (while, for)
- **While cyklus**: Opakuje dokud je podmínka pravdivá
  ```python
  pocet = 0
  while pocet < 5:
      print(f"Počet: {pocet}")
      pocet += 1
  ```
- **For cyklus**: Opakuje určitý počet krát
  ```python
  for i in range(3):
      print(f"Opakování: {i}")
  ```

### Slide 6: Vstup a výstup
- **Vstup od uživatele**: `input()`
  ```python
  jmeno = input("Jak se jmenuješ? ")
  vek = int(input("Kolik ti je let? "))
  ```
- **Výstup**: `print()`
  ```python
  print(f"Ahoj {jmeno}, je ti {vek} let!")
  ```
- **F-string**: Moderní způsob formátování textu

### Slide 7: Mini-hra 1: Hádej číslo - návrh
- **Cíl**: Uhodnout náhodné číslo 1-100
- **Mechanika**: 
  - Generování náhodného čísla (`random.randint()`)
  - Smyčka s počítáním pokusů (`while` cyklus)
  - Nápověda „větší/menší" (podmínky `if/elif/else`)
- **Herní smyčka**: Input → logika → feedback → opakování

### Slide 8: Hádej číslo - živé kódování
**Demonstrace lektora - postupné psaní kódu s vysvětlením:**
```python
import random  # Import knihovny

cislo = random.randint(1, 100)  # Náhodné číslo
pokusy = 0  # Počítadlo
uhodnuto = False  # Stavová proměnná

while not uhodnuto:  # Herní smyčka
    tip = int(input("Tvůj tip: "))
    pokusy += 1
    
    if tip == cislo:  # Kontrola výhry
        print(f"Správně! Počet pokusů: {pokusy}")
        uhodnuto = True
    elif tip < cislo:  # Nápověda
        print("Větší!")
    else:
        print("Menší!")
```

### Slide 9: Mini-hra 2: Reakční trenažér - návrh
- **Cíl**: Změřit reakční čas hráče
- **Mechanika**:
  - Odpočet 3-2-1 (`time.sleep()`)
  - Náhodné zpoždění (`random.uniform()`)
  - Měření času reakce (`time.time()`)
- **Nové koncepty**: Práce s časem, měření výkonu

### Slide 10: Reakční trenažér - živé kódování
**Demonstrace lektora - postupné psaní s diskusí:**
```python
import time
import random

print("Připrav se...")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)

# Náhodné zpoždění pro překvapení
time.sleep(random.uniform(1, 5))

print("STOP!")
start = time.time()  # Začátek měření
input()  # Čekání na stisk
end = time.time()  # Konec měření

reakce = (end - start) * 1000  # Převod na ms
print(f"Tvá reakce: {reakce:.0f}ms")
```

### Slide 11: Demonstrace - Proměnné v akci
- **Live coding**: Experimenty s datovými typy
- Ukázat chyby a jak je debugovat
- Co se stane když... (common mistakes)
- **Diskuse**: Otázky dětí k programování

### Slide 12: Společné testování her
- **Dobrovolníci**: Zkusit obě hry
- **Pozorování**: Sledovat jak fungují
- **Diskuse**: Co by se dalo vylepšit?
- **Nápady**: Jaké další mini-hry by šly vytvořit?

### Slide 13: Reflexe a porozumění
- **Diskuse**: Co bylo nejtěžší na programování?
- Které koncepty byly nejzajímavější?
- Jak se tyto koncepty použijí v Unity (C#)?
- **Porovnání**: Python konzole vs. Unity skripty

### Slide 14: Domácí úkol
- **Teoretický úkol**: Napsat pseudokód pro vlastní mini-hru
  - Jaké by měla mechaniky?
  - Jaké proměnné by potřebovala?
  - Jaká bude herní smyčka?
- **Volitelně**: Zkusit upravit ukázkové hry doma
- Přinést nápady na vylepšení

### Slide 15: Co nás čeká příště
- **00c**: Vibe coded – webové mini-hry
- HTML/JS v prohlížeči
- Canvas a requestAnimationFrame
- Reakční hra v prohlížeči
