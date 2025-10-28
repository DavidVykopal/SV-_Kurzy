# 00c: Prezentace - Vibe coding – HTML5 ukázka + Blockly Games

## Struktura prezentace (15 slidů)

### Slide 1: Titulní slide
- **Název**: Vibe coding – HTML5 ukázka + Blockly Games
- **Podtitul**: Demo + trénink logiky v JavaScriptu (bloky)
- **Datum**: Říjen 2025
- **Lektor**: [Jméno]

### Slide 2: Cíle hodiny
- Vidět krátkou ukázku HTML5 mini‑hry (jen demo)
- Procvičit programovací logiku přes Blockly Games
- Pochopit základy JS: sekvence, podmínky, cykly, funkce
- Spolupracovat v párech (pair programming)

### Slide 3: Program hodiny (agenda)
- 5–10 min: HTML5 vibe coding (demo)
- 30–40 min: Blockly Games – Maze → Bird/Turtle
- 3–5 min: Sdílení a reflexe

### Slide 4: HTML5 vibe coding – co uvidíte (demo)
- Vstup (eventy), stav hry, vykreslení na canvas
- Herní smyčka `requestAnimationFrame`
- Bez samostatné práce žáků – jen rychlá ukázka

### Slide 5: Herní smyčka v prohlížeči (princip)
```javascript
function gameLoop() {
    handleInput();      // 1) vstup
    updateGame();       // 2) update stavu
    render();           // 3) vykreslení
    requestAnimationFrame(gameLoop); // 4) opakování
}
```

### Slide 6: Proč Blockly Games?
- Vizuální bloky → méně chyb v syntaxi, více pozornosti na logiku
- Okamžitá zpětná vazba a rostoucí obtížnost
- Možnost zobrazit vygenerovaný JavaScript

### Slide 7: Blockly Games – Maze (Labyrint)
- Cíl: dovést postavu k cíli nejkratší logickou sekvencí
- Ovládání: šipky/otočení, kroky, cykly
- Odkaz: `https://blockly.games/maze`

### Slide 8: Maze – tipy a strategie
1) Začněte sekvencí kroků
2) Zkraťte řešení pomocí `repeat`
3) Přidejte `if` pro rozcestí
4) Optimalizujte: méně bloků, čitelnější řešení

### Slide 9: Blockly Games – Bird (Pták)
- Cíl: proletět checkpointy správným načasováním
- Klíčové bloky: `if` podmínky, změna výšky
- Odkaz: `https://blockly.games/bird`

### Slide 10: Blockly Games – Turtle (Želva)
- Cíl: kreslit tvary pomocí pohybů a otáčení
- Klíčové bloky: `repeat`, úhly, někdy proměnné
- Odkaz: `https://blockly.games/turtle`

### Slide 11: Postup ve třídě
- Začneme Maze level 1–7; rychlejší → 8–10
- Poté Bird 1–5, případně Turtle 1–5
- Kdo skončí dřív: zkouší optimalizovat řešení (méně bloků)

### Slide 12: Pair programming
- Role: Řidič (ovládá myš/klávesnici) a Navigátor (radí, kontroluje)
- Střídání rolí po 5–7 minutách nebo po levelu

### Slide 13: Sdílení a reflexe
- Ukázka různých řešení na projektoru
- Zapněte „Zobrazit JavaScript“ a podívejme se, jak vypadají bloky v kódu
- Co bylo nejtěžší/nejzajímavější?

### Slide 14: Domácí úkol
- Dokončit rozpracované levely (Maze/Bird/Turtle)
- Poslat screenshot nejlepšího řešení
- Volitelně: Zobrazit JavaScript a opsat krátký úryvek do sešitu

### Slide 15: Příště
- 00d – Společné hraní a analýza her, herní business
