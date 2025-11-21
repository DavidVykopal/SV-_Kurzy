# Blok 7: UI a UX (24–26)

## Přehled bloku
**Cíl:** Naučit děti principy návrhu uživatelského rozhraní a user experience pro hry.
**Výstup:** Profesionálně vypadající menu systémy a UI elementy v hrách.

---

## Hodina 24: Menu a tlačítka (45 minut)

### Cíle hodiny
- Pochopit základy UI designu pro hry
- Vytvořit hlavní menu s navigací
- Naučit se pracovat s tlačítky a events

### Materiály
- Unity projekt s jednoduchou hrou
- Grafické assety pro UI (tlacítka, pozadí)
- Font soubory

### Průběh hodiny

#### 1. Úvod do UI designu (10 minut)

**Co je UI (User Interface):**
- Vše, s čím hráč interaguje
- Tlačítka, menu, texty, indikátory
- Musí být intuitivní a krásné

**Základní principy herního UI:**
- **Jednoduše je lépe** - nepřetížit screen
- **Konzistence** - stejný styl v celé hře
- **Feedback** - hráč musí vědět, co se stalo
- **Přístupnost** - všichni to musí umět použít

**Příklady dobrého UI:**
- Minecraft - jednoduché, čitellné
- Mario - jasné ikony, barvy
- Among Us - minimální ale funkční

#### 2. Canvas a UI elementy (10 minut)

**Unity UI systém:**
1. Canvas - "plátno" pro všechny UI elementy
2. UI elementy - tlačítka, texty, obrázky

**Vytvoření Canvas:**
```
Hierarchy → UI → Canvas
```

**Canvas nastaveni:**
- **Render Mode:** Screen Space - Overlay (vždy nahoře)
- **UI Scale Mode:** Scale With Screen Size
- **Reference Resolution:** 1920x1080

**Základní UI elementy:**
- **Button** - tlačítko s textem
- **Image** - obrázek nebo ikona
- **Text** - text (starší verze)
- **TextMeshPro** - lepší text s efekty

#### 3. Hlavní menu (20 minut)

**Struktura hlavního menu:**
```
MainMenu (Canvas)
├── Background (Image)
├── Title (TextMeshPro)
├── ButtonPanel (Panel)
│   ├── PlayButton
│   ├── OptionsButton
│   └── QuitButton
└── VersionText (Text)
```

**MenuManager skript:**
```csharp
using UnityEngine;
using UnityEngine.SceneManagement;
using UnityEngine.UI;

public class MenuManager : MonoBehaviour
{
    [Header("Menu Panels")]
    public GameObject mainMenuPanel;
    public GameObject optionsPanel;
    public GameObject creditsPanel;
    
    [Header("Buttons")]
    public Button playButton;
    public Button optionsButton;
    public Button creditsButton;
    public Button quitButton;
    public Button backButton;
    
    [Header("Nastavení")]
    public string gameSceneName = "GameScene";
    
    void Start()
    {
        // Nastav button listenery
        if (playButton) playButton.onClick.AddListener(PlayGame);
        if (optionsButton) optionsButton.onClick.AddListener(OpenOptions);
        if (creditsButton) creditsButton.onClick.AddListener(OpenCredits);
        if (quitButton) quitButton.onClick.AddListener(QuitGame);
        if (backButton) backButton.onClick.AddListener(BackToMain);
        
        // Zoba všechny panely kromě hlavního
        ShowMainMenu();
    }
    
    public void PlayGame()
    {
        Debug.Log("Loading game...");
        Time.timeScale = 1f; // Ujisti se, že hra běží
        SceneManager.LoadScene(gameSceneName);
    }
    
    public void OpenOptions()
    {
        mainMenuPanel.SetActive(false);
        optionsPanel.SetActive(true);
    }
    
    public void OpenCredits()
    {
        mainMenuPanel.SetActive(false);
        creditsPanel.SetActive(true);
    }
    
    public void BackToMain()
    {
        ShowMainMenu();
    }
    
    public void QuitGame()
    {
        Debug.Log("Quitting game...");
        Application.Quit();
        
        #if UNITY_EDITOR
        UnityEditor.EditorApplication.isPlaying = false;
        #endif
    }
    
    void ShowMainMenu()
    {
        mainMenuPanel.SetActive(true);
        if (optionsPanel) optionsPanel.SetActive(false);
        if (creditsPanel) creditsPanel.SetActive(false);
    }
}
```

**Stylizace tlačítek:**
1. Vyberte tlačítko
2. V Inspector najděte "Button (Script)"
3. Colors:
   - Normal Color: světlá barva
   - Highlighted Color: jasnější barva
   - Pressed Color: tmavší barva
   - Disabled Color: šedá

#### 4. Animace tlačítek (5 minut)

**Jednoduchá animace hover:**
```csharp
using UnityEngine;
using UnityEngine.EventSystems;

public class ButtonHoverEffect : MonoBehaviour, IPointerEnterHandler, IPointerExitHandler
{
    [Header("Animace")]
    public float scaleAmount = 1.1f;
    public float animSpeed = 0.2f;
    
    private Vector3 originalScale;
    private RectTransform rectTransform;
    
    void Start()
    {
        rectTransform = GetComponent<RectTransform>();
        originalScale = rectTransform.localScale;
    }
    
    public void OnPointerEnter(PointerEventData eventData)
    {
        // Zvětšit tlačítko
        LeanTween.scale(rectTransform, originalScale * scaleAmount, animSpeed)
                 .setEase(LeanTweenType.easeOutBack);
    }
    
    public void OnPointerExit(PointerEventData eventData)
    {
        // Vrátit na původní velikost
        LeanTween.scale(rectTransform, originalScale, animSpeed)
                 .setEase(LeanTweenType.easeOutBack);
    }
}
```

### Úkol pro děti
Vytvořte hlavní menu pro svou hru s alespoň třemi tlačítky a vlastním pozadím.

---

## Hodina 25: Skóre, životy a HUD (45 minut)

### Cíle hodiny
- Navrhnout funkční HUD (Heads-Up Display)
- Vytvořit systémy pro zobrazování skóre a zdraví
- Přidat progress bary a indikátory

### Průběh hodiny

#### 1. Co je HUD? (5 minut)

**HUD (Heads-Up Display):**
- UI elementy během hraní
- Informace o stavu hry
- Nesmí rušit gameplay
- Musí být rychle čitelré

**Typické HUD elementy:**
- Skóre/body
- Zdraví/životy
- Munice/energie
- Minimap
- Inventory
- Timer

#### 2. Systém skóre (15 minut)

**AnimatedScore skript:**
```csharp
using UnityEngine;
using UnityEngine.UI;
using System.Collections;

public class ScoreManager : MonoBehaviour
{
    [Header("UI References")]
    public Text scoreText;
    public Text highScoreText;
    
    [Header("Animace")]
    public float countDuration = 0.5f;
    public AnimationCurve countCurve = AnimationCurve.EaseInOut(0, 0, 1, 1);
    
    private int currentScore = 0;
    private int displayScore = 0;
    private int highScore = 0;
    
    void Start()
    {
        // Načti high score
        highScore = PlayerPrefs.GetInt("HighScore", 0);
        UpdateUI();
    }
    
    public void AddScore(int points)
    {
        currentScore += points;
        
        // Animované počítání
        StopAllCoroutines();
        StartCoroutine(AnimateScore(displayScore, currentScore));
        
        // Kontrola high score
        if (currentScore > highScore)
        {
            highScore = currentScore;
            PlayerPrefs.SetInt("HighScore", highScore);
            
            // Efekt nového rekordu
            StartCoroutine(HighScoreEffect());
        }
    }
    
    System.Collections.IEnumerator AnimateScore(int startScore, int endScore)
    {
        float elapsed = 0f;
        
        while (elapsed < countDuration)
        {
            elapsed += Time.deltaTime;
            float progress = elapsed / countDuration;
            
            // Použij animation curve
            float curveValue = countCurve.Evaluate(progress);
            displayScore = Mathf.RoundToInt(Mathf.Lerp(startScore, endScore, curveValue));
            
            UpdateUI();
            yield return null;
        }
        
        displayScore = endScore;
        UpdateUI();
    }
    
    System.Collections.IEnumerator HighScoreEffect()
    {
        // Blikání textu při novém rekordu
        Color originalColor = highScoreText.color;
        
        for (int i = 0; i < 6; i++)
        {
            highScoreText.color = Color.yellow;
            yield return new WaitForSeconds(0.2f);
            highScoreText.color = originalColor;
            yield return new WaitForSeconds(0.2f);
        }
    }
    
    void UpdateUI()
    {
        if (scoreText) scoreText.text = "Skóre: " + displayScore;
        if (highScoreText) highScoreText.text = "Rekord: " + highScore;
    }
    
    public int GetScore()
    {
        return currentScore;
    }
    
    public void ResetScore()
    {
        currentScore = 0;
        displayScore = 0;
        UpdateUI();
    }
}
```

#### 3. Systém zdraví s UI (15 minut)

**HealthSystem s různými vizualizacemi:**
```csharp
using UnityEngine;
using UnityEngine.UI;
using System.Collections.Generic;

public class HealthUI : MonoBehaviour
{
    [Header("Health Bar")]
    public Slider healthSlider;
    public Image healthFill;
    public Gradient healthGradient;
    
    [Header("Heart System")]
    public Transform heartContainer;
    public GameObject heartPrefab;
    private List<Image> heartImages = new List<Image>();
    
    [Header("Numeric Display")]
    public Text healthText;
    
    [Header("Effects")]
    public Image damageVignette;
    public float vignetteSpeed = 2f;
    
    private float maxHealth;
    private float currentHealth;
    
    public void InitializeHealth(float maxHP)
    {
        maxHealth = maxHP;
        currentHealth = maxHP;
        
        SetupHeartSystem();
        UpdateHealthUI();
    }
    
    void SetupHeartSystem()
    {
        // Vytvoř srdce
        int heartCount = Mathf.CeilToInt(maxHealth / 25f); // Každé srdce = 25 HP
        
        for (int i = 0; i < heartCount; i++)
        {
            GameObject heart = Instantiate(heartPrefab, heartContainer);
            heartImages.Add(heart.GetComponent<Image>());
        }
    }
    
    public void UpdateHealth(float health)
    {
        float previousHealth = currentHealth;
        currentHealth = health;
        
        UpdateHealthUI();
        
        // Damage efekt
        if (health < previousHealth)
        {
            StartCoroutine(DamageEffect());
        }
    }
    
    void UpdateHealthUI()
    {
        // Health bar
        if (healthSlider)
        {
            healthSlider.value = currentHealth / maxHealth;
            
            if (healthFill)
            {
                healthFill.color = healthGradient.Evaluate(healthSlider.value);
            }
        }
        
        // Srdce
        UpdateHearts();
        
        // Numeric text
        if (healthText)
        {
            healthText.text = $"{currentHealth:F0}/{maxHealth:F0}";
        }
    }
    
    void UpdateHearts()
    {
        float healthPerHeart = maxHealth / heartImages.Count;
        
        for (int i = 0; i < heartImages.Count; i++)
        {
            float heartMinHealth = i * healthPerHeart;
            float heartMaxHealth = (i + 1) * healthPerHeart;
            
            if (currentHealth >= heartMaxHealth)
            {
                // Plné srdce
                heartImages[i].color = Color.red;
                heartImages[i].fillAmount = 1f;
            }
            else if (currentHealth > heartMinHealth)
            {
                // Částečně plné srdce
                float fillAmount = (currentHealth - heartMinHealth) / healthPerHeart;
                heartImages[i].fillAmount = fillAmount;
                heartImages[i].color = Color.red;
            }
            else
            {
                // Prázdné srdce
                heartImages[i].color = Color.gray;
                heartImages[i].fillAmount = 1f;
            }
        }
    }
    
    System.Collections.IEnumerator DamageEffect()
    {
        if (damageVignette)
        {
            float alpha = 0.5f;
            damageVignette.color = new Color(1, 0, 0, alpha);
            
            while (alpha > 0)
            {
                alpha -= Time.deltaTime * vignetteSpeed;
                damageVignette.color = new Color(1, 0, 0, Mathf.Max(0, alpha));
                yield return null;
            }
        }
    }
}
```

#### 4. Minimap systém (10 minut)

**Jednoduchá minimap:**
```csharp
using UnityEngine;
using UnityEngine.UI;

public class Minimap : MonoBehaviour
{
    [Header("Nastavení")]
    public Transform player;
    public Camera minimapCamera;
    public float zoomLevel = 10f;
    
    [Header("UI")]
    public RectTransform minimapRect;
    public Image playerIcon;
    
    void LateUpdate()
    {
        if (player && minimapCamera)
        {
            // Nastav pozici kamery nad hráčem
            Vector3 newPosition = player.position;
            newPosition.y = minimapCamera.transform.position.y;
            minimapCamera.transform.position = newPosition;
            
            // Rotace player ikony
            if (playerIcon)
            {
                playerIcon.rectTransform.rotation = Quaternion.Euler(0, 0, -player.eulerAngles.y);
            }
        }
    }
    
    public void SetZoom(float zoom)
    {
        zoomLevel = zoom;
        if (minimapCamera)
        {
            minimapCamera.orthographicSize = zoomLevel;
        }
    }
}
```

### Úkol pro děti
Přidejte do své hry HUD se skóre, zdravím (buď srdce nebo progress bar) a jednoduchým indikátorem.

---

## Hodina 26: UX principy (45 minut)

### Cíle hodiny
- Pochopit rozdíl mezi UI a UX
- Naučit se základní principy user experience
- Aplikovat UX principy na herní design

### Průběh hodiny

#### 1. UI vs UX (10 minut)

**UI (User Interface):**
- Jak věci vypadají
- Tlačítka, barvy, fonty
- "Knížka"

**UX (User Experience):**
- Jak se věci používají
- Jak se hráč cítí
- "Příběh knihy"

**Analogie s restaurací:**
- UI = jak vypadá jídelní lístek
- UX = celý zážitek v restauraci

#### 2. Základní UX principy (15 minut)

**1. Intuitivnost - "Neměl bych přemýšlet"**
```csharp
// Správné - jasné označení
public Button startGameButton; // "Start Game"
public Button exitButton;      // "Exit"

// Špatné - nejasné označení
public Button button1;         // "OK" - co to dělá?
public Button button2;         // "Cancel" - cancel čeho?
```

**2. Feedback - "Vím, co se stalo"**
```csharp
using UnityEngine;
using UnityEngine.UI;

public class ButtonFeedback : MonoBehaviour
{
    public AudioClip clickSound;
    public ParticleSystem clickEffect;
    
    public void OnButtonClick()
    {
        // Audio feedback
        if (clickSound)
            AudioSource.PlayClipAtPoint(clickSound, transform.position);
            
        // Vizuální feedback
        if (clickEffect)
            clickEffect.Play();
            
        // Haptický feedback (mobily)
        #if UNITY_ANDROID || UNITY_IOS
        Handheld.Vibrate();
        #endif
    }
}
```

**3. Consistency - "Vše funguje stejně"**
- Stejné barvy pro stejné akce
- Stejné ovládání v celé hře
- Stejná umístění UI elementů

**4. Accessibility - "Všichni to mohou použít"**
```csharp
using UnityEngine;
using UnityEngine.UI;

public class AccessibilityHelper : MonoBehaviour
{
    [Header("Color Blind Support")]
    public bool useColorBlindFriendlyColors = true;
    
    [Header("Font Size")]
    public Slider fontSizeSlider;
    public Text[] allTexts;
    
    void Start()
    {
        if (fontSizeSlider)
        {
            fontSizeSlider.onValueChanged.AddListener(ChangeFontSize);
        }
    }
    
    void ChangeFontSize(float multiplier)
    {
        foreach (Text text in allTexts)
        {
            text.fontSize = Mathf.RoundToInt(text.fontSize * multiplier);
        }
    }
}
```

#### 3. Herní UX principy (15 minut)

**1. Onboarding - "Jak začít"**
```csharp
using UnityEngine;
using UnityEngine.UI;

public class TutorialManager : MonoBehaviour
{
    [Header("Tutorial Steps")]
    public GameObject[] tutorialSteps;
    public Button nextButton;
    public Button skipButton;
    
    private int currentStep = 0;
    
    void Start()
    {
        // Ukaž jenom první krok
        ShowStep(0);
        
        nextButton.onClick.AddListener(NextStep);
        skipButton.onClick.AddListener(SkipTutorial);
    }
    
    public void NextStep()
    {
        currentStep++;
        
        if (currentStep < tutorialSteps.Length)
        {
            ShowStep(currentStep);
        }
        else
        {
            EndTutorial();
        }
    }
    
    void ShowStep(int stepIndex)
    {
        // Skryj všechny kroky
        for (int i = 0; i < tutorialSteps.Length; i++)
        {
            tutorialSteps[i].SetActive(i == stepIndex);
        }
    }
    
    public void SkipTutorial()
    {
        PlayerPrefs.SetInt("TutorialCompleted", 1);
        EndTutorial();
    }
    
    void EndTutorial()
    {
        PlayerPrefs.SetInt("TutorialCompleted", 1);
        gameObject.SetActive(false);
    }
}
```

**2. Flow State - "Hráč zapoměněl na čas"**
- Správná obtížnost (ne moc lehké, ne moc těžké)
- Minimální přerušení
- Jasné cíle

**3. Forgiveness - "Odpouštění chyb"**
```csharp
using UnityEngine;

public class ForgivenessSystem : MonoBehaviour
{
    [Header("Coyote Time - hráč může skočit kratče po optuštění platformy")]
    public float coyoteTime = 0.2f;
    private float coyoteCounter;
    
    [Header("Jump Buffer - skok se 'zapamětá' i před dopadem")]
    public float jumpBufferTime = 0.2f;
    private float jumpBufferCounter;
    
    private bool isGrounded;
    
    void Update()
    {
        // Coyote time
        if (isGrounded)
        {
            coyoteCounter = coyoteTime;
        }
        else
        {
            coyoteCounter -= Time.deltaTime;
        }
        
        // Jump buffer
        if (Input.GetKeyDown(KeyCode.Space))
        {
            jumpBufferCounter = jumpBufferTime;
        }
        else
        {
            jumpBufferCounter -= Time.deltaTime;
        }
        
        // Skok s odpouštěním
        if (jumpBufferCounter > 0f && coyoteCounter > 0f)
        {
            Jump();
            jumpBufferCounter = 0f;
        }
    }
    
    void Jump()
    {
        // Skok logika...
        Debug.Log("Skok!");
    }
}
```

#### 4. Testování UX (5 minut)

**Jak testovat UX:**
1. **Sledujte hráče** - bez komentářů
2. **"Think aloud"** - hráč říká, co si myslí
3. **Hledáme frustraci** - kdy hráč neví, co dělat
4. **Měříme čas** - jak dlouho trvá naučit se ovládání

**Jednoduché UX testy:**
- Dej hru někomu, kdo ji nikdy neviděl
- Nerik mu nic
- Pozoruj, kde se zasekne
- Oprav problémy

### Aktivita
Ve dvojicích si děti testují navzájem svoje hry a hledají UX problémy.

### Shrnutí bloku
**Čeho jsme dosáhli:**
- Profesionálně vypadající menu systémy
- Funkční HUD s animacemi
- Pochopení UX principů
- Schopnost testovat a vylepšovat uživatelský zážitek

**Připravili jsme se na:**
- Profesionální level design
- Celkový game design thinking
- Finální projekty
