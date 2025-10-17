# 00b2: Vibe coding – praktické opáčko a Python online (říjen)

## Cíle hodiny
- **Zopakovat základy programování**: proměnné, podmínky, cykly.
- **Vyzkoušet první psaní kódu** v online Python prostředí.
- **Dokončit mini-hry z minula**: guessing number a reakční hra.
- **Představit koncept vibe codingu** a ukázat jak funguje v praxi.
- Motivovat děti k experimentování a vlastní kreativitě.

## Materiály
- **Online Python prostředí** (Python.org online console, Replit.com, nebo programiz.com).
- Projektor + Cursor pro ukázku vibe codingu.
- Šablony obou mini-her připravené ke stažení/otevření.

## Průběh hodiny (60–75 min)

### 1. Rychlé opáčko – základy programování (10–15 min)

**Interaktivní quiz:**
David klade otázky, děti odpovídají:

**Proměnné:**
- "Co je proměnná?" → Krabička na uložení hodnoty
- "Jaké znáte datové typy?" → čísla, text, True/False
- Příklad na tabuli:
  ```python
  jmeno = "Anna"
  vek = 14
  ```

**Podmínky:**
- "Co dělá IF?" → Rozhoduje mezi variantami
- Příklad:
  ```python
  if vek >= 13:
      print("Teenager")
  ```

**Cykly:**
- "K čemu je cyklus?" → Opakování kódu
- Příklad:
  ```python
  for i in range(3):
      print("Ahoj!")
  ```

**Gamifikace:**
- Kdo odpoví správně, dostane bod.
- Rychlá soutěž na tabuli: "Napište podmínku která..."

### 2. První krůčky v online Python (10–15 min)

**David ukazuje online prostředí:**
1. **Otevře Replit.com** (nebo programiz.com/python-programming/online-compiler/)
2. **Ukáže základní interface:**
   - Kam píšu kód
   - Jak ho spustím
   - Kde vidím výstup
   - Jak zadám vstup

3. **Společně napíšou první program:**
   ```python
   jmeno = input("Jak se jmenuješ? ")
   print(f"Ahoj {jmeno}!")
   ```

4. **Děti si to zkusí samy** (5 min rychlá praxe):
   - Každý si otevře Python online
   - Napíše a spustí jednoduchý program
   - Zkusí změnit text nebo přidat další řádek

**Troubleshooting:**
- David pomáhá s technickými problémy.
- Sdílí odkaz na funkční online editor.

### 3. Mini-hra 1: Hádej číslo (15–20 min)

**David ukáže hotový program:**
```python
import random

cislo = random.randint(1, 100)
pokusy = 0

print("Hádej číslo od 1 do 100!")

while True:
    tip = int(input("Tvůj tip: "))
    pokusy += 1
    
    if tip < cislo:
        print("Větší!")
    elif tip > cislo:
        print("Menší!")
    else:
        print(f"Správně! Trefil jsi to na {pokusy} pokusů!")
        break
```

**Vysvětlí:**
- Jak funguje `random.randint()`
- Proč je tam `while True` (nekonečná smyčka)
- Co dělá `break` (ukončení smyčky)

**Úkol pro děti:**
"Zkuste hru upravit nebo vylepšit:"
- Změnit rozsah čísel (1–50, 1–1000)
- Přidat obtížnost (méně pokusů = lepší skóre)
- Přidat životy (max 7 pokusů)
- Změnit text zpráv
- Přidat emoji do výpisů
- **Vlastní nápad!**

### 4. Mini-hra 2: Reakční trenažér (10–15 min)

**David ukáže druhou hru:**
```python
import time
import random

print("Reakční hra!")
print("Zmáčkni ENTER jakmile se objeví GO!")
input("Připrav se...")

cekej = random.uniform(2, 5)
time.sleep(cekej)
print("GO!")

start = time.time()
input()
konec = time.time()

reakce = konec - start
print(f"Tvoje reakce: {reakce:.3f} sekund")

if reakce < 0.3:
    print("Wow! Jsi blesková!")
elif reakce < 0.5:
    print("Výborné!")
else:
    print("Slušné, ale můžeš lépe!")
```

**Úkol pro děti:**
"Upravte nebo vylepšete reakční hru:"
- Změnit hodnocení (lepší = rychlejší kategorie)
- Přidat více kol a průměrnou reakci
- Přidat countdown před GO
- Změnit z ENTER na napsání specifického slova
- **Vymyslet vlastní variantu!**

### 5. COOL MOMENT: Co je Vibe Coding? (10 min)

**David představí koncept:**
- "Vibe coding = programování s pomocí AI asistenta"
- "Místo googlování píšete v češtině co chcete a AI to udělá"
- "Je to jako mít zkušeného programátora vedle sebe"

**Live ukázka v Cursoru:**
David napíše do Cursoru prompt a nechá AI udělat hru:
```
Prompt: "Udělej mi jednoduchou hádací hru kde uživatel hádá 
zvíře které jsem si vymyslel. Má 5 pokusů."
```

**Ukáže:**
- Jak AI vygeneruje kód
- Jak kód vypadá
- Jak ho spustí
- Jak ho případně upraví dalším promptem

**Důležité:**
- AI není magie, musíte vědět co chcete
- Musíte umět kód číst a pochopit co dělá
- Proto se učíme základy!

**Diskuze:**
- "Co byste chtěli aby AI udělalo za vás?"
- "Jakou hru byste chtěli vytvořit?"

### 6. Volné experimentování a reflexe (5–10 min)

**Děti můžou:**
- Dokončit úpravy svých her
- Zkusit si vymyslet úplně novou mini-hru
- Zeptat se na cokoliv

**Sdílení:**
- Kdo chce ukáže co vytvořil
- Co bylo nejtěžší?
- Co bylo nejzajímavější?

## Online Python prostředí – doporučené

### Nejjednodušší:
- **Programiz**: https://www.programiz.com/python-programming/online-compiler/
  - ✅ Žádná registrace
  - ✅ Funguje okamžitě
  - ✅ Jednoduchý interface

### Pro pokročilejší:
- **Replit**: https://replit.com/
  - ✅ Ukládá projekty
  - ✅ Sdílení kódu
  - ⚠️ Vyžaduje registraci

### Backup:
- **Python.org Shell**: https://www.python.org/shell/
  - Základní konzole pro rychlé testy

## 🏠 Domácí úkol (dobrovolný)

### Povinná část:
- Dokončit alespoň jednu úpravu mini-hry z hodiny.

### Bonusová výzva:
- Zkusit vymyslet a naprogramovat vlastní mini-hru.
- Může to být: kvíz, kalkulačka, generátor náhodných příběhů, kostka, atd.

### Super bonus:
- Zkombinovat obě hry do jedné (uživatel si vybere kterou chce hrát).

## 📝 Poznámky pro Davida

### Příprava před hodinou:
- [ ] Otestovat online Python prostředí (Replit + Programiz).
- [ ] Připravit obě mini-hry jako code snippets ke sdílení.
- [ ] Mít Cursor otevřený a připravený na vibe coding demo.
- [ ] Připravit 2–3 zajímavé prompty pro ukázku AI coding.

### Během hodiny:
- **Tempo:** Nechej děti zkoušet a experimentovat, nepospíchej.
- **Chyby jsou OK:** Když něco nefunguje, ukažuj jak chybu najít.
- **Individuální přístup:** Někdo bude rychlejší, dej mu větší výzvu.
- **Kreativita first:** Podporuj vlastní nápady, i když jsou divné.

### Pro rychlé děti:
- "Zkus přidat menu kde si hráč vybere obtížnost"
- "Udělej kombinaci obou her"
- "Vymysli úplně novou hru s tím co znáš"

### Pro pomalejší děti:
- Klidně ať jen změní čísla nebo texty
- I malá změna je úspěch
- Důležité je pochopit princip, ne mít perfektní kód

### Troubleshooting:
- Pokud online editor nefunguje, přepni na jiný
- Můžeš kód sdílet přes Google Doc nebo Pastebin
- V nouzi použij VS Code lokálně (pokud mají Python)

### Po hodině:
- Sdílej dětem odkazy na online prostředí
- Pošli jim code snippety obou her
- Vyfoť/ulož zajímavé úpravy dětí jako inspiraci pro další

## ✅ Úspěšná hodina = když:
- [ ] Děti si poprvé napsaly a spustily vlastní Python kód
- [ ] Každý udělal alespoň malou úpravu hry
- [ ] Pochopili koncept proměnných, podmínek a cyklů v praxi
- [ ] Viděli že programování není černá magie
- [ ] Odcházejí s nápadem na vlastní projekt
- [ ] Jsou nadšení z možností AI/vibe codingu


