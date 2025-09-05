# Blok 5: Základy 3D (17–19)

## Přehled bloku
**Cíl:** Přechod z 2D do 3D prostředí, naučit základy 3D modelování a navigace.
**Výstup:** Základní 3D scéna s pohyblivou postavou a interaktivními objekty.

---

## Hodina 17: Navigace v 3D (45 minut)

### Cíle hodiny
- Pochopit rozdíl mezi 2D a 3D prostředím
- Naučit se navigaci ve 3D scéně
- Ovládat 3D kameru

### Materiály
- Nový Unity projekt (3D template)
- Základní 3D objekty (Unity primitives)

### Průběh hodiny

#### 1. Rozdíl mezi 2D a 3D (10 minut)

**2D vs 3D:**
- **2D:** X, Y souradnice (levy-pravy, nahoru-dolu)
- **3D:** X, Y, Z souradnice (levy-pravy, nahoru-dolu, dopredu-dozadu)

**Transform v 3D:**
- **Position:** X, Y, Z pozice
- **Rotation:** X, Y, Z rotace (Euler angles)
- **Scale:** X, Y, Z velikost

**Praktická ukázka:**
1. Vytvoříme nový 3D projekt
2. Přidáme Cube do scény
3. Meníme Transform hodnoty
4. Pozorujeme rozdíly

#### 2. Navigace ve Scene view (10 minut)

**Základní ovládání:**
- **Pravé tlačítko + pohyb myši:** Otočení kamery
- **Střední tlačítko + pohyb myši:** Posun kamery
- **Kolečko myši:** Přiblížení/Oddálení
- **F klávesa:** Zaměření na vybraný objekt
- **Alt + levé tlačítko:** Orbit kolem objektu

**Nástroje pro pohyb:**
- **Q:** Hand tool (posun scény)
- **W:** Move tool (posun objektu)
- **E:** Rotate tool (otočení objektu)
- **R:** Scale tool (velikost objektu)

#### 3. Gizmos a coordinates (10 minut)

**Koordinátní systém Unity:**
- **X osa:** Červená (levy-pravy)
- **Y osa:** Zelená (nahoru-dolu)
- **Z osa:** Modrá (dopredu-dozadu)

**Global vs Local souradnice:**
- **Global:** Vztazené k celemu svetu
- **Local:** Vztazené k objektu samému

**Praktické cvičení:**
1. Přidáme několik Cubeů
2. Rozmistíme je v prostoru
3. Zkoušíme různé nástroje
4. Meníme mezi Global/Local módy

#### 4. 3D kamera (15 minut)

**Vlastnosti 3D kamery:**
- **Field of View:** Úhel záběru (60° standard)
- **Near/Far Clipping Plane:** Co kamera vidí
- **Projection:** Perspective vs Orthographic

**Základní kamerový skript:**
```csharp
using UnityEngine;

public class ZakladniKamera : MonoBehaviour
{
    [Header("Nastavení kamery")]
    public float rychlostPohybu = 5f;
    public float citlivostMysi = 2f;
    
    private float rotaceX = 0f;
    
    void Start()
    {
        // Zamknout kurzor na střed obrazovky
        Cursor.lockState = CursorLockMode.Locked;
    }
    
    void Update()
    {
        // Pohyb kamery
        PohybKamery();
        
        // Otaceni kamery mysi
        OtaceniKamery();
    }
    
    void PohybKamery()
    {
        float h = Input.GetAxis("Horizontal"); // A,D keys
        float v = Input.GetAxis("Vertical");   // W,S keys
        
        Vector3 smer = transform.right * h + transform.forward * v;
        transform.position += smer * rychlostPohybu * Time.deltaTime;
    }
    
    void OtaceniKamery()
    {
        float mouseX = Input.GetAxis("Mouse X");
        float mouseY = Input.GetAxis("Mouse Y");
        
        // Horizontalní otočení (Y osa)
        transform.Rotate(0, mouseX * citlivostMysi, 0);
        
        // Vertikální otočení (X osa)
        rotaceX -= mouseY * citlivostMysi;
        rotaceX = Mathf.Clamp(rotaceX, -90, 90);
        Camera.main.transform.localRotation = Quaternion.Euler(rotaceX, 0, 0);
    }
    
    void OnApplicationFocus(bool hasFocus)
    {
        if (hasFocus)
        {
            Cursor.lockState = CursorLockMode.Locked;
        }
        else
        {
            Cursor.lockState = CursorLockMode.None;
        }
    }
}
```

### Úkol pro děti
Vytvořte 3D "stavbeničku" - rozmistěte různé 3D objekty (kostky, koule, válce) ve scéně a naučte se v ní pohybovat.

---

## Hodina 18: Práce s objekty, fyzika (45 minut)

### Cíle hodiny
- Naučit se pracovat se základními 3D objekty
- Pochopit 3D fyziku v Unity
- Vytvořit interaktivní 3D scénu

### Průběh hodiny

#### 1. Základní 3D objekty (10 minut)

**Unity Primitives:**
- **Cube:** Základní kostka
- **Sphere:** Koule
- **Cylinder:** Válec
- **Capsule:** Tobolka (pro postavy)
- **Plane:** Rovinná plocha
- **Quad:** Čtvercová plocha

**Vytváření objektů:**
1. Pravý klik v Hierarchy
2. 3D Object → vybereme tvar
3. Nastavíme pozici, rotaci, velikost

#### 2. Materiály a textury (10 minut)

**Co jsou materiály:**
Materiály určují, jak objekt vypadá (barva, lesk, průhlednost).

**Vytvoření materiálu:**
1. Pravý klik v Project → Create → Material
2. Pojmenujeme (např. "Cerveny_Material")
3. V Inspector měníme Albedo (barvu)
4. Přetažením na objekt aplikujeme

**Základní vlastnosti materiálu:**
- **Albedo:** Základní barva
- **Metallic:** Kovový vzhled
- **Smoothness:** Hladkost povrchu
- **Emission:** Světělo ze sebe

#### 3. 3D fyzika (15 minut)

**Rigidbody v 3D:**
Stejné principy jako 2D, ale se 3 rozměry.

```csharp
using UnityEngine;

public class FyzikaObjekt : MonoBehaviour
{
    [Header("Síla")]
    public float silaSskoku = 500f;
    public float silaPohybu = 10f;
    
    private Rigidbody rb;
    
    void Start()
    {
        rb = GetComponent<Rigidbody>();
    }
    
    void Update()
    {
        // Pohyb pomocí WASD
        float h = Input.GetAxis("Horizontal");
        float v = Input.GetAxis("Vertical");
        
        Vector3 pohyb = new Vector3(h, 0, v) * silaPohybu;
        rb.AddForce(pohyb);
        
        // Skok pomocí mezerníku
        if (Input.GetKeyDown(KeyCode.Space))
        {
            rb.AddForce(Vector3.up * silaSskoku);
        }
    }
}
```

**Colliders v 3D:**
- **Box Collider:** Pro kostky
- **Sphere Collider:** Pro koule
- **Capsule Collider:** Pro postavy
- **Mesh Collider:** Pro složité tvary

#### 4. Jednoduchá 3D scéna (10 minut)

**Vytvoření playground:**
1. **Podlaha:** Plane se Scale (10, 1, 10)
2. **Stěny:** Kostky jako hranice
3. **Rampy:** Rotované kostky
4. **Pohyblivé objekty:** S Rigidbody
5. **Hráč:** Capsule s pohybovým skriptem

**Organizace scény:**
```
Level_Playground
├── Environment
│   ├── Floor
│   ├── Walls
│   └── Ramps
├── Player
└── InteractiveObjects
    ├── MovingCubes
    └── Collectibles
```

### Úkol pro děti
Vytvořte 3D "parkúr" – scénu s různými překážkami, kterými může projízdět nebo proskakovat pohyblivý objekt.

---

## Hodina 19: První 3D scéna (45 minut)

### Cíle hodiny
- Integrovat všechny naučené prvky
- Vytvořit kompletní 3D scénu s cílem
- Přidat osvětlení a atmosféru

### Průběh hodiny

#### 1. Plánování 3D scény (10 minut)

**Typy 3D scén pro začátečníky:**
- **Sbíratel:** Sběr předmětů v labyřintu
- **Parkour:** Doskočení z bodu A do bodu B
- **Puzzle:** Přesun objektů na správná místa
- **Závodní:** Projízdka trasou co nejrychleji

**Plánování na papir:**
1. Nakreslíte půdorys scény shora
2. Označte start a cíl
3. Přidejte překážky a zajimavosti

#### 2. Level design v 3D (15 minut)

**Základy 3D level designu:**
- **Orientace:** Hráč musí vedět, kam má jit
- **Landmarks:** Výrazné objekty pro orientaci
- **Rhythm:** Stridaní akce a odpockinku
- **Verticalita:** Využití výšky prostoru

**Praktické tipy:**
```csharp
using UnityEngine;

public class Checkpoint : MonoBehaviour
{
    public Transform respawnPoint;
    public ParticleSystem aktivacniEfekt;
    
    private void OnTriggerEnter(Collider other)
    {
        if (other.CompareTag("Player"))
        {
            // Nastav checkpoint
            GameManager gm = FindObjectOfType<GameManager>();
            if (gm != null)
            {
                gm.NastavCheckpoint(respawnPoint.position);
            }
            
            // Efekt
            if (aktivacniEfekt != null)
            {
                aktivacniEfekt.Play();
            }
            
            Debug.Log("Checkpoint aktivován!");
        }
    }
}
```

#### 3. Osvětlení (10 minut)

**Typy světla v Unity:**
- **Directional Light:** Slunce (nekonecná vzdalnost)
- **Point Light:** Žárovka (svíti všemi směry)
- **Spot Light:** Reflektor (kuzel světla)
- **Area Light:** Plošné světlo

**Základní nastavení osvětlení:**
1. Directional Light pro obecné osvětlení
2. Point Lights pro zajimavá místa
3. Nastavení barvy a intensity

**Atmosféra pomocí světla:**
- Teplé barvy (zlutá, oranžová) = příjemné
- Studené barvy (modrá, fialová) = mysteriosní
- Stíny vytvářejí hloubku

#### 4. Dokoncení a testování (10 minut)

**Finalni úpavy scény:**
1. Testování plynného pohybu
2. Kontrola kolizí
3. Nastavení cíle/výhernych podmínek
4. Přidání zvuků a efektů

**Game Manager pro 3D scénu:**
```csharp
using UnityEngine;
using UnityEngine.SceneManagement;

public class GameManager3D : MonoBehaviour
{
    [Header("Nastavení hry")]
    public Transform startPoint;
    public Transform goalPoint;
    public float casNaLevel = 60f;
    
    private Vector3 checkpointPozice;
    private float zbyvajiciCas;
    
    void Start()
    {
        checkpointPozice = startPoint.position;
        zbyvajiciCas = casNaLevel;
    }
    
    void Update()
    {
        // Odpocet casu
        zbyvajiciCas -= Time.deltaTime;
        
        if (zbyvajiciCas <= 0)
        {
            GameOver();
        }
    }
    
    public void NastavCheckpoint(Vector3 novaPozice)
    {
        checkpointPozice = novaPozice;
    }
    
    public void RespawnHrace()
    {
        GameObject hrac = GameObject.FindGameObjectWithTag("Player");
        if (hrac != null)
        {
            hrac.transform.position = checkpointPozice;
            Rigidbody rb = hrac.GetComponent<Rigidbody>();
            if (rb != null)
            {
                rb.velocity = Vector3.zero;
            }
        }
    }
    
    public void Vyhra()
    {
        Debug.Log("Gratuluji! Vyhrál jsi!");
        Time.timeScale = 0f;
    }
    
    void GameOver()
    {
        Debug.Log("Cas vyprsel!");
        SceneManager.LoadScene(SceneManager.GetActiveScene().buildIndex);
    }
}
```

### Prezentace
Každý žák ukáže svou 3D scénu a vysvetli, jaké výzvy při jejím vytváření řešil.

### Shrnutí bloku
**Čeho jsme dosáhli:**
- Porozumění 3D prostředí a navigace
- Základy 3D fyziky a kolizí
- Tvorbu materiálů a osvětlení
- Kompletní funkční 3D scénu

**Připravili jsme se na:**
- Tvorbu FPS hry
- Složitější 3D mechaniky
- Pokrocilé kamerové systémy
