# Blok 3: První 2D hra - Plošinovka od nuly (3 hodiny)

## Přehled bloku
**Formát:** David vytváří plošinovku LIVE před dětmi - od empty project k playable game
**Cíl:** Ukázat celý game dev workflow - assety, kód, testing, polish
**Cool faktor:** Během 3 hodin vznikne hra kterou můžeš hrát!

---

## Hodina 14: Assety a prostředí - stavění světa (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Nový projekt setup (5 min)
**COOL MOMENT:** "Za 45 minut z prázdna do hry!"

**Live v Unity:**
- Unity Hub → New Project
- Template: "2D Core"
- Name: "MojePlošinovka"
- Create!

**Čekání na loading?** → Ukaž cool 2D game trailer

#### 2. Import assetů - grafika zdarma (10 min)
**Dvě možnosti - ukaž obě:**

**Možnost A: Asset Store**
- Window → Asset Store
- Search: "2D platformer free"
- Stáhni "Pixel Adventure" nebo podobný pack
- Import → Select All → Import

**Možnost B: Jednoduché shapes**
- "Nechceme čekat? Použijeme squares!"
- 2D Object → Sprites → Square
- "Minecraft styl - placeholders!"

**COOL MOMENT:**
"Profesionální vývojáři začínají s placeholders! Grafika až nakonec."

#### 3. Vytvoření levelu - live design (20 min)
**David staví level před dětmi:**

**Platformy:**
1. Create → 2D Object → Sprite → Square
2. Rename: "Platform_Ground"
3. Scale: X=10, Y=1 (dlouhá, nízká)
4. Position: Y=-3 (dole)
5. Add Component → Box Collider 2D
6. Set Layer → "Ground" (create new)

**Duplicating for more platforms:**
- Ctrl+D (duplicate)
- Umísti výš a různě
- "Jako level editor! Point and click!"

**Rychlý level design:**
```
Platform Layout:
     [П]        [П]
              [П]    
  [П]                [П]

[═══════════════════════]  Ground
```

**Visual polish:**
- Color code platforms (Material → Color)
- Green = ground
- Brown = platforms  
- "Barvy pomohou orientaci!"

#### 4. Camera setup (5 min)
**Adjust kameru:**
- Select Main Camera
- Size: 5-8 (podle potřeby)
- Background Color: Sky blue

**COOL MOMENT - Test mode:**
- Zmáčkni Play
- "Vidíte level! Zatím nemůžeme nic dělat, ale svět existuje!"
- Stop

#### 5. Player placeholder (5 min)
**Vytvoř hráče:**
- 2D Object → Sprite → Square  
- Rename: "Player"
- Color: Red (aby vyčníval)
- Position: (0, 0, 0)
- Add Component → Rigidbody2D
  - Mass: 1
  - Gravity Scale: 3
- Add Component → Box Collider 2D

**Quick test:**
- Play → Player spadne na ground!
- "Fyzika funguje! ✅"

### 👥 ZAPOJENÍ
- "Jakou barvu má mít hráč?" → hlasování
- "Kam dáme platformy?" → level design suggestions
- "Má to být lehké nebo těžké?" → gap sizes
- "Testujte očima: Dá se tam vyskočit?" → gap analysis

### 💻 CO BY DĚTI MOHLY DĚLAT
- Vytvořit vlastní level layout
- Experimentovat s barvami a shapes
- Design papírového prototypu level
- Import vlastních sprite assetů

---

## Hodina 15: Pohyb a mechaniky - make it playable (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Movement script - live coding (20 min)
**COOL MOMENT:** "Z nehybného k ovladatelnému za 10 řádků!"

**Create script:**
- Right click Project → Create → C# Script
- Name: "PlayerMovement"
- Double click → otevře se editor

**David píše LIVE (pomalu, vysvětluje každý řádek):**
```csharp
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    [Header("Movement")]
    public float moveSpeed = 5f;
    public float jumpForce = 10f;
    
    [Header("Ground Check")]
    public Transform groundCheck;
    public float groundCheckRadius = 0.2f;
    public LayerMask groundLayer;
    
    private Rigidbody2D rb;
    private bool isGrounded;
    
    void Start()
    {
        rb = GetComponent<Rigidbody2D>();
    }
    
    void Update()
    {
        // Horizontal movement
        float moveInput = Input.GetAxis("Horizontal");
        rb.velocity = new Vector2(moveInput * moveSpeed, rb.velocity.y);
        
        // Ground check
        isGrounded = Physics2D.OverlapCircle(groundCheck.position, groundCheckRadius, groundLayer);
        
        // Jump
        if (Input.GetButtonDown("Jump") && isGrounded)
        {
            rb.velocity = new Vector2(rb.velocity.x, jumpForce);
        }
    }
    
    // Visual debug
    void OnDrawGizmosSelected()
    {
        if (groundCheck != null)
        {
            Gizmos.color = Color.red;
            Gizmos.DrawWireSphere(groundCheck.position, groundCheckRadius);
        }
    }
}
```

**Vysvětlení během psaní:**
- `[Header]` → "Organizace v Inspectoru"
- `moveSpeed` → "Jak rychle běží"
- `jumpForce` → "Jak vysoko skáče"
- `isGrounded` → "Je na zemi? Pak může skočit"
- `OnDrawGizmos` → "Debug helper - vidíme ground check"

#### 2. Script setup v Unity (10 min)
**Připojení skriptu:**
1. Drag "PlayerMovement" script na Player objekt
2. Inspector → vidíme public variables!

**Ground Check setup:**
- Create Empty GameObject jako child Playera
- Name: "GroundCheck"
- Position: (0, -0.6, 0) - pod nohama
- Drag do "Ground Check" pole

**Layer setup:**
- Platforms → Inspector → Layer → Ground
- Player Movement → Ground Layer → select "Ground"

**COOL MOMENT - První test:**
- Zmáčkni Play
- Stiskni A/D nebo šipky → POHYB! 🎉
- Space → SKOK! 🎉
- "HRA JE OVLADATELNÁ!"

#### 3. Camera follow - smooth movement (10 min)
**Kamera co sleduje hráče:**

**Create new script: "CameraFollow"**
```csharp
using UnityEngine;

public class CameraFollow : MonoBehaviour
{
    public Transform target;
    public float smoothSpeed = 0.125f;
    public Vector3 offset = new Vector3(0, 0, -10);
    
    void LateUpdate()
    {
        if (target == null) return;
        
        Vector3 desiredPosition = target.position + offset;
        Vector3 smoothedPosition = Vector3.Lerp(transform.position, desiredPosition, smoothSpeed);
        transform.position = smoothedPosition;
    }
}
```

**Setup:**
- Attach na Main Camera
- Drag Player do "Target" pole
- Test → Kamera sleduje! 📷

#### 4. Quick polish (5 min)
**Drobné vylepšení:**

**Flip sprite při pohybu:**
```csharp
// Přidej do PlayerMovement Update():
if (moveInput > 0)
    transform.localScale = new Vector3(1, 1, 1);
else if (moveInput < 0)
    transform.localScale = new Vector3(-1, 1, 1);
```

**Test všeho:**
- Pohyb doleva/doprava ✅
- Skok ✅  
- Kamera sleduje ✅
- Sprite se otáčí ✅

**"MÁME FUNKČNÍ CORE MECHANIC!"**

### 👥 ZAPOJENÍ
- "Jak rychle má běžet? 5 nebo 10?" → speed testing
- "Vysoký nebo nízký skok?" → jump tuning
- "Testujte! Je to příjemné ovládat?" → feel testing
- Děti mohou testovat (pokud možné)

### 💻 CO BY DĚTI MOHLY DĚLAT
- Napsat stejný movement script
- Experimentovat s speed/jump values
- Přidat double jump feature
- Vytvořit složitější level pro test

---

## Hodina 16: Game over, score a dokončení (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Sběratelné objekty - mince (15 min)
**COOL MOMENT:** "Sbírej a počítej!"

**Create coin:**
- 2D Sprite → Circle (nebo coin asset)
- Color: Yellow/Gold
- Add Component → Circle Collider 2D
  - **Is Trigger: TRUE** ← důležité!
- Tag: "Coin" (create new)

**Coin script:**
```csharp
using UnityEngine;

public class Coin : MonoBehaviour
{
    public int value = 1;
    
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            GameManager.instance.AddScore(value);
            Destroy(gameObject);  // Zmizí!
        }
    }
}
```

**Roztrousení mincí po levelu:**
- Duplicate coin
- Rozmísti zajímavě (na platformách, ve vzduchu)
- "Level design! Risk vs reward!"

#### 2. Game Manager - centrální řízení (15 min)
**Singleton pattern (simplified pro děti):**

**Create GameManager script:**
```csharp
using UnityEngine;
using TMPro;

public class GameManager : MonoBehaviour
{
    public static GameManager instance;  // Singleton
    
    [Header("UI")]
    public TextMeshProUGUI scoreText;
    public GameObject gameOverPanel;
    
    private int score = 0;
    
    void Awake()
    {
        // Singleton setup
        if (instance == null)
            instance = this;
        else
            Destroy(gameObject);
    }
    
    void Start()
    {
        gameOverPanel.SetActive(false);
        UpdateScoreUI();
    }
    
    public void AddScore(int amount)
    {
        score += amount;
        UpdateScoreUI();
        Debug.Log("Skóre: " + score);
    }
    
    void UpdateScoreUI()
    {
        if (scoreText != null)
            scoreText.text = "Coins: " + score;
    }
    
    public void GameOver()
    {
        gameOverPanel.SetActive(true);
        Time.timeScale = 0;  // Pause!
    }
    
    public void RestartGame()
    {
        Time.timeScale = 1;
        UnityEngine.SceneManagement.SceneManager.LoadScene(0);
    }
}
```

**Setup:**
- Create Empty GameObject → "GameManager"
- Attach script

#### 3. UI System - score display (10 min)
**Canvas vytvoření:**
- Right click Hierarchy → UI → Canvas
- Auto vytvoří Canvas + EventSystem ✅

**Score text:**
- Right click Canvas → UI → Text - TextMeshPro
- (First time: Import TMP Essentials)
- Name: "ScoreText"
- Anchor: Top Left
- Text: "Coins: 0"
- Font Size: 36
- Color: Yellow

**Game Over panel:**
- Right click Canvas → UI → Panel
- Name: "GameOverPanel"
- Color: Semi-transparent red
- Add child: Text → "GAME OVER"
- Add child: Button → "Restart"

**Wire up:**
- GameManager → Drag ScoreText do script field
- GameManager → Drag GameOverPanel do script field
- Restart Button → OnClick → GameManager.RestartGame()

#### 4. Death zone - Game Over trigger (5 min)
**Pod úrovní:**
- Create Empty GameObject: "DeathZone"
- Position: Y = -10 (pod vším)
- Add Component → Box Collider 2D
  - Is Trigger: TRUE
  - Size: X = 100, Y = 1 (široký)

**DeathZone script:**
```csharp
using UnityEngine;

public class DeathZone : MonoBehaviour
{
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.CompareTag("Player"))
        {
            GameManager.instance.GameOver();
        }
    }
}
```

**FINAL TEST - Complete gameplay:**
1. Play
2. Pohyb a skok ✅
3. Sbírání mincí → skóre roste ✅
4. Spadnutí dolů → Game Over ✅
5. Restart button → hra se restartuje ✅

**"HOTOVÁ HRA! 🎉"**

### 👥 ZAPOJENÍ
- "Kolik mincí má být v levelu?"
- "Kde je risk postavit minci?" → nad propastí?
- "Jaká barva pro Game Over screen?"
- "Testování: Je hra zábavná? Nebo frustrující?"

### 💻 CO BY DĚTI MOHLY DĚLAT
- Dokončit svou vlastní plošinovku
- Přidat power-ups (double jump, speed boost)
- Vytvořit více levelů
- Přidat nepřátele (moving obstacles)
- Design complex level s různými challenges
- Polish: particles při sbírání, zvuky, animace

---

## Shrnutí bloku 3

### Co děti viděly za 3 hodiny:
✅ **Hodina 14:** Assety, level design, physics setup
✅ **Hodina 15:** Movement coding, camera follow, playable game
✅ **Hodina 16:** Collectibles, score system, UI, game over

### Vytvořeno od nuly:
- 🎮 Kompletní playable 2D platformer
- 👾 Ovladatelná postava s fyzikou
- 🪙 Sbíratelné objekty a skóre
- 📊 UI systém (HUD + menus)
- 💀 Game over mechanika
- 🔄 Restart funkcionalita

### Key learnings (implicitně):
- **Game dev workflow:** Design → Code → Test → Polish
- **Iteration:** Rychle testuj, často upravuj
- **Core mechanic first:** Pohyb a skok jsou základ, zbytek je polish
- **Placeholders OK:** Nemusíš mít krásné assety hned
- **Scripting patterns:** Singleton, Triggers, UI updates
- **Feel matters:** Hodnoty (speed, jump) tvoří feeling hry

### Co dál:
- Další bloky přidají: Animace, zvuky, efekty, více mechanik
- Děti můžou expandovat tuto hru nebo začít novou

---

## Poznámky pro Davida

### Preparation je klíč:
- ✅ **Před hodinou TEST celý workflow** - nesmí být překvapení
- ✅ **Měj backup project** - ready-made pokud live coding selže
- ✅ **Assets ready** - stažené nebo placeholders prepared

### Live coding tips:
- **Píš POMALU** - děti musí číst co píšeš
- **Komentuj v češtině** každý řádek
- **Syntax errors jsou OK** - ukaž troubleshooting!
- **Test každých 10 min** - okamžitá feedback
- **Velké písmo** - 18pt+ v editoru

### Energy management přes 3 hodiny:
- **Hodina 14:** Setup, může být slower (stavění, vizuál)
- **Hodina 15:** HIGH ENERGY - pohyb funguje = wow!
- **Hodina 16:** Features a dokončení - satisfying konec

### Timing:
- Každá hodina = 45 min
- Nech 5 min buffer na questions/troubleshooting
- Pokud jsi rychlejší → přidej extra features (animace rotate, particles)
- Pokud pomalejší → skip některé polish steps

### Common issues:
- **Player padá skrz platformy:** Check Collider 2D a Rigidbody settings
- **Skok nefunguje:** Ground check layer a position
- **UI neviditelné:** Canvas Render Mode = Screen Space Overlay
- **Script errors:** Usually typo - ukáž jak číst error v Console

### Engagement hooks:
- "Jakou mechaniku přidat?" → děti rozhodují
- "Je to moc lehké nebo těžké?" → balance discussion
- "Kdo by chtěl tohle testovat?" → volunteers
- Real-time suggestions: "Zkusme nápad od Martina!"

### Celebration moments:
- ✅ První pohyb → "MÁME POHYB!"
- ✅ První skok → "SKÁČE!"
- ✅ První coin collect → "FUNGUJE!"
- ✅ Kompletní gameplay loop → "HOTOVÁ HRA! 🎉"

### After class:
- Upload projekt někam (Google Drive/GitHub) aby děti mohly
- Screenshot nebo krátké video z hotové hry
- → Ukázat rodičům "to jsme vytvořili!"

---

## Bonus: Rozšíření pokud je čas

### Quick wins (5-10 min each):

**1. Rotation animation pro mince:**
```csharp
void Update() {
    transform.Rotate(0, 0, 90 * Time.deltaTime);
}
```

**2. Sound effects:**
- Import coin sound
- Přidej AudioSource component
- PlayOneShot při sbírání

**3. Particle efekt při sbírání:**
- Particle System na minci
- Play on destroy

**4. Health system:**
- 3 životy místo instant death
- Hearts UI
- Invincibility frames po damage

**5. Moving platforms:**
- Platform co se pohybuje tam a zpět
- Player jako child když stojí na platformě

### Kdyď jsou děti extra rychlé:
- Začni další level
- Přidej boss fight
- Menu screen s play button
- Settings (volume, difficulty)

### Pokud tech selhává:
- Přepni na Roblox Studio → podobný workflow
- Ukaž hotovou hru místo live coding
- Pusť inspirativní game dev video

---

**Výsledek:** Za 3 hodiny mají děti viděly jak vzniká hra od absolutního nuly k playable stavu. To je motivující a demystifikuje game development! 🚀

