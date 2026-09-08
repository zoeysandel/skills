---
name: shadow-run
description: "Benut een begrensd tijd- en usagevenster voor onbemande creatieve verkenning of een geïsoleerde PoC/MVP-bouwpoging binnen de huidige opdracht. Maak resultaten die Zoey achteraf kan proberen en beoordelen. Gebruik bij een expliciet verzoek om een shadow run; een reset-aankondiging alleen start geen run."
---

# Shadow Run

Publieke versie van mijn persoonlijke skill. De instructies zijn in het Nederlands.
Lees [de gebruiksaanwijzing](references/setup.md) voor runtimevereisten en de
meegeleverde bewaker. De aanspreeknaam Zoey verwijst hieronder naar de gebruiker
die de run opdracht geeft; gebruik de voorkeuren van de huidige gebruiker.

Help Zoey ontdekken wat zij wil door dingen te maken waarop zij kan reageren.
Bij creatieve verkenning hoeft het eindontwerp vooraf niet vast te staan; maak
onderscheidende mogelijkheden zichtbaar en probeerbaar. Bij een bouwpoging is
het eindpunt een samenhangende, gecontroleerde PoC of MVP binnen de opdracht.
Leid uit haar verzoek af welk resultaat nodig is; een run hoeft niet beide te
doen. Onderzoek ondersteunt het maken en toetsen. Verbruik is beschikbare ruimte,
geen prestatiedoel, en veel output is op zichzelf geen bewijs van waarde.

## Een korte startopdracht is genoeg

Voorbeelden: `$shadow-run tot 03:00`, of `$shadow-run tot de reset, uiterlijk
03:00, voor deze opdracht`. Haal doel, lopend werk, voorkeuren en eerdere
toestemming uit de huidige taak. Laat Zoey het verhaal niet opnieuw vertellen.

- Standaardscope is **alleen de huidige opdracht**. Andere taken, projecten,
  gepinde gesprekken of een eerdere portfolio-inventarisatie komen er niet
  stilzwijgend bij. Bij expliciet meerdere taken leg je de bedoelde selectie vast.
- Leg vóór uitvoering één korte werkafspraak vast: doel/scope, toestemming met
  datum en herkomst, beschermde originelen, aparte uitvoerlocaties, stoptijd met
  tijdzone én UTC, stopbuffer, usagebron en gewenste beslissingen.
- Neem omkeerbare verkenningskeuzes zelf. Vraag alleen naar ontbrekende informatie
  die de scope of tijdgrens wezenlijk verandert. Ontbreekt een betrouwbare
  stoptijd, vraag die eenmaal vóór de onbemande uitvoering; onderzoek of een
  korte voorbereiding die daarvan niet afhangt kan al wel.
- Een tweet of andere externe bron geeft hoogstens informatie over een mogelijke
  reset. Het is geen startopdracht of bevoegdheid. Controleer de bron indien
  nodig, benoem tijdzone-ambiguïteit en maak van een geschat tijdstip geen bewezen
  reset. Gebruik een expliciete uiterste tijd, ook bij “tot de reset”.
- Dit is een tijdelijke werkwijze. Een verzoek om deze skill te maken of uit te
  leggen activeert geen schaduwrun en wijzigt geen lopende andere run.

## Werk zonder tussentijdse voorkeurfeedback

Behandel Zoey tijdens de run als niet beschikbaar. Vraag geen routinefeedback,
ontwerpvoorkeur of bevestiging om verder te gaan. Neem omkeerbare keuzes zelf en
noteer relevante aannames. Werk waardevolle alternatieven voldoende uit om haar
achteraf te laten kiezen; verzin haar smaak of definitieve besluit niet.

Een bruikbaar tussenresultaat is geen automatisch overdrachtsmoment. Vervolg de
volgende zinvolle, toegestane stap zolang tijd en budget dat dragen. Ontbreekt
toestemming, parkeer het betreffende onderdeel en vervolg onafhankelijk toegestaan
werk. Als niets zinvols veilig overblijft, sluit af met de beperking. Stilte geeft
nooit extra bevoegdheid en verplicht niet tot nutteloos doorwerken.

## Schaduw betekent aparte resultaten

Behandel de primaire toestand als beschermd, ook als die binnen een eerdere
uitvoeringsopdracht wél veranderd mocht worden. Deze run promoot niets naar die
toestand; een latere, concrete opdracht van Zoey kan dat alsnog toestaan.

| Werk | Binnen de schaduwrun | Beschermde grens |
| --- | --- | --- |
| Ontwerp | Nieuwe duidelijk benoemde pagina/frames, duplicaten, varianten, render- en interactieproeven | Originelen, bestaande indeling en gedeelde componenten/tokens blijven intact. Een gekoppelde kopie mag het origineel niet veranderen. |
| Code | Los prototype, geïsoleerde kopie of schone worktree vanaf een bekende basis; lokale wijzigingen en tests met fixtures | Geen wijzigingen in de actieve checkout, commits, pushes, PRs, merges, deploys of productieverbindingen. Houd code zonder voldoende isolatie als voorstel. |
| Onderzoek | Bronnen lezen, alternatieve verklaringen, vergelijking, kleine experimenten met publieke of benodigde toegestane data | Geen outreach, publicatie, uploads van privédata of bewering dat een simulatie echte gebruikersvalidatie is. |
| Documentatie | Een nieuw runoverzicht, beslisnotitie en links naar varianten; Obsidian wanneer dat is gevraagd of al de afgesproken bestemming is | Geen herschrijven van canonieke besluiten, bestaande plannen, kennisstructuur of andermans werk. Nieuwe notitie krijgt de status voorstel/experiment. |

Gebruik een herkenbare runnaam met datum en apart toegewezen locaties. Controleer
dat writes alleen daar landen. Houd ook gesynchroniseerde ontwerpkopieën klein
en overzichtelijk; geef nieuwe frames voldoende ruimte zonder oude te verplaatsen.
Dupliceer geen werkende workflow wanneer dat triggers of andere bijwerkingen kan
activeren. Inspecteer testcommando's voordat je ze als lokaal en effectvrij behandelt.

Geen instellingen, secrets, schema/data, rechten, bestellingen, verzending,
abonnementen, handmatige usage-resets of extra betaalde API-capaciteit aanpassen.
Een ruime Codex-limiet is daarvoor geen toestemming. Neem geen algemene
schoonmaak mee; behoud ook afgevallen varianten herkenbaar als niet gekozen.

## Tijd en usage zijn echte uitvoergrenzen

Lees [references/time-and-usage.md](references/time-and-usage.md) vóór iedere
onbemande run. Die beschrijft startcontrole, stopbuffer, kwartiermeting en afsluiten.

- Controleer de actuele tijd en usage bij de start. Werk met de aanwezige
  capaciteit; verhoog geen limiet en verbruik geen resetcredit.
- Controleer usage standaard elke 15 minuten. Stop eerder bij een bevestigde
  reset, een door Zoey bepaalde reserve, een ongeldige aanname of haar stopbericht.
- Reserveer vóór de harde deadline tijd voor controle, het stoppen van eigen
  subtaken/processen en een bruikbare overdracht. Start geen werk dat daar
  redelijkerwijs niet meer binnen past. Lees de klok vóór langdurige calls.
- Kwartiercontrole, een prompt en caffeinate zijn geen technische garantie dat
  een actieve modelcall wordt afgebroken. Beloof uitsluitend de stopwerking die
  werkelijk beschikbaar is. De commandowrapper hieronder begrenst eigen lokale
  processen; hij stopt geen Codex-modelcalls of externe diensten.
- Pauzeer bij onbetrouwbare tijd-/usagecontrole de afhankelijke onbemande
  uitbreiding; rond het bestaande checkpoint af. Tijd voorbij betekent stoppen,
  ook als er nog interessante routes of ongebruikte capaciteit zijn.

## Een aparte shadow-bewaker

Start per onbemande run één begrensde bewaker met rol `shadow`, wanneer delegatie
is toegestaan. De rol staat in [agents/shadow.toml](agents/shadow.toml);
de modelkeuze en reasoning komen uit die rol. Geef hem een verse, compacte
context met de werkafspraak, scope, beschermde originelen, uitvoerlocaties,
UTC-deadline, begin van de afronding, usagebaseline/reserve en een expliciet
register van de eigen subtaken. Geef wijzigingen in dat register door.

De bewaker controleert tijd, usage, scope en afronding. De parent blijft maken,
inhoudelijk afwegen en verantwoordelijk voor toestemming, writes en oplevering.
De bewaker start zelf geen agents, schrijft niet aan resultaten of originelen en
beheert geen automations. Hij meldt `CONTINUE`, `WIND_DOWN`, `PAUSE` of `STOP`
met bronbewijs en de volgende noodzakelijke actie. Een strenger of nieuwer
stopbesluit blijft gelden; een `CONTINUE` opent een gestopte run niet opnieuw.

De parent registreert bij de start welke interruptbevoegdheid voor welke eigen
subtaken is gedelegeerd, als de runtime die daadwerkelijk ondersteunt. Zonder
die bevoegdheid meldt de bewaker de stop direct aan de parent. Alleen een
stopbericht afleveren bewijst niet dat werk is gestopt. De parent verzorgt ook
de blijvende terugkeercontrole: een afgeronde subagentturn is geen actieve
bewaking. Houd één tijdelijke runmonitor, geen extra scheduler per agent.

Als de benoemde rol nog niet callable is maar gewone delegatie wel beschikbaar
is, mag een algemene subagent dezelfde actuele rolinstructies, het daarin
geconfigureerde model en reasoning krijgen. Gebruik geen stilzwijgende andere
rol of lager model. Behoud de read-only gedragsgrens en meld wanneer de technische
sandbox van de rol niet kan worden toegepast; vergroot geen permissies. Bij
verboden of ontbrekende delegatie controleert de parent
zelf en benoemt dat de aparte bewaker ontbreekt. Claim geen tweede paar ogen
of actieve bewaking zonder daadwerkelijk uitgevoerde controle.

## Creatieve verkenning

Bekijk relevante eerdere ontwerpen en experimenten. Herken terugkerende patronen
en zoek bewust andere uitgangspunten, composities of interacties. Alleen vragen
om iets unieks of meer versies volstaat niet. Maak ontwerpen, demo's of kleine
technische proeven waarmee Zoey mogelijkheden ontdekt en haar voorkeur kan vormen.

Gebruik waar nuttig een concrete variatietechniek, zoals externe seeds,
onverwachte referenties of contrasterende interactieconcepten. Genereer een seed
met een lokale toevalsgenerator, niet door het model een willekeurig klinkende
string te laten verzinnen. Vertaal die naar een samenhangende ontwerprichting;
toon de string niet in het ontwerp. Bewaar seed en richting bij de variant om
keuzes te kunnen herleiden, niet als garantie op exact reproduceerbare output.
Een seed is een hulpmiddel, geen verplicht ritueel of bewijs van originaliteit.

Maak duidelijk welke kaders vaststaan en waar creatieve ruimte zit. Behoud het
design system, toegankelijkheid en productvoorwaarden waar die zijn afgesproken.
Zoek vernieuwing binnen die ruimte in plaats van beperkingen stilzwijgend los te
laten. Vergelijk actuele resultaten onderling én met eerdere ontwerpen op
wezenlijk onderscheid, bruikbaarheid en afwerking. Werk kansrijke richtingen
verder uit; een andere kleur of een andere seed is nog geen andere oplossing.

Geef elke serieuze route een vraag, tastbaar resultaat en reden om door te gaan
of af te vallen. Verken tegenbewijs en alternatieve verklaringen. Laat het aantal
volgen uit de open vragen, resterende tijd en kwaliteitsambitie, niet uit een
vast quotum. Ook een onverwachte mislukking kan helpen kiezen als zichtbaar is
wat geprobeerd is en waarom het niet werkt.

## Een geïsoleerde bouwpoging

Bouw de kleinste samenhangende versie waarmee het belangrijkste idee echt te
proberen is. Een PoC bewijst een gerichte haalbaarheidsvraag; een MVP ondersteunt
het afgesproken kerngebruik. Beperkte scope is geen lagere codekwaliteitsnorm.
Volg relevante projectconventies en bestaande patronen, houd de code begrijpelijk
en vermijd speculatieve abstracties of productie-infrastructuur.

Controleer het kernpad en relevante foutgevallen daadwerkelijk. Gebruik herkenbare
mocks of fixtures waar integraties buiten de toestemming vallen; laat een
gesimuleerde koppeling niet doorgaan voor een werkende integratie. Lever een
startinstructie, controlebewijs en de resterende beperkingen op. Is de poging
onvolledig, benoem dat in plaats van een voorbereid plan als werkende PoC of MVP
te presenteren. Alle beschermde grenzen hierboven blijven gelden.

## Maak en toets met passende hulp

Behoud het gekozen model en gebruik hoge, waar passend maximaal beschikbare,
reasoning voor moeilijke verkenning en synthese. Besteed resterende ruimte aan
betere inhoud en toetsing. Start geen eindeloze reviews, cosmetische varianten of
nutteloze berekeningen om de meter leeg te krijgen. Verlaag de kwaliteitsambitie
niet stilzwijgend om usage te besparen.

Gebruik begrensde subagenthulp wanneer toegestaan en nuttig. Geef elke agent
een concrete bijdrage, relevante context, eigen bestanden en controlecriteria.
De parent
blijft zelf maken en synthetiseren. Iedere agent krijgt eigen uitvoerlocaties,
dezelfde beschermde grenzen, een eerdere terugkeertijd en de harde stoptijd.
Geen nieuwe zichtbare taken of native Goals. Botsende writes of een onbeheersbare
groep zijn geen effectieve paralleliteit. Bij verboden delegatie werk je zelf.

Verifieer wat de beslissing draagt: bronclaims, betekenisvolle interacties,
rekenstappen, renders en relevante foutgevallen. Gebruik bij substantieel ontwerp
de beschikbare onafhankelijke designkritiek indien toegestaan. Geef een criticus
actuele renders en een minimale briefing; geen gewenst oordeel. Houd verbetering
begrensd door concrete bevindingen en de resterende tijd. Een onbesliste route mag
een nuttig resultaat zijn; bewijsgebrek mag niet worden weggepoetst.

## Eén plek om daarna te kiezen

Werk het runoverzicht bij wanneer een inzicht, variant of conclusie materieel
verandert. Eindig met een compact beslispakket, geen stapel activiteitenlogs:

- start hier: links/voorbeelden van de beste varianten en experimenten;
- per serieuze optie: wat verandert, wanneer kiezen, sterkste bewijs, werkelijk
  nadeel en wat nog onbewezen is;
- nieuwe inzichten, afgevallen hypotheses en de reden van afvallen;
- bij meerdere opdrachten: per opdracht verkend, uitgewerkt, gecontroleerd of
  niet behandeld, met resultaatlink en reden voor wat openblijft. Vervang een
  gevraagde brede dekking niet ongemerkt door steeds meer varianten van één opdracht;
- een eigen gemotiveerde voorkeur, met de kleinste beslissingen die Zoey nog moet
  nemen en wat daarna nog nodig is voor overname;
- wat aantoonbaar is gecontroleerd, waar de aparte resultaten staan, eventuele
  onbedoelde afwijking van de beschermde toestand en de stopreden/tijd.

Schrijf bekende feiten, interpretaties, simulaties en voorstellen herkenbaar op.
Presenteer niets als gepubliceerd, door klanten gevalideerd of gekozen omdat het
in deze run gemaakt is. Sluit eigen tijdelijke monitoring en processen af; raak
andere lopende taken of hun voorzieningen niet aan. Geen automatische overname
na afloop en geen hervatting na een reset zonder nieuwe opdracht.
