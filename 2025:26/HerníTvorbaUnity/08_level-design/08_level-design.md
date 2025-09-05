# Blok 8: Level design (27–30)

## Přehled bloku
**Cíl:** Naučit děti principy navrhování herních levelů a vytváření zajimavých herních zážitků.
**Výstup:** Kompletní level s promysleným designem, vyvvaženou obtizností a testováním.

---

## Hodina 27: Principy level designu (45 minut)

### Cíle hodiny
- Pochopit, co dělá level dobrým
- Naučit se základní principy level designu
- Analyzovat existující hry a jejich levely

### Materiály
- Ukázky levelů z různých her
- Papír na náčrty
- Barevné tužky

### Průběh hodiny

#### 1. Co je level design? (10 minut)

**Definice Level Designu:**
Level design je umění vytváření herních prostředí, které :
- Vypráví příběh
- Učí hráče nové mechaniky
- Poskytují vhodnou výzvu
- Jsou zábavné a pamětihodné

**Příklady velkých levelů:**
- **World 1-1 Super Mario Bros** - učí vše potřebné
- **The First Temple Zelda BOTW** - učí základní mechaniky
- **Portal Test Chamber 1** - postupně učí portal mechaniku

#### 2. Základní principy (15 minut)

**1. "Show, Don't Tell" - Ukaž, neřík**
```
Špatné: Text "Press Space to jump"
Dobré: Malá propast, která "nucí" hráče skočit
```

**2. Pacing - Rytmus**
- **Action:** Intenzivní souboje, rychlé sekvence
- **Rest:** Klidné chvíle, exploration
- **Crescendo:** Gradace k boss fightovi

**3. Readability - čitelnost**
```csharp
// Příklad: Vizuální rozdělení elementů
public class LevelElement : MonoBehaviour
{
    public enum ElementType
    {
        Platform,    // Hnědá - bezpečné
        Hazard,      // Červená - nebezpečné
        Collectible, // Žlutá - sbíratelné
        Interactive  // Zelená - interaktivní
    }
    
    public ElementType type;
    
    void Start()
    {
        // Nastav barvu podle typu
        Renderer rend = GetComponent<Renderer>();
        switch(type)
        {
            case ElementType.Platform:
                rend.material.color = new Color(0.6f, 0.4f, 0.2f); // Hnědá
                break;
            case ElementType.Hazard:
                rend.material.color = Color.red;
                break;
            case ElementType.Collectible:
                rend.material.color = Color.yellow;
                break;
            case ElementType.Interactive:
                rend.material.color = Color.green;
                break;
        }
    }
}
```

**4. Player Agency - Hráčova volba**
- Více cest k cíli
- Volba obtížnosti
- Skryté oblasti k prozkoumání

#### 3. Typy level designu (15 minut)

**Lineární (Linear):**
- Jeden jasný směr
- Kontrolovaný zážitek
- Dobré pro tutoriály
- Příklad: Crash Bandicoot

**Otevřený (Open):**
- Více možností
- Exploration
- Hráč si volí tempo
- Příklad: Minecraft

**Hub World:**
- Hlavní oblast s více pod-levely
- Progres odemyká nové oblasti
- Příklad: Super Mario 64

**Metroidvania:**
- Propojené oblasti
- Nové schopnosti odemykají staré místa
- Příklad: Hollow Knight

#### 4. Náčrty a plánování (5 minut)

**Postup navrhování levelu:**
1. **Cíl levelu** - Co se hráč naučí?
2. **Hrubý náčrt** - Základní layout
3. **Mechaniky** - Co hráč bude dělat?
4. **Pacing** - Kdy bude akce, kdy klid?
5. **Testování** - Funguje to?

### Úkol pro děti
Nakreslěte náčrt levelu pro svou hru. Označte start, cíl, překážky a zajimavá místa.

---

## Hodina 28: Stavba levelů (45 minut)

### Cíle hodiny
- Převést náčrty do Unity
- Naučit se efektivní workflow pro level building
- Použít prefaby a modularitu

### Průběh hodiny

#### 1. Příprava Assetů (10 minut)

**Modularita - sestavitelné kousky:**
```
LevelAssets/
├── Platforms/
│   ├── Platform_1x1.prefab
│   ├── Platform_2x1.prefab
│   └── Platform_Corner.prefab
├── Hazards/
│   ├── Spikes.prefab
│   └── MovingPlatform.prefab
└── Collectibles/
    ├── Coin.prefab
    └── PowerUp.prefab
```

**LevelBuilder helper skript:**
```csharp
using UnityEngine;
using System.Collections.Generic;

#if UNITY_EDITOR
using UnityEditor;
#endif

public class LevelBuilder : MonoBehaviour
{
    [Header("Building Tools")]
    public GameObject[] platformPrefabs;
    public GameObject[] hazardPrefabs;
    public GameObject[] collectiblePrefabs;
    
    [Header("Snap Settings")]
    public float gridSize = 1f;
    public bool snapToGrid = true;
    
    #if UNITY_EDITOR
    [Header("Quick Build (Editor Only)")]
    public KeyCode buildKey = KeyCode.B;
    
    void Update()
    {
        if (!Application.isPlaying && Input.GetKeyDown(buildKey))
        {
            QuickPlace();
        }
    }
    
    void QuickPlace()
    {
        Vector3 mousePos = Camera.main.ScreenToWorldPoint(Input.mousePosition);
        mousePos.z = 0;
        
        if (snapToGrid)
        {
            mousePos.x = Mathf.Round(mousePos.x / gridSize) * gridSize;
            mousePos.y = Mathf.Round(mousePos.y / gridSize) * gridSize;
        }
        
        // Postav posledně vybraný prefab
        if (platformPrefabs.Length > 0)
        {
            GameObject newPlatform = PrefabUtility.InstantiatePrefab(platformPrefabs[0]) as GameObject;
            newPlatform.transform.position = mousePos;
            newPlatform.transform.parent = transform;
        }
    }
    #endif
    
    [ContextMenu("Organize Level")]
    public void OrganizeLevel()
    {
        // Automaticky zorganizuj objekty do složek
        OrganizeByType("Platform", "Platforms");
        OrganizeByType("Hazard", "Hazards");
        OrganizeByType("Collectible", "Collectibles");
    }
    
    void OrganizeByType(string tag, string folderName)
    {
        GameObject folder = GameObject.Find(folderName);
        if (folder == null)
        {
            folder = new GameObject(folderName);
            folder.transform.parent = transform;
        }
        
        GameObject[] objects = GameObject.FindGameObjectsWithTag(tag);
        foreach (GameObject obj in objects)
        {
            if (obj.transform.parent != folder.transform)
            {
                obj.transform.parent = folder.transform;
            }
        }
    }
}
```

#### 2. Greyboxing - hrubá verze (15 minut)

**Co je greyboxing:**
- Rychlá verze levelu z jednoduchých tvarů
- Testování mechanik před detailním designem
- "Kostry" místo krsaýných assetů

**Greybox workflow:**
1. Unity cubes pro základní platformy
2. Správné rozměry a colliders
3. Základní testování
4. Až když funguje - krasné assety

**GreyboxPlacer skript:**
```csharp
using UnityEngine;

public class GreyboxPlacer : MonoBehaviour
{
    [Header("Greybox Materials")]
    public Material platformMaterial;
    public Material hazardMaterial;
    public Material goalMaterial;
    
    public void CreatePlatform(Vector3 position, Vector3 size)
    {
        GameObject platform = GameObject.CreatePrimitive(PrimitiveType.Cube);
        platform.transform.position = position;
        platform.transform.localScale = size;
        platform.name = "GreyboxPlatform";
        platform.tag = "Platform";
        
        if (platformMaterial)
            platform.GetComponent<Renderer>().material = platformMaterial;
            
        platform.transform.parent = transform;
    }
    
    public void CreateHazard(Vector3 position)
    {
        GameObject hazard = GameObject.CreatePrimitive(PrimitiveType.Cube);
        hazard.transform.position = position;
        hazard.transform.localScale = new Vector3(1, 0.5f, 1);
        hazard.name = "GreyboxHazard";
        hazard.tag = "Hazard";
        
        if (hazardMaterial)
            hazard.GetComponent<Renderer>().material = hazardMaterial;
            
        // Přidej hazard komponentu
        hazard.AddComponent<Hazard>();
        hazard.transform.parent = transform;
    }
    
    [ContextMenu("Build from Sketch")]
    public void BuildFromSketch()
    {
        // Tady by mohl být kód na načtení z obrázku nebo dat
        Debug.Log("Building level from sketch...");
        
        // Příklad: jednoduchý level
        CreatePlatform(new Vector3(0, 0, 0), new Vector3(10, 1, 1));
        CreatePlatform(new Vector3(5, 2, 0), new Vector3(3, 1, 1));
        CreateHazard(new Vector3(2, 0.75f, 0));
    }
}
```

#### 3. Level Scripting (15 minut)

**Interaktivní prvky:**
```csharp
using UnityEngine;

public class MovingPlatform : MonoBehaviour
{
    [Header("Movement")]
    public Transform pointA;
    public Transform pointB;
    public float speed = 2f;
    public AnimationCurve movementCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);
    
    private float journey = 0f;
    private bool movingToB = true;
    
    void Update()
    {
        // Pohyb tam a zpět
        if (movingToB)
        {
            journey += speed * Time.deltaTime;
            if (journey >= 1f)
            {
                journey = 1f;
                movingToB = false;
            }
        }
        else
        {
            journey -= speed * Time.deltaTime;
            if (journey <= 0f)
            {
                journey = 0f;
                movingToB = true;
            }
        }
        
        // Aplikuj curve a pozici
        float curveValue = movementCurve.Evaluate(journey);
        transform.position = Vector3.Lerp(pointA.position, pointB.position, curveValue);
    }
    
    void OnDrawGizmos()
    {
        if (pointA && pointB)
        {
            Gizmos.color = Color.yellow;
            Gizmos.DrawLine(pointA.position, pointB.position);
            
            Gizmos.color = Color.red;
            Gizmos.DrawWireSphere(pointA.position, 0.3f);
            Gizmos.DrawWireSphere(pointB.position, 0.3f);
        }
    }
}
```

**Switch/Door systém:**
```csharp
using UnityEngine;

public class Switch : MonoBehaviour
{
    [Header("Target")]
    public Door targetDoor;
    
    [Header("Visual")]
    public Renderer switchRenderer;
    public Color inactiveColor = Color.red;
    public Color activeColor = Color.green;
    
    private bool isActivated = false;
    
    void Start()
    {
        UpdateVisual();
    }
    
    void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            isActivated = !isActivated;
            
            if (targetDoor)
            {
                if (isActivated)
                    targetDoor.Open();
                else
                    targetDoor.Close();
            }
            
            UpdateVisual();
        }
    }
    
    void UpdateVisual()
    {
        if (switchRenderer)
        {
            switchRenderer.material.color = isActivated ? activeColor : inactiveColor;
        }
    }
}

public class Door : MonoBehaviour
{
    [Header("Animation")]
    public float openHeight = 3f;
    public float animSpeed = 2f;
    
    private Vector3 closedPosition;
    private Vector3 openPosition;
    private bool isOpen = false;
    
    void Start()
    {
        closedPosition = transform.position;
        openPosition = closedPosition + Vector3.up * openHeight;
    }
    
    public void Open()
    {
        isOpen = true;
        StopAllCoroutines();
        StartCoroutine(MoveTo(openPosition));
    }
    
    public void Close()
    {
        isOpen = false;
        StopAllCoroutines();
        StartCoroutine(MoveTo(closedPosition));
    }
    
    System.Collections.IEnumerator MoveTo(Vector3 target)
    {
        while (Vector3.Distance(transform.position, target) > 0.01f)
        {
            transform.position = Vector3.MoveTowards(transform.position, target, animSpeed * Time.deltaTime);
            yield return null;
        }
        transform.position = target;
    }
}
```

#### 4. Prefab system (5 minut)

**Vytváření prefabů:**
1. Nastav objekt ve scéně
2. Přetaž z Hierarchy do Project
3. Pojmenuj smysluplně
4. Používej Prefab Variants pro variace

### Úkol pro děti
Postavťte svůj level podle náčrtu z předchozí hodiny. Začněte greyboxingem.

---

## Hodina 29: Balancování obtížnosti (45 minut)

### Cíle hodiny
- Pochopit, co je game balance
- Naučit se měřit a upravovat obtížnost
- Vytvořit systémy pro adaptivní obtížnost

### Průběh hodiny

#### 1. Co je game balance? (10 minut)

**Definice:**
Game balance je umění vytváření vhodné výzvy pro hráče různých úrovní.

**Flow Channel - ideaální obtížnost:**
```
Obtížnost
│
│     / (Frustrace - moc těžké)
│    /
│   *  <- FLOW (ideální)
│  /
│ /______ (Núda - moc lehké)
└────────> Schopnosti hráče
```

**Typy výzev:**
- **Skill-based** - reflex, přesnost
- **Knowledge-based** - záhadky, strategie  
- **Time-based** - tlak času
- **Resource-based** - management zdrojů

#### 2. Měření obtížnosti (15 minut)

**DifficultyAnalyzer skript:**
```csharp
using UnityEngine;
using System.Collections.Generic;

public class DifficultyAnalyzer : MonoBehaviour
{
    [Header("Metrics")]
    public int deaths = 0;
    public float levelStartTime;
    public float totalPlayTime = 0;
    public int attempts = 0;
    
    [Header("Difficulty Factors")]
    [Range(0f, 10f)] public float jumpDifficulty = 1f;
    [Range(0f, 10f)] public float enemyDifficulty = 1f;
    [Range(0f, 10f)] public float timePressure = 1f;
    [Range(0f, 10f)] public float puzzleComplexity = 1f;
    
    private List<float> attemptTimes = new List<float>();
    
    void Start()
    {
        levelStartTime = Time.time;
        attempts++;
        
        Debug.Log($"Level pokus #{attempts}");
    }
    
    public void PlayerDied()
    {
        deaths++;
        
        float attemptTime = Time.time - levelStartTime;
        attemptTimes.Add(attemptTime);
        totalPlayTime += attemptTime;
        
        Debug.Log($"Smrt #{deaths}, čas pokusu: {attemptTime:F1}s");
        
        // Restart metrics
        levelStartTime = Time.time;
        attempts++;
        
        AnalyzeDifficulty();
    }
    
    public void LevelCompleted()
    {
        float attemptTime = Time.time - levelStartTime;
        totalPlayTime += attemptTime;
        attemptTimes.Add(attemptTime);
        
        Debug.Log($"Level dokončen! Celkový čas: {totalPlayTime:F1}s, Pokusů: {attempts}");
        
        AnalyzeDifficulty();
    }
    
    void AnalyzeDifficulty()
    {
        float averageAttemptTime = totalPlayTime / attempts;
        float difficultyScore = CalculateDifficultyScore();
        
        Debug.Log($"Průměrný čas pokusu: {averageAttemptTime:F1}s");
        Debug.Log($"Obtížnost skóre: {difficultyScore:F1}/10");
        
        // Doporučení
        if (deaths > 5 && averageAttemptTime < 30f)
        {
            Debug.LogWarning("⚠️ Level může být příliš těžký!");
        }
        else if (deaths == 0 && totalPlayTime < 60f)
        {
            Debug.LogWarning("⚠️ Level může být příliš lehký!");
        }
        else
        {
            Debug.Log("✓ Obtížnost vypadá vyvváženě");
        }
    }
    
    float CalculateDifficultyScore()
    {
        return (jumpDifficulty + enemyDifficulty + timePressure + puzzleComplexity) / 4f;
    }
    
    [ContextMenu("Reset Metrics")]
    public void ResetMetrics()
    {
        deaths = 0;
        totalPlayTime = 0;
        attempts = 0;
        attemptTimes.Clear();
        levelStartTime = Time.time;
    }
}
```

#### 3. Adaptivní obtížnost (15 minut)

**DynamicDifficulty skript:**
```csharp
using UnityEngine;

public class DynamicDifficulty : MonoBehaviour
{
    [Header("Player Performance")]
    public int recentDeaths = 0;
    public float recentSuccessRate = 1f;
    public int maxRecentDeaths = 3;
    
    [Header("Difficulty Adjustments")]
    [Range(0.5f, 2f)] public float difficultyMultiplier = 1f;
    public bool enableDynamicDifficulty = true;
    
    [Header("What to Adjust")]
    public bool adjustEnemyHealth = true;
    public bool adjustPlayerHealth = true;
    public bool adjustJumpHeight = true;
    
    private PlayerHealth playerHealth;
    private PlayerMovement playerMovement;
    
    void Start()
    {
        playerHealth = FindObjectOfType<PlayerHealth>();
        playerMovement = FindObjectOfType<PlayerMovement>();
    }
    
    public void OnPlayerDeath()
    {
        if (!enableDynamicDifficulty) return;
        
        recentDeaths++;
        
        if (recentDeaths >= maxRecentDeaths)
        {
            MakeEasier();
            recentDeaths = 0; // Reset counter
        }
    }
    
    public void OnPlayerSuccess()
    {
        if (!enableDynamicDifficulty) return;
        
        recentSuccessRate = Mathf.Min(1f, recentSuccessRate + 0.1f);
        
        // Pokud je hráč moc dobrý, zvětš obtížnost
        if (recentSuccessRate > 0.9f)
        {
            MakeHarder();
        }
    }
    
    void MakeEasier()
    {
        difficultyMultiplier = Mathf.Max(0.5f, difficultyMultiplier - 0.1f);
        
        Debug.Log($"Snižuji obtížnost na {difficultyMultiplier:F1}x");
        
        ApplyDifficulty();
        
        // Vizuální feedback
        ShowDifficultyChange("Obtížnost snížena", Color.green);
    }
    
    void MakeHarder()
    {
        difficultyMultiplier = Mathf.Min(2f, difficultyMultiplier + 0.1f);
        
        Debug.Log($"Zvyšuji obtížnost na {difficultyMultiplier:F1}x");
        
        ApplyDifficulty();
        
        ShowDifficultyChange("Obtížnost zvýšena", Color.red);
    }
    
    void ApplyDifficulty()
    {
        // Uprav zdraví hráče
        if (adjustPlayerHealth && playerHealth)
        {
            float newMaxHealth = playerHealth.maxHealth * (2f - difficultyMultiplier);
            playerHealth.SetMaxHealth(newMaxHealth);
        }
        
        // Uprav výšku skoku
        if (adjustJumpHeight && playerMovement)
        {
            playerMovement.sílaSkoku *= (2f - difficultyMultiplier);
        }
        
        // Uprav nepřátele
        if (adjustEnemyHealth)
        {
            Enemy[] enemies = FindObjectsOfType<Enemy>();
            foreach (Enemy enemy in enemies)
            {
                enemy.maxHealth *= difficultyMultiplier;
                enemy.currentHealth = enemy.maxHealth;
            }
        }
    }
    
    void ShowDifficultyChange(string message, Color color)
    {
        // Tady by mohl být UI feedback
        Debug.Log($"<color=#{ColorUtility.ToHtmlStringRGB(color)}>{message}</color>");
    }
}
```

#### 4. A/B testování obtížnosti (5 minut)

**LevelVariant systém:**
```csharp
using UnityEngine;

public class LevelVariantTester : MonoBehaviour
{
    [System.Serializable]
    public class LevelVariant
    {
        public string name;
        public int enemyCount;
        public float platformSpacing;
        public int collectibleCount;
        
        [Range(1f, 5f)] public float estimatedDifficulty;
    }
    
    [Header("Variants to Test")]
    public LevelVariant[] variants;
    
    private int currentVariantIndex = 0;
    
    void Start()
    {
        // Randomly choose variant for this playtest
        currentVariantIndex = Random.Range(0, variants.Length);
        ApplyVariant(variants[currentVariantIndex]);
        
        Debug.Log($"Testing variant: {variants[currentVariantIndex].name}");
    }
    
    void ApplyVariant(LevelVariant variant)
    {
        // Apply the variant settings to the level
        // This would modify enemy spawns, platform positions, etc.
        
        Debug.Log($"Applying variant: {variant.name}");
        Debug.Log($"- Enemy count: {variant.enemyCount}");
        Debug.Log($"- Platform spacing: {variant.platformSpacing}");
        Debug.Log($"- Expected difficulty: {variant.estimatedDifficulty}/5");
    }
}
```

### Úkol pro děti
Přidejte do svého levelu DifficultyAnalyzer a nechte někoho jiného hru vyzkoušet. Pozorujte metriky.

---

## Hodina 30: Testování levelu (45 minut)

### Cíle hodiny
- Naučit se metody testování levelů
- Provest playtesting session
- Iterovat na základě feedbacku

### Průběh hodiny

#### 1. Druhy testování (10 minut)

**Developer Testing:**
- Tvưrce testuje svůj vlastní level
- Rychlé, ale má bias
- Dobré pro základní funkcenost

**Peer Testing:**
- Test mezi spolužáky
- Vzájemný feedback
- Podobná úroveň zkušeností

**Fresh Eyes Testing:**
- člověk, který hru nikdy neviděl
- Najde problémy s onboardingem
- Nejcennější feedback

#### 2. Playtesting checklist (10 minut)

**Před testováním:**
```csharp
using UnityEngine;
using System.Collections.Generic;

public class PlaytestLogger : MonoBehaviour
{
    [Header("What to Track")]
    public bool trackPlayerPath = true;
    public bool trackDeathLocations = true;
    public bool trackTimeSpent = true;
    public bool trackInputs = true;
    
    [Header("Data")]
    public List<Vector3> playerPositions = new List<Vector3>();
    public List<Vector3> deathPositions = new List<Vector3>();
    public List<float> inputTimestamps = new List<float>();
    public List<string> inputTypes = new List<string>();
    
    private Transform player;
    private float startTime;
    
    void Start()
    {
        player = GameObject.FindGameObjectWithTag("Player")?.transform;
        startTime = Time.time;
        
        Debug.Log("=== PLAYTEST SESSION START ===");
        Debug.Log($"Level: {UnityEngine.SceneManagement.SceneManager.GetActiveScene().name}");
        Debug.Log($"Start Time: {System.DateTime.Now}");
    }
    
    void Update()
    {
        // Track player path
        if (trackPlayerPath && player != null)
        {
            if (Time.fixedTime % 0.5f < Time.fixedDeltaTime) // Every 0.5 seconds
            {
                playerPositions.Add(player.position);
            }
        }
        
        // Track inputs
        if (trackInputs)
        {
            if (Input.GetKeyDown(KeyCode.Space))
            {
                LogInput("Jump");
            }
            if (Input.GetKeyDown(KeyCode.W))
            {
                LogInput("Move Forward");
            }
        }
    }
    
    public void LogDeath(Vector3 deathPosition)
    {
        if (trackDeathLocations)
        {
            deathPositions.Add(deathPosition);
            Debug.Log($"Death at: {deathPosition}, Time: {Time.time - startTime:F1}s");
        }
    }
    
    void LogInput(string inputType)
    {
        inputTimestamps.Add(Time.time - startTime);
        inputTypes.Add(inputType);
    }
    
    public void EndPlaytest()
    {
        Debug.Log("=== PLAYTEST SESSION END ===");
        Debug.Log($"Total Time: {Time.time - startTime:F1}s");
        Debug.Log($"Deaths: {deathPositions.Count}");
        Debug.Log($"Path Points: {playerPositions.Count}");
        Debug.Log($"Inputs: {inputTypes.Count}");
        
        AnalyzeResults();
    }
    
    void AnalyzeResults()
    {
        // Analyze death clusters
        if (deathPositions.Count > 0)
        {
            Debug.Log("--- DEATH ANALYSIS ---");
            
            // Find most common death area
            Dictionary<Vector3, int> deathClusters = new Dictionary<Vector3, int>();
            
            foreach (Vector3 deathPos in deathPositions)
            {
                Vector3 rounded = new Vector3(
                    Mathf.Round(deathPos.x),
                    Mathf.Round(deathPos.y),
                    Mathf.Round(deathPos.z)
                );
                
                if (deathClusters.ContainsKey(rounded))
                    deathClusters[rounded]++;
                else
                    deathClusters[rounded] = 1;
            }
            
            foreach (var cluster in deathClusters)
            {
                if (cluster.Value > 2) // More than 2 deaths in same area
                {
                    Debug.LogWarning($"⚠️ Death hotspot at {cluster.Key}: {cluster.Value} deaths");
                }
            }
        }
    }
    
    void OnDrawGizmos()
    {
        // Draw player path
        if (playerPositions.Count > 1)
        {
            Gizmos.color = Color.blue;
            for (int i = 1; i < playerPositions.Count; i++)
            {
                Gizmos.DrawLine(playerPositions[i-1], playerPositions[i]);
            }
        }
        
        // Draw death positions
        Gizmos.color = Color.red;
        foreach (Vector3 deathPos in deathPositions)
        {
            Gizmos.DrawWireSphere(deathPos, 0.5f);
        }
    }
}
```

#### 3. Feedback sbírání (15 minut)

**Playtesting Questions:**
```csharp
using UnityEngine;
using UnityEngine.UI;

public class FeedbackCollector : MonoBehaviour
{
    [Header("Feedback UI")]
    public GameObject feedbackPanel;
    public Slider funSlider;
    public Slider difficultySlider;
    public InputField commentsField;
    public Button submitButton;
    
    [System.Serializable]
    public class FeedbackData
    {
        public float funRating;        // 1-5
        public float difficultyRating; // 1-5 (1=easy, 5=hard)
        public string comments;
        public float playTime;
        public int deaths;
        public bool completed;
    }
    
    private FeedbackData currentFeedback;
    
    void Start()
    {
        currentFeedback = new FeedbackData();
        feedbackPanel.SetActive(false);
        
        if (submitButton)
            submitButton.onClick.AddListener(SubmitFeedback);
    }
    
    public void ShowFeedbackForm()
    {
        feedbackPanel.SetActive(true);
        Time.timeScale = 0f; // Pause game
        
        // Pre-fill known data
        PlaytestLogger logger = FindObjectOfType<PlaytestLogger>();
        if (logger)
        {
            currentFeedback.playTime = Time.time;
            currentFeedback.deaths = logger.deathPositions.Count;
        }
    }
    
    public void SubmitFeedback()
    {
        // Collect data from UI
        if (funSlider) currentFeedback.funRating = funSlider.value;
        if (difficultySlider) currentFeedback.difficultyRating = difficultySlider.value;
        if (commentsField) currentFeedback.comments = commentsField.text;
        
        // Save/log feedback
        SaveFeedback(currentFeedback);
        
        Debug.Log("=== FEEDBACK RECEIVED ===");
        Debug.Log($"Fun: {currentFeedback.funRating}/5");
        Debug.Log($"Difficulty: {currentFeedback.difficultyRating}/5");
        Debug.Log($"Comments: {currentFeedback.comments}");
        
        feedbackPanel.SetActive(false);
        Time.timeScale = 1f;
    }
    
    void SaveFeedback(FeedbackData feedback)
    {
        string json = JsonUtility.ToJson(feedback, true);
        string filename = $"feedback_{System.DateTime.Now:yyyy-MM-dd_HH-mm-ss}.json";
        
        #if UNITY_EDITOR
        string path = System.IO.Path.Combine(Application.dataPath, "Feedback", filename);
        System.IO.Directory.CreateDirectory(System.IO.Path.GetDirectoryName(path));
        System.IO.File.WriteAllText(path, json);
        Debug.Log($"Feedback saved to: {path}");
        #endif
    }
}
```

#### 4. Iterační proces (10 minut)

**Postup po testování:**
1. **Analyze** - co data říkájí?
2. **Prioritize** - co je nejvážnější problém?
3. **Fix** - oprav jeden problém
4. **Test** - znovu otestuj
5. **Repeat** - opakuj dokud není level dobrý

**LevelIterator helper:**
```csharp
using UnityEngine;
using System.Collections.Generic;

public class LevelIterator : MonoBehaviour
{
    [Header("Version Control")]
    public int versionNumber = 1;
    public List<string> changeLog = new List<string>();
    
    [Header("Common Fixes")]
    public float platformSpacing = 2f;
    public float jumpHeight = 5f;
    public int checkpointFrequency = 3;
    
    public void AddChange(string change)
    {
        changeLog.Add($"v{versionNumber}: {change}");
        Debug.Log($"Level change logged: {change}");
    }
    
    [ContextMenu("Increase Jump Height")]
    public void IncreaseJumpHeight()
    {
        PlayerMovement player = FindObjectOfType<PlayerMovement>();
        if (player)
        {
            player.rychlostSkoku *= 1.1f;
            AddChange($"Increased jump height to {player.rychlostSkoku:F1}");
        }
    }
    
    [ContextMenu("Add More Checkpoints")]
    public void AddMoreCheckpoints()
    {
        // This would add checkpoint objects at regular intervals
        AddChange("Added more checkpoints");
    }
    
    [ContextMenu("Reduce Platform Gaps")]
    public void ReducePlatformGaps()
    {
        // This would move platforms closer together
        AddChange("Reduced platform gaps");
    }
    
    public void NewVersion()
    {
        versionNumber++;
        Debug.Log($"--- LEVEL VERSION {versionNumber} ---");
    }
}
```

### Aktivita - Playtesting Session
Děti se rozdělí do dvojic:
1. Jeden hráč hraje, druhý pozoruje a zapisuje
2. Po 10 minutach si vymění
3. Diskutují feedback
4. Upravují svoje levely

### Shrnutí bloku
**Čeho jsme dosáhli:**
- Porozumění principy level designu
- Praktické dovednosti pro stavbu levelů
- Systémy pro měření a upravu obtížnosti
- Metody testování a iterace

**Připravili jsme se na:**
- Velké finální projekty
- Komplexní game design rozhodnutí
- Profesionální přístup k vývoji her
