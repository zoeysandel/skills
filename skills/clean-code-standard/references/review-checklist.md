# Review volgens de clean code standard

Gebruik dit bij een review van een PR, een map of een codebase. Het doel is een oordeel dat iemand kan gebruiken om de code te verbeteren, niet een opsomming van alles wat opvalt.

## Stappen

Controleer eerst correctheid en regressierisico aan de hand van de diff, relevante aanroepers en bestaande tests. Gebruik daarvoor de beschikbare Codex-tools; een Claude-slashcommand is niet nodig. Pas daarna deze checklist voor kwaliteit en structuur toe.

1. Bepaal de scope. Een PR: `git diff --stat <base>...HEAD` en `git log --oneline <base>..HEAD`. Een map: alle files die git volgt (`git ls-files`), plus wat ignored maar aanwezig is als het tussen de code staat. Sla code over die aantoonbaar een ongewijzigde kopie van een externe bron is, en zeg dat.
2. Maak een inventaris. Per file: regels, en in een regel wat erin staat (klassen, functies, waar hij door wordt aangeroepen). Een AST-outline (docstring, functies en klassen met regelbereik) is daarvoor sneller dan elke file helemaal lezen. Lees daarna de files die verdacht zijn helemaal.
3. Classificeer elke file: kern, test, eenmalige verkenning, dubbel of dood (door niets aangeroepen behalve zijn eigen test).
4. Loop de checklist hieronder door. Noteer bij elke bevinding `file:regel`, het probleem in een zin, en het gevolg of de oplossing.
5. Verifieer de ernstigste bevindingen zelf, door de code te lezen of iets te draaien. Zeg per bevinding of hij gelezen, gedraaid of alleen vermoed is.
6. Schrijf het rapport volgens het format onderaan.

Bij een grote scope kun je per principe een aparte subagent inzetten (codekwaliteit, leesbaarheid, best practices, duplicatie, logica, structuur, AI slop). Geef ze de code en niet je eigen conclusies, zodat ze onafhankelijk kijken. Wat twee agents los van elkaar vinden, weegt zwaarder.

## Checklist

### Evals en controles (ernstigst, want hier hangt vertrouwen aan)
- Kan een eval of controle groen geven bij lege of ontbrekende invoer?
- Vallen regels stil weg, bijvoorbeeld doordat ze als dict-sleutel samenvallen?
- Is er per eval een test die laat zien dat hij een bekende fout vangt, en wordt die afgedwongen?
- Kan een controle door de opzet nooit falen?
- Geeft het programma een exit-code ongelijk aan 0 bij een fout?
- Zeggen de README en docstrings hetzelfde als de code (bijvoorbeeld de tolerantie)?

### Fouten en robuustheid
- Rijen of waarden die stil worden overgeslagen.
- Kolommen op positie in plaats van op kopnaam.
- Kale `except`, `except: pass`.
- Magische getallen, vaste klant-, jaar- of datumwaarden, harde paden.
- Delen door iets dat nul kan zijn, `None` in een som.
- Shell zonder `set -euo pipefail`.

### Namen en leesbaarheid
- Werklabels, personen of sessiestappen als naam of in docstrings.
- Cryptische afkortingen, posities in plaats van veldnamen.
- Meerdere statements per regel, functies op één regel.
- Taal door elkaar binnen een file of map.
- Testnamen die niet zeggen wat ze afdekken.

### OOP, ICE en SOLID
- Begrippen die als losse dicts of tuples rondgaan in plaats van als klasse.
- Externe systemen zonder eigen interface, formaatkennis verspreid over files.
- Functies of files met meer dan één verantwoordelijkheid (signaal: functie langer dan een scherm, file langer dan 200 regels).
- Varianten via `if`-takken op strings in plaats van eigen klassen.
- Kern die direct van een bestand of tool afhangt in plaats van een interface.

### DRY
- Dezelfde helper of parser meerdere keren, en of de kopieën al verschillend gedrag hebben (dat is een bug, geen stijl).
- Gekopieerde testfixtures.
- Overlappende modules die dezelfde controles doen met andere toleranties.

### Structuur en omvang
- Mappen die op persoon, sessie of nummer zijn geordend in plaats van op verantwoordelijkheid.
- Code, invoer en uitvoer in dezelfde map. Uitvoer die buiten `.gitignore` kan landen.
- `sys.path`-hacks, geneste packages met dezelfde naam (`r10/r10`).
- Tests verspreid zonder één commando dat ze allemaal draait.
- Verkenningsscripts die als blijvende code zijn gecommit.
- PR-omvang: hoeveel files en regels, en is hij in logische stukken te splitsen?

### AI slop
- Docstrings met sessiesporen ("Stap 2"), commentaar dat de geschiedenis vertelt.
- Achtergebleven hypotheses of varianten die bij elke run nog worden berekend.
- Ongebruikte imports, functies, parameters of uitvoersleutels.
- Met de hand overgetypte resultaten in een README, correctiecommits op getallen.
- Code voor gevallen die niet kunnen voorkomen, opties die niemand gebruikt.

## Rapport

Schrijf in de taal van de gebruiker. Houd het compact.

1. Oordeel in twee zinnen: wat is goed, wat is het grootste probleem.
2. Inventaris als tabel: file, regels, wat erin staat, classificatie.
3. Bevindingen per thema, ernstigste eerst. Per bevinding `file:regel`, het probleem, het gevolg, en of het gelezen, gedraaid of vermoed is. Begin met alles wat een eval of controle onbetrouwbaar maakt.
4. Wat goed is. Noem het concreet, zodat het behouden blijft.
5. Voorstel: een filetree van hoe het eruit moet zien volgens de structuur in SKILL.md, met per file een regel uitleg, en wat er met elke huidige file gebeurt (opgaan in, archief, weg). Bij een te grote PR: een voorstel om te splitsen, met files per PR en een volgorde.
6. Vragen voor de gebruiker, alleen waar een keuze echt bij hen ligt.
