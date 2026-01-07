# Tvorba herních assetů: Animace, hudba a zvuky

---

## Proč jsou animace, hudba a zvuky důležité?

**Animace**
- Oživují hru
- Dávají postavám život

**Hudba**
- Vytváří atmosféru
- Navozuje emoce

**Zvuky**
- Dávají feedback hráči
- Zlepšují zážitek

---

## Co je animace?

**Animace = iluze pohybu**

- Sled obrázků nebo pozic rychle za sebou
- Lidské oko vnímá jako plynulý pohyb
- Standardní rychlost: **24-30 snímků za sekundu** (FPS)

---

## Typy animací

**2D animace**
- Sled 2D obrázků (sprite animace)

**3D animace**
- Animace 3D modelu pomocí kostry

**Procedurální animace**
- Automaticky generovaná (fyzika)

---

## 2D Sprite animace

**Co to je?**
- Sled 2D obrázků (spriteů)
- Každý obrázek = jeden snímek animace
- Obrázky se přehrávají rychle za sebou

**Sprite sheet**
- Všechny snímky v jednom obrázku
- Organizované do řádků a sloupců
- Úspora místa a snadná práce

---

## Proces tvorby 2D animace

1. Vytvořit jednotlivé snímky
2. Uspořádat do sprite sheetu
3. Použít ve hře (GDevelop, Unity)

**Software:**
- Aseprite (specializovaný na sprite animace)
- Photoshop/GIMP (sprite sheets)
- Blender (renderování spriteů z 3D)

---

## 3D animace

**Co to je?**
- Animace 3D modelu pomocí kostry (rig)
- Kostra = struktura kostí uvnitř modelu
- Kosti ovládají pohyb částí modelu

---

## Proces tvorby 3D animace

1. **Rigging** - Vytvoření kostry
2. **Weight painting** - Propojení kostry s modelem
3. **Animace** - Pohyb kostí v čase
4. **Rendering** - Vytvoření finálního videa nebo sprite sheetu

---

## Základní pojmy animace

**Bone (kost)**
- Jedna kost v kostře

**Keyframe (klíčový snímek)**
- Pozice v určitém čase

**Timeline**
- Časová osa animace

**Interpolation**
- Automatické vyplnění mezi keyframy

---

## Praktická ukázka: Animace v Blenderu

**Základní animace transformace**

1. Vytvořit objekt (např. koule)
2. Nastavit první pozici (keyframe)
3. Posunout čas na timeline
4. Posunout objekt na novou pozici
5. Přidat keyframe (I → Location)
6. Přehrát animaci (Space)

---

## Typy transformací

**Location (Pozice)**
- I → Location
- Objekt se pohybuje

**Rotation (Rotace)**
- I → Rotation
- Objekt se otáčí

**Scale (Velikost)**
- I → Scale
- Objekt se zvětšuje/zmenšuje

---

## Praktický příklad: Skákající koule

**Postup:**

1. **Frame 1:** Koule na zemi → Keyframe
2. **Frame 15:** Koule ve vzduchu → Keyframe
3. **Frame 30:** Koule zpět na zemi → Keyframe
4. Nastavit jako cyklus → Koule skáče stále dokola

---

## Hudba ve hrách

**Typy hudby:**

**Pozadí hudba**
- Atmosférická hudba, opakuje se

**Dynamická hudba**
- Mění se podle situace ve hře

**Smyčková hudba**
- Hudba, která se opakuje bez přerušení

---

## Formáty hudby

**MP3**
- Komprimovaný, malá velikost

**OGG**
- Lepší kvalita, vhodné pro hry

**WAV**
- Nezkomprimovaný, velká velikost

---

## Základní pojmy hudby

**Tempo**
- Rychlost hudby (BPM - beats per minute)

**Melodie**
- Hlavní melodická linka

**Rytmus**
- Opakující se vzor

**Harmonie**
- Souzvuk více tónů

---

## Zvuky ve hrách

**Typy zvuků:**

**SFX (Sound Effects)**
- Zvuky akcí (skok, střelba, sbírání)

**UI zvuky**
- Zvuky rozhraní (kliknutí, potvrzení)

**Ambientní zvuky**
- Zvuky prostředí (vítr, déšť)

---

## Vlastnosti zvuků

**Délka**
- Krátké zvuky (SFX) vs. dlouhé (hudba)

**Kvalita**
- Vzorkovací frekvence (44.1 kHz standard)

**Formát**
- WAV (nekvalitní), OGG (komprimovaný)

**Důležité pro hry:**
- Krátké zvuky pro rychlou reakci
- Správná hlasitost
- Průhledné smyčky

---

## Audacity - zdarma a open source

**Co to je?**
- Audio editor pro nahrávání a úpravu zvuků
- Vhodné pro hudbu i zvuky

**Hlavní prvky:**
- Timeline - Časová osa nahrávky
- Vlnová forma - Vizuální zobrazení zvuku
- Nástroje - Výběr, střih, mazání
- Efekty - Různé efekty pro úpravu

---

## Nahrávání zvuku v Audacity

**Postup:**

1. Připravit mikrofon nebo nástroj
2. Kliknout na Record (červené tlačítko)
3. Nahrát zvuk
4. Kliknout na Stop

**Úprava:**
- Výběr části zvuku
- Střih (Cut, Copy, Paste)
- Mazání částí

---

## Úprava zvuku v Audacity

**Základní úpravy:**

**Normalize**
- Upravit hlasitost

**Fade In/Out**
- Postupné zesílení/zeslabení

**Echo/Reverb**
- Ozvěna

**Change Speed**
- Změna rychlosti (vyšší = vyšší tón)

---

## Vytvoření hudby v Audacity

**Základní možnosti:**

- **Generování tónů:** Generate → Tone
- **Kombinování zvuků:** Více stop (tracks)
- **Úprava:** Efekty, změna rychlosti

**Praktický příklad:**
- Vytvořit jednoduchou melodii
- Přidat rytmus
- Uložit jako hudební soubor

---

## Praktické cvičení

**Úkol: Vytvořit vlastní asset**

**Možnosti:**

1. **Animace v Blenderu**
   - Jednoduchá animace objektu
   - Skákající koule, rotující objekt

2. **Zvuk v Audacity**
   - Nahrát vlastní zvuk
   - Upravit (hlasitost, efekty)

3. **Hudba v Audacity**
   - Vytvořit jednoduchou melodii
   - Přidat rytmus

---

## Klíčové pojmy

- **Animace** - Iluze pohybu pomocí sledu obrázků
- **Sprite animace** - Sled 2D obrázků
- **3D animace** - Animace pomocí kostry
- **Keyframe** - Klíčový snímek animace
- **SFX** - Sound Effects - zvuky akcí
- **Tempo** - Rychlost hudby (BPM)
- **Fade In/Out** - Postupné zesílení/zeslabení

---

## Použití assetů ve hrách

**Animace**
- Můžeme použít v GDevelop nebo Unity

**Hudba a zvuky**
- Můžeme použít ve hrách

**Vlastní assety = jedinečná hra**

---

## Shrnutí celého bloku

- ✅ Naučili jsme se vytvářet 2D grafiku
- ✅ Naučili jsme se vytvářet 3D modely
- ✅ Naučili jsme se vytvářet animace
- ✅ Naučili jsme se vytvářet hudbu a zvuky

**Teď můžeme vytvářet kompletní hry s vlastními assety!**

---

## Domácí úkol (dobrovolný)

- Dokončit asset, který jsme začali
- Vytvořit další asset (animace, zvuk, hudba)
- Prozkoumat další funkce Blenderu nebo Audacity
- Přinést nápad na hru s vlastními assety
