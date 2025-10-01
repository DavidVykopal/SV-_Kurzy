# 00c: Prezentace - Vibe coded – webové mini-hry

## Struktura prezentace (15 slidů)

### Slide 1: Titulní slide
- **Název**: Vibe coded – webové mini-hry
- **Podtitul**: Rychlý vznik malé webové hry v prohlížeči
- **Datum**: Říjen 2025
- **Lektor**: [Jméno]

### Slide 2: Cíle hodiny
- Ukázat rychlý vznik malé webové hry v prohlížeči
- Pochopit vstup, vykreslení a jednoduchý stav hry
- Porovnat web vs. Unity/Roblox
- Vytvořit reakční hru v HTML/JS

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

### Slide 7: Mini-hra: Reakční hra
- **Cíl**: Změřit reakční čas hráče
- **Mechanika**:
  - Tlačítko Start
  - Náhodné zpoždění
  - Změřit reakční čas
  - Zobrazit skóre
- **Čas**: 25-30 minut

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

### Slide 11: Rozšíření: Top 3 výsledky
- Uložení nejlepších výsledků
- Zobrazení leaderboardu
- Jednoduchá grafika
- **Čas**: 10 minut

### Slide 12: Praktická část - Reakční hra
- Otevřít editor kódu
- Vytvořit HTML/JS skeleton
- Implementovat reakční hru
- **Čas**: 20 minut

### Slide 13: Praktická část - Rozšíření
- Přidat top 3 výsledky
- Vylepšit grafiku
- Otestovat hru
- **Čas**: 10 minut

### Slide 14: Krátká reflexe
- Co bylo nejtěžší?
- Jaké možnosti nabízí web?
- Kdy byste použili web vs. Unity?
- **Čas**: 5 minut

### Slide 15: Domácí úkol a příště
- **Domácí úkol**: Přidat skóre/časovač a poslat screenshot/link
- **Příště**: 00d - Společné hraní a analýza her
- Herní business a pozice v gamingu
- Typy her a enginy
