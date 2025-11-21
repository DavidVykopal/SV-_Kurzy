# Blok 2: Základy programování v C# (7–9)

## Přehled bloku
**Cíl:** Naučit děti základy programování v jazyce C# pro Unity.
**Výstup:** Děti umí napsat jednoduché skripty pro pohyb objektů a základní interakce.

---

## Hodina 7: První kroky v C# (45 minut)

### Cíle hodiny
- Pochopit rozdíl mezi Visual Scriptingem a C#
- Naučit se základní syntaxi C#
- Napsat svůj první C# skript

### Materiály
- Unity projekty
- Připravené kód příklady
- Reference kárty se základní syntaxí

### Průběh hodiny

#### 1. Proč se učit C#? (10 minut)

**Výhody C# oproti Visual Scriptingu:**
- Rychlejší výkon
- Více možností
- Profesionální standard
- Lepší pro složitější logiku

**Analogie s jazyky:**
- Visual Scripting = obrázková kniha
- C# = text s pravidly gramatiky

#### 2. Základní syntaxe C# (15 minut)

**Struktura C# skriptu:**
```csharp
using UnityEngine;

public class MujPrvniSkript : MonoBehaviour
{
    // Tady píšeme náš kód
    void Start()
    {
        Debug.Log("Ahoj Unity!");
    }
    
    void Update()
    {
        // Tento kód se opakuje každý frame
    }
}
```

**Vysvětlení částí:**
- `using UnityEngine;` - říká, že používáme Unity funkce
- `public class` - náš skript
- `void Start()` - spustí se jednou na začátku
- `void Update()` - opakuje se stále dokola
- `Debug.Log()` - vypíše text do konzole
- `//` - komentář (poznámka)

#### 3. Vytvoření prvního skriptu (15 minut)

**Postup:**
1. Pravý klik v Project okně
2. Create → C# Script
3. Pojmenujeme "MujPrvniSkript"
4. Dvojklik pro otevření v editoru

**První kód:**
```csharp
using UnityEngine;

public class MujPrvniSkript : MonoBehaviour
{
    void Start()
    {
        Debug.Log("Ahoj, jsem tvůj první skript!");
        Debug.Log("Jmenuji se " + gameObject.name);
    }
    
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.Space))
        {
            Debug.Log("Stiskl jsi mezerník!");
        }
    }
}
```

#### 4. Připojení skriptu k objektu (5 minut)

**Postup:**
1. Vybereme objekt ve scéně
2. Přetažením skript z Project do Inspector
3. Stiskneme Play
4. Podíváme se do Console okna
5. Zkoušíme stisknout mezerník

### Úkol na doma
Upravte skript tak, aby reagoval na různé klávesy (např. W, A, S, D) a vypisoval různé zprávy.

---

## Hodina 8: Proměnné a pohyb (45 minut)

### Cíle hodiny
- Pochopit, co jsou proměnné
- Naučit se základní datové typy
- Vytvořit skript pro pohyb postavy

### Průběh hodiny

#### 1. Co jsou proměnné? (10 minut)

**Definice:** Proměnná je "krabíčka", kde si můžeme uložit hodnotu.

**Analogie:**
- Proměnná = šuplata s štítkem
- Hodnota = co je v šupletě
- Jméno proměnné = štítek na šupletě

**Základní typy:**
```csharp
int vek = 10;                    // celé číslo
float rychlost = 5.5f;          // desetinné číslo
string jmeno = "Petr";          // text
bool jeZiv = true;              // pravda/nepravda
```

#### 2. Proměnné v Unity (10 minut)

**Speciální typy pro Unity:**
```csharp
Vector3 pozice = new Vector3(0, 0, 0);     // 3D pozice
Color barva = Color.red;                    // barva
GameObject objekt;                          // odkaz na objekt
```

**Public proměnné:**
```csharp
public class PohybPostavy : MonoBehaviour
{
    public float rychlost = 5f;    // Zobrazí se v Inspector
    private int skore = 0;         // Nezobrazí se v Inspector
}
```

#### 3. Skript pro pohyb postavy (20 minut)

**Kompletní skript:**
```csharp
using UnityEngine;

public class PohybPostavy : MonoBehaviour
{
    public float rychlost = 5f;
    public float rychlostSkoku = 10f;
    
    private Rigidbody2D rb;
    private bool naPudoru = true;
    
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }
    
    void Update()
    {
        // Horizontal pohyb
        float pohybX = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(pohybX * rychlost, rb.velocity.y);
        
        // Skok
        if (Input.GetKeyDown(KeyCode.Space) && naPudoru)
        {
            rb.velocity = new Vector2(rb.velocity.x, rychlostSkoku);
            naPudoru = false;
        }
    }
    
    void OnCollisionEnter2D(Collision2D collision)
    {
        if (collision.gameObject.CompareTag("Ground"))
        {
            naPudoru = true;
        }
    }
}
```

#### 4. Nastavení objektu (5 minut)

**Příprava postavy:**
1. Přidáme Rigidbody2D komponentu
2. Přidáme Collider2D komponentu
3. Nastavíme Tag "Player"
4. Připojíme náš skript

**Příprava podlahy:**
1. Vytvoříme objekt pro podlahu
2. Přidáme Collider2D
3. Nastavíme Tag "Ground"

### Testování
Šipkami nebo WASD hráč pohybuje postavou, mezerníkem skočí.

---

## Hodina 9: Funkce a metody (45 minut)

### Cíle hodiny
- Pochopit, co jsou funkce/metody
- Naučit se vytvářet vlastní funkce
- Zorganizovat kód pomocí funkcí

### Průběh hodiny

#### 1. Co jsou funkce? (10 minut)

**Definice:** Funkce je "mini-program" uvnitř našeho programu.

**Analogie s recepty:**
```csharp
// Recept na snidaně
void UdelSniDani()
{
    UvaRejPalaciky();
    UdelKafe();
    ProstTul();
}

// Recept na palačinky
void UvaRejPalaciky()
{
    Debug.Log("Míchám testo");
    Debug.Log("Smážím palačinky");
}
```

#### 2. Syntaxe funkcí (15 minut)

**Základní struktura:**
```csharp
// void = nnic nevrací
// public = vidí to i ostatní skripty
// private = vidí to jen tento skript

public void NazevFunkce()
{
    // Kód funkce
}
```

**Funkce s parametry:**
```csharp
void PozdravHrace(string jmeno, int vek)
{
    Debug.Log("Ahoj " + jmeno + ", je ti " + vek + " let!");
}

// Použití:
PozdravHrace("Anna", 10);
```

**Funkce s návratovou hodnotou:**
```csharp
int Secti(int a, int b)
{
    int vysledek = a + b;
    return vysledek;
}

// Použití:
int soucet = Secti(5, 3);  // soucet = 8
```

#### 3. Praktické využití (15 minut)

**Refaktorování původního skriptu:**
```csharp
using UnityEngine;

public class PohybPostavy : MonoBehaviour
{
    public float rychlost = 5f;
    public float rychlostSkoku = 10f;
    
    private Rigidbody2D rb;
    private bool naPudoru = true;
    
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }
    
    void Update()
    {
        ZpracujPohyb();
        ZpracujSkok();
    }
    
    void ZpracujPohyb()
    {
        float pohybX = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(pohybX * rychlost, rb.velocity.y);
    }
    
    void ZpracujSkok()
    {
        if (Input.GetKeyDown(KeyCode.Space) && naPudoru)
        {
            Skok();
        }
    }
    
    void Skok()
    {
        rb.velocity = new Vector2(rb.velocity.x, rychlostSkoku);
        naPudoru = false;
        Debug.Log("Skočil jsem!");
    }
    
    bool JeNaPudoru()
    {
        // Kontrola kolize s podlahou
        return naPudoru;
    }
}
```

#### 4. Cvičení (5 minut)

**Úkol + Git workflow:** Vytvořte funkci, která:
1. Se jmenuje `ZvysSkore`
2. Přijme parametr `int body`
3. Přičte body k celkovému skóre
4. Vypíše nové skóre

**Git workflow:**
1. Před začátkem práce: Pullnout nejnovější verzi
2. Během práce: Commitovat po každé funkční části
3. Na konci: Pushnout vše na GitHub
4. Commit message: "Přidal jsem systém skóre s funkcí ZvysSkore"

**Řešení:**
```csharp
public int celkoveSkore = 0;

void ZvysSkore(int body)
{
    celkoveSkore += body;
    Debug.Log("Skóre: " + celkoveSkore);
}

// Použití:
ZvysSkore(10);  // Přidá 10 bodů
```

### Shrnutí bloku
**Co jsme se naučili:**
- Základní syntaxi C#
- Práci s proměnnými a datovými typy
- Vytváření a používání funkcí
- Základy pohybového systému pro postavy

**Připravili jsme se na:**
- Tvorbu první kompletní 2D hry
- Práci se složitějšími skripty
- Interakce mezi objekty
- Profesionální workflow s Git správou verzí

### Git Shrnutí - co jsme se naučili
- **Workflow:** Pull → Code → Commit → Push
- **Commit často:** Každou funkční změnu zvlášt
- **Popisné messages:** Co jste udělali, ne jak
- **Unity .gitignore:** Vždy používejte při Unity projektech
