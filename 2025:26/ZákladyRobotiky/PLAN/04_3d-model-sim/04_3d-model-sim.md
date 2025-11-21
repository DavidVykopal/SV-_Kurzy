# Blok 4: 3D modelování a tisk (14–15)

## Hodina 14: Teorie 3D tisku, modelovací software (Tinkercad 3D, Fusion 360)

### Cíle hodiny
- Pochopit principy 3D tisku a aditivní výroby
- Seznámit se s 3D modelovacími nástroji
- Vytvořit první 3D model pro robotický projekt

### Materiály
- Počítače s internetem
- Tinkercad 3D (online)
- Fusion 360 pro vzdělávání (demonstrace)
- Ukázky 3D vytištěných dílů

### Průběh hodiny (45 min)

#### 1. Úvod do 3D tisku (15 min)
**Co je 3D tisk?**
- **Aditivní výroba:** Vytváření objektu vrstva za vrstvou
- **Materiály:** PLA, ABS plasty (pro začátečníky PLA)
- **Rozdíl od klasické výroby:** Místo odebírání materiálu jej přidáváme

**Jak 3D tiskárna funguje:**
1. **3D model** (soubor STL)
2. **Slicer** (např. Cura) → G-kód
3. **Tiskárna** čte G-kód a tiskne vrstvu za vrstvou
4. **Hotový díl** po odstranění podpěr

**Výhody pro robotiku:**
- Vlastní díly přesně na míru
- Rychlé prototypování
- Opravy a náhradní díly
- Kreativní možnosti

**Ukázky praktických dílů:**
- Krabičky pro Arduino
- Držáky sensorů
- Ozubená kola a mechanismy
- Dekorativní prvky

#### 2. Tinkercad 3D - základy (25 min)
**Přihlášení a začátek:**
- Stejný účet jako pro Circuits
- **3D Design** → Create new design

**Základní operace:**
1. **Workplane** (pracovní rovina) - kde modelujeme
2. **Základní tvary:**
   - Box (kvádr)
   - Cylinder (válec)
   - Sphere (koule)
   - Pyramid (jehlan)

**Manipulace s objekty:**
- **Posun:** Táhání za šipky
- **Rotace:** Zakřivené šipky
- **Změna velikosti:** Kostičky v rozích
- **Výška:** Černá šipka nahoru

**Praktické cvičení - Krabička pro Arduino:**
```
1. Vytvořit Box: 60×40×15mm
2. Vytvořit menší Box: 56×36×12mm 
3. Druhý box nastavit jako "Hole" (díra)
4. Umístit díru dovnitř prvního boxu
5. Select All → Group
6. Výsledek: dutá krabička
```

#### 3. Pokročilejší funkce (5 min)
**Align nástroj:** Přesné zarovnání objektů
**Duplicate:** Kopírování objektů
**Text:** Přidání popisků a nápisů
**Import:** STL soubory z internetu

### Domácí úkol
Vytvořit v Tinkercad 3D držák pro senzor (válec s dírou a přírubou pro šroubky).

---

## Hodina 15: Ukázka sliceru a 3D tiskárny

### Cíle hodiny
- Porozumět procesu přípravy modelu pro tisk
- Seznámit se se slicery (Cura/PrusaSlicer)
- Vidět skutečný 3D tisk v akci

### Materiály
- Počítače se slicerem (Cura - zdarma)
- 3D tiskárna (ukázka)
- PLA filament
- Hotové 3D modely ze Tinkercad
- Ukázkové vytištěné díly

### Průběh hodiny (45 min)

#### 1. Export z Tinkercad (10 min)
**Příprava modelu k tisku:**
1. V Tinkercad → **Export** → STL
2. Stažení souboru (.stl)
3. **Kontrola modelu:** Musí být "watertight" (uzavřený)

**Pravidla pro 3D tisk:**
- Minimální tloušťka stěn: 0.8mm (2× šířka trysky)
- Převisy max. 45° (jinak potřeba podpěry)
- První vrstva musí dobře přilehnout k podložce

#### 2. Slicer software - Cura (20 min)
**Co je to slicer?**
- Převádí 3D model (STL) na instrukce pro tiskárnu (G-kód)
- Rozdělí model na tisíce tenkých vrstev
- Vypočítá cestu trysky a rychlosti

**Základní nastavení v Cura:**
```
Kvalita tisku:
- Výška vrstvy: 0.2mm (zlatý střed)
- Rychlost tisku: 50mm/s
- Teplota trysky: 200°C (PLA)
- Teplota podložky: 60°C

Podpory a výplň:
- Výplň: 20% (pro běžné díly)
- Podpěry: Pouze kde potřeba
- Adheze podložky: Brim (pro první tisk)
```

**Praktická ukázka:**
1. Načtení STL souboru do Cura
2. Orientace modelu (nejdůležitější rozhodnutí!)
3. Nastavení základních parametrů
4. **Slice** → generování G-kódu
5. Preview: Simulace tisku vrstvu za vrstvou

#### 3. Živá ukázka 3D tisku (15 min)
**Proces tisku:**
1. **Kalibrace podložky:** Správná vzdálenost trysky
2. **Zahřátí:** Tryska + podložka na správnou teplotu
3. **První vrstva:** Nejdůležitější pro úspěch tisku
4. **Tisk:** Vrstva za vrstvou, opatrně sledujeme

**Běžné problémy a řešení:**
- **Warping:** Model se ohýbá → lepší adheze
- **Stringing:** Vlákna mezi díly → nižší teplota
- **Layer shifting:** Posunutí vrstev → mechanické problémy
- **Clogged nozzle:** Ucpaná tryska → vyčištění

**Bezpečnost:**
- Horké části tiskárny (200°C+)
- Pohyblivé díly
- Větrání při tisku ABS

#### 4. Praktické využití v robotice (bonus)
**Příklady projektů pro Python Arduino projekty:**
- **Krabička na Arduino:** Ochrana elektroniky s otvory pro kabely
- **Držáky sensorů:** Přesné umístění pro teplotní a světelné senzory
- **Kola robotů:** Vlastní design pro mobilní Python roboty
- **Spojovací díly:** Mechanické spoje pro modulární systémy
- **Ozdobné prvky:** Personalizace projektů s Python logem

### Projekt k odevzdání
1. 3D model užitečného dílu pro robotiku (Tinkercad)
2. Export do STL
3. Základní slicing v Cura s komentářem nastavení
4. Popis účelu dílu (3-4 věty)

### Rozšíření pro pokročilé
- **Fusion 360:** Profesionální CAD software
- **Parametrické modelování:** Modely s proměnnými rozměry
- **Animace:** Pohyblivé mechanismy
- **Simulace:** Pevnost materiálu

### Shrnutí bloku 4
- Rozumíme principu 3D tisku
- Umíme vytvářet jednoduché 3D modely
- Víme, jak připravit model k tisku
- Chápeme možnosti 3D tisku v robotice
- Jsme připraveni navrhovat vlastní díly pro projekty

### Poznámky pro učitele
- **Časová náročnost:** 3D tisk trvá hodiny, připravit ukázkové díly předem
- **Materiály:** PLA filament je bezpečný a bez zápachu
- **Alternativa:** Pokud není k dispozici tiskárna, použít online služby nebo fotografie procesu
- **Inspirace:** Thingiverse.com pro ukázky projektů
- **Náklady:** PLA filament ~500 Kč/kg, jeden díl stojí jednotky korun
