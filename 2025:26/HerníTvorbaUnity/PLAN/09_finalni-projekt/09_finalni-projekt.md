# Blok 9: Závěrečný projekt (31–35)

## Přehled bloku
**Cíl:** Děti vytvoří vlastní kompletní hru od nápadu po finální produkt.
**Výstup:** Funkční, hratelná hra, kterou si děti mohou hrdost představit na finální prezentaci.

---

## Hodina 31: Výběr a plánování projektu (45 minut)

### Cíle hodiny
- Zvolit vhodný projekt na základě vlastních dovedností
- Vytvořit detailní plán vývoje
- Nastavi realistický scope

### Materiály
- Papír na plánování
- Příklady různých typů her
- Template pro game design document

### Průběh hodiny

#### 1. Brainstorming nápadů (10 minut)

**Typy projektů podle času:**

**Malé projekty (1-2 hodiny):**
- Vyhlepšení existujících projektů
- Mini-hry (Snake, Pong, Tetris)
- Jednoduché puzzle hry

**Střední projekty (3-4 hodiny):**
- Nová plošinovka s originální mechanikou
- Základní FPS s vlastním level designem
- Top-down adventura

**Velké projekty (5 hodin):**
- RPG s character developmentem
- Strategy hra
- Kompletní herní série

**Brainstorming otázky:**
- Jaký žánr mám nejradši?
- Co se mi povedlo nejlépe v předchozích projektech?
- Co nového bych se chtěl naučit?
- Jaký typ hry jsem ještě nezkusil?

#### 2. Scope Management (15 minut)

**"Scope Creep" - Nebezpečí rozrůstání:**
- Začneme s jednoduchou hrou
- Postupně přidáváme funkce
- Nakonec nic nedokončíme

**ProjectScopeManager:**
```csharp
using UnityEngine;
using System.Collections.Generic;

[System.Serializable]
public class ProjectScope
{
    [Header("Základní hra (MUST HAVE)")]
    public List<string> coreFeatures = new List<string>();
    
    [Header("Rozšíření (NICE TO HAVE)")]
    public List<string> additionalFeatures = new List<string>();
    
    [Header("Sené žádné (DREAM FEATURES)")]
    public List<string> dreamFeatures = new List<string>();
    
    [Header("Progress")]
    [Range(0, 100)] public int coreCompletion = 0;
    [Range(0, 100)] public int additionalCompletion = 0;
    [Range(0, 100)] public int dreamCompletion = 0;
}

public class ProjectScopeManager : MonoBehaviour
{
    public ProjectScope scope;
    
    [Header("Time Management")]
    public int totalHoursAvailable = 5;
    public int hoursSpentOnCore = 0;
    public int hoursSpentOnAdditional = 0;
    
    void Start()
    {
        Debug.Log("=== PROJECT SCOPE ===");
        Debug.Log($"Core Features ({scope.coreFeatures.Count}):");
        foreach (string feature in scope.coreFeatures)
        {
            Debug.Log($"- {feature}");
        }
    }
    
    public bool CanWorkOnAdditionalFeatures()
    {
        return scope.coreCompletion >= 80 && hoursSpentOnCore < totalHoursAvailable * 0.7f;
    }
    
    public bool CanWorkOnDreamFeatures()
    {
        return scope.coreCompletion >= 100 && scope.additionalCompletion >= 50;
    }
    
    [ContextMenu("Evaluate Scope")]
    public void EvaluateScope()
    {
        Debug.Log($"--- SCOPE EVALUATION ---");
        Debug.Log($"Core: {scope.coreCompletion}%");
        Debug.Log($"Additional: {scope.additionalCompletion}%");
        Debug.Log($"Dream: {scope.dreamCompletion}%");
        
        if (scope.coreCompletion < 80)
        {
            Debug.LogWarning("⚠️ Focus on core features!");
        }
        else if (CanWorkOnAdditionalFeatures())
        {
            Debug.Log("✓ Ready for additional features");
        }
        
        if (CanWorkOnDreamFeatures())
        {
            Debug.Log("✨ Dream features unlocked!");
        }
    }
}
```

#### 3. Game Design Document (15 minut)

**Mini GDD Template:**
```csharp
using UnityEngine;

[CreateAssetMenu(fileName = "New Game Design", menuName = "Game Design Document")]
public class GameDesignDocument : ScriptableObject
{
    [Header("Základní informace")]
    public string gameName;
    public string genre;
    [TextArea(3, 5)] public string gameDescription;
    
    [Header("Cílová skupina")]
    public string targetAudience;
    public int estimatedPlayTime; // v minutách
    
    [Header("Mechaniky")]
    [TextArea(2, 4)] public string coreGameplay;
    [TextArea(2, 4)] public string winCondition;
    [TextArea(2, 4)] public string loseCondition;
    
    [Header("Vizuální styl")]
    public string artStyle;
    public Color primaryColor = Color.blue;
    public Color secondaryColor = Color.white;
    public Color accentColor = Color.yellow;
    
    [Header("Audio")]
    public string musicStyle;
    public bool needsSoundEffects = true;
    public bool needsVoiceActing = false;
    
    [Header("Technical")]
    public bool is2D = true;
    public bool needsPhysics = true;
    public bool needsAI = false;
    public bool needsNetworking = false;
    
    [Header("Rozváhnutí")]
    [TextArea(3, 5)] public string technicalChallenges;
    [TextArea(3, 5)] public string uniqueSellingPoints;
    
    public void PrintGDD()
    {
        Debug.Log($"=== GAME DESIGN DOCUMENT ===\n" +
                 $"Name: {gameName}\n" +
                 $"Genre: {genre}\n" +
                 $"Description: {gameDescription}\n" +
                 $"Target: {targetAudience}\n" +
                 $"Play Time: {estimatedPlayTime} minutes\n" +
                 $"Core Gameplay: {coreGameplay}");
    }
}
```

#### 4. Project Planning (5 minut)

**Milestone struktura s Git workflow:**
1. **Prototyp** (1 hodina) - Základní mechaniky
   - Git: Branch "prototype", commit "Basic gameplay working"
2. **Greybox** (1 hodina) - Level layout 
   - Git: Branch "level-design", commit "Level layout complete"
3. **Art Pass** (1 hodina) - Vizuální styl
   - Git: Branch "art-integration", commit "Art assets integrated"
4. **Polish** (1 hodina) - Audio, UI, efekty
   - Git: Branch "polish", commit "Audio and UI complete"
5. **Testing** (1 hodina) - Bug fixing, balance
   - Git: Merge all branches, commit "Final version ready"

**Git Workflow pro finální projekt:**
```bash
# Vytvoření projektního repository
1. GitHub: New Repository "muj-finalni-projekt"
2. Clone do lokálního počítače
3. Zkopírovat Unity .gitignore
4. První commit: "Initial project setup"

# Práce s branches pro každý milestone
5. git checkout -b prototype
6. Pracovat na prototypu
7. git commit -m "Added basic player movement"
8. git checkout main && git merge prototype
9. Opakovat pro další milestones
```

### Úkol na domů
Vytvořte Game Design Document pro svůj projekt a přiněste příště.

---

## Hodina 32: Prototyp a základní mechaniky (45 minut)

### Cíle hodiny
- Implementovat core gameplay loop
- Vytvořit hratelnou verzi bez grafiky
- Testovat základní mechaniky

### Průběh hodiny

#### 1. Rapid Prototyping principy (5 minut)

**"Fail Fast" filosofie:**
- Rychle vytvořit základní verzi
- Rychle otestovat
- Pokud nefunguje, rychle změnit

**Prototyping pravidla:**
- Používej Unity primitives
- Žádné fancy grafiky
- Fokus na gameplay
- Měř čas strávený na každé feature

#### 2. Core Loop implementace (30 minut)

**Příklad - Tower Defense prototyp:**
```csharp
using UnityEngine;
using System.Collections.Generic;

public class TowerDefensePrototype : MonoBehaviour
{
    [Header("Game State")]
    public int playerHealth = 10;
    public int playerMoney = 100;
    public int currentWave = 1;
    
    [Header("Prefabs")]
    public GameObject enemyPrefab;
    public GameObject towerPrefab;
    
    [Header("Spawn Points")]
    public Transform[] enemySpawnPoints;
    public Transform enemyGoal;
    
    private List<GameObject> activeTowers = new List<GameObject>();
    private List<GameObject> activeEnemies = new List<GameObject>();
    
    void Start()
    {
        Debug.Log("Tower Defense Prototype Started!");
        StartWave();
    }
    
    void Update()
    {
        // Simple input for tower placement
        if (Input.GetMouseButtonDown(0))
        {
            PlaceTower();
        }
        
        // Check win/lose conditions
        if (playerHealth <= 0)
        {
            GameOver();
        }
        
        if (activeEnemies.Count == 0)
        {
            NextWave();
        }
    }
    
    void PlaceTower()
    {
        if (playerMoney < 50) return;
        
        Vector3 mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        mousePos.z = 0;
        
        GameObject tower = Instantiate(towerPrefab, mousePos, Quaternion.identity);
        activeTowers.Add(tower);
        playerMoney -= 50;
        
        Debug.Log($"Tower placed! Money: {playerMoney}");
    }
    
    void StartWave()
    {
        Debug.Log($"Wave {currentWave} starting!");
        
        for (int i = 0; i < currentWave + 2; i++)
        {
            Invoke("SpawnEnemy", i * 2f);
        }
    }
    
    void SpawnEnemy()
    {
        if (enemySpawnPoints.Length == 0) return;
        
        Transform spawnPoint = enemySpawnPoints[Random.Range(0, enemySpawnPoints.Length)];
        GameObject enemy = Instantiate(enemyPrefab, spawnPoint.position, Quaternion.identity);
        
        // Give enemy a simple AI to move toward goal
        SimpleEnemyAI ai = enemy.GetComponent<SimpleEnemyAI>();
        if (ai) ai.target = enemyGoal;
        
        activeEnemies.Add(enemy);
    }
    
    public void EnemyReachedGoal(GameObject enemy)
    {
        playerHealth--;
        activeEnemies.Remove(enemy);
        Destroy(enemy);
        
        Debug.Log($"Enemy reached goal! Health: {playerHealth}");
    }
    
    public void EnemyKilled(GameObject enemy)
    {
        playerMoney += 10;
        activeEnemies.Remove(enemy);
        Destroy(enemy);
        
        Debug.Log($"Enemy killed! Money: {playerMoney}");
    }
    
    void NextWave()
    {
        currentWave++;
        Invoke("StartWave", 3f);
    }
    
    void GameOver()
    {
        Debug.Log("Game Over!");
        Time.timeScale = 0f;
    }
}
```

**Jednoduchá AI pro testování:**
```csharp
using UnityEngine;

public class SimpleEnemyAI : MonoBehaviour
{
    public Transform target;
    public float speed = 2f;
    public int health = 3;
    
    private TowerDefensePrototype gameManager;
    
    void Start()
    {
        gameManager = FindObjectOfType<TowerDefensePrototype>();
    }
    
    void Update()
    {
        if (target)
        {
            // Move toward target
            Vector3 direction = (target.position - transform.position).normalized;
            transform.position += direction * speed * Time.deltaTime;
            
            // Check if reached goal
            if (Vector3.Distance(transform.position, target.position) < 0.5f)
            {
                if (gameManager)
                    gameManager.EnemyReachedGoal(gameObject);
            }
        }
    }
    
    public void TakeDamage(int damage)
    {
        health -= damage;
        
        if (health <= 0)
        {
            if (gameManager)
                gameManager.EnemyKilled(gameObject);
        }
    }
    
    void OnDrawGizmos()
    {
        if (target)
        {
            Gizmos.color = Color.red;
            Gizmos.DrawLine(transform.position, target.position);
        }
    }
}
```

#### 3. Rychlé testování (10 minut)

**Prototyp testovací otázky:**
- Je core loop zábavný?
- Jsou ovládácí prvky intuitivní?
- Je jasné, co je cílem?
- Funguje základní gameplay?

### Úkol + Git setup
Vytvořte hratelnou verzi svou hry s Unity primitivy. Fokus na mechaniky, ne na grafiku.

**Git setup pro finální projekt:**
1. Vytvořte nové GitHub repository s názvem vašeho projektu
2. Klonujte si jej lokálně
3. Zkopírujte Unity projekt do této složky
4. Přidejte Unity .gitignore
5. První commit: "Initial Unity project for [NÁZEV HRY]"
6. Vytvořte branch "prototype" pro experimentování
7. Každý den: commit s popisem pokroku
8. Jednou týdně: merge do main branch

---

## Hodina 33: Tvorba prostředí a art pass (45 minut)

### Cíle hodiny
- Převést greybox do vizuálně přívětivé podoby
- Vytvořit konzistentní art style
- Přidat základní osvětlení a atmosféru

### Průběh hodiny

#### 1. Art Direction (10 minut)

**Volba art stylu:**
- **Pixel Art** - nostalgický, jednoduchý
- **Low Poly** - moderní, čistý
- **Cartoon** - přítělský, barevný
- **Realistic** - náročný, detailí

**ColorPalette manager:**
```csharp
using UnityEngine;

[CreateAssetMenu(fileName = "New Color Palette", menuName = "Art/Color Palette")]
public class ColorPalette : ScriptableObject
{
    [Header("Primary Colors")]
    public Color backgroundColor = Color.blue;
    public Color primaryColor = Color.white;
    public Color secondaryColor = Color.gray;
    
    [Header("Accent Colors")]
    public Color accentColor = Color.yellow;
    public Color dangerColor = Color.red;
    public Color safeColor = Color.green;
    
    [Header("UI Colors")]
    public Color textColor = Color.black;
    public Color buttonColor = Color.white;
    public Color highlightColor = Color.cyan;
    
    public void ApplyToPrimitive(GameObject primitive, MaterialType type)
    {
        Renderer renderer = primitive.GetComponent<Renderer>();
        if (renderer)
        {
            Material mat = new Material(Shader.Find("Standard"));
            
            switch (type)
            {
                case MaterialType.Platform:
                    mat.color = primaryColor;
                    break;
                case MaterialType.Hazard:
                    mat.color = dangerColor;
                    break;
                case MaterialType.Collectible:
                    mat.color = accentColor;
                    break;
                case MaterialType.Background:
                    mat.color = backgroundColor;
                    break;
            }
            
            renderer.material = mat;
        }
    }
}

public enum MaterialType
{
    Platform,
    Hazard,
    Collectible,
    Background
}
```

#### 2. Asset Creation/Import (15 minut)

**Kde získat assety:**
- Unity Asset Store (zdarma sekce)
- OpenGameArt.org
- Kenney.nl (velné assety)
- Vytvoit vlastní (Krita, Piskel)

**AssetReplacer tool:**
```csharp
using UnityEngine;

#if UNITY_EDITOR
using UnityEditor;
#endif

public class AssetReplacer : MonoBehaviour
{
    [Header("Asset Mapping")]
    public GameObject cubePlatform;
    public GameObject sphereCollectible;
    public GameObject capsuleEnemy;
    
    [Header("Replacement Assets")]
    public GameObject newPlatformAsset;
    public GameObject newCollectibleAsset;
    public GameObject newEnemyAsset;
    
    #if UNITY_EDITOR
    [ContextMenu("Replace All Assets")]
    public void ReplaceAllAssets()
    {
        // Replace all cube platforms
        GameObject[] cubes = FindObjectsWithName("Cube");
        foreach (GameObject cube in cubes)
        {
            if (cube.CompareTag("Platform") && newPlatformAsset)
            {
                ReplaceGameObject(cube, newPlatformAsset);
            }
        }
        
        // Replace all sphere collectibles
        GameObject[] spheres = FindObjectsWithName("Sphere");
        foreach (GameObject sphere in spheres)
        {
            if (sphere.CompareTag("Collectible") && newCollectibleAsset)
            {
                ReplaceGameObject(sphere, newCollectibleAsset);
            }
        }
        
        Debug.Log("Asset replacement completed!");
    }
    
    GameObject[] FindObjectsWithName(string name)
    {
        GameObject[] allObjects = FindObjectsOfType<GameObject>();
        System.Collections.Generic.List<GameObject> matching = new System.Collections.Generic.List<GameObject>();
        
        foreach (GameObject obj in allObjects)
        {
            if (obj.name.Contains(name))
            {
                matching.Add(obj);
            }
        }
        
        return matching.ToArray();
    }
    
    void ReplaceGameObject(GameObject oldObject, GameObject newPrefab)
    {
        Vector3 position = oldObject.transform.position;
        Quaternion rotation = oldObject.transform.rotation;
        Vector3 scale = oldObject.transform.localScale;
        Transform parent = oldObject.transform.parent;
        string objectName = oldObject.name;
        string tag = oldObject.tag;
        
        DestroyImmediate(oldObject);
        
        GameObject newObject = PrefabUtility.InstantiatePrefab(newPrefab) as GameObject;
        newObject.transform.position = position;
        newObject.transform.rotation = rotation;
        newObject.transform.localScale = scale;
        newObject.transform.parent = parent;
        newObject.name = objectName;
        newObject.tag = tag;
    }
    #endif
}
```

#### 3. Lighting a atmosféra (15 minut)

**Základní lighting setup:**
```csharp
using UnityEngine;

public class LightingManager : MonoBehaviour
{
    [Header("Lighting Presets")]
    public LightingPreset[] presets;
    
    [Header("Current Settings")]
    [Range(0, 1)] public float timeOfDay = 0.5f;
    public bool dynamicLighting = false;
    
    private Light directionalLight;
    
    void Start()
    {
        directionalLight = FindObjectOfType<Light>();
        if (directionalLight && directionalLight.type != LightType.Directional)
        {
            directionalLight = null;
        }
    }
    
    void Update()
    {
        if (dynamicLighting)
        {
            timeOfDay += Time.deltaTime * 0.1f;
            if (timeOfDay > 1) timeOfDay = 0;
        }
        
        ApplyLighting();
    }
    
    void ApplyLighting()
    {
        if (presets.Length == 0) return;
        
        // Simple interpolation between presets
        int index = Mathf.FloorToInt(timeOfDay * presets.Length);
        int nextIndex = (index + 1) % presets.Length;
        
        float t = (timeOfDay * presets.Length) - index;
        
        LightingPreset current = presets[index];
        LightingPreset next = presets[nextIndex];
        
        // Apply to directional light
        if (directionalLight)
        {
            directionalLight.color = Color.Lerp(current.lightColor, next.lightColor, t);
            directionalLight.intensity = Mathf.Lerp(current.lightIntensity, next.lightIntensity, t);
        }
        
        // Apply to camera background
        Camera.main.backgroundColor = Color.Lerp(current.backgroundColor, next.backgroundColor, t);
        
        // Apply fog
        RenderSettings.fog = current.useFog || next.useFog;
        if (RenderSettings.fog)
        {
            RenderSettings.fogColor = Color.Lerp(current.fogColor, next.fogColor, t);
        }
    }
}

[System.Serializable]
public class LightingPreset
{
    public string name;
    public Color lightColor = Color.white;
    public float lightIntensity = 1f;
    public Color backgroundColor = Color.blue;
    public bool useFog = false;
    public Color fogColor = Color.gray;
}
```

#### 4. Visual effects (5 minut)

**Jednoduché post-processing:**
- Window → Package Manager
- Install "Post Processing"
- Přidat Post Process Volume
- Vytvořit Post Process Profile
- Experimentovat s Color Grading, Bloom, Vignette

### Úkol
Nahraiťte greybox assety krásnými a přidejte atmosféru své hře.

---

## Hodina 34: Audio, UI a polish (45 minut)

### Cíle hodiny
- Přidat kompletní audio design
- Doladit UI na profesionální úroveň
- Přidat "juice" - malé detaily, které hra u zdá kvalitní

### Průběh hodiny

#### 1. Kompletní audio integration (15 minut)

**AudioManager system:**
```csharp
using UnityEngine;
using System.Collections;
using System.Collections.Generic;

public class AudioManager : MonoBehaviour
{
    [Header("Audio Sources")]
    public AudioSource musicSource;
    public AudioSource sfxSource;
    public AudioSource ambientSource;
    
    [Header("Audio Clips")]
    public AudioClip[] musicTracks;
    public AudioClip[] soundEffects;
    public AudioClip[] ambientSounds;
    
    [Header("Settings")]
    [Range(0, 1)] public float masterVolume = 1f;
    [Range(0, 1)] public float musicVolume = 0.7f;
    [Range(0, 1)] public float sfxVolume = 1f;
    [Range(0, 1)] public float ambientVolume = 0.5f;
    
    public static AudioManager Instance { get; private set; }
    
    private Dictionary<string, AudioClip> audioDict = new Dictionary<string, AudioClip>();
    
    void Awake()
    {
        // Singleton pattern
        if (Instance == null)
        {
            Instance = this;
            DontDestroyOnLoad(gameObject);
            
            SetupAudioDictionary();
        }
        else
        {
            Destroy(gameObject);
        }
    }
    
    void SetupAudioDictionary()
    {
        // Index all audio clips by name
        foreach (AudioClip clip in soundEffects)
        {
            if (clip) audioDict[clip.name] = clip;
        }
        
        foreach (AudioClip clip in musicTracks)
        {
            if (clip) audioDict[clip.name] = clip;
        }
    }
    
    public void PlaySFX(string clipName)
    {
        if (audioDict.ContainsKey(clipName))
        {
            sfxSource.PlayOneShot(audioDict[clipName], sfxVolume * masterVolume);
        }
        else
        {
            Debug.LogWarning($"Audio clip '{clipName}' not found!");
        }
    }
    
    public void PlayMusic(string trackName, bool loop = true)
    {
        if (audioDict.ContainsKey(trackName))
        {
            musicSource.clip = audioDict[trackName];
            musicSource.loop = loop;
            musicSource.volume = musicVolume * masterVolume;
            musicSource.Play();
        }
    }
    
    public void PlayAmbient(string ambientName)
    {
        if (audioDict.ContainsKey(ambientName))
        {
            ambientSource.clip = audioDict[ambientName];
            ambientSource.loop = true;
            ambientSource.volume = ambientVolume * masterVolume;
            ambientSource.Play();
        }
    }
    
    public void SetMasterVolume(float volume)
    {
        masterVolume = volume;
        UpdateAllVolumes();
    }
    
    void UpdateAllVolumes()
    {
        musicSource.volume = musicVolume * masterVolume;
        // SFX volume is applied per-clip
        ambientSource.volume = ambientVolume * masterVolume;
    }
    
    // Easy access methods for common sounds
    public void PlayJump() { PlaySFX("Jump"); }
    public void PlayCoin() { PlaySFX("Coin"); }
    public void PlayHit() { PlaySFX("Hit"); }
    public void PlayDeath() { PlaySFX("Death"); }
    public void PlayVictory() { PlaySFX("Victory"); }
}
```

#### 2. UI Polish (15 minut)

**Advanced UI animations:**
```csharp
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class UIAnimator : MonoBehaviour
{
    [Header("Animation Settings")]
    public float animationSpeed = 1f;
    public AnimationCurve scaleCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);
    public AnimationCurve fadeCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);
    
    private RectTransform rectTransform;
    private CanvasGroup canvasGroup;
    private Vector3 originalScale;
    private float originalAlpha;
    
    void Start()
    {
        rectTransform = GetComponent<RectTransform>();
        canvasGroup = GetComponent<CanvasGroup>();
        
        if (!canvasGroup)
            canvasGroup = gameObject.AddComponent<CanvasGroup>();
            
        originalScale = rectTransform.localScale;
        originalAlpha = canvasGroup.alpha;
    }
    
    [ContextMenu("Animate In")]
    public void AnimateIn()
    {
        StartCoroutine(AnimateInCoroutine());
    }
    
    [ContextMenu("Animate Out")]
    public void AnimateOut()
    {
        StartCoroutine(AnimateOutCoroutine());
    }
    
    IEnumerator AnimateInCoroutine()
    {
        // Start from small and transparent
        rectTransform.localScale = Vector3.zero;
        canvasGroup.alpha = 0f;
        
        float elapsed = 0f;
        float duration = 1f / animationSpeed;
        
        while (elapsed < duration)
        {
            elapsed += Time.unscaledDeltaTime;
            float progress = elapsed / duration;
            
            // Scale animation
            float scaleValue = scaleCurve.Evaluate(progress);
            rectTransform.localScale = Vector3.Lerp(Vector3.zero, originalScale, scaleValue);
            
            // Fade animation
            float fadeValue = fadeCurve.Evaluate(progress);
            canvasGroup.alpha = Mathf.Lerp(0f, originalAlpha, fadeValue);
            
            yield return null;
        }
        
        // Ensure final values
        rectTransform.localScale = originalScale;
        canvasGroup.alpha = originalAlpha;
    }
    
    IEnumerator AnimateOutCoroutine()
    {
        float elapsed = 0f;
        float duration = 1f / animationSpeed;
        
        Vector3 startScale = rectTransform.localScale;
        float startAlpha = canvasGroup.alpha;
        
        while (elapsed < duration)
        {
            elapsed += Time.unscaledDeltaTime;
            float progress = elapsed / duration;
            
            // Reverse animations
            float scaleValue = scaleCurve.Evaluate(1f - progress);
            rectTransform.localScale = Vector3.Lerp(Vector3.zero, startScale, scaleValue);
            
            float fadeValue = fadeCurve.Evaluate(1f - progress);
            canvasGroup.alpha = Mathf.Lerp(0f, startAlpha, fadeValue);
            
            yield return null;
        }
        
        // Hide completely
        gameObject.SetActive(false);
    }
    
    public void PulseEffect()
    {
        StartCoroutine(PulseCoroutine());
    }
    
    IEnumerator PulseCoroutine()
    {
        Vector3 targetScale = originalScale * 1.2f;
        
        // Scale up
        yield return StartCoroutine(ScaleTo(targetScale, 0.1f));
        // Scale back
        yield return StartCoroutine(ScaleTo(originalScale, 0.1f));
    }
    
    IEnumerator ScaleTo(Vector3 target, float duration)
    {
        Vector3 startScale = rectTransform.localScale;
        float elapsed = 0f;
        
        while (elapsed < duration)
        {
            elapsed += Time.unscaledDeltaTime;
            float progress = elapsed / duration;
            
            rectTransform.localScale = Vector3.Lerp(startScale, target, progress);
            yield return null;
        }
        
        rectTransform.localScale = target;
    }
}
```

#### 3. Game "Juice" (10 minut)

**JuiceManager - makes everything feel better:**
```csharp
using UnityEngine;
using System.Collections;

public class JuiceManager : MonoBehaviour
{
    [Header("Screen Shake")]
    public float shakeIntensity = 0.1f;
    public float shakeDuration = 0.2f;
    
    [Header("Time Effects")]
    public float slowMotionScale = 0.3f;
    public float slowMotionDuration = 0.5f;
    
    private Camera mainCamera;
    private Vector3 originalCameraPosition;
    
    public static JuiceManager Instance { get; private set; }
    
    void Awake()
    {
        if (Instance == null)
        {
            Instance = this;
            mainCamera = Camera.main;
            if (mainCamera)
                originalCameraPosition = mainCamera.transform.position;
        }
        else
        {
            Destroy(gameObject);
        }
    }
    
    public void ScreenShake(float intensity = -1, float duration = -1)
    {
        if (intensity < 0) intensity = shakeIntensity;
        if (duration < 0) duration = shakeDuration;
        
        StartCoroutine(ScreenShakeCoroutine(intensity, duration));
    }
    
    IEnumerator ScreenShakeCoroutine(float intensity, float duration)
    {
        float elapsed = 0f;
        
        while (elapsed < duration)
        {
            elapsed += Time.unscaledDeltaTime;
            
            float strength = intensity * (1f - elapsed / duration);
            
            Vector3 randomOffset = Random.insideUnitSphere * strength;
            randomOffset.z = 0; // Keep camera at same Z depth
            
            mainCamera.transform.position = originalCameraPosition + randomOffset;
            
            yield return null;
        }
        
        mainCamera.transform.position = originalCameraPosition;
    }
    
    public void SlowMotion()
    {
        StartCoroutine(SlowMotionCoroutine());
    }
    
    IEnumerator SlowMotionCoroutine()
    {
        Time.timeScale = slowMotionScale;
        yield return new WaitForSecondsRealtime(slowMotionDuration);
        Time.timeScale = 1f;
    }
    
    public void HitStop(float duration = 0.1f)
    {
        StartCoroutine(HitStopCoroutine(duration));
    }
    
    IEnumerator HitStopCoroutine(float duration)
    {
        Time.timeScale = 0f;
        yield return new WaitForSecondsRealtime(duration);
        Time.timeScale = 1f;
    }
    
    // Easy access methods
    public void OnPlayerHit() 
    { 
        ScreenShake(0.2f, 0.3f); 
        HitStop(0.05f);
        AudioManager.Instance?.PlayHit();
    }
    
    public void OnEnemyKilled() 
    { 
        SlowMotion(); 
        ScreenShake(0.15f, 0.2f);
        AudioManager.Instance?.PlaySFX("EnemyDeath");
    }
    
    public void OnLevelComplete() 
    { 
        AudioManager.Instance?.PlayVictory();
        // Maybe some confetti particles?
    }
}
```

#### 4. Final touches (5 minut)

**Build Settings optimization:**
- Player Settings → Optimize for size
- Texture compression
- Audio compression
- Remove unused assets

### Úkol
Přidejte audio, vylepšete UI a přidejte alespoň 3 "juice" efekty do své hry.

---

## Hodina 35: Testování, bug fixing a finaliza
(45 minut)

### Cíle hodiny
- Provést kompletní testování hry
- Opravit nejkritickjší bugs
- Připravit hru na prezentaci

### Průběh hodiny

#### 1. Systematic testing (15 minut)

**Bug Testing Checklist:**
```csharp
using UnityEngine;
using System.Collections.Generic;

[System.Serializable]
public class BugReport
{
    public string title;
    public BugSeverity severity;
    public string description;
    public string stepsToReproduce;
    public bool isFixed = false;
}

public enum BugSeverity
{
    Critical,    // Game crashes, unplayable
    High,        // Major features broken
    Medium,      // Minor features broken
    Low,         // Cosmetic issues
    Enhancement  // Nice to have
}

public class BugTracker : MonoBehaviour
{
    [Header("Bug Reports")]
    public List<BugReport> bugs = new List<BugReport>();
    
    [Header("Statistics")]
    public int criticalBugs = 0;
    public int highPriorityBugs = 0;
    public int totalBugs = 0;
    public int fixedBugs = 0;
    
    void Start()
    {
        RefreshStatistics();
    }
    
    public void AddBug(string title, BugSeverity severity, string description, string steps)
    {
        BugReport newBug = new BugReport
        {
            title = title,
            severity = severity,
            description = description,
            stepsToReproduce = steps
        };
        
        bugs.Add(newBug);
        RefreshStatistics();
        
        Debug.Log($"New {severity} bug reported: {title}");
    }
    
    public void MarkAsFixed(int bugIndex)
    {
        if (bugIndex < bugs.Count)
        {
            bugs[bugIndex].isFixed = true;
            RefreshStatistics();
            Debug.Log($"Bug fixed: {bugs[bugIndex].title}");
        }
    }
    
    void RefreshStatistics()
    {
        criticalBugs = 0;
        highPriorityBugs = 0;
        totalBugs = bugs.Count;
        fixedBugs = 0;
        
        foreach (BugReport bug in bugs)
        {
            if (bug.isFixed)
                fixedBugs++;
            else
            {
                if (bug.severity == BugSeverity.Critical)
                    criticalBugs++;
                else if (bug.severity == BugSeverity.High)
                    highPriorityBugs++;
            }
        }
    }
    
    public bool IsReadyForRelease()
    {
        return criticalBugs == 0 && highPriorityBugs <= 1;
    }
    
    [ContextMenu("Print Bug Report")]
    public void PrintBugReport()
    {
        Debug.Log("=== BUG REPORT ===");
        Debug.Log($"Total Bugs: {totalBugs}");
        Debug.Log($"Fixed: {fixedBugs}");
        Debug.Log($"Critical: {criticalBugs}");
        Debug.Log($"High Priority: {highPriorityBugs}");
        Debug.Log($"Ready for Release: {(IsReadyForRelease() ? "YES" : "NO")}");
    }
}
```

#### 2. Performance optimization (15 minut)

**PerformanceProfiler:**
```csharp
using UnityEngine;
using UnityEngine.Profiling;

public class PerformanceProfiler : MonoBehaviour
{
    [Header("Performance Metrics")]
    public float currentFPS;
    public long usedMemoryMB;
    public int drawCalls;
    public int triangles;
    
    [Header("Thresholds")]
    public float minAcceptableFPS = 30f;
    public long maxMemoryMB = 512;
    
    private float fpsTimer;
    private int frameCount;
    
    void Update()
    {
        MeasureFPS();
        MeasureMemory();
        MeasureRendering();
        
        CheckPerformanceThresholds();
    }
    
    void MeasureFPS()
    {
        fpsTimer += Time.unscaledDeltaTime;
        frameCount++;
        
        if (fpsTimer >= 1f)
        {
            currentFPS = frameCount / fpsTimer;
            fpsTimer = 0f;
            frameCount = 0;
        }
    }
    
    void MeasureMemory()
    {
        usedMemoryMB = Profiler.GetTotalAllocatedMemory(false) / (1024 * 1024);
    }
    
    void MeasureRendering()
    {
        drawCalls = UnityEngine.Rendering.DebugUI.GetDrawCallCount();
        triangles = UnityEngine.Rendering.DebugUI.GetTriangleCount();
    }
    
    void CheckPerformanceThresholds()
    {
        if (currentFPS < minAcceptableFPS)
        {
            Debug.LogWarning($"⚠️ Low FPS: {currentFPS:F1} (target: {minAcceptableFPS})");
        }
        
        if (usedMemoryMB > maxMemoryMB)
        {
            Debug.LogWarning($"⚠️ High memory usage: {usedMemoryMB}MB (limit: {maxMemoryMB}MB)");
        }
    }
    
    void OnGUI()
    {
        GUILayout.BeginVertical("box");
        GUILayout.Label($"FPS: {currentFPS:F1}");
        GUILayout.Label($"Memory: {usedMemoryMB}MB");
        GUILayout.Label($"Draw Calls: {drawCalls}");
        GUILayout.Label($"Triangles: {triangles}");
        GUILayout.EndVertical();
    }
}
```

#### 3. Final build a export (10 minut)

**BuildManager for final release:**
```csharp
using UnityEngine;
#if UNITY_EDITOR
using UnityEditor;
using UnityEditor.Build.Reporting;
#endif

public class BuildManager : MonoBehaviour
{
    [Header("Build Settings")]
    public string gameName = "MyAwesomeGame";
    public string version = "1.0";
    public bool developmentBuild = false;
    
    #if UNITY_EDITOR
    [ContextMenu("Build Game")]
    public void BuildGame()
    {
        string buildPath = $"Builds/{gameName}_v{version}";
        
        BuildPlayerOptions buildOptions = new BuildPlayerOptions
        {
            scenes = GetEnabledScenes(),
            locationPathName = buildPath,
            target = EditorUserBuildSettings.activeBuildTarget,
            options = developmentBuild ? BuildOptions.Development : BuildOptions.None
        };
        
        Debug.Log($"Building {gameName} v{version}...");
        
        BuildReport report = BuildPipeline.BuildPlayer(buildOptions);
        
        if (report.summary.result == BuildResult.Succeeded)
        {
            Debug.Log($"Build completed: {report.summary.totalSize} bytes");
            EditorUtility.RevealInFinder(buildPath);
        }
        else
        {
            Debug.LogError($"Build failed: {report.summary.result}");
        }
    }
    
    string[] GetEnabledScenes()
    {
        System.Collections.Generic.List<string> scenes = new System.Collections.Generic.List<string>();
        
        foreach (EditorBuildSettingsScene scene in EditorBuildSettings.scenes)
        {
            if (scene.enabled)
                scenes.Add(scene.path);
        }
        
        return scenes.ToArray();
    }
    
    [ContextMenu("Prepare for Build")]
    public void PrepareForBuild()
    {
        // Remove debug components
        BugTracker bugTracker = FindObjectOfType<BugTracker>();
        if (bugTracker) DestroyImmediate(bugTracker.gameObject);
        
        PerformanceProfiler profiler = FindObjectOfType<PerformanceProfiler>();
        if (profiler) DestroyImmediate(profiler.gameObject);
        
        Debug.Log("Game prepared for final build");
    }
    #endif
}
```

#### 4. Presentation příprava (5 minut)

**PresentationHelper:**
```csharp
using UnityEngine;

public class PresentationHelper : MonoBehaviour
{
    [Header("Demo Settings")]
    public bool skipIntros = true;
    public bool unlockAllLevels = true;
    public bool godMode = false;
    public float demoTimeLimit = 300f; // 5 minutes
    
    private float demoStartTime;
    
    void Start()
    {
        demoStartTime = Time.time;
        
        if (skipIntros)
        {
            // Skip any intro sequences
            Debug.Log("Demo mode: Skipping intros");
        }
        
        if (unlockAllLevels)
        {
            PlayerPrefs.SetInt("AllLevelsUnlocked", 1);
            Debug.Log("Demo mode: All levels unlocked");
        }
    }
    
    void Update()
    {
        // Demo time limit
        if (Time.time - demoStartTime > demoTimeLimit)
        {
            Debug.Log("Demo time limit reached");
            ShowThankYou();
        }
        
        // Quick reset for demos
        if (Input.GetKeyDown(KeyCode.R) && Input.GetKey(KeyCode.LeftControl))
        {
            RestartDemo();
        }
    }
    
    void ShowThankYou()
    {
        // Show thank you screen or return to menu
        Debug.Log("Thank you for watching our game demo!");
    }
    
    public void RestartDemo()
    {
        demoStartTime = Time.time;
        UnityEngine.SceneManagement.SceneManager.LoadScene(0);
    }
}
```

### Shrnutí bloku
**Čeho jsme dosáhli:**
- Kompletní vlastní hru od nápadu po finální produkt
- Systematický přístup k vývoji (GDD, prototyp, iterace)
- Profesionální workflow pro asset management
- Testovací a debugging dovednosti
- Připravenou prezentaci

**Připravili jsme se na:**
- Finální prezentaci svaého díla
- Oslavu úspěšného dokončení kurzu
- Možné pokračování v samostatném vývoji
