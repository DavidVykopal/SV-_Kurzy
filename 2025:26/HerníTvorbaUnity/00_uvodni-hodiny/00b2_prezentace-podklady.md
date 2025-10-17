# 00b2: Prezentace - Vibe coding – praktické opáčko a Python online

## Struktura prezentace (18 slidů)

### Slide 1: Titulní slide
- **Název**: Vibe coding – praktické opáčko a Python online
- **Podtitul**: První kroky v programování + AI asistované kódování
- **Datum**: Říjen 2025
- **Lektor**: David Výkopal

---

### Slide 2: Cíle hodiny
- Zopakovat základy programování zábavnou formou
- Napsat první vlastní Python kód v online prostředí
- Vytvořit a upravit dvě mini-hry (hádání čísel, reakční hra)
- Poznat koncept vibe codingu a AI asistované programování
- Rozvíjet kreativitu a experimentování s kódem

---

### Slide 3: Opáčko - Kvíz! 🎯
**Interaktivní kvíz (děti odpovídají, získávají body):**

**Otázka 1**: Co je proměnná?
- A) Krabička na uložení hodnoty ✅
- B) Něco co se pořád mění
- C) Chyba v kódu

**Otázka 2**: Jaké znáte datové typy?
- (děti vyjmenovávají: čísla, text, boolean...)

**Otázka 3**: Co dělá IF?
- A) Opakuje kód
- B) Rozhoduje mezi variantami ✅
- C) Ukládá hodnotu

**Otázka 4**: K čemu je cyklus?
- A) Pro jízdu na kole
- B) Pro opakování kódu ✅
- C) Pro podmínky

---

### Slide 4: Proměnné - rychlé opáčko
**Živý příklad na tabuli/obrazovce:**
```python
jmeno = "Anna"      # Text (string)
vek = 14            # Číslo (integer)
vyska = 165.5       # Desetinné číslo (float)
je_student = True   # Pravda/nepravda (boolean)
```

**Interaktivní úkol:**
"Vytvořte proměnné pro vaše údaje!"
- Děti diktují své hodnoty, David píše na obrazovku

---

### Slide 5: Podmínky - IF/ELIF/ELSE
**Živý příklad:**
```python
vek = 14

if vek >= 18:
    print("Jsi dospělý")
elif vek >= 13:
    print("Jsi teenager")  # ← Toto se spustí!
else:
    print("Jsi dítě")
```

**Diskuse:** 
- "Co by to napsalo pokud vek = 20?"
- "A pokud vek = 10?"

---

### Slide 6: Cykly - WHILE a FOR
**While cyklus (dokud je podmínka pravdivá):**
```python
pocet = 0
while pocet < 3:
    print(f"Číslo: {pocet}")
    pocet += 1

# Výstup: 0, 1, 2
```

**For cyklus (přesný počet opakování):**
```python
for i in range(3):
    print(f"Opakování: {i}")

# Výstup: 0, 1, 2
```

---

### Slide 7: Online Python prostředí
**Ukázka prostředí (Replit.com nebo Programiz.com):**

📍 **Co budeme používat:**
- **Replit.com** - ukládá projekty, sdílení kódu
- **Programiz.com/python-programming/online-compiler/** - rychlý start bez registrace

📍 **Interface:**
- ✍️ Levá strana: Píšeš kód
- ▶️ Tlačítko Run: Spustíš program
- 📺 Pravá strana: Vidíš výstup

---

### Slide 8: První program společně! (live demo)
**David píše s dětmi:**
```python
jmeno = input("Jak se jmenuješ? ")
vek = input("Kolik ti je let? ")

print(f"Ahoj {jmeno}!")
print(f"Je ti {vek} let!")
```

**Pak to děti zkusí samy (5 min):**
- Každý si otevře online Python
- Napíše a spustí tento program
- Zkusí přidat další řádek

---

### Slide 9: Mini-hra 1 - Hádej číslo (koncept)
**Jak to bude fungovat:**
1. 🎲 Počítač si vymyslí náhodné číslo (1-100)
2. 💭 Ty tipuješ
3. 💬 Počítač řekne "větší" nebo "menší"
4. 🔄 Opakuješ dokud neuhodneš
5. 🎉 Počítač řekne kolik jsi měl pokusů

**Jaké koncepty použijeme?**
- ✅ Proměnné (náhodné číslo, pokusy)
- ✅ Cyklus (while opakování)
- ✅ Podmínky (if větší/menší/správně)
- ✅ Vstup/výstup (input, print)

---

### Slide 10: Hádej číslo - živé kódování
**David píše kód s vysvětlením:**
```python
import random  # Import knihovny pro náhodu

cislo = random.randint(1, 100)  # Náhodné číslo 1-100
pokusy = 0  # Počítadlo pokusů

print("Hádej číslo od 1 do 100!")

while True:  # Nekonečná smyčka
    tip = int(input("Tvůj tip: "))  # Vstup od uživatele
    pokusy += 1  # Přičti pokus
    
    if tip < cislo:
        print("Větší!")
    elif tip > cislo:
        print("Menší!")
    else:
        print(f"Správně! Trefil jsi to na {pokusy} pokusů!")
        break  # Ukonči smyčku
```

**Testování:**
- David si zahraje hru
- Ukáže jak fungují všechny větve

---

### Slide 11: Úkol pro děti - Upravte hru!
**Zkuste přidat/změnit:**

🎯 **Jednodušší úpravy:**
- Změnit rozsah čísel (např. 1-50)
- Změnit texty zpráv
- Přidat emoji do výpisů

🎯 **Středně těžké:**
- Přidat obtížnost (čím méně pokusů, tím lepší)
- Přidat životy (max 7 pokusů, pak game over)
- Přidat nápovědu každých 5 pokusů

🎯 **Pokročilé:**
- Udělat menu s výběrem obtížnosti
- Přidat high score
- Uložit nejlepší výsledek

**Čas: 15-20 minut samostatné práce**

---

### Slide 12: Mini-hra 2 - Reakční trenažér (koncept)
**Jak to bude fungovat:**
1. ⏱️ Příprava: "Připrav se..."
2. ⏳ Náhodné čekání (2-5 sekund)
3. 🚨 Signál: "GO!"
4. ⚡ Měření: Jak rychle zmáčkneš Enter
5. 📊 Výsledek: Tvoje reakce v sekundách

**Nový koncept:**
- ⏰ Práce s časem (`time` modul)
- ⏱️ Měření času (`time.time()`)
- 😴 Zpoždění (`time.sleep()`)

---

### Slide 13: Reakční trenažér - živé kódování
**David píše a vysvětluje:**
```python
import time
import random

print("=== Reakční hra ===")
print("Zmáčkni ENTER když se objeví GO!")

input("Stiskni ENTER pro start...")

# Náhodné čekání pro překvapení
cekej = random.uniform(2, 5)
print("Připrav se...")
time.sleep(cekej)

print("GO!")

# Měření začíná
start = time.time()
input()  # Čekání na stisk
konec = time.time()

# Výpočet reakce
reakce = konec - start
print(f"Tvoje reakce: {reakce:.3f} sekund")

# Hodnocení
if reakce < 0.3:
    print("🚀 Wow! Jsi blesková!")
elif reakce < 0.5:
    print("⚡ Výborné!")
elif reakce < 0.8:
    print("✅ Slušné!")
else:
    print("🐌 Můžeš lépe!")
```

---

### Slide 14: Úkol pro děti - Upravte trenažér!
**Možné úpravy:**

🎯 **Jednodušší:**
- Změnit hodnocení (lepší = rychlejší kategorie)
- Přidat více emoji
- Změnit rozsah čekání

🎯 **Středně těžké:**
- Přidat více kol (3-5) a spočítat průměr
- Přidat countdown před GO (3-2-1)
- Uložit nejlepší čas

🎯 **Pokročilé:**
- Falešný start = penalizace
- Různé typy signálů (čísla, barvy)
- Kombinace s hádací hrou

**Čas: 10-15 minut**

---

### Slide 15: 🤖 COOL MOMENT: Co je Vibe Coding?
**Představení konceptu:**

🎯 **Vibe Coding = Programování s AI asistentem**

**Tradiční programování:**
- Googlíš Stack Overflow
- Kopíruješ kód
- Debugguješ chyby
- Dlouhé hledání řešení

**Vibe Coding:**
- Napíšeš v češtině co chceš
- AI to udělá za tebe
- Můžeš to dál upravovat
- Jako mít zkušeného programátora vedle

**Důležité:**
- ⚠️ AI není magie – musíš vědět CO chceš
- ⚠️ Musíš umět číst kód a pochopit ho
- ⚠️ Proto se učíme základy!

---

### Slide 16: Live demo - Vibe Coding v Cursoru
**David ukazuje v Cursoru:**

**Prompt 1:**
```
Udělej mi jednoduchou hádací hru kde uživatel hádá 
zvíře které jsem si vymyslel. Má 5 pokusů.
```

**AI vygeneruje kód → David ho spustí a ukáže**

**Prompt 2:**
```
Přidej do toho nápovědy po každém špatném pokusu 
(velikost zvířete, kde žije)
```

**AI upraví kód → David ukáže rozdíl**

**Diskuse s dětmi:**
- "Co byste chtěli aby AI udělalo?"
- "Jakou hru byste chtěli vytvořit?"
- "Proč je důležité umět základy?"

---

### Slide 17: Reflexe a sdílení
**Společná diskuse:**
- Co bylo nejtěžší na programování?
- Co bylo nejzajímavější?
- Jaký typ úpravy se vám nejvíc povedl?
- Co byste chtěli příště vytvořit?

**Dobrovolné sdílení:**
- Kdo chce ukázat co vytvořil?
- Nějaké zajímavé úpravy her?
- Narazili jste na nějakou chybu a vyřešili ji?

---

### Slide 18: Domácí úkol a co nás čeká
**Domácí úkol (dobrovolný):**

📝 **Povinná část:**
- Dokončit alespoň jednu úpravu mini-hry

🌟 **Bonusová výzva:**
- Vymyslet a naprogramovat vlastní mini-hru
  - Kvíz, kalkulačka, generátor příběhů...

⭐ **Super bonus:**
- Zkombinovat obě hry do jedné s menu

**Co nás čeká příště:**
- **00c**: Vibe coded – webové mini-hry
- HTML/CSS/JavaScript
- Hry v prohlížeči s grafikou
- Canvas a animace

---

## 📝 Poznámky pro prezentaci

### Timing slidů:
1. **Slide 1-6** (10-15 min): Úvod, kvíz, opáčko základů
2. **Slide 7-8** (10 min): Online prostředí a první program
3. **Slide 9-11** (20 min): Hádej číslo - demo + úpravy dětí
4. **Slide 12-14** (15 min): Reakční hra - demo + úpravy dětí
5. **Slide 15-16** (10 min): Vibe coding ukázka
6. **Slide 17-18** (5-10 min): Reflexe a závěr

### Během kvízu (Slide 3-6):
- Udělej to jako soutěž, přiděl body
- Ať děti odpovídají nahlas
- Chval správné odpovědi
- U chyb vysvětli proč je to jinak

### Během live demos (Slide 10, 13, 16):
- **Piš pomalu** a komentuj každý řádek
- **Ptej se dětí**: "Co sem dám podle vás?"
- **Dělej i chyby**: Ukaž jak je debugovat
- **Testuj průběžně**: Spouštěj často, ne až na konci

### Během samostatné práce (Slide 11, 14):
- Sdílej odkaz na online Python prostředí
- Můžeš sdílet kód přes Pastebin nebo Google Doc
- Chodíš mezi dětmi a pomáháš
- Povzbuzuj kreativitu, i divné nápady jsou OK
- Ukazuj zajímavé řešení ostatním

### Pro rychlé děti:
- Dávej pokročilejší výzvy
- Nech je pomoct ostatním
- Povzbuzuj k vlastním nápadům

### Pro pomalejší děti:
- I malá změna (text, číslo) je úspěch
- Důležité je pochopit princip
- Můžou pracovat ve dvojici

### Vizuální prvky na slidech:
- Slide 3: Grafické kvízové otázky
- Slide 4-6: Kód s barevným syntax highlighting
- Slide 7: Screenshot online Python prostředí
- Slide 9, 12: Flowchart jak hra funguje
- Slide 15: Porovnání tradiční vs. vibe coding
- Slide 16: Screen recording Cursor demo

### Backup plány:
- Pokud online editor nefunguje → lokální Python v VS Code
- Pokud internet padne → předpřipravené soubory offline
- Pokud je hodina rychlejší → extra výzvy připravené


