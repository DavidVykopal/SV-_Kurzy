# Blok 6: Tvorba 3D hry - FPS (20–23)

## Přehled bloku
**Cíl:** Vytvořit jednoduchou FPS (First Person Shooter) hru s ovládáním, střelbou a základní AI.
**Výstup:** Funkční 3D FPS hra s nepřáteli, střelbou a jednoduchými úkoly.

---

## Hodina 20: Ovládání hráče (FPS) (45 minut)

### Cíle hodiny
- Vytvořit FPS controller pro postavu
- Implementovat plynný pohyb a otočení kamery
- Přidat základní mechaniky (skok, běh)

### Materiály
- Nový 3D projekt "MojeFPSHra"
- Základní 3D level (podlaha + stěny)

### Průběh hodiny

#### 1. Co je FPS hra? (10 minut)

**FPS (First Person Shooter) charakteristiky:**
- Pohled z první osoby
- Hráč vidí svět očima postavy
- Často obsahuje střelbu a akci
- Příklady: Minecraft (přepnutí do FPS), Valorant, Counter-Strike

**Základní komponenty FPS:**
- **Controller:** Pohyb hráče
- **Kamera:** Pohled z první osoby
- **Input:** Ovládání myší a klávesnicí
- **Physics:** Kolize a gravitace

#### 2. Nastavení postavy (10 minut)

**Struktura FPS hráče:**
```
Player (prázdný GameObject)
├── CharacterController komponent
├── PlayerMovement skript
└── Main Camera (jako child)
    └── MouseLook skript
```

**Postup nastavení:**
1. Vytvoříme prázdný GameObject "Player"
2. Přidáme Character Controller komponentu
3. Nastavíme Character Controller:
   - Height: 2
   - Radius: 0.5
   - Center: Y = 1
4. Přesuneme Main Camera jako child objektu Player
5. Nastavíme kameru na pozici (0, 1.8, 0)

#### 3. Pohybový systém (20 minut)

**PlayerMovement skript:**
```csharp
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    [Header("Pohyb")]
    public float rychlostChůze = 6f;
    public float rychlostBěhu = 12f;
    public float sílaSkoku = 8f;
    public float gravitace = 20f;
    
    [Header("Nastavení")]
    public bool můžeBěhat = true;
    public bool můžeSkok = true;
    
    private CharacterController controller;
    private Vector3 pohybSměr = Vector3.zero;
    private bool běží;
    
    void Start()
    {
        controller = GetComponent<CharacterController>();
    }
    
    void Update()
    {
        // Detekce inputu
        float h = Input.GetAxis("Horizontal"); // A,D
        float v = Input.GetAxis("Vertical");   // W,S
        běží = Input.GetKey(KeyCode.LeftShift) && můžeBěhat;
        
        // Jestli jsme na zemi
        if (controller.isGrounded)
        {
            // Vypočítej směr pohybu
            pohybSměr = transform.TransformDirection(new Vector3(h, 0, v));
            
            // Vyber rychlost
            float aktualníRychlost = běží ? rychlostBěhu : rychlostChůze;
            pohybSměr *= aktualníRychlost;
            
            // Skok
            if (Input.GetKeyDown(KeyCode.Space) && můžeSkok)
            {
                pohybSměr.y = sílaSkoku;
            }
        }
        
        // Aplikuj gravitaci
        pohybSměr.y -= gravitace * Time.deltaTime;
        
        // Pohyb
        controller.Move(pohybSměr * Time.deltaTime);
    }
    
    public bool JeNaZemi()
    {
        return controller.isGrounded;
    }
    
    public bool Běží()
    {
        return běží && controller.isGrounded;
    }
}
```

**MouseLook skript pro kameru:**
```csharp
using UnityEngine;

public class MouseLook : MonoBehaviour
{
    [Header("Citlivost myši")]
    public float citlivostX = 2f;
    public float citlivostY = 2f;
    
    [Header("Omezení")]
    public float minY = -90f;
    public float maxY = 90f;
    
    private float rotaceY = 0f;
    private Transform playerTransform;
    
    void Start()
    {
        // Najdi player transform
        playerTransform = transform.parent;
        
        // Zamkni kurzor
        Cursor.lockState = CursorLockMode.Locked;
    }
    
    void Update()
    {
        // ESC pro odemknutí kurzoru
        if (Input.GetKeyDown(KeyCode.Escape))
        {
            Cursor.lockState = CursorLockMode.None;
        }
        
        // Mouse input
        float mouseX = Input.GetAxis("Mouse X");
        float mouseY = Input.GetAxis("Mouse Y");
        
        // Horizontální otáčení (player)
        if (playerTransform != null)
        {
            playerTransform.Rotate(0, mouseX * citlivostX, 0);
        }
        
        // Vertikální otáčení (kamera)
        rotaceY -= mouseY * citlivostY;
        rotaceY = Mathf.Clamp(rotaceY, minY, maxY);
        transform.localRotation = Quaternion.Euler(rotaceY, 0, 0);
    }
}
```

#### 4. Testování a ladění (5 minut)

**Checklist pro testování:**
- ✓ Pohyb WASD funguje plynně
- ✓ Myš otáčí kameru správným směrem
- ✓ Shift zvyšuje rychlost
- ✓ Mezera funguje pro skok
- ✓ Gravitace funguje správně

### Úkol pro děti
Vytvořte jednoduchý level (kostky jako stěny, podlahu) a vyzkoušejte pohyb. Přidejte rampu pro testování skoku.

---

## Hodina 21: Kamera a střelba (45 minut)

### Cíle hodiny
- Vylepšit kamerový systém
- Implementovat základní střelbu
- Přidat vizualizaci střelby (raycast)

### Průběh hodiny

#### 1. Vylepšení kamery (10 minut)

**Headbobbing (houpání hlavy) při chůzi:**
```csharp
using UnityEngine;

public class CameraEffects : MonoBehaviour
{
    [Header("Head Bobbing")]
    public float bobFrequence = 2f;
    public float bobIntenzita = 0.05f;
    
    private Vector3 původníPozice;
    private float bobTimer;
    private PlayerMovement playerMovement;
    
    void Start()
    {
        původníPozice = transform.localPosition;
        playerMovement = transform.parent.GetComponent<PlayerMovement>();
    }
    
    void Update()
    {
        if (playerMovement != null && playerMovement.JeNaZemi())
        {
            // Pohyb = bobbing
            float h = Input.GetAxis("Horizontal");
            float v = Input.GetAxis("Vertical");
            
            if (Mathf.Abs(h) > 0.1f || Mathf.Abs(v) > 0.1f)
            {
                bobTimer += Time.deltaTime * bobFrequence;
                float bobOffset = Mathf.Sin(bobTimer) * bobIntenzita;
                transform.localPosition = původníPozice + new Vector3(0, bobOffset, 0);
            }
            else
            {
                // Plynulé vrácení do původní pozice
                transform.localPosition = Vector3.Lerp(
                    transform.localPosition, 
                    původníPozice, 
                    Time.deltaTime * 5f
                );
                bobTimer = 0;
            }
        }
    }
}
```

#### 2. Systém střelby (20 minut)

**WeaponController skript:**
```csharp
using UnityEngine;

public class WeaponController : MonoBehaviour
{
    [Header("Nastavení zbraně")]
    public int maxAmmo = 30;
    public int currentAmmo;
    public float damage = 25f;
    public float range = 100f;
    public float fireRate = 15f;
    public float reloadTime = 2f;
    
    [Header("Efekty")]
    public ParticleSystem muzzleFlash;
    public GameObject bulletHoleEffect;
    public AudioClip shootSound;
    public AudioClip reloadSound;
    
    private float nextTimeToFire = 0f;
    private bool isReloading = false;
    private Camera fpsCam;
    private AudioSource audioSource;
    
    void Start()
    {
        currentAmmo = maxAmmo;
        fpsCam = GetComponentInParent<Camera>();
        audioSource = GetComponent<AudioSource>();
    }
    
    void Update()
    {
        // Reload
        if (Input.GetKeyDown(KeyCode.R) && currentAmmo < maxAmmo && !isReloading)
        {
            StartCoroutine(Reload());
            return;
        }
        
        if (isReloading) return;
        
        // Střelba
        if (Input.GetButton("Fire1") && Time.time >= nextTimeToFire)
        {
            nextTimeToFire = Time.time + 1f / fireRate;
            Shoot();
        }
    }
    
    void Shoot()
    {
        if (currentAmmo <= 0)
        {
            // Prázdná zbraň
            return;
        }
        
        currentAmmo--;
        
        // Muzzle flash
        if (muzzleFlash != null)
        {
            muzzleFlash.Play();
        }
        
        // Zvuk
        if (shootSound != null)
        {
            audioSource.PlayOneShot(shootSound);
        }
        
        // Raycast
        RaycastHit hit;
        if (Physics.Raycast(fpsCam.transform.position, fpsCam.transform.forward, out hit, range))
        {
            Debug.Log("Zasáhl: " + hit.transform.name);
            
            // Efekt zásahu
            if (bulletHoleEffect != null)
            {
                GameObject hole = Instantiate(bulletHoleEffect, hit.point, Quaternion.LookRotation(hit.normal));
                Destroy(hole, 10f);
            }
            
            // Poškození
            Enemy enemy = hit.transform.GetComponent<Enemy>();
            if (enemy != null)
            {
                enemy.TakeDamage(damage);
            }
        }
    }
    
    System.Collections.IEnumerator Reload()
    {
        isReloading = true;
        
        if (reloadSound != null)
        {
            audioSource.PlayOneShot(reloadSound);
        }
        
        yield return new WaitForSeconds(reloadTime);
        
        currentAmmo = maxAmmo;
        isReloading = false;
    }
}
```

#### 3. Crosshair (zaměřovač) (10 minut)

**UI Crosshair:**
1. Canvas → UI → Image
2. Nastavíme na střed obrazovky
3. Malý bílý křížek nebo tečka

**Crosshair skript:**
```csharp
using UnityEngine;
using UnityEngine.UI;

public class Crosshair : MonoBehaviour
{
    public Image crosshairImage;
    public Color normalColor = Color.white;
    public Color hitColor = Color.red;
    public float colorChangeTime = 0.1f;
    
    void Start()
    {
        if (crosshairImage == null)
            crosshairImage = GetComponent<Image>();
    }
    
    public void OnHit()
    {
        StartCoroutine(CrosshairHitEffect());
    }
    
    System.Collections.IEnumerator CrosshairHitEffect()
    {
        crosshairImage.color = hitColor;
        yield return new WaitForSeconds(colorChangeTime);
        crosshairImage.color = normalColor;
    }
}
```

#### 4. Debug vizualizace (5 minut)

**Vizualizace raycast v Scene view:**
```csharp
// Přidat do WeaponController Shoot() metody:
Debug.DrawRay(fpsCam.transform.position, fpsCam.transform.forward * range, Color.red, 0.1f);
```

### Úkol pro děti
Přidejte do levelu několik kostek a vyzkoušejte střelbu. Pozorujte Debug.DrawRay v Scene view.

---

## Hodina 22: Nepřátelé, AI (45 minut)

### Cíle hodiny
- Vytvořit základní AI nepřítele
- Implementovat systém zdraví pro nepřátele
- Přidat jednoduchou AI logiku (sledování hráče)

### Průběh hodiny

#### 1. Základní nepřítel (15 minut)

**Struktura nepřítele:**
```
Enemy (Capsule)
├── CapsuleCollider
├── Rigidbody (IsKinematic = true)
├── NavMeshAgent
├── Enemy skript
└── EnemyAI skript
```

**Enemy skript (zdraví):**
```csharp
using UnityEngine;

public class Enemy : MonoBehaviour
{
    [Header("Zdraví")]
    public float maxHealth = 100f;
    public float currentHealth;
    
    [Header("Efekty")]
    public ParticleSystem deathEffect;
    public AudioClip hitSound;
    public AudioClip deathSound;
    
    private AudioSource audioSource;
    private EnemyAI enemyAI;
    
    void Start()
    {
        currentHealth = maxHealth;
        audioSource = GetComponent<AudioSource>();
        enemyAI = GetComponent<EnemyAI>();
    }
    
    public void TakeDamage(float damage)
    {
        currentHealth -= damage;
        
        // Zvuk zásahu
        if (hitSound != null)
        {
            audioSource.PlayOneShot(hitSound);
        }
        
        // Efekt poškození
        StartCoroutine(DamageEffect());
        
        // Informuj AI
        if (enemyAI != null)
        {
            enemyAI.OnDamaged();
        }
        
        if (currentHealth <= 0)
        {
            Die();
        }
    }
    
    System.Collections.IEnumerator DamageEffect()
    {
        Renderer renderer = GetComponent<Renderer>();
        Color originalColor = renderer.material.color;
        
        renderer.material.color = Color.red;
        yield return new WaitForSeconds(0.1f);
        renderer.material.color = originalColor;
    }
    
    void Die()
    {
        // Efekt smrti
        if (deathEffect != null)
        {
            Instantiate(deathEffect, transform.position, Quaternion.identity);
        }
        
        // Zvuk smrti
        if (deathSound != null)
        {
            AudioSource.PlayClipAtPoint(deathSound, transform.position);
        }
        
        // Přidat skóre
        GameManager gm = FindObjectOfType<GameManager>();
        if (gm != null)
        {
            gm.PridejSkore(10);
        }
        
        Destroy(gameObject);
    }
}
```

#### 2. NavMesh a AI pohyb (15 minut)

**Nastavení NavMesh:**
1. Window → AI → Navigation
2. Označíme podlahu a stěny
3. V Navigation okně: Object tab → Navigation Static ✓
4. Přejdeme na Bake tab → Bake

**EnemyAI skript:**
```csharp
using UnityEngine;
using UnityEngine.AI;

public class EnemyAI : MonoBehaviour
{
    [Header("AI Nastavení")]
    public float detectionRange = 10f;
    public float attackRange = 2f;
    public float patrolRange = 5f;
    public float damage = 10f;
    public float attackCooldown = 2f;
    
    [Header("Patrol")]
    public Transform[] patrolPoints;
    
    private NavMeshAgent agent;
    private Transform player;
    private Vector3 startPosition;
    private float lastAttackTime;
    private int currentPatrolIndex;
    
    public enum AIState
    {
        Patrol,
        Chase,
        Attack,
        ReturnToPatrol
    }
    
    public AIState currentState = AIState.Patrol;
    
    void Start()
    {
        agent = GetComponent<NavMeshAgent>();
        player = GameObject.FindGameObjectWithTag("Player").transform;
        startPosition = transform.position;
        
        SetupPatrol();
    }
    
    void Update()
    {
        float distanceToPlayer = Vector3.Distance(transform.position, player.position);
        
        switch (currentState)
        {
            case AIState.Patrol:
                PatrolBehavior();
                if (distanceToPlayer <= detectionRange)
                {
                    currentState = AIState.Chase;
                }
                break;
                
            case AIState.Chase:
                ChaseBehavior();
                if (distanceToPlayer <= attackRange)
                {
                    currentState = AIState.Attack;
                }
                else if (distanceToPlayer > detectionRange * 1.5f)
                {
                    currentState = AIState.ReturnToPatrol;
                }
                break;
                
            case AIState.Attack:
                AttackBehavior();
                if (distanceToPlayer > attackRange)
                {
                    currentState = AIState.Chase;
                }
                break;
                
            case AIState.ReturnToPatrol:
                ReturnToPatrolBehavior();
                if (Vector3.Distance(transform.position, startPosition) < 2f)
                {
                    currentState = AIState.Patrol;
                }
                break;
        }
    }
    
    void PatrolBehavior()
    {
        if (patrolPoints.Length == 0) return;
        
        if (!agent.pathPending && agent.remainingDistance < 0.5f)
        {
            currentPatrolIndex = (currentPatrolIndex + 1) % patrolPoints.Length;
            agent.SetDestination(patrolPoints[currentPatrolIndex].position);
        }
    }
    
    void ChaseBehavior()
    {
        agent.SetDestination(player.position);
    }
    
    void AttackBehavior()
    {
        agent.SetDestination(transform.position); // Stop moving
        
        // Otočit se k hráči
        Vector3 direction = (player.position - transform.position).normalized;
        transform.rotation = Quaternion.LookRotation(direction);
        
        // Útok
        if (Time.time - lastAttackTime > attackCooldown)
        {
            AttackPlayer();
            lastAttackTime = Time.time;
        }
    }
    
    void ReturnToPatrolBehavior()
    {
        agent.SetDestination(startPosition);
    }
    
    void AttackPlayer()
    {
        Debug.Log("Nepřítel útočí!");
        
        // Damage hráče
        PlayerHealth playerHealth = player.GetComponent<PlayerHealth>();
        if (playerHealth != null)
        {
            playerHealth.TakeDamage(damage);
        }
    }
    
    public void OnDamaged()
    {
        // Když je poškozený, přejde do chase mode
        currentState = AIState.Chase;
    }
    
    void SetupPatrol()
    {
        if (patrolPoints.Length > 0)
        {
            agent.SetDestination(patrolPoints[0].position);
        }
    }
    
    void OnDrawGizmosSelected()
    {
        // Vizualizace ranges
        Gizmos.color = Color.yellow;
        Gizmos.DrawWireSphere(transform.position, detectionRange);
        
        Gizmos.color = Color.red;
        Gizmos.DrawWireSphere(transform.position, attackRange);
    }
}
```

#### 3. Zdraví hráče (10 minut)

**PlayerHealth skript:**
```csharp
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class PlayerHealth : MonoBehaviour
{
    [Header("Zdraví")]
    public float maxHealth = 100f;
    public float currentHealth;
    
    [Header("UI")]
    public Slider healthBar;
    public Image damageOverlay;
    
    [Header("Efekty")]
    public AudioClip hurtSound;
    
    private AudioSource audioSource;
    
    void Start()
    {
        currentHealth = maxHealth;
        audioSource = GetComponent<AudioSource>();
        UpdateHealthUI();
    }
    
    public void TakeDamage(float damage)
    {
        currentHealth -= damage;
        currentHealth = Mathf.Clamp(currentHealth, 0, maxHealth);
        
        // Zvuk poškození
        if (hurtSound != null)
        {
            audioSource.PlayOneShot(hurtSound);
        }
        
        // Vizuální efekt
        StartCoroutine(DamageEffect());
        
        UpdateHealthUI();
        
        if (currentHealth <= 0)
        {
            Die();
        }
    }
    
    System.Collections.IEnumerator DamageEffect()
    {
        if (damageOverlay != null)
        {
            damageOverlay.color = new Color(1, 0, 0, 0.3f);
            
            float fadeTime = 1f;
            float elapsed = 0f;
            
            while (elapsed < fadeTime)
            {
                elapsed += Time.deltaTime;
                float alpha = Mathf.Lerp(0.3f, 0, elapsed / fadeTime);
                damageOverlay.color = new Color(1, 0, 0, alpha);
                yield return null;
            }
            
            damageOverlay.color = new Color(1, 0, 0, 0);
        }
    }
    
    void UpdateHealthUI()
    {
        if (healthBar != null)
        {
            healthBar.value = currentHealth / maxHealth;
        }
    }
    
    void Die()
    {
        Debug.Log("Hráč zemřel!");
        Time.timeScale = 0f;
        // Můžeme zde přidat game over screen
        
        // Restart po 2 sekundách
        Invoke("RestartLevel", 2f);
    }
    
    void RestartLevel()
    {
        Time.timeScale = 1f;
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
}
```

#### 4. Testování AI (5 minut)

**Vytvoření test levelů:**
1. Postavíme několik nepřátel
2. Nastavíme patrol pointy
3. Testujeme detection range
4. Kontrolujeme NavMesh

### Úkol pro děti
Vytvořte level s 2-3 nepřáteli, kteří patrol různé oblasti. Vyzkoušejte útěk a souboj.

---

## Hodina 23: Dokončení FPS hry (45 minut)

### Cíle hodiny
- Přidat game objectives (úkoly)
- Implementovat kompletní UI
- Doladit gameplay a balance
- Připravit hru k prezentaci

### Průběh hodiny

#### 1. Game objectives (15 minut)

**GameManager pro FPS:**
```csharp
using UnityEngine;
using UnityEngine.UI;
using UnityEngine.SceneManagement;

public class FPSGameManager : MonoBehaviour
{
    [Header("Cíle hry")]
    public int neprateleKZniceni = 5;
    public int predmetyKSebrání = 3;
    
    [Header("UI")]
    public Text skoreText;
    public Text ammunitiaText;
    public Text objectiveText;
    public GameObject winPanel;
    public GameObject gameOverPanel;
    
    private int skore = 0;
    private int zniceniNepratele = 0;
    private int sebranePredmety = 0;
    
    void Start()
    {
        UpdateUI();
        
        if (winPanel) winPanel.SetActive(false);
        if (gameOverPanel) gameOverPanel.SetActive(false);
    }
    
    public void PridejSkore(int body)
    {
        skore += body;
        UpdateUI();
    }
    
    public void NepratelsKill()
    {
        zniceniNepratele++;
        PridejSkore(50);
        CheckWinCondition();
    }
    
    public void PredmetSebral()
    {
        sebranePredmety++;
        PridejSkore(25);
        CheckWinCondition();
    }
    
    void CheckWinCondition()
    {
        if (zniceniNepratele >= neprateleKZniceni && sebranePredmety >= predmetyKSebrání)
        {
            Victory();
        }
    }
    
    void Victory()
    {
        Debug.Log("Výhra!");
        if (winPanel)
        {
            winPanel.SetActive(true);
            Time.timeScale = 0f;
            Cursor.lockState = CursorLockMode.None;
        }
    }
    
    public void GameOver()
    {
        if (gameOverPanel)
        {
            gameOverPanel.SetActive(true);
            Time.timeScale = 0f;
            Cursor.lockState = CursorLockMode.None;
        }
    }
    
    void UpdateUI()
    {
        if (skoreText)
            skoreText.text = "Skóre: " + skore;
            
        if (objectiveText)
        {
            string obj = $"Nepřátelé: {zniceniNepratele}/{neprateleKZniceni}\n";
            obj += $"Předměty: {sebranePredmety}/{predmetyKSebrání}";
            objectiveText.text = obj;
        }
    }
    
    public void UpdateAmmoUI(int current, int max)
    {
        if (ammunitiaText)
            ammunitiaText.text = $"Munice: {current}/{max}";
    }
    
    public void RestartGame()
    {
        Time.timeScale = 1f;
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
    
    public void QuitGame()
    {
        Application.Quit();
    }
}
```

#### 2. Kompletní UI systém (15 minut)

**UI Layout:**
```
Canvas
├── HUD
│   ├── SkoreText (levý horní)
│   ├── AmmunitionText (pravý dolní)
│   ├── ObjectiveText (levý dolní)
│   ├── HealthBar (dolní střed)
│   └── Crosshair (střed)
├── WinPanel
│   ├── "Victory!" text
│   ├── RestartButton
│   └── QuitButton
└── GameOverPanel
    ├── "Game Over" text
    ├── RestartButton
    └── QuitButton
```

#### 3. Balance a doladění (10 minut)

**Testování a úpravy:**
- Rychlost pohybu hráče
- Poškození zbraní
- Zdraví nepřátel
- Detection range AI
- Množství munice

**Performance optimalizace:**
```csharp
// Do EnemyAI přidat:
void Update()
{
    // Update AI pouze každých pár frameů pro optimalizaci
    if (Time.frameCount % 5 != 0) return;
    
    // Zbytek AI kódu...
}
```

#### 4. Build a testování (5 minut)

**Finální build:**
1. File → Build Settings
2. Player Settings:
   - Company Name
   - Product Name
   - Version
3. Build hry
4. Testování na různých rozlišeních

### Prezentace
Každý žák prezentuje svou FPS hru:
- Ukáže gameplay
- Vysvětlí, co se naučil nejtěžšího
- Co by chtěl přidat v budoucnu

### Shrnutí bloku
**Čeho jsme dosáhli:**
- Funkční FPS controller
- Systém střelby s raycast
- Inteligentní AI nepřátele s NavMesh
- Kompletní UI a game management
- Dokončenou hru s jasným cílem

**Připravili jsme se na:**
- Pokročilé UI/UX design
- Level design principy
- Větší a složitější projekty
