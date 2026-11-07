---
name: clean-code-standard
description: De codestandaard van Zoey voor code die Codex bouwt of reviewt. OOP, TDD, SOLID, DRY en ICE, namen die zeggen wat iets doet, een mappenstructuur die je zonder uitleg snapt, en evals die aantoonbaar werken. Gebruik deze skill altijd voordat je code schrijft, een script of tool bouwt, een eval of test opzet, code herstructureert, of een PR of codebase reviewt, ook als de gebruiker de standaard niet noemt. Triggers - bouw dit, schrijf een script, maak een eval, review deze PR, review deze code, ruim dit op, herstructureer, is dit goede code, wat vind je van deze map.
---

# Clean code standard

Code wordt vaker gelezen dan geschreven. De lezer is een collega, de klant of jijzelf over drie maanden, en die kent de werksessie niet waarin de code ontstond. Alles in deze skill volgt uit die ene vraag: kan iemand die er niet bij was een file openen en binnen een paar minuten snappen wat hij doet en waarom?

## Twee modi

- Bouwen: lees de principes hieronder, maak eerst de filetree inzichtelijk (zie "Werkwijze bij bouwen"). Werk zelfstandig door als de gebruiker de uitvoering al heeft geautoriseerd; vraag alleen akkoord bij een wezenlijke open structuurkeuze.
- Reviewen: volg `references/review-checklist.md`. Dat bestand bevat de stappen, de checklist per principe en het format van het rapport.

Gebruik `references/voorbeelden.md` als je twijfelt hoe iets eruit moet zien. Daar staan slechte en goede versies naast elkaar.

## Principes

### Namen zeggen wat iets doet

Een naam is een beschrijving, geen verwijzing. `duo_export_checks.py` legt zichzelf uit, `r10/` werkt alleen voor wie de lijst kent waar het naar verwijst.

- Geen interne werklabels als map-, file- of functienaam: geen regelnummers (`r8`, `k05`), geen personen (`sil/`), geen sessiestappen ("Stap 3" in een docstring). Een werklabel mag in een README-tabel naast de echte naam, zodat het verband vindbaar blijft.
- Geen cryptische afkortingen (`mA`, `rep`, `C`, `L`, `a` voor args, `r2` voor afronden, `kpl` voor cost centre).
- Een naam zegt ook voor welk formaat of welke bron iets is: `parse_dutch_amount`, niet `parse_amount`; `from_duo_period_column`, niet `from_duo_text`; `is_empty_cell`, niet `is_blank`.
- Tests: de klasse noemt de unit (`TestParseDutchAmount`), de test heet `test_<situatie>_<verwachte uitkomst>`, bijvoorbeeld `test_empty_cell_raises_value_error` of `test_date_before_start_returns_zero`. Bij een falende test zie je zo meteen welke situatie misging en wat er verwacht werd. `test_k03` of klasse `T` zegt niets.
- Alles in de code is Engels: namen, docstrings, commentaar en testnamen. Er werkt een Engelstalig team (Filipijnen) mee, dus Nederlands in code sluit lezers uit. Neem de Engelse termen uit de vocabulaire van de klant (`0-identity/vocabulary.md` als die er is). Nederlands staat alleen in stringconstanten die een externe bron letterlijk zo schrijft, zoals een kolomkop van DUO of een tabbladnaam in Excel. De README heeft een vertaaltabel van code-term naar de Nederlandse term die de klant gebruikt.

### OOP en ICE: Isolate, Contain, Encapsulate

Elk begrip krijgt één klasse die zijn eigen regels bewaakt. Een beschikking weet zelf hoe lang hij loopt, een AFAS-mutatie kent zelf de tekenafspraak. Losse functies die dicts doorgeven met posities als `t[0]` tot `t[3]` worden een dataclass met veldnamen.

- Isolate: elk extern systeem (een API, een Excel-model, een CSV-export, AFAS) zit achter een eigen interface aan de rand. De kern weet niet of data uit een bestand of een API komt.
- Contain: kennis over een formaat, een encoding of een tekenafspraak staat op precies één plek. Lekt `cp850` of "baten staan met een min" naar vijf files, dan is het niet contained.
- Encapsulate: een klasse laat zijn bedoeling zien, niet zijn opslag. Andere code vraagt `decision.months_in_year(2026)`, niet `(eind - begin).days // 30`.

### SOLID, zoals het hier telt

- Single responsibility: een file doet één ding, een functie doet één ding. Een `main()` die inleest, rekent, scoort en wegschrijft is vier functies. Richtlijn: een functie past op een scherm (zo'n 30 regels), een file blijft onder de 200 regels. Groeit een file erboven, dan zitten er meestal twee verantwoordelijkheden in.
- Open/closed: een nieuwe variant komt erbij als nieuwe klasse, niet als extra `if mutant == "..."` in bestaande code.
- Liskov: elke implementatie van een interface is echt uitwisselbaar. Een tweede engine of databron levert hetzelfde contract.
- Interface segregation: kleine interfaces. Een eval die alleen boekregels nodig heeft, krijgt geen hele workbook.
- Dependency inversion: de kern hangt af van een `Protocol` (`SubsidyEngine`, `AfasMutationSource`), de concrete implementatie wordt van buiten meegegeven. Zo kan een export later een live koppeling worden zonder dat de kern verandert.

### Een module groepeert op onderwerp, niet op wie hem gebruikt

Liever een map dan een voorvoegsel: `formats/dutch_notation.py` en `formats/spreadsheet_cells.py`, niet `dutch_formats.py` naast `spreadsheet_formats.py`. Elke map krijgt in zijn `__init__.py` een docstring die in een regel per file zegt wat erin staat, zodat je de map kunt lezen zonder alle files te openen.

Eén onderwerp, één bestand. Twee bestanden met bijna dezelfde naam over hetzelfde (`reference-run-skor.json` naast `f2-reference-run-skor.md`) laten de lezer raden welke de bron is. Voeg ze samen. Een machineleesbare variant komt er pas als code hem leest, en heet dan hetzelfde als de notitie, met hetzelfde voorvoegsel.

Een functie staat in de module over het onderwerp waar hij over gaat. `is_empty_cell` gaat over CSV- en Excel-cellen, dus hoort in `spreadsheet_cells.py`, ook al gebruiken alleen de Nederlandse parsers hem. Stel bij elke functie de vraag: als ik de modulenaam lees, verwacht ik deze functie hier?

### DRY

Elk stuk kennis bestaat één keer. Twee kopieën lopen altijd uit elkaar: in de harness gaf de ene `xl_dec` `None` terug en de andere `0`, en de ene parser haalde het duizendtalpunt weg en de andere niet.

- Parsers, normalisatie, toleranties en constanten staan op één plek en worden geïmporteerd.
- Testdata bouw je met gedeelde builders (`DecisionBuilder`), niet met gekopieerde fixtures per testfile.
- Zie je jezelf iets voor de tweede keer schrijven, zoek dan eerst of het al bestaat.

DRY gaat over kennis, niet over toevallig gelijke regels. Twee dingen die nu hetzelfde lijken maar om verschillende redenen veranderen, mogen apart blijven.

### TDD

Schrijf bij nieuw gedrag en bugfixes de test eerst, op verzonnen data, en laat hem falen voordat je de code schrijft. Voor omkeerbare wijzigingen met weinig impact, zoals tekst of metadata, volstaat passende directe validatie; voeg geen tests toe die alleen de implementatie herhalen. De test beschrijft het gedrag in de taal van het domein. Daarna de kleinste code die hem groen maakt, daarna opruimen.

- Bouw van binnen naar buiten: parsing, domein, readers, services, evaluatie, cli. Elke laag is getest voordat de volgende erop leunt.
- Een test die echte klantdata nodig heeft, staat apart (`tests/client_data/`) en draait alleen met een expliciete vlag. Zonder die vlag meldt hij "overgeslagen", hij telt nooit als geslaagd.
- Bij een refactor van bestaande code: leg eerst de huidige uitkomsten vast als regressietest, verhuis daarna.

### Evals en controles moeten aantoonbaar werken

Een eval is een meetlat. Een meetlat die groen kan geven zonder te meten is erger dan geen meetlat, want je gaat erop vertrouwen.

Elke eval of controle:
- is een klasse met `name` (wat hij checkt) en `reason` (welk risico hij afdekt, waarom we hem gebruiken);
- weigert lege invoer: nul rijen is "niet getoetst", nooit groen;
- vergelijkt regels als multiset, zodat dubbele regels nooit stil in een dict verdwijnen;
- haalt zijn tolerantie uit één gedeelde plek;
- heeft minstens twee tests: hij slaagt op correcte data, en hij faalt op een bekende fout. Die tweede test is het bewijs dat de eval werkt. Gebruik daarvoor kapotte implementaties (mutanten) als aparte klassen, en laat de test falen als een mutant ongemerkt doorkomt;
- leidt tot een exit-code ongelijk aan 0 bij een fout of een niet-getoetste eval.

Een controle die door de opzet nooit kan falen, schrap je of herschrijf je. Hij telt anders mee in "11 van 11" zonder iets te toetsen.

### Fouten zijn luid

- Een rij met het verkeerde aantal kolommen geeft een foutmelding, hij wordt niet stil overgeslagen.
- Kolommen uit een Excel of CSV lees je op kopnaam, niet op positie (`v[24]`). Ontbreekt een verwachte kop, dan stopt het programma met een duidelijke melding.
- Geen kale `except Exception` en zeker geen `except: pass`. Vang de specifieke fout die je verwacht.
- Shellscripts: `set -euo pipefail`, anders verdwijnt een fout in een `| tee`.

### Geen magische waarden

Een getal of string met betekenis krijgt een naam. `[277:]` is onleesbaar en breekt bij de volgende export. Klant-, jaar- en datumwaarden (`"41148"`, `2026`, `date(2026, 9, 30)`) zijn argumenten of configuratie, nooit vast in de code. Paden naar binaries komen uit configuratie of `shutil.which`, niet hard uit `/System/Library/...`.

### Leesbaar schrijven

- Eén statement per regel. Geen puntkomma's, geen functies op één regel, geen lambda's als naam voor een functie.
- Volledig getypt, zoals in TypeScript: elke functie, parameter en return-waarde, ook in tests. In Python draait `mypy --strict` (geconfigureerd in `pyproject.toml`) naast de tests, en beide moeten slagen. Een `# type: ignore` krijgt altijd de specifieke foutcode plus de reden erachter.
- Elke publieke functie, klasse en module krijgt een docstring. Die zegt in een regel wat erin gaat, wat eruit komt en waarvoor het gebruikt wordt, met een voorbeeld als het om een formaat gaat ("163.579,33" becomes 163579.33). Ga ervan uit dat de lezer de bron niet kent: welk bestand, welke kolom, waarom. Een naam alleen is niet genoeg, ook als hij goed is.
- Een klasse die data uit een bestand of systeem vasthoudt, krijgt een multiline docstring met vaste kopjes, nooit een bron achter een komma in de eerste zin:
  ```
  """Wat het is, in een zin.

  Source
      workbook   welk bestand
      sheet      welk tabblad
      one row    per wat

  Fields
      veldnaam   kolomnaam in de bron, en wat het betekent

  Example
      een rekenvoorbeeld als het gedrag niet vanzelf spreekt
  """
  ```
- Vertaal een vakterm naar de echte Engelse vakterm, niet letterlijk. Afroming is top-slicing, niet skimming. Twijfel je, zoek de term op die het vakgebied in het Engels gebruikt, en zet hem in de vertaaltabel van de README.
- Commentaar legt het waarom uit, niet het wat. Geen commentaar dat de geschiedenis vertelt ("nu doen we...", "fixed X").
- Ongebruikte imports, functies en parameters gaan weg. Code die alleen door zijn eigen test wordt aangeroepen, is dood tot er een echte gebruiker is.

## Structuur

### Mappen

Een map groepeert op verantwoordelijkheid, zodat je aan de boom ziet hoe het systeem werkt. Voor een Python-project:

```
<project>/
├── README.md            wat, waarom, hoe draaien, tabel werklabel → module
├── pyproject.toml       package, dependencies, pytest; geen sys.path-hacks
├── .gitignore           in elk geval output/
├── src/<package>/
│   ├── domain/          de begrippen als klassen, zonder I/O
│   ├── parsing/         formaatkennis (bedragen, datums, koppen), één versie
│   ├── readers/         alle file- en API-toegang, één reader per bron
│   ├── <extern>/        per extern systeem (bv. afas/) een eigen package achter een Protocol
│   ├── services/        bedrijfsregels die meerdere delen gebruiken
│   ├── evaluation/      evals en controles, met een gedeelde basisklasse
│   ├── reporting/       uitvoer naar een vaste output/-map
│   └── cli.py           argparse, subcommands, exit-codes
└── tests/               spiegelt src/, plus builders.py en client_data/
```

Pas de lagen aan op wat het project nodig heeft. Een klein script hoeft geen zeven mappen, maar zodra er meer dan een handvol files is, ordenen ze zich op verantwoordelijkheid en nooit op wie het schreef of in welke sessie.

### Uitvoer en data

Uitvoer gaat naar één vaste map, berekend vanaf de projectmap en niet vanaf de huidige werkmap, en die map staat in `.gitignore`. Een vrij te kiezen uitvoerpad kan klantdata buiten de ignore laten landen. Code, invoer en uitvoer staan nooit in dezelfde map.

### Verkennen is geen opleveren

Een script waarmee je iets uitzoekt, is geen gereedschap. Commit het niet als blijvende code. Moet het bewaard blijven omdat er een uitkomst op leunt, dan gaat het naar het archief, met de uitkomst in het dossier of de README. Resultaten typ je niet met de hand over in een README, je laat de tool ze wegschrijven.

## Werkwijze bij bouwen

1. Begrijp eerst het probleem en de begrippen. Welke dingen bestaan er in het domein, welke externe systemen spelen mee?
2. Maak bij nieuwe of gewijzigde structuur een filetree met per file in een regel wat erin komt. Laat die zien. Werk bij een al geautoriseerde opdracht zelfstandig door; vraag alleen akkoord wanneer een wezenlijke structuurkeuze nog bij de gebruiker ligt.
3. Bouw in kleine stappen, van binnen naar buiten, met de test eerst.
4. Als commits binnen de opdracht passen: commit per stap, niet per sessie. Eén commit is één afgerond stuk (een module met zijn tests), en de geschiedenis leest als het bouwverhaal: skelet, formats, domein, readers. Het commitbericht zegt waarom deze stap nodig was en welke keuze erin zit, niet alleen wat er veranderde. Elke commit slaagt los op tests en type checker; controleer dit met passende tests en de type checker op de betreffende stand. Herhaal geslaagde checks alleen bij nieuwe wijzigingen of concrete twijfel.
5. Eén PR per samenhangend stuk. Richtlijn: een PR die een reviewer niet in een half uur kan lezen (ruwweg meer dan 10 files of 400 regels nieuwe code), splits je. Een PR bouwt niet zichtbaar voort op experimenten in eerdere commits.
6. Kijk voor je oplevert met de checklist uit `references/review-checklist.md` naar je eigen code, alsof iemand anders hem schreef.
