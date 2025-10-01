# 00b: Vibe coded – terminálové mini‑hry (říjen)

## Cíle hodiny
- **Pochopit úplné základy programování**: proměnné, podmínky, cykly
- Zážitkově procvičit proměnné, podmínky a cykly na malém projektu.
- Rychle prototypovat mini‑hru v konzoli (Python konzolová aplikace).
- **Pochopit herní smyčku** a základní programovací koncepty.

## Materiály
- **VS Code/Rider s podporou Python**.
- **Python interpreter** (nainstalovaný).
- Šablona pro Python konzolovou aplikaci.

## Před hodinou (příprava lektora)
- Připravit šablonu Python konzolové aplikace s hotovou skeletovou strukturou.
- Ověřit, že běží vstup z klávesnice a výpis na konzoli.
- **Připravit příklady** základních programovacích konceptů.

## Průběh hodiny (60–75 min)
1. **Úvod: Co je herní smyčka v konzoli** (5 min)
2. **Základy programování** (15–20 min)
   - **Proměnné**: Co to je, jak se používají
   - **Datové typy**: čísla, text, boolean
   - **Podmínky**: if, else, elif
   - **Cykly**: while, for
   - **Vstup/výstup**: input(), print()
3. **Mini‑hra 1: Hádej číslo** (20 min)
   - Generování náhodného čísla 1–100.
   - Smyčka s počítáním pokusů, nápověda „větší/menší".
4. **Mini‑hra 2: Reakční trenažér** (10–15 min)
   - Odpočet, start, měření času reakce.
5. **Sdílení a krátká reflexe** (5 min)

## Základy programování - příklady

### Proměnné a datové typy
```python
# Čísla
vek = 15
vyska = 175.5

# Text
jmeno = "David"
zprava = "Ahoj světe!"

# Boolean (pravda/nepravda)
je_student = True
je_ucitel = False
```

### Podmínky
```python
if vek >= 18:
    print("Jsi dospělý")
elif vek >= 13:
    print("Jsi teenager")
else:
    print("Jsi dítě")
```

### Cykly
```python
# While cyklus
pocet = 0
while pocet < 5:
    print(f"Počet: {pocet}")
    pocet += 1

# For cyklus
for i in range(3):
    print(f"Opakování: {i}")
```

### Vstup a výstup
```python
# Vstup od uživatele
jmeno = input("Jak se jmenuješ? ")
vek = int(input("Kolik ti je let? "))

# Výstup
print(f"Ahoj {jmeno}, je ti {vek} let!")
```

## Domácí úkol
- Vylepšit jednu z mini‑her (skóre, životy, obtížnost) a připravit krátkou ukázku.
- **Bonus**: Vytvořit vlastní mini-hru s použitím všech základních konceptů.


