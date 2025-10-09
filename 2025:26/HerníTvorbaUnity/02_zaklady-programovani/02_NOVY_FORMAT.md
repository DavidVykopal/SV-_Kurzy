# Blok 2: Základy programování v C# - Demonstrační formát (3 hodiny)

## Přehled bloku
**Formát:** David kóduje live, děti sledují a navrhují
**Cíl:** Ukázat, že programování není scary, ale logické a zábavné
**Cool faktor:** Okamžitá vizuální odezva - napíšeš kód, zmáčkneš play, vidíš efekt!

---

## Hodina 11: První C# kód - "Hello World" až "Hello Movement" (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Vytvoření prvního skriptu (10 min)
**COOL MOMENT:** "Z prázdného souboru k pohybu za 10 minut!"

```csharp
// David píše live, vysvětluje každý řádek:
using UnityEngine;

public class PlayerMovement : MonoBehaviour
{
    void Start()
    {
        Debug.Log("Ahoj Unity!");  // Vidíte? Console ukáže text!
    }
}
```

**Prepare** skript na objekt → Play → zpráva v Console!
"Gratulujeme, napsali jsme první program!"

#### 2. Proměnné - "krabičky na hodnoty" (15 min)

```csharp
public class PlayerMovement : MonoBehaviour
{
    public float speed = 5f;  // "Rychlost můžeme měnit v Inspectoru!"
    
    void Update()
    {
        // David ukazuje: změním speed v Inspectoru → postava jde rychleji!
    }
}
```

**Live demo různých typů:**
- `int lives = 3;` → "Celé číslo pro životy"
- `string playerName = "Hero";` → "Text pro jméno"
- `bool isAlive = true;` → "Ano/ne pro stav"

"Vidíte? Proměnné jsou jako RPG stats pro objekty!"

#### 3. Input a pohyb (20 min)
**COOL MOMENT:** "Teď postava poslechne klávesnici!"

```csharp
void Update()
{
    // Horizontal = A/D nebo šipky
    float horizontal = Input.GetAxis("Horizontal");
    
    // Posun objektu
    transform.position += new Vector3(horizontal * speed * Time.deltaTime, 0, 0);
}
```

**Zmáčkni Play → Stiskni D → Postava se hýbe!**
"Napsali jsme OVLÁDÁNÍ!"

**Experimentování live:**
- Změň `horizontal` na `vertical` → pohyb nahoru/dolů
- Změň `speed` → různá rychlost
- Přidej `* 2` → double speed

### 👥 ZAPOJENÍ DĚTÍ
- "Jakou rychlost máme dát? 5? 10?" → hlasování
- "Co se stane když dám záporné číslo?" → predictions
- "Máme přidat skok?" → návrhy funkcí
- Děti volají směr: "Vlevo! Vpravo!" → David testuje

### 💻 CO BY DĚTI MOHLY DĚLAT
- Napsat stejný skript podle návodu
- Experimentovat s hodnotami
- Přidat svou vlastní proměnnou (např. `jumpHeight`)

---

## Hodina 12: Podmínky a logika - "Když-pak" (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. If statements - rozhodování (15 min)
**Analogie:** "Hra je jako videoh brain - musí se rozhodovat!"

```csharp
void Update()
{
    if (Input.GetKeyDown(KeyCode.Space))
    {
        Debug.Log("Skočil jsem!");
        // Později přidáme skutečný skok
    }
}
```

**Press Space → zpráva v console!**
"Tak funguje KAŽDÉ tlačítko v každé hře!"

#### 2. Else - "Jinak..." (10 min)

```csharp
if (Input.GetKey(KeyCode.W))
{
    Debug.Log("Jdu vpřed");
}
else
{
    Debug.Log("Stojím");
}
```

"IF = když děláš tohle, ELSE = když ne"

#### 3. Else if - více možností (10 min)

```csharp
if (Input.GetKey(KeyCode.W))
{
    Debug.Log("Sever!");
}
else if (Input.GetKey(KeyCode.S))
{
    Debug.Log("Jih!");
}
else if (Input.GetKey(KeyCode.A))
{
    Debug.Log("Západ!");
}
else if (Input.GetKey(KeyCode.D))
{
    Debug.Log("Východ!");
}
```

"Hra zkouší podmínky jedna po druhé!"

#### 4. Praktická aplikace - systém zdraví (10 min)
**COOL MOMENT:** "Teď přidáme životy!"

```csharp
public int health = 3;

void Update()
{
    if (Input.GetKeyDown(KeyCode.H))  // H = hit (pro test)
    {
        health = health - 1;  // Uber život
        Debug.Log("Aj! Zdraví: " + health);
        
        if (health <= 0)
        {
            Debug.Log("Game Over!");
            // Restart hry později
        }
    }
}
```

**Stiskni H třikrát → Game Over!**
"Takhle fungují životy ve VŠECH hrách!"

### 👥 ZAPOJENÍ
- "Kolik životů má mít hráč?" → diskuze o game balance
- "Co má hra udělat při smrti?" → návrhy (restart, menu, animace)
- Děti testují: "Zkus umřít! Funguje to?"

### 💻 CO BY DĚTI MOHLY DĚLAT
- Přidat health system do své hry
- Vytvořit power-up který přidá život
- Experimentovat s různým počtem životů

---

## Hodina 13: Funkce - organizace kódu (45 min)

### 🎮 CO DAVID UKAZUJE

#### 1. Problém špaget kódu (5 min)
**Ukaž špatný příklad:**

```csharp
void Update()
{
    // 100 řádků kódu všechno dohromady
    if (Input.GetKeyDown(KeyCode.Space))
    {
        rb.velocity = new Vector2(rb.velocity.x, jumpForce);
        PlaySound("jump");
        particles.Play();
        animator.SetTrigger("Jump");
        // ...CHAOS!
    }
}
```

"Tohle je nečitelné! Potřebujeme FUNKCE!"

#### 2. Vytvoření první funkce (15 min)
**Refactoring live:**

```csharp
// Vytvořím vlastní funkci:
void Jump()
{
    rb.velocity = new Vector2(rb.velocity.x, jumpForce);
    PlaySound("jump");
    particles.Play();
    animator.SetTrigger("Jump");
    Debug.Log("Skočil jsem!");
}

void Update()
{
    if (Input.GetKeyDown(KeyCode.Space))
    {
        Jump();  // Zavolám funkci!
    }
}
```

"Vidíte? Update() je teď čitelný! Jump() obsahuje detaily!"

#### 3. Funkce s parametry (15 min)
**COOL MOMENT:** "Funkce můžou přijímat vstup!"

```csharp
void TakeDamage(int damage)
{
    health = health - damage;
    Debug.Log("Au! Ztratil jsem " + damage + " životů");
    
    if (health <= 0)
    {
        Die();
    }
}

void Die()
{
    Debug.Log("Zemřel jsem!");
    // Animace smrti, restart, atd.
}

void Update()
{
    if (Input.GetKeyDown(KeyCode.Alpha1))
    {
        TakeDamage(1);  // Malé poškození
    }
    if (Input.GetKeyDown(KeyCode.Alpha3))
    {
        TakeDamage(3);  // Velké poškození!
    }
}
```

**Test:** Zmáčkni 1 → -1 život, Zmáčkni 3 → -3 životy!
"Jedna funkce, různé hodnoty!"

#### 4. Return values - funkce co vracejí hodnotu (10 min)

```csharp
bool IsAlive()
{
    return health > 0;
}

void Update()
{
    if (!IsAlive())
    {
        Debug.Log("Mrtvý, nemůžu se hýbat");
        return;  // Ukonči Update()
    }
    
    // Normální pohyb jen pokud žije
    float horizontal = Input.GetAxis("Horizontal");
    transform.position += new Vector3(horizontal * speed * Time.deltaTime, 0, 0);
}
```

"Funkce řekne ANO nebo NE → rozhoduji podle toho!"

### 👥 ZAPOJENÍ
- Děti navrhují jaké funkce vytvořit: "PowerUp()", "Shoot()", "Heal()"
- "Kolik damage má dělat nepřítel?" → čísla do parametrů
- Code review: "Je tenhle kód čitelný?"

### 💻 CO BY DĚTI MOHLY DĚLAT
- Refactorovat svůj kód do funkcí
- Vytvořit funkci `CollectCoin(int value)`
- Vytvořit funkci `Heal(int amount)`
- Organizovat kód aby byl čistý

---

## Shrnutí bloku 2

### Co děti viděly:
✅ Psaní skutečného C# kódu
✅ Proměnné a datové typy
✅ If/else podmínky
✅ Funkce a parametry
✅ Systém zdraví a damage
✅ Organizaci kódu

### Key takeaway:
**"Programování = dávání rozkazů počítači přesným jazykem"**

Každý kód má okamžitou vizuální odezvu → satisfying!

---

## Poznámky pro Davida

### Důležité:
- **Píš pomalu** - ať děti vidí každý znak
- **Komentuj v češtině** - vysvětluj co děláš
- **Test často** - každých 5 minut zmáčkni Play
- **Dělej chyby záměrně** - ukáž error, ukaž opravu
- **Celebrate small wins** - "Funguje to! Úspěch!"

### Troubleshooting:
- Syntax error? → "Vidíte? Zapomněl jsem středník! Počítač je přesný!"
- NullReference? → "Zapomněl jsem přiřadit proměnnou!"
- Nefunguje? → "Debug.Log na rescue!" → troubleshoot live

### Live coding tips:
1. **Příprava:** Test všechen kód před hodinou
2. **Backup:** Měj prepared skripty ready pokud live coding selže
3. **Speed:** Lidem nestíhají sledovat rychlé psaní - JDI POMALU
4. **Font size:** VELKÉ písmo aby všichni viděli!

