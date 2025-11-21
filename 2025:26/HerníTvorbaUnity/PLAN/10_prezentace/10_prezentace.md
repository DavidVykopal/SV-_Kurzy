# Blok 10: Prezentace a showcase (36–38)

## Přehled bloku
**Cíl:** Děti představí své hry, reflexe celého kurzu a oslava úspěchů.
**Výstup:** Veřejná prezentace projektů, certifikáty a inspirace pro další tvorbu.

---

## Hodina 36: Příprava prezentací (45 minut)

### Cíle hodiny
- Naučit se prezentovat své dílo efektivně
- Připravit demo verze her pro prezentaci
- Vytvořit podpůrné materiály (screenshots, videa)

### Materiály
- Projektory nebo velké obrazovky
- Mikrofonový systém (pokud dostupný)
- Nástroje pro nahrávání obrazovky (OBS Studio)

### Průběh hodiny

#### 1. Jak prezentovat hru? (10 minut)

**Struktura prezentace (3-5 minut na žáka):**
1. **Název a žánr** (15 sekund)
2. **Inspirace** - Co vás inspirovalo? (30 sekund)
3. **Demo gameplay** - Zahrajte si live (2-3 minuty)
4. **Nejtěžší výzva** - Co bylo nejobtížnější? (30 sekund)
5. **Nejhoréjší moment** - Na co jste nejhřdejší? (30 sekunds)
6. **Q&A** - Otázky z publika (30 sekund)

**Tipy pro dobrou prezentaci:**
- Mluv hlasitě a jasně
- Obraťte se k publiku, ne jen na obrazovku
- Připravte si backup plán (screenshot/video) pokud hra nebude fungovat
- Buďte hrdí na to, co jste vytvořili!

#### 2. Demo příprava (15 minut)

**PresentationMode skript:**
```csharp
using UnityEngine;
using UnityEngine.SceneManagement;

public class PresentationMode : MonoBehaviour
{
    [Header("Demo Settings")]
    public bool autoStartDemo = true;
    public string demoStartLevel = "Level1";
    public float autoRestartTime = 180f; // 3 minutes
    
    [Header("UI Adjustments")]
    public bool hideDebugUI = true;
    public bool showInstructions = true;
    public bool enlargeUI = true;
    
    [Header("Cheats for Demo")]
    public bool invincibilityMode = false;
    public bool skipToEnd = false;
    public bool showAllSecrets = false;
    
    private float demoStartTime;
    private Canvas instructionCanvas;
    
    void Start()
    {
        Debug.Log("=== PRESENTATION MODE ACTIVE ===");
        
        demoStartTime = Time.time;
        
        ApplyDemoSettings();
        CreateInstructions();
        
        if (autoStartDemo)
        {
            StartDemo();
        }
    }
    
    void Update()
    {
        // Auto-restart demo after time limit
        if (Time.time - demoStartTime > autoRestartTime)
        {
            RestartDemo();
        }
        
        // Quick restart with F5
        if (Input.GetKeyDown(KeyCode.F5))
        {
            RestartDemo();
        }
        
        // Skip to end with F9 (for emergency)
        if (Input.GetKeyDown(KeyCode.F9) && skipToEnd)
        {
            ShowWinScreen();
        }
    }
    
    void ApplyDemoSettings()
    {
        if (hideDebugUI)
        {
            // Hide any debug UI elements
            GameObject[] debugObjects = GameObject.FindGameObjectsWithTag("DebugUI");
            foreach (GameObject obj in debugObjects)
            {
                obj.SetActive(false);
            }
        }
        
        if (enlargeUI)
        {
            // Make UI elements bigger for presentation
            Canvas[] canvases = FindObjectsOfType<Canvas>();
            foreach (Canvas canvas in canvases)
            {
                if (canvas.renderMode == RenderMode.ScreenSpaceOverlay)
                {
                    CanvasScaler scaler = canvas.GetComponent<CanvasScaler>();
                    if (scaler)
                    {
                        scaler.scaleFactor = 1.2f; // 20% bigger
                    }
                }
            }
        }
        
        if (invincibilityMode)
        {
            PlayerHealth health = FindObjectOfType<PlayerHealth>();
            if (health)
            {
                health.maxHealth = 9999;
                health.currentHealth = 9999;
            }
        }
    }
    
    void CreateInstructions()
    {
        if (!showInstructions) return;
        
        GameObject instructionObj = new GameObject("DemoInstructions");
        instructionCanvas = instructionObj.AddComponent<Canvas>();
        instructionCanvas.renderMode = RenderMode.ScreenSpaceOverlay;
        instructionCanvas.sortingOrder = 1000; // Always on top
        
        instructionObj.AddComponent<UnityEngine.UI.CanvasScaler>();
        instructionObj.AddComponent<UnityEngine.UI.GraphicRaycaster>();
        
        // Create instruction text
        GameObject textObj = new GameObject("InstructionText");
        textObj.transform.parent = instructionObj.transform;
        
        UnityEngine.UI.Text instructionText = textObj.AddComponent<UnityEngine.UI.Text>();
        instructionText.text = "F5 - Restart Demo | Demo auto-restarts every 3 minutes";
        instructionText.font = Resources.GetBuiltinResource<Font>("Arial.ttf");
        instructionText.fontSize = 16;
        instructionText.color = Color.white;
        
        // Position at bottom of screen
        RectTransform textRect = textObj.GetComponent<RectTransform>();
        textRect.anchorMin = new Vector2(0, 0);
        textRect.anchorMax = new Vector2(1, 0);
        textRect.offsetMin = new Vector2(10, 10);
        textRect.offsetMax = new Vector2(-10, 30);
    }
    
    public void StartDemo()
    {
        if (!string.IsNullOrEmpty(demoStartLevel))
        {
            SceneManager.LoadScene(demoStartLevel);
        }
    }
    
    public void RestartDemo()
    {
        Debug.Log("Restarting demo...");
        demoStartTime = Time.time;
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
    
    void ShowWinScreen()
    {
        // Emergency skip to end
        GameManager gm = FindObjectOfType<GameManager>();
        if (gm)
        {
            gm.Victory();
        }
    }
    
    void OnGUI()
    {
        // Show demo info in corner
        GUI.color = new Color(1, 1, 1, 0.7f);
        float remainingTime = autoRestartTime - (Time.time - demoStartTime);
        
        GUI.Label(new Rect(10, Screen.height - 50, 200, 20), 
                 $"Demo: {remainingTime:F0}s remaining");
    }
}
```

#### 3. Screenshot a video nahrávání (15 minut)

**ScreenshotManager:**
```csharp
using UnityEngine;
using System.IO;

public class ScreenshotManager : MonoBehaviour
{
    [Header("Screenshot Settings")]
    public KeyCode screenshotKey = KeyCode.F12;
    public int screenshotScale = 2; // 2x resolution
    public bool hideUIForScreenshot = true;
    
    [Header("Auto Screenshots")]
    public bool takeAutoScreenshots = false;
    public float autoScreenshotInterval = 30f;
    
    private float lastScreenshotTime;
    
    void Update()
    {
        if (Input.GetKeyDown(screenshotKey))
        {
            TakeScreenshot();
        }
        
        if (takeAutoScreenshots && Time.time - lastScreenshotTime > autoScreenshotInterval)
        {
            TakeScreenshot();
            lastScreenshotTime = Time.time;
        }
    }
    
    public void TakeScreenshot()
    {
        StartCoroutine(CaptureScreenshot());
    }
    
    System.Collections.IEnumerator CaptureScreenshot()
    {
        Canvas[] canvases = null;
        bool[] originalCanvasStates = null;
        
        // Hide UI if requested
        if (hideUIForScreenshot)
        {
            canvases = FindObjectsOfType<Canvas>();
            originalCanvasStates = new bool[canvases.Length];
            
            for (int i = 0; i < canvases.Length; i++)
            {
                originalCanvasStates[i] = canvases[i].enabled;
                canvases[i].enabled = false;
            }
        }
        
        // Wait a frame for UI to hide
        yield return new WaitForEndOfFrame();
        
        // Take screenshot
        string timestamp = System.DateTime.Now.ToString("yyyy-MM-dd_HH-mm-ss");
        string filename = $"Screenshot_{timestamp}.png";
        
        #if UNITY_EDITOR
        string directory = Path.Combine(Application.dataPath, "Screenshots");
        #else
        string directory = Path.Combine(Application.persistentDataPath, "Screenshots");
        #endif
        
        if (!Directory.Exists(directory))
        {
            Directory.CreateDirectory(directory);
        }
        
        string fullPath = Path.Combine(directory, filename);
        
        ScreenCapture.CaptureScreenshot(fullPath, screenshotScale);
        
        Debug.Log($"Screenshot saved: {fullPath}");
        
        // Restore UI
        if (hideUIForScreenshot && canvases != null)
        {
            for (int i = 0; i < canvases.Length; i++)
            {
                canvases[i].enabled = originalCanvasStates[i];
            }
        }
    }
    
    [ContextMenu("Open Screenshot Folder")]
    public void OpenScreenshotFolder()
    {
        #if UNITY_EDITOR
        string directory = Path.Combine(Application.dataPath, "Screenshots");
        #else
        string directory = Path.Combine(Application.persistentDataPath, "Screenshots");
        #endif
        
        if (Directory.Exists(directory))
        {
            #if UNITY_EDITOR_WIN
            System.Diagnostics.Process.Start("explorer.exe", directory);
            #elif UNITY_EDITOR_OSX
            System.Diagnostics.Process.Start("open", directory);
            #endif
        }
    }
}
```

#### 4. Príprava elevator pitch (5 minut)

**Elevator Pitch šablona:**
```
"Má hra se jmenuje [NÁZEV] a je to [ZANŘ]. 
Inspirovalo mě [CO/KDO] a chtěl jsem vytvořit [CEL]. 
Nejtěžší bylo [VYZVA], ale nakonec se mi povedlo [USPECH].
Na hře jsem nejhřdejší na [KONKRÉTNÍ FEATURE]."
```

**Příklad:**
```
"Má hra se jmenuje 'Robot Escape' a je to 2D plošinovka. 
Inspirovalo mě Portal a chtěl jsem vytvořit hru o roboto, který utíká z laboratoře. 
Nejtěžší bylo naprogramovat teleportování, ale nakonec se mi povedlo vytvořit 5 levelů. 
Na hře jsem nejhřdejší na to, že robot má různé animace a hra má vlastní hudbu."
```

### Úkol
Připravte si elevator pitch a otestujte demo svou hry.

---

## Hodina 37: Hlavní prezentace (45 minut)

### Cíle hodiny
- Presentační vystoupení všech žáků
- Vzájemný feedback a ocenění
- Dokumentace a sdílení výsledků

### Příprava učitele
- Pozvat rodiče/zástupcě školy
- Připravit certifikaty
- Nastavi projektory/obrazovky
- Připravit kamer pro nahrávání

### Průběh hodiny

#### 1. Úvod a připomenutí cesty (5 minut)

**Reflexe celé cesty:**
- Odk trhd jsme začínali (hello world v Unity)
- Co vše jsme se naučili
- Jakých pokrok jsme dosáhli

**Kurz v číslech:**
```csharp
using UnityEngine;

public class CourseStats : MonoBehaviour
{
    [Header("Course Statistics")]
    public int totalHours = 35;
    public int totalProjects = 8;
    public int linesOfCodeWritten = 1500;
    public int bugsFixed = 50;
    public int coffeesConsumed = 0; // They're kids! :)
    
    [Header("Skills Learned")]
    public string[] skillsLearned = {
        "C# programming",
        "Unity Engine",
        "2D and 3D game development",
        "UI/UX design",
        "Level design",
        "Game balance",
        "Audio integration",
        "Visual effects",
        "Project management",
        "Presentation skills"
    };
    
    void Start()
    {
        PrintCourseStats();
    }
    
    void PrintCourseStats()
    {
        Debug.Log("=== UNITY COURSE COMPLETED! ===");
        Debug.Log($"Hours spent learning: {totalHours}");
        Debug.Log($"Projects completed: {totalProjects}");
        Debug.Log($"Lines of code: {linesOfCodeWritten}+");
        Debug.Log($"Skills mastered: {skillsLearned.Length}");
        
        foreach (string skill in skillsLearned)
        {
            Debug.Log($"- {skill}");
        }
    }
}
```

#### 2. Prezentace projektů (30 minut)

**Formať prezentace:**
- Každý žák má 5 minut
- 3 minuty demo + 2 minuty otázky
- Po každé prezentaci potlesk!

**PresentationTimer:**
```csharp
using UnityEngine;
using UnityEngine.UI;

public class PresentationTimer : MonoBehaviour
{
    [Header("Timer Settings")]
    public float presentationTime = 300f; // 5 minutes
    public float warningTime = 60f; // Warning at 1 minute left
    
    [Header("UI")]
    public Text timerText;
    public Image timerBar;
    public GameObject warningPanel;
    
    private float remainingTime;
    private bool timerRunning = false;
    private bool warningShown = false;
    
    void Start()
    {
        remainingTime = presentationTime;
        UpdateTimerUI();
        
        if (warningPanel)
            warningPanel.SetActive(false);
    }
    
    void Update()
    {
        if (timerRunning)
        {
            remainingTime -= Time.deltaTime;
            
            if (remainingTime <= warningTime && !warningShown)
            {
                ShowWarning();
                warningShown = true;
            }
            
            if (remainingTime <= 0)
            {
                TimeUp();
            }
            
            UpdateTimerUI();
        }
        
        // Control keys
        if (Input.GetKeyDown(KeyCode.Space))
        {
            ToggleTimer();
        }
        
        if (Input.GetKeyDown(KeyCode.R))
        {
            ResetTimer();
        }
    }
    
    public void StartTimer()
    {
        timerRunning = true;
        Debug.Log("Presentation timer started!");
    }
    
    public void StopTimer()
    {
        timerRunning = false;
        Debug.Log("Presentation timer stopped");
    }
    
    public void ToggleTimer()
    {
        timerRunning = !timerRunning;
    }
    
    public void ResetTimer()
    {
        remainingTime = presentationTime;
        timerRunning = false;
        warningShown = false;
        
        if (warningPanel)
            warningPanel.SetActive(false);
            
        UpdateTimerUI();
    }
    
    void ShowWarning()
    {
        Debug.Log("⚠️ 1 minute remaining!");
        
        if (warningPanel)
            warningPanel.SetActive(true);
    }
    
    void TimeUp()
    {
        timerRunning = false;
        remainingTime = 0;
        
        Debug.Log("⏰ Time's up!");
        
        // Visual indication
        if (timerBar)
        {
            timerBar.color = Color.red;
        }
    }
    
    void UpdateTimerUI()
    {
        if (timerText)
        {
            int minutes = Mathf.FloorToInt(remainingTime / 60);
            int seconds = Mathf.FloorToInt(remainingTime % 60);
            timerText.text = $"{minutes:00}:{seconds:00}";
        }
        
        if (timerBar)
        {
            timerBar.fillAmount = remainingTime / presentationTime;
            
            // Color coding
            if (remainingTime > warningTime)
                timerBar.color = Color.green;
            else if (remainingTime > 0)
                timerBar.color = Color.yellow;
            else
                timerBar.color = Color.red;
        }
    }
}
```

#### 3. Hodnocení a feedback (10 minut)

**Pe Review System:**
```csharp
using UnityEngine;
using System.Collections.Generic;

[System.Serializable]
public class PeerReview
{
    public string reviewerName;
    public string projectName;
    [Range(1, 5)] public int creativityScore;
    [Range(1, 5)] public int technicalScore;
    [Range(1, 5)] public int presentationScore;
    [TextArea(2, 4)] public string positives;
    [TextArea(2, 4)] public string suggestions;
}

public class PeerReviewSystem : MonoBehaviour
{
    [Header("Reviews")]
    public List<PeerReview> allReviews = new List<PeerReview>();
    
    [Header("Awards")]
    public string mostCreativeProject;
    public string bestTechnicalProject;
    public string bestPresentationProject;
    public string audienceChoiceProject;
    
    public void AddReview(PeerReview review)
    {
        allReviews.Add(review);
        Debug.Log($"Review added for {review.projectName} by {review.reviewerName}");
    }
    
    [ContextMenu("Calculate Awards")]
    public void CalculateAwards()
    {
        Dictionary<string, float> creativityScores = new Dictionary<string, float>();
        Dictionary<string, float> technicalScores = new Dictionary<string, float>();
        Dictionary<string, float> presentationScores = new Dictionary<string, float>();
        Dictionary<string, int> projectCounts = new Dictionary<string, int>();
        
        foreach (PeerReview review in allReviews)
        {
            string project = review.projectName;
            
            if (!creativityScores.ContainsKey(project))
            {
                creativityScores[project] = 0;
                technicalScores[project] = 0;
                presentationScores[project] = 0;
                projectCounts[project] = 0;
            }
            
            creativityScores[project] += review.creativityScore;
            technicalScores[project] += review.technicalScore;
            presentationScores[project] += review.presentationScore;
            projectCounts[project]++;
        }
        
        // Calculate averages and find winners
        float highestCreativity = 0;
        float highestTechnical = 0;
        float highestPresentation = 0;
        
        foreach (string project in creativityScores.Keys)
        {
            if (projectCounts[project] > 0)
            {
                float avgCreativity = creativityScores[project] / projectCounts[project];
                float avgTechnical = technicalScores[project] / projectCounts[project];
                float avgPresentation = presentationScores[project] / projectCounts[project];
                
                if (avgCreativity > highestCreativity)
                {
                    highestCreativity = avgCreativity;
                    mostCreativeProject = project;
                }
                
                if (avgTechnical > highestTechnical)
                {
                    highestTechnical = avgTechnical;
                    bestTechnicalProject = project;
                }
                
                if (avgPresentation > highestPresentation)
                {
                    highestPresentation = avgPresentation;
                    bestPresentationProject = project;
                }
            }
        }
        
        Debug.Log("=== AWARDS ===");
        Debug.Log($"Most Creative: {mostCreativeProject}");
        Debug.Log($"Best Technical: {bestTechnicalProject}");
        Debug.Log($"Best Presentation: {bestPresentationProject}");
    }
}
```

### Speciální ocenění
- **Nejkreativnější projekt**
- **Nejlepší technické řešení**
- **Nejlepší prezentace**
- **Volba publika**
- **Největší pokrok**
- **Nejvtipnější hra**

---

## Hodina 38: Reflexe a uzavření kurzu (45 minut)

### Cíle hodiny
- Zhodnotit cestu vzdělávání
- Diskutovat o budoucích plánech
- Předaj certifikáty a uzavřít kurz

### Průběh hodiny

#### 1. Reflexe kurzu (15 minut)

**Co jsme se naučili:**
- Programování v C#
- Ovládání Unity Engine
- Principy game designu
- Práce s 2D a 3D grafikou
- Audio integration
- UI/UX design
- Level design
- Project management
- Prezentační dovednost

**Diskuzní otázky:**
- Co bylo nejzajímavější?
- Co bylo nejtěžší?
- Co byste chtěli vědět víc?
- Jaké hry vás teď inspirují?

#### 2. Budoucí plány (15 minut)

**Další kroky ve vývoji her:**

**Začátečníci:**
- Vylepšete své stávající projekty
- Sledujte Unity tutoriály na YouTube
- Zkoušejte malé projekty každý týden

**Pokročilí:**
- Naučte se pokrocilé Unity funkce (Networking, VR)
- Experimentujte s jinými enginy (Unreal, Godot)
- Účastněte se game jamů

**Profesiální:**
- Studujte Computer Science nebo Game Design
- Vytvořte portfolio na itch.io
- Připojte se k indie dev komunitě

**LearningPathGuide:**
```csharp
using UnityEngine;
using System.Collections.Generic;

[System.Serializable]
public class LearningPath
{
    public string pathName;
    public int difficultyLevel; // 1-10
    public string[] prerequisites;
    public string[] skills;
    public string[] resources;
    public int estimatedWeeks;
}

public class LearningPathGuide : MonoBehaviour
{
    [Header("Available Paths")]
    public LearningPath[] learningPaths;
    
    void Start()
    {
        SetupLearningPaths();
        PrintAllPaths();
    }
    
    void SetupLearningPaths()
    {
        learningPaths = new LearningPath[]
        {
            new LearningPath
            {
                pathName = "Unity Intermediate",
                difficultyLevel = 6,
                prerequisites = new[] { "Basic C#", "Unity Basics", "Completed Course" },
                skills = new[] { "Advanced Scripting", "Custom Editors", "Optimization" },
                resources = new[] { "Unity Learn", "Brackeys YouTube", "Unity Documentation" },
                estimatedWeeks = 12
            },
            new LearningPath
            {
                pathName = "Game Artist",
                difficultyLevel = 5,
                prerequisites = new[] { "Basic Art Skills", "Unity Basics" },
                skills = new[] { "3D Modeling", "Texturing", "Animation", "Shaders" },
                resources = new[] { "Blender", "Substance Painter", "Unity ShaderGraph" },
                estimatedWeeks = 20
            },
            new LearningPath
            {
                pathName = "Game Designer",
                difficultyLevel = 7,
                prerequisites = new[] { "Unity Basics", "Level Design Basics" },
                skills = new[] { "Systems Design", "Balancing", "Analytics", "Psychology" },
                resources = new[] { "Game Design Books", "GDC Talks", "Case Studies" },
                estimatedWeeks = 16
            },
            new LearningPath
            {
                pathName = "Indie Developer",
                difficultyLevel = 9,
                prerequisites = new[] { "Programming", "Game Design", "Art Basics" },
                skills = new[] { "Business", "Marketing", "Publishing", "Community" },
                resources = new[] { "Indie Game Dev Books", "Steam", "itch.io", "Discord Communities" },
                estimatedWeeks = 52
            }
        };
    }
    
    void PrintAllPaths()
    {
        Debug.Log("=== LEARNING PATHS AFTER COURSE ===");
        
        foreach (LearningPath path in learningPaths)
        {
            Debug.Log($"\n{path.pathName} (Difficulty: {path.difficultyLevel}/10)");
            Debug.Log($"Time: ~{path.estimatedWeeks} weeks");
            Debug.Log($"Skills: {string.Join(", ", path.skills)}");
            Debug.Log($"Resources: {string.Join(", ", path.resources)}");
        }
    }
    
    public LearningPath RecommendPath(string[] currentSkills, int availableHoursPerWeek)
    {
        // Simple recommendation logic
        foreach (LearningPath path in learningPaths)
        {
            bool hasPrerequisites = true;
            foreach (string prereq in path.prerequisites)
            {
                bool hasPrereq = false;
                foreach (string skill in currentSkills)
                {
                    if (skill.Contains(prereq))
                    {
                        hasPrereq = true;
                        break;
                    }
                }
                if (!hasPrereq)
                {
                    hasPrerequisites = false;
                    break;
                }
            }
            
            if (hasPrerequisites && (path.estimatedWeeks * 3) <= availableHoursPerWeek * 52)
            {
                return path;
            }
        }
        
        return learningPaths[0]; // Default to intermediate
    }
}
```

#### 3. Certifikáty a ocenění (10 minut)

**CertificateGenerator:**
```csharp
using UnityEngine;
using System;

[System.Serializable]
public class Certificate
{
    public string studentName;
    public string courseName;
    public DateTime completionDate;
    public string[] skillsAchieved;
    public int totalHours;
    public string instructorName;
    public string specialRecognition;
}

public class CertificateGenerator : MonoBehaviour
{
    [Header("Course Info")]
    public string courseName = "Unity Game Development for Kids";
    public string instructorName = "Instructor Name";
    public int totalCourseHours = 35;
    
    [Header("Template")]
    public string certificateTemplate = @"
    ===============================================
    🏆 CERTIFICATE OF COMPLETION 🏆
    ===============================================
    
    This certifies that
    
    {STUDENT_NAME}
    
    has successfully completed the course
    
    {COURSE_NAME}
    
    comprising {TOTAL_HOURS} hours of instruction
    
    Date: {COMPLETION_DATE}
    Instructor: {INSTRUCTOR_NAME}
    
    Skills Mastered:
    {SKILLS_LIST}
    
    {SPECIAL_RECOGNITION}
    
    ===============================================
    ";
    
    public void GenerateCertificate(string studentName, string[] skills, string specialNote = "")
    {
        Certificate cert = new Certificate
        {
            studentName = studentName,
            courseName = courseName,
            completionDate = DateTime.Now,
            skillsAchieved = skills,
            totalHours = totalCourseHours,
            instructorName = instructorName,
            specialRecognition = specialNote
        };
        
        string certificate = certificateTemplate;
        certificate = certificate.Replace("{STUDENT_NAME}", cert.studentName);
        certificate = certificate.Replace("{COURSE_NAME}", cert.courseName);
        certificate = certificate.Replace("{TOTAL_HOURS}", cert.totalHours.ToString());
        certificate = certificate.Replace("{COMPLETION_DATE}", cert.completionDate.ToShortDateString());
        certificate = certificate.Replace("{INSTRUCTOR_NAME}", cert.instructorName);
        
        string skillsList = "";
        foreach (string skill in cert.skillsAchieved)
        {
            skillsList += $"    ✓ {skill}\n";
        }
        certificate = certificate.Replace("{SKILLS_LIST}", skillsList);
        
        if (!string.IsNullOrEmpty(cert.specialRecognition))
        {
            certificate = certificate.Replace("{SPECIAL_RECOGNITION}", 
                $"\n    🎆 Special Recognition: {cert.specialRecognition} 🎆\n");
        }
        else
        {
            certificate = certificate.Replace("{SPECIAL_RECOGNITION}", "");
        }
        
        Debug.Log(certificate);
        
        // Save to file if desired
        #if UNITY_EDITOR
        string filename = $"Certificate_{studentName.Replace(" ", "_")}_{DateTime.Now:yyyy-MM-dd}.txt";
        string path = System.IO.Path.Combine(Application.dataPath, "Certificates", filename);
        System.IO.Directory.CreateDirectory(System.IO.Path.GetDirectoryName(path));
        System.IO.File.WriteAllText(path, certificate);
        #endif
    }
}
```

#### 4. Uzavření (5 minut)

**Finální slova:**
- Gratulace k dokončení kurzu!
- Jste teď programátoři a game developeři
- Pokračujte v tvorbě, experimentujte
- Sdílejte své hry s přáteli a rodinou
- Nezapomeňte - každá velká hra začínala malým nápadem!

**Kontakty pro budoucí pomoc:**
- Discord server/skupina
- Email učitele
- Online komunity
- Doporučené kanály a web

### Finální inspirace
"Úroveň vaších dovedností není určena tím, co už umíte, ale tím, co jste ochotní se naučit. Pokračujte v tvorbě, zkoušejte nové věci a nebutte se bát chyb - každá chyba je příležitost se naučit něco nového!"

### Shrnutí celého kurzu
**Co jsme společně dosáhli:**
- Od úplných začátečníků po samostatné vývojáře
- Kompletní her a projektů
- Nové přátele a společné zážitky
- Základy pro životnu touhu po učení a tvorbě

**Vzpomínky na cestu:**
- První "Hello World" v Unity
- První úspěšný skok v plošinovce
- Moment kdy hra konečně fungovala
- Radost z úspěšné prezentace

**GRATULACE K ÚspĚŠNÉMU DOKONČENÍ KURZU! 🎉🎮💻**
