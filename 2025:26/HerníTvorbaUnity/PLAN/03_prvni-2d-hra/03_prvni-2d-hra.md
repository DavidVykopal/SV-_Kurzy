# Blok 3: První 2D hra - Plošinovka (10–12)

## Přehled bloku
**Cíl:** Vytvořit kompletní jednoduchou 2D plošinovku s ovládáním postavy, sběrem předmětů a základními nepřáteli.
**Výstup:** Funkční hra, kterou si děti mohou zahrát a ukázat rodílům.

---

## Hodina 10: Assety a prostředí (45 minut)

### Cíle hodiny
- Pochopit, co jsou assety a jak se používají
- Naučit se importovat obrázky do Unity
- Vytvořit základní level design

### Materiály
- Sada 2D spriteů (postava, platformy, sbíratelé předměty, pozadí)
- Připravené assety lze stáhnout z Unity Asset Store nebo použít jednoduché geometrické tvary

### Příprava učitele
Stáhněte pack 2D spriteů nebo připravte jednoduche geometrické tvary různých barev.

### Průběh hodiny

#### 1. Co jsou assety? (10 minut)

**Definice:** Assety jsou všechny soubory, které používáme v naší hře.

**Typy assetů:**
- **Sprites** - 2D obrázky
- **Textures** - povrchy pro 3D objekty
- **Audio** - zvuky a hudba
- **Scripts** - naše C# kódy
- **Materials** - vlastnosti povrchů
- **Prefabs** - předpřipravené objekty

#### 2. Import spriteů (10 minut)

**Způsoby importu:**
1. **Přetažením** - soubory přetažíme do Project okna
2. **Pravým klikem** - Import New Asset...
3. **Kopírováním** do složky Assets

**Nastavení spriteů:**
1. Vybereme importovaný obrázek
2. V Inspector nastavíme:
   - Texture Type: Sprite (2D and UI)
   - Pixels Per Unit: 100 (pro veřejší obrázky)
   - Filter Mode: Point (for pixel art)
3. Stiskneme Apply

#### 3. Vytvoření postavy (15 minut)

**Postup:**
1. Přetažením sprite do scény
2. Přejmenujeme na "Player"
3. Přidáme komponenty:
   - Rigidbody2D (pro fyziku)
   - BoxCollider2D (pro kolize)
   - Náš PohybPostavy skript

**Nastavení Rigidbody2D:**
- Mass: 1
- Drag: 0
- Angular Drag: 0.05
- Gravity Scale: 3
- Freeze Rotation Z: True

#### 4. Vytvoření platform a prostředí (10 minut)

**Platformy:**
1. Přetažením sprite platformy do scény
2. Přidáme BoxCollider2D
3. Nastavíme tag "Ground"
4. Duplikujeme (Ctrl+D) pro více platform

**Pozadí:**
1. Přetažením sprite pozadí
2. Umístíme za všechny objekty (Z pozice = 10)
3. Zvětšíme podle potřeby

**Úkol pro děti:**
Vytvořte level s alespoň 5 platformami různých výšek, aby postava mohla skákat z jedné na druhou.

### Tip pro učitele
Pokud nemáte grafické assety, použijte Unity předpřipravené tvary (pravý klik → 2D Object → Sprites).

---

## Hodina 11: Ovládání postavy + skripty (45 minut)

### Cíle hodiny
- Vylepšit pohybový systém postavy
- Přidat animace postavy
- Implementovat správné kolize

### Průběh hodiny

#### 1. Vylepšení pohybu (15 minut)

**Rozšířený PohybPostavy skript:**
```csharp
using UnityEngine;

public class PohybPostavy : MonoBehaviour
{
    [Header("Pohyb")]
    public float rychlost = 5f;
    public float rychlostSkoku = 12f;
    
    [Header("Detekce podlahy")]
    public Transform kontrolaPodlahy;
    public float polomerKontroly = 0.1f;
    public LayerMask podlahaLayer;
    
    private Rigidbody2D rb;
    private bool naPudoru;
    private float vstupX;
    private bool otocenyVpravo = true;
    
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }
    
    void Update()
    {
        vstupX = Input.GetAxis("Horizontal");
        
        if (Input.GetKeyDown(KeyCode.Space) && naPudoru)
        {
            Skok();
        }
    }
    
    void FixedUpdate()
    {
        // Kontrola podlahy
        naPudoru = Physics2D.OverlapCircle(kontrolaPodlahy.position, polomerKontroly, podlahaLayer);
        
        // Pohyb
        rb.velocity = new Vector2(vstupX * rychlost, rb.velocity.y);
        
        // Otočení postavy
        if (vstupX > 0 && !otocenyVpravo)
        {
            Otoc();
        }
        else if (vstupX < 0 && otocenyVpravo)
        {
            Otoc();
        }
    }
    
    void Skok()
    {
        rb.velocity = new Vector2(rb.velocity.x, rychlostSkoku);
    }
    
    void Otoc()
    {
        otocenyVpravo = !otocenyVpravo;
        transform.Rotate(0f, 180f, 0f);
    }
    
    void OnDrawGizmosSelected()
    {
        if (kontrolaPodlahy == null) return;
        Gizmos.color = naPudoru ? Color.green : Color.red;
        Gizmos.DrawWireSphere(kontrolaPodlahy.position, polomerKontroly);
    }
}
```

#### 2. Nastavení kontroly podlahy (10 minut)

**Postup:**
1. Vytvoříme prázdný GameObject jako dite postavy
2. Pojmenujeme "KontrolaPodlahy"
3. Umístíme pod nohy postavy
4. Přiřadíme do skriptu v poli "Kontrola Podlahy"
5. Nastavíme Layer pro platformy (Layer → Create New Layer → "Podlaha")
6. V skriptu nastavíme Podlaha Layer

#### 3. Sbírání předmětů (15 minut)

**Skript pro sbíratelé předměty:**
```csharp
using UnityEngine;

public class SbiratelnyPredmet : MonoBehaviour
{
    [Header("Nastavení")]
    public int hodnota = 10;
    public AudioClip zvukSebratin;
    
    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            // Zvýší skóre
            GameManager gameManager = FindObjectOfType<GameManager>();
            if (gameManager != null)
            {
                gameManager.PridejSkore(hodnota);
            }
            
            // Zahráj zvuk
            if (zvukSebratin != null)
            {
                AudioSource.PlayClipAtPoint(zvukSebratin, transform.position);
            }
            
            // Znič předmět
            Destroy(gameObject);
        }
    }
}
```

**Nastavení sbíratelého předmětu:**
1. Přetažením sprite (např. mince) do scény
2. Přidáme CircleCollider2D
3. Nastavíme Is Trigger = true
4. Přidáme skript SbiratelnyPredmet
5. Duplikujeme po levelů

#### 4. Základní GameManager (5 minut)

**Jednoduchý GameManager skript:**
```csharp
using UnityEngine;
using UnityEngine.UI;

public class GameManager : MonoBehaviour
{
    public int skore = 0;
    public Text skoreText;
    
    void Start()
    {
        AktualizujSkoreUI();
    }
    
    public void PridejSkore(int body)
    {
        skore += body;
        AktualizujSkoreUI();
        Debug.Log("Skóre: " + skore);
    }
    
    void AktualizujSkoreUI()
    {
        if (skoreText != null)
        {
            skoreText.text = "Skóre: " + skore;
        }
    }
}
```

### Úkol pro děti
Rozmistěte po levelů sbíratelé předměty a vyzkoušejte, jestli funguje sběr a počítání skóre.

---

## Hodina 12: Herní logika a dokončení plošinovky (45 minut)

### Cíle hodiny
- Přidat nepřátele a nebezpečné zony
- Implementovat systém životů
- Vytvořit základní UI
- Dokončit hru

### Průběh hodiny

#### 1. Nebezpečné zony (10 minut)

**Skript pro nebezpečné objekty:**
```csharp
using UnityEngine;

public class Nebezpeci : MonoBehaviour
{
    public int poskozeni = 1;
    
    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            Zdravi zdraviHrace = other.GetComponent<Zdravi>();
            if (zdraviHrace != null)
            {
                zdraviHrace.UberZdravi(poskozeni);
            }
        }
    }
}
```

**Systém zdraví:**
```csharp
using UnityEngine;
using UnityEngine.SceneManagement;

public class Zdravi : MonoBehaviour
{
    [Header("Zdraví")]
    public int maxZdravi = 3;
    public int aktualniZdravi;
    
    [Header("Efekty")]
    public float casBlikani = 0.1f;
    public int pocetBliknuti = 3;
    
    private SpriteRenderer spriteRenderer;
    private bool neporazitelny = false;
    
    void Start()
    {
        aktualniZdravi = maxZdravi;
        spriteRenderer = GetComponent<SpriteRenderer>();
        
        // Aktualizuj UI
        GameManager gm = FindObjectOfType<GameManager>();
        if (gm != null)
        {
            gm.AktualizujZdravi(aktualniZdravi, maxZdravi);
        }
    }
    
    public void UberZdravi(int poskozeni)
    {
        if (neporazitelny) return;
        
        aktualniZdravi -= poskozeni;
        
        // Aktualizuj UI
        GameManager gm = FindObjectOfType<GameManager>();
        if (gm != null)
        {
            gm.AktualizujZdravi(aktualniZdravi, maxZdravi);
        }
        
        if (aktualniZdravi <= 0)
        {
            Smrt();
        }
        else
        {
            StartCoroutine(EffektPoskozeni());
        }
    }
    
    System.Collections.IEnumerator EffektPoskozeni()
    {
        neporazitelny = true;
        
        for (int i = 0; i < pocetBliknuti; i++)
        {
            spriteRenderer.color = Color.red;
            yield return new WaitForSeconds(casBlikani);
            spriteRenderer.color = Color.white;
            yield return new WaitForSeconds(casBlikani);
        }
        
        neporazitelny = false;
    }
    
    void Smrt()
    {
        Debug.Log("Hráč zemřel!");
        // Restart scény
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
}
```

#### 2. Jednoduchý nepřátel (10 minut)

**Pohybující se nepřátel:**
```csharp
using UnityEngine;

public class JednoduchyNepitel : MonoBehaviour
{
    public float rychlost = 2f;
    public Transform kontrolaBodu;
    public float vzdalenostKontroly = 1f;
    public LayerMask podlahaLayer;
    
    private Rigidbody2D rb;
    private bool pohybVpravo = true;
    
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }
    
    void FixedUpdate()
    {
        // Kontrola, jestli může pokračovat
        bool vidipudu = Physics2D.Raycast(kontrolaBodu.position, Vector2.down, vzdalenostKontroly, podlahaLayer);
        
        if (!vidipudu)
        {
            // Otoč se
            pohybVpravo = !pohybVpravo;
            transform.Rotate(0f, 180f, 0f);
        }
        
        // Pohyb
        float smer = pohybVpravo ? 1f : -1f;
        rb.velocity = new Vector2(smer * rychlost, rb.velocity.y);
    }
    
    void OnDrawGizmosSelected()
    {
        if (kontrolaBodu == null) return;
        Gizmos.color = Color.blue;
        Gizmos.DrawRay(kontrolaBodu.position, Vector2.down * vzdalenostKontroly);
    }
}
```

#### 3. UI systém (15 minut)

**Rozšířený GameManager s UI:**
```csharp
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class GameManager : MonoBehaviour
{
    [Header("Skóre")]
    public int skore = 0;
    public Text skoreText;
    
    [Header("Zdraví")]
    public Image[] srdceUI;
    
    [Header("Cile")]
    public int ciloveSkore = 100;
    public GameObject vyherniPanel;
    
    void Start()
    {
        AktualizujSkoreUI();
        if (vyherniPanel != null)
            vyherniPanel.SetActive(false);
    }
    
    public void PridejSkore(int body)
    {
        skore += body;
        AktualizujSkoreUI();
        
        if (skore >= ciloveSkore)
        {
            Vyhra();
        }
    }
    
    void AktualizujSkoreUI()
    {
        if (skoreText != null)
        {
            skoreText.text = "Skóre: " + skore;
        }
    }
    
    public void AktualizujZdravi(int aktualniZdravi, int maxZdravi)
    {
        for (int i = 0; i < srdceUI.Length; i++)
        {
            if (i < aktualniZdravi)
            {
                srdceUI[i].color = Color.red;
            }
            else
            {
                srdceUI[i].color = Color.gray;
            }
        }
    }
    
    void Vyhra()
    {
        Debug.Log("Vyhrál jsi!");
        if (vyherniPanel != null)
        {
            vyherniPanel.SetActive(true);
            Time.timeScale = 0f; // Zastavit hru
        }
    }
    
    public void RestartHry()
    {
        Time.timeScale = 1f;
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
}
```

#### 4. Vytvoření UI (10 minut)

**Postup vytvoření UI:**
1. Pravý klik v Hierarchy → UI → Canvas
2. Přidáme Text pro skóre (UI → Text)
3. Přidáme Image pro srdce (UI → Image, duplikujeme 3×)
4. Přidáme Panel pro výhernu obrazovku
5. Propojíme s GameManagerem

### Domácí úkol
Vylepšete svou hru přidáním více levelů, sbíratelých předmětů nebo nepřátel.

### Shrnutí bloku
**Čeho jsme dosáhli:**
- Kompletní funkční 2D plošinovku
- Systém pohybu s animacemi
- Sběr předmětů a počítání skóre
- Systém zdraví a smrti
- Základní nepřátelě
- Funkční UI

**Připravili jsme se na:**
- Práci s animacemi a zvuky
- Složitější herní mechaniky
- Vylepšování existujících projektů
