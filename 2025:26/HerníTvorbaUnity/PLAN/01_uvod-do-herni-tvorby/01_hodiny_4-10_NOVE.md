# Hodiny 4-10: Unity a tvorba her - Demonstrační formát

## Hodina 4: Screencast - "Jak vytvořím hru od nuly" (45 min)

### 🎮 CO DAVID UKAZUJE
**COOL MOMENT:** David vytvoří jednoduchou hru ZA 45 MINUT před dětmi!

**Timelapseův přístup - rychlá tvorba:**
1. **Otevřu Unity** (2 min) - "Tak, mám prázdný projekt..."
2. **Přidám postavu** (5 min) - drag & drop sprite, Rigidbody
3. **Pohyb** (10 min) - jednoduchý C# skript nebo visual scripting
4. **Platformy** (5 min) - vytvoření levelu
5. **Sbíratelné objekty** (10 min) - mince + jednoduchý počítadlo
6. **Nepřítel** (8 min) - pohybující se překážka
7. **TEST!** (5 min) - hraju vlastní hru před dětmi

"Vidíte? Za hodinu máme funkční hru!"

### 👥 ZAPOJENÍ DĚTÍ
- "Co má postava dělat?" → návrhy
- "Kam dát platformy?" → design levelu společně
- "Kolik životů?" → game balance diskuze
- Děti testují: "Je to moc těžké? Moc lehké?"

### 💻 CO BY DĚTI MOHLY DĚLAT
- V Unity: Vytvořit podobnou hru podle tutoriálu
- V Roblox Studio: Obby level s checkpointy
- V Minecraft: Parkour mapa

---

## Hodina 5: Unity rozhraní - tour (45 min)

### 🎮 CO DAVID UKAZUJE
**Tour po Unity jako "herní kuchyně":**

**Scene view** = "Tady stavíme level"
- Ukázka: Pohyb kamery, Add objects
- "Je to jako Minecraft creative mode!"

**Game view** = "Tak to vidí hráč"
- Play mode ON → ukázka rozdílu
- "Tady testujeme hru"

**Inspector** = "Detail každého objektu"
- Vyberu kostku → ukážu Transform, barvu, fyziku
- "Každý objekt má vlastnosti jako postavy v RPG!"

**Project** = "Naše assety - obrázky, zvuky, skripty"

**Hierarchy** = "Seznam všeho ve hře"

**COOL MOMENT:** Změním gravitaci → všechno létá!

### 👥 ZAPOJENÍ
- "Tipněte co se stane když..." predictions
- "Která část je nejdůležitější?" hlasování
- Návrhy: "Zkus změnit..."

### 💻 CO BY DĚTI MOHLY DĚLAT  
- Prozkoumat Unity interface samostatně
- Experimentovat s basic objects
- Změnit barvy, velikosti, pozice

---

## Hodina 6: C# vs Visual Scripting - živé porovnání (45 min)

### 🎮 CO DAVID UKAZUJE
**Side-by-side comparison:**

**Visual Scripting (levá polovina obrazovky):**
```
[On Update] → [Get Key W] → [If True] → [Move Up]
```
"Vidíte? Blokočky jako LEGO!"

**C# kód (pravá polovina):**
```csharp
void Update() {
    if (Input.GetKey(KeyCode.W)) {
        transform.position += Vector3.up * speed;
    }
}
```
"A tady to samé napsané textem!"

**COOL MOMENT:** Změním hodnotu v obou → stejný efekt!
"Oba jazyky dělají to samé, jen jinak vypadají"

**Výhody Visual Scripting:**
- Rychlé pro prototypy
- Vizuální
- Nelze udělat syntax error

**Výhody C#:**
- Rychlejší výkon
- Více možností
- Standardní v game dev

### 👥 ZAPOJENÍ
- "Který způsob se vám líbí víc?"
- "Je blokový nebo textový srozumitelnější?"
- Děti navrhují co přidat → David kóduje/blockuje live

### 💻 CO BY DĚTI MOHLY DĚLAT
- Zkusit oba přístupy
- Vytvořit stejnou vec v obou
- Rozhodnout se, co jim víc sedí

---

## Hodina 7: Asset Store a hotové součástky (45 min)

### 🎮 CO DAVID UKAZUJE
**COOL MOMENT:** "Teď vezmu hotovou postavu z Asset Store..."
*Download, import, BAM - krásná animovaná postava!*

**Unity Asset Store tour:**
1. **Free assety** - ukaž kategorii
2. **Stažení** - live download character
3. **Import do projektu**
4. **Použití** - drag do scény
5. **Magie!** - postava je animovaná, funguje

**Ukázka kategorií:**
- **Characters** - postavy ready-to-use
- **Environments** - celé levely!
- **Particles** - efekty (oheň, kouř, magie)
- **Sounds** - zvuky zdarma

**Před/Po porovnání:**
- *PŘED:* Bílá kostka jako postava
- *PO:* Krásný rytíř s animacemi
- "Vidíte? Za 5 minut!"

### 👥 ZAPOJENÍ
- "Jaké assety byste chtěli?"
- Browse Asset Store společně
- "Tohle nebo támhle?" hlasování

### 💻 CO BY DĚTI MOHLY DĚLAT
- Procházet Asset Store
- St\u00e1hnout free assety
- Postavit level z hotových částí

---

## Hodina 8: Fyzika v Unity - cool experimenty (45 min)

### 🎮 CO DAVID UKAZUJE
**Fyzikální sandbox - live experimentation!**

**COOL MOMENTS sekvence:**

**1. Gravitace:** (5 min)
- Spusť 10 koulí ve vzduchu → spadnou
- Změň gravity scale → létají pomalu
- Negative gravity → padají nahoru!

**2. Síly:** (10 min)
- AddForce na kouli → výstřel jako dělo!
- Různé force modes → různé efekty
- "Takto fungují výbuchy ve hrách!"

**3. Kolize:** (10 min)
- Objekt vs. objekt → odrazí se
- Trigger vs. Collider rozdíl
- "Tohle je jak sbírání mincí funguje"

**4. Ragdoll:** (10 min)
- Postaví člověka z kloubů
- Fall down → realistické padání!
- "Jako když umře postava v GTA"

**5. Destrukce:** (10 min)
- Zeď z kostek
- Vrhnu kouli → rozpadne se!
- "Hollywood style!"

### 👥 ZAPOJENÍ
- Děti vykřikují nápady: "Zkus větší sílu!" "Udělej to těžší!"
- Predikce: "Co se stane když..."
- Soutěž: Navrhni nejšílenější fyziku

### 💻 CO BY DĚTI MOHLY DĚLAT
- Physics playground - experimentální scéna
- Vytvoř domino efekt
- Stavba která se musí zřítit realisticky

---

## Hodina 9: Particle systémy a efekty - vizuální magie (45 min)

### 🎮 CO DAVID UKAZUJE
**COOL MOMENT:** Pustá scéna → přidám particle system → OHEŇ/EXPLOZE/MAGIE!

**Postupné wow momenty:**

**1. Oheň:** (10 min)
- Particle System → nastav barvy (oranž, červená)
- Shape: Cone → plameny nahoru!
- Přidej glow → vypadá epicky

**2. Exploze:** (10 min)
- Burst mode → jednorázový efekt
- Force over lifetime → odletí daleko
- "Jako granát ve hře!"

**3. Magické efekty:** (15 min)
- Trail renderer → šleha za objektem
- Sparkles → třpytky
- Glow materials → záře

**4. Počasí:** (10 min)
- Déšť → tisíce kapek
- Sníh → pomalé padání
- Mlha → atmosféra

**Před/Po:**
- *PŘED:* Nudná scéna
- *PO:* Epický fantasy svět s efekty!

### 👥 ZAPOJENÍ
- "Jakou barvu má mít magie?"
- "Rychlý nebo pomalý efekt?"
- Děti vybírají parametry

### 💻 CO BY DĚTI MOHLY DĚLAT
- Vytvořit vlastní magický efekt
- Design particle pro svou hru
- Kombinovat více systémů

---

## Hodina 10: Zvuky a hudba - audio makes magic (45 min)

### 🎮 CO DAVID UKAZUJE
**COOL MOMENT: Porovnání**
- Spustím hru **BEZ** zvuku → "Hmm, OK..."
- Spustím **SE** zvukem → "WHOAAA!"
- "Zvuk = 50% dojmu!"

**Live audio implementation:**

**1. Základy:** (10 min)
- Import audio souboru
- Audio Source component
- Play on awake → automatický start
- "Hudba na pozadí hotova!"

**2. Sound effects:** (15 min)
- Skok → "boing!" zvuk
- Sbírání mince → "pling!"
- Smrt → "auch!"
- "Každá akce má zvuk"

**3. 3D audio:** (10 min)
- Spatial Blend → 3D zvuk
- Ukaž: Vzdálený zvuk je tichý
- Přiblíž se → hlasitější
- "Jako v reálném světě!"

**4. Audio mixer:** (10 min)
- Hlasitost hudby vs. efekty
- Fade in/out
- "Professionální audio system"

### 👥 ZAPOJENÍ
- Děti navrhují jaký zvuk kam
- Test: "Je to moc hlasité?"
- Hledání zvuků online (freesound.org)

### 💻 CO BY DĚTI MOHLY DĚLAT
- Přidat zvuky do své hry
- Nahrát vlastní zvuky (mobil)
- Vytvořit audio-rich experience

---

## Shrnutí hodin 4-10

### Co děti viděly:
✅ Kompletní tvorbu hry od nuly
✅ Unity rozhraní detailně  
✅ Visual Scripting i C# programming
✅ Asset Store a hotové součástky
✅ Fyzikální experimenty
✅ Vizuální efekty (particles)
✅ Audio a zvuky

### Co se naučily (pasivně):
- Herní vývoj není rocket science
- Unity je mocný nástroj
- Existuje mnoho způsobů jak něco udělat
- Hotové assety šetří čas
- Detail (efekty, zvuky) dělá hru živou

### Co je připravené (po 10. hodině):
Děti mají představu CO JE MOŽNÉ a pokud by software fungoval, můžou začít experimentovat pod vedením nebo samostatně.

---

## 📌 POZNÁMKY PRO DAVIDA

### Důležité pro všechny hodiny:
1. **Show, don't tell** - Ukazuj víc než mluvíš
2. **Wow každých 10 minut** - Udržuj pozornost cool momenty
3. **Zapojuj děti** - Ptej se, nech hlasovat, berte návrhy
4. **Testuj před hodinou** - Ať vše funguje smooth
5. **Enjoy it!** - Tvé nadšení je nakažlivé

### Fallback plány:
- Unity crashne? → Ukaž Roblox Studio místo toho
- Internet nefunguje? → Pracuj s offline assety
- Děti jsou unavené? → Pusť cool ukázkové video jako break

### Po hodině:
- Zeptej se co je bavilo nejvíc
- Co chtěly zkusit samy
- Co bylo nejcoolenější moment

