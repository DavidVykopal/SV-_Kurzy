# 00b: Prezentace - Vibe coded – terminálové mini-hry

## Struktura prezentace (15 slidů)

### Slide 1: Titulní slide
- **Název**: Vibe coded – terminálové mini-hry
- **Podtitul**: Programování her v C# konzoli
- **Datum**: Říjen 2025
- **Lektor**: [Jméno]

### Slide 2: Cíle hodiny
- **Pochopit úplné základy programování**: proměnné, podmínky, cykly
- Zážitkově procvičit proměnné, podmínky a cykly na malém projektu
- Rychle prototypovat mini-hru v konzoli (Python)
- Pochopit herní smyčku a základní programovací koncepty
- Vytvořit 2 funkční mini-hry

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

### Slide 7: Mini-hra 1: Hádej číslo
- **Cíl**: Uhodnout náhodné číslo 1-100
- **Mechanika**: 
  - Generování náhodného čísla
  - Smyčka s počítáním pokusů
  - Nápověda „větší/menší"
- **Čas**: 20 minut

### Slide 8: Hádej číslo - Python kód
```python
import random

cislo = random.randint(1, 100)
pokusy = 0
uhodnuto = False

while not uhodnuto:
    tip = int(input("Tvůj tip: "))
    pokusy += 1
    
    if tip == cislo:
        print(f"Správně! Počet pokusů: {pokusy}")
        uhodnuto = True
    elif tip < cislo:
        print("Větší!")
    else:
        print("Menší!")
```

### Slide 9: Mini-hra 2: Reakční trenažér
- **Cíl**: Změřit reakční čas hráče
- **Mechanika**:
  - Odpočet 3-2-1
  - Náhodné zpoždění
  - Měření času reakce
- **Čas**: 10-15 minut

### Slide 10: Reakční trenažér - Python kód
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

time.sleep(random.uniform(1, 5))

print("STOP!")
start = time.time()
input()
end = time.time()

reakce = (end - start) * 1000
print(f"Tvá reakce: {reakce:.0f}ms")
```

### Slide 11: Praktická část - Základy programování
- Otevřít VS Code s Python
- Vytvořit nový Python soubor
- Vyzkoušet proměnné, podmínky, cykly
- **Čas**: 15 minut

### Slide 12: Praktická část - Mini-hry
- Implementovat hádej číslo
- Implementovat reakční trenažér
- Otestovat obě hry
- **Čas**: 20 minut

### Slide 13: Sdílení a reflexe
- Ukázat své hry ostatním
- Co bylo nejtěžší z programování?
- Jaké funkce byste přidali?
- **Čas**: 5 minut

### Slide 14: Domácí úkol
- Vylepšit jednu z mini-her:
  - Skóre/statistiky
  - Životy
  - Obtížnost
- **Bonus**: Vytvořit vlastní mini-hru s použitím všech základních konceptů
- Připravit krátkou ukázku

### Slide 15: Co nás čeká příště
- **00c**: Vibe coded – webové mini-hry
- HTML/JS v prohlížeči
- Canvas a requestAnimationFrame
- Reakční hra v prohlížeči
