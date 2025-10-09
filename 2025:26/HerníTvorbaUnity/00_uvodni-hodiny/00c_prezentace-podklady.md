# 00c: Prezentace - Vibe coded – webové mini-hry

## Struktura prezentace (15 slidů)

### Slide 1: Titulní slide
- **Název**: Vibe coded – webové mini-hry
- **Podtitul**: Rychlý vznik malé webové hry v prohlížeči
- **Datum**: Říjen 2025
- **Lektor**: [Jméno]

### Slide 2: Cíle hodiny
- Vidět demonstraci rychlého vzniku webové hry
- Pochopit koncepty: vstup, vykreslení, stav hry
- Porovnat výhody a nevýhody web vs. Unity/Roblox
- Sledovat tvorbu reakční hry v HTML/JS
- Získat přehled o webových herních technologiích

### Slide 3: Web vs. Unity/Roblox – kdy co použít?
- **Web**: Rychlé prototypy, jednoduché hry, okamžitý přístup
- **Unity**: Komplexní 3D hry, mobilní hry, profesionální vývoj
- **Roblox**: Vizuální programování, multiplayer, sociální aspekty

### Slide 4: Showcase: Minecraft projekt z workshopu
- **Ukázka vlastního Minecraft projektu**
- Spuštění na lokální síti pro multiplayer
- Demonstrace možností webových her
- **Čas**: 10-15 minut

### Slide 5: HTML/JS skeleton
- **Canvas element** pro vykreslování
- **requestAnimationFrame** pro herní smyčku
- **Event listeners** pro vstup
- Základní struktura projektu

### Slide 6: Herní smyčka v prohlížeči
```javascript
function gameLoop() {
    // 1. Input handling
    handleInput();
    
    // 2. Update game state
    updateGame();
    
    // 3. Render
    render();
    
    // 4. Continue loop
    requestAnimationFrame(gameLoop);
}
```

### Slide 7: Mini-hra: Reakční hra - design
- **Cíl**: Změřit reakční čas hráče
- **Mechanika**:
  - Tlačítko Start
  - Náhodné zpoždění (`setTimeout`)
  - Změřit reakční čas (`Date.now()`)
  - Zobrazit skóre
- **Demonstrace**: Lektor programuje live s vysvětlením

### Slide 8: Reakční hra - algoritmus
1. Tlačítko "Start" → změnit na "Čekej..."
2. Náhodné zpoždění (1-5 sekund)
3. Změnit na "KLIKNI!" + změřit čas
4. Čekat na kliknutí
5. Vypočítat reakční čas
6. Zobrazit výsledek

### Slide 9: Reakční hra - HTML struktura
```html
<!DOCTYPE html>
<html>
<head>
    <title>Reakční hra</title>
    <style>
        #gameCanvas { border: 1px solid black; }
        #startBtn { font-size: 20px; padding: 10px; }
    </style>
</head>
<body>
    <canvas id="gameCanvas" width="400" height="300"></canvas>
    <br>
    <button id="startBtn">Start</button>
    <div id="score">Reakční čas: --</div>
</body>
</html>
```

### Slide 10: Reakční hra - JavaScript logika
```javascript
let gameState = 'waiting';
let startTime = 0;

document.getElementById('startBtn').onclick = function() {
    if (gameState === 'waiting') {
        startGame();
    } else if (gameState === 'ready') {
        measureReaction();
    }
};

function startGame() {
    gameState = 'ready';
    this.textContent = 'Čekej...';
    
    setTimeout(() => {
        this.textContent = 'KLIKNI!';
        startTime = Date.now();
    }, Math.random() * 4000 + 1000);
}
```

### Slide 11: Rozšíření: Top 3 výsledky - teorie
- **LocalStorage API**: Ukládání dat v prohlížeči
- Struktura dat pro leaderboard (array of objects)
- Řazení výsledků (`.sort()`)
- **Demonstrace**: Ukázka přidání leaderboardu

### Slide 12: Live coding - Reakční hra
- **Lektor programuje**: HTML struktura
- Přidání CSS stylů
- JavaScript logika krok po kroku
- **Interaktivní**: Děti navrhují vylepšení

### Slide 13: Společné testování
- **Dobrovolníci**: Zkusit hru na projekci
- Srovnání reakčních časů
- **Diskuse**: Co by se dalo vylepšit?
- Nápady na další webové hry

### Slide 14: Reflexe a porovnání platfo
- **Diskuse**: Co bylo nejtěžší/nejzajímavější?
- **Porovnání platforem**:
  - Web: rychlé, dostupné, limitované
  - Unity: výkonné, profesionální, složitější
  - Roblox: sociální, jednoduché, limitované
- Kdy použít kterou platformu?

### Slide 15: Domácí úkol a příště
- **Domácí úkol**: Navrhnout na papír vlastní webovou hru
  - Mechaniky, UI layout, herní smyčka
  - Nakreslit mockup rozhraní
- **Volitelně**: Zkusit upravit ukázkovou hru doma
- **Příště**: 00d - Společné hraní a analýza her, herní business
