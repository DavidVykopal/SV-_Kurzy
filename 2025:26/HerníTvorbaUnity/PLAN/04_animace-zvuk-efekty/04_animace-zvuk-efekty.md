# Blok 4: Animace, zvuk a efekty (13–16)

## Přehled bloku
**Cíl:** Naučit děti vytvářet animace, přidávat zvuky a vizuální efekty do svých her.
**Výstup:** Vylepšená plošinovka s animacemi, zvuky a efekty.

---

## Hodina 13: Sprity a animace (45 minut)

### Cíle hodiny
- Pochopit principy 2D animace
- Vytvořit animace pro postavu (idle, walk, jump)
- Naučit se používat Animator Controller

### Materiály
- Sprite sheety s animacemi postavy
- Nástroj pro rozdělení sprite sheetů (Sprite Editor)

### Průběh hodiny

#### 1. Co je 2D animace? (10 minut)

**Princip animace:**
- Animace = rychlé střídání obrázků
- Jako listování v sešitě s nakreslenými obrázky
- 12-24 snímků za sekundu = plynulá animace

**Typy animací pro postavy:**
- **Idle** - postava stálá (dychaní, mrknání)
- **Walk/Run** - chůze/běh
- **Jump** - skok (vzlet, let, pád)
- **Attack** - útok
- **Death** - smrt

#### 2. Příprava sprite sheetů (10 minut)

**Co je sprite sheet:**
Veliký obrázek obsahující všechny snímky animace v řadě.

**Rozdělení sprite sheetu:**
1. Vybereme sprite sheet v Project
2. V Inspector nastavíme:
   - Texture Type: Sprite (2D and UI)
   - Sprite Mode: Multiple
3. Klikneme na "Sprite Editor"
4. Použijeme "Slice" → "Grid By Cell Count"
5. Nastavíme počet sloupec a řádků
6. Klikneme "Slice" a "Apply"

#### 3. Vytvoření animací (20 minut)

**Postup vytvoření animace:**
1. Vybereme postavu ve scéně
2. Otevřeme Animation okno (Window → Animation → Animation)
3. Klikneme "Create" a pojmenujeme animaci (např. "Player_Idle")
4. Přidáváme klíčové snímky (keyframes):
   - Klikneme na červené tlačítko (Record)
   - Měníme sprite na SpriteRenderer komponentě
   - Posouváme timeline a měníme sprite

**Animace Idle (klidný stav):**
```
Frame 0:00 - sprite_idle_1
Frame 0:20 - sprite_idle_2  
Frame 0:40 - sprite_idle_1
```

**Animace Walk (chůze):**
```
Frame 0:00 - sprite_walk_1
Frame 0:10 - sprite_walk_2
Frame 0:20 - sprite_walk_3
Frame 0:30 - sprite_walk_4
```

#### 4. Animator Controller (5 minut)

**Nastavení přechodů:**
1. Otevřeme Animator okno (Window → Animation → Animator)
2. Vidíme naše animace jako "boxy"
3. Klikneme pravým na Idle → "Make Transition" → Walk
4. Nastavíme podmínky přechodu (parametry)

### Úkol pro děti
Vytvořte alespoň 2 animace pro svou postavu (Idle a Walk).

---

## Hodina 14: Zvuky a hudba (45 minut)

### Cíle hodiny
- Pochopit rozdíl mezi hudbou a sound efekty
- Naučit se importovat a používat audiosoubory
- Přidat zvuky do hry

### Materiály
- Sbírka zvuků (skok, sběr mince, hudba na pozadí)
- Freesound.org, Zapsplat.com (s registrací) nebo OpenGameArt.org

### Průběh hodiny

#### 1. Typy zvuků ve hrách (10 minut)

**Kategorie zvuků:**
- **Hudba na pozadí** (Background Music) - dlouhá, opakující se
- **Sound efekty** (SFX) - krátké, okamžité
- **Ambientové zvuky** - atmosféra prostředí
- **Hlas** (Voice) - mluvené slovo

**Příklady sound efektů:**
- Skok postavy
- Sběr předmětu
- Explode, střelba
- Otevření dveří
- Kráčení po různých povrzích

#### 2. Import zvuků do Unity (10 minut)

**Podporované formáty:**
- WAV (nejlepší kvalita)
- MP3 (menší soubory)
- OGG (dobrý kompromis)

**Postup importu:**
1. Přetažením audiosoubory do Project
2. V Inspector nastavíme:
   - **Pro hudbu:** Audio Type = Music, Compression = Vorbis
   - **Pro SFX:** Audio Type = SFX, Compression = PCM

#### 3. Hudba na pozadí (10 minut)

**Přidání pozadní hudby:**
1. Vytvoříme prázdný GameObject "MusicManager"
2. Přidáme AudioSource komponentu
3. Přiřadíme AudioClip s hudbou
4. Nastavíme:
   - Play On Awake = true
   - Loop = true
   - Volume = 0.5

**Skript pro správu hudby:**
```csharp
using UnityEngine;

public class MusicManager : MonoBehaviour
{
    [Header("Nastavení hudby")]
    public AudioClip pozadniHudba;
    public float hlasitost = 0.5f;
    
    private AudioSource audioSource;
    
    void Start()
    {
        audioSource = GetComponent<AudioSource>();
        audioSource.clip = pozadniHudba;
        audioSource.volume = hlasitost;
        audioSource.loop = true;
        audioSource.Play();
    }
    
    public void NastavHlasitost(float novaHlasitost)
    {
        audioSource.volume = novaHlasitost;
    }
    
    public void ZapnoutVypnoutHudbu()
    {
        if (audioSource.isPlaying)
        {
            audioSource.Pause();
        }
        else
        {
            audioSource.Play();
        }
    }
}
```

#### 4. Sound efekty (15 minut)

**Rozšíření PohybPostavy skriptu:**
```csharp
using UnityEngine;

public class PohybPostavy : MonoBehaviour
{
    [Header("Pohyb")]
    public float rychlost = 5f;
    public float rychlostSkoku = 12f;
    
    [Header("Zvuky")]
    public AudioClip zvukSkoku;
    public AudioClip zvukChuzee;
    public float hlasitostZvuku = 1f;
    
    private AudioSource audioSource;
    private Rigidbody2D rb;
    private bool naPudoru;
    private bool chodi;
    
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
        audioSource = GetComponent<AudioSource>();
    }
    
    void Update()
    {
        float vstupX = Input.GetAxis("Horizontal");
        
        // Kontrola chůze
        bool predchoziChozi = chodi;
        chodi = (Mathf.Abs(vstupX) > 0.1f && naPudoru);
        
        // Zvuk chůze
        if (chodi && !predchoziChozi)
        {
            ZahrajZvuk(zvukChuzee, true);
        }
        else if (!chozi && predchoziChozi)
        {
            audioSource.Stop();
        }
        
        // Skok
        if (Input.GetKeyDown(KeyCode.Space) && naPudoru)
        {
            Skok();
            ZahrajZvuk(zvukSkoku, false);
        }
        
        // Pohyb
        rb.velocity = new Vector2(vstupX * rychlost, rb.velocity.y);
    }
    
    void Skok()
    {
        rb.velocity = new Vector2(rb.velocity.x, rychlostSkoku);
    }
    
    void ZahrajZvuk(AudioClip clip, bool opakovat)
    {
        if (clip != null)
        {
            audioSource.clip = clip;
            audioSource.volume = hlasitostZvuku;
            audioSource.loop = opakovat;
            audioSource.Play();
        }
    }
}
```

**Zvuk pro sbíratelé předměty (aktualizace):**
```csharp
// V SbiratelnyPredmet skriptu přidáme:
public AudioClip zvukSebratin;

private void OnTriggerEnter2D(Collider2D other)
{
    if (other.CompareTag("Player"))
    {
        // Zahráj zvuk
        if (zvukSebratin != null)
        {
            AudioSource.PlayClipAtPoint(zvukSebratin, transform.position);
        }
        
        // ... zbytek kódu
    }
}
```

### Úkol pro děti
Přidejte do své hry alespoň 3 různé zvuky (skok, sběr, pozadní hudba).

---

## Hodina 15: Partiklové efekty (45 minut)

### Cíle hodiny
- Pochopit, co jsou particle systémy
- Vytvořit základní efekty (exploze, sběr předmětu, snížení)
- Nastavit particle systém v Unity

### Průběh hodiny

#### 1. Co jsou particle systémy? (10 minut)

**Definice:** Particle systém vytváří mnoho malých objektů (particles), které simulují efekty.

**Příklady použití:**
- Ohňeň, kouř
- Exploze
- Snížení, deště
- Magické efekty
- Jískry při sběru předmětu

#### 2. Základní particle systém (15 minut)

**Vytvoření particle systému:**
1. Pravý klik v Hierarchy → Effects → Particle System
2. Ve scéně vidíme bílé particles

**Základní nastavení:**
- **Start Lifetime:** jak dlouho particles žije
- **Start Speed:** rychlost particles
- **Start Size:** velikost particles
- **Start Color:** barva particles
- **Rate over Time:** kolik particles za sekundu

#### 3. Efekt sběru předmětu (10 minut)

**Nastavení pro jískry:**
1. Start Lifetime: 0.5
2. Start Speed: 3
3. Start Size: 0.1
4. Start Color: žlutá
5. Max Particles: 20
6. Rate over Time: 0 (nechceme neustálé particles)
7. Bursts: Count = 10, Time = 0 (jednorázový výbušek)

**Shape modul:**
- Shape: Circle
- Radius: 0.5

**Přidání do SbiratelnyPredmet:**
```csharp
using UnityEngine;

public class SbiratelnyPredmet : MonoBehaviour
{
    public int hodnota = 10;
    public AudioClip zvukSebratin;
    public ParticleSystem efektSebratin;
    
    private void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            // Particle efekt
            if (efektSebratin != null)
            {
                Instantiate(efektSebratin, transform.position, Quaternion.identity);
            }
            
            // Zvuk
            if (zvukSebratin != null)
            {
                AudioSource.PlayClipAtPoint(zvukSebratin, transform.position);
            }
            
            // Skóre
            GameManager gm = FindObjectOfType<GameManager>();
            if (gm != null)
            {
                gm.PridejSkore(hodnota);
            }
            
            Destroy(gameObject);
        }
    }
}
```

#### 4. Prefaby pro opakované použití (10 minut)

**Vytvoření prefabů:**
1. Particle system přetažením z Hierarchy do Project
2. Pojmenujeme "Efekt_SberPredmetu"
3. Můžeme používat víckrát

**Auto-destrukce particle systému:**
```csharp
using UnityEngine;

public class AutoDestrukceParticle : MonoBehaviour
{
    void Start()
    {
        ParticleSystem ps = GetComponent<ParticleSystem>();
        if (ps != null)
        {
            float životnost = ps.main.startLifetimeMultiplier + ps.main.duration;
            Destroy(gameObject, životnost);
        }
    }
}
```

### Úkol pro děti
Vytvořte vlastní particle efekt (jiné barvy, tvary, chování) a přidejte ho do své hry.

---

## Hodina 16: Vylepšení malé hry (45 minut)

### Cíle hodiny
- Implementovat všechny naučené prvky
- Vylepšit gameplay a user experience
- Připravit hru na prezentaci

### Průběh hodiny

#### 1. Kontrola a integrace (15 minut)

**Checklist pro hru:**
- ✓ Postavy mají animace (idle, walk, jump)
- ✓ Zvuky pro skok, sběr, pozadní hudba
- ✓ Particle efekty při sběru předmětů
- ✓ UI ukazuje skóre a zdraví
- ✓ Hra má jasný cíl

**Testování:**
Každý žák si zahráje svou hru a označí, co funguje a co ne.

#### 2. Animator Controller pro postavu (10 minut)

**Kompletní animator setup:**
```csharp
using UnityEngine;

public class AnimatorKontroler : MonoBehaviour
{
    private Animator animator;
    private Rigidbody2D rb;
    private bool naPudoru;
    
    void Start()
    {
        animator = GetComponent<Animator>();
        rb = GetComponent<Rigidbody2D>();
    }
    
    void Update()
    {
        // Parametry pro animator
        float rychlostX = Mathf.Abs(rb.velocity.x);
        float rychlostY = rb.velocity.y;
        
        animator.SetFloat("Speed", rychlostX);
        animator.SetBool("IsGrounded", naPudoru);
        animator.SetFloat("VelocityY", rychlostY);
    }
    
    public void NastavNaPudoru(bool hodnota)
    {
        naPudoru = hodnota;
    }
}
```

#### 3. Vylepšení UI a feedbacku (10 minut)

**Animované UI skóre:**
```csharp
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class AnimovaneUI : MonoBehaviour
{
    public Text skoreText;
    public float dobaTrvaniAnimace = 0.5f;
    
    private int aktualniSkore = 0;
    private int cilobeSkore = 0;
    
    public void AktualizujSkore(int noveSkore)
    {
        ciloveSkore = noveSkore;
        StartCoroutine(AnimujSkore());
    }
    
    IEnumerator AnimujSkore()
    {
        float casStart = Time.time;
        int startSkore = aktualniSkore;
        
        while (Time.time - casStart < dobaTrvaniAnimace)
        {
            float progress = (Time.time - casStart) / dobaTrvaniAnimace;
            aktualniSkore = Mathf.RoundToInt(Mathf.Lerp(startSkore, ciloveSkore, progress));
            skoreText.text = "Skóre: " + aktualniSkore;
            yield return null;
        }
        
        aktualniSkore = ciloveSkore;
        skoreText.text = "Skóre: " + aktualniSkore;
    }
}
```

#### 4. Finalizace a testování (10 minut)

**Poslední úpavy:**
- Nastavení hlasitosti zvuků
- Kontrola kolizí
- Testování na různých rozlišeních
- Přidání restart tlačítka

**Export hry:**
1. File → Build Settings
2. Vybereme platformu (PC, Mac & Linux Standalone)
3. Klikneme "Build"
4. Uložíme do složky "Builds"

### Prezentace her
Každý žák ukáže svou hru ostatním a řekne, co se mu podařilo a co bylo nejtrudější.

### Shrnutí bloku
**Čeho jsme dosáhli:**
- 2D animace pro postavy
- Integrovaný zvukový design
- Vizuální efekty pomocí particles
- Vylepšené UI s animacemi
- Exportovatelná hra

**Připravili jsme se na:**
- Práci ve 3D prostředí
- Složitější mechaniky a systémy
- Profesionálnější přístup k game designu
