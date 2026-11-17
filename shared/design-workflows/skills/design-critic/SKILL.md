---
name: design-critic
description: Laat een gerenderde interface onafhankelijk beoordelen tegen de gekozen richting en smaak, of verbeter die met maximaal twee kritiek- en verbeterrondes. Gebruik voor visuele kritiek op bestaande schermontwerpen en gerenderde interfaces.
---

# Design critic

Maak onafhankelijke, concrete ontwerpfeedback makkelijk inzetbaar. Alleen
beoordelen is read-only. Wijzig het ontwerp uitsluitend wanneer de gebruiker
ook om verbetering vraagt. Deze skill ontwerpt geen nieuwe productrichting.

## Context klaarzetten

Haal uit gesprek en project: te beoordelen pagina/staat, doel, doelgroep,
gekozen stijl, harde randvoorwaarden en aangeleverde visuele referenties.
Gebruik de geaccepteerde visuele keuzes en relevante voorkeuren als ontwerpcriteria. Onderscheid een gekozen richting van nog te verkennen opties.
Als smaak of richting nog open is, gebruik `design-direct` voor afstemming;
beoordeel beschikbare opties dan als voorstellen, zonder een keuze te verzinnen.
Inspecteer voor lokale wijzigingen de geldende projectregels en bestaande staat.
Gebruik beschikbare context; vraag alleen als een ontbrekend doel, target of
tegenstrijdige ontwerpafspraak het oordeel wezenlijk verandert.

Verkrijg actuele screenshots met een beschikbare browser- of screenshottool,
of gebruik de aangeleverde afbeeldingen. Noteer viewport en relevante staat.
Kies dekking passend bij de vraag; beweer geen volledige review bij één uitsnede.
Een screenshot van de gebruiker mag direct worden beoordeeld zonder repository.
Zonder toegang tot een render of leesbare screenshot: benoem het ontbrekende
bewijs en vraag om het target of beeld. Beoordeel geen uiterlijk uit code alleen.

## Onafhankelijke criticus

Lees de [criticusbriefing](references/critic-brief.md). Start één onafhankelijke
subagent zonder gespreksgeschiedenis wanneer de host dat ondersteunt en de
opdracht delegatie toestaat. Geef de briefing mee of gebruik een aantoonbaar
gelijkwaardige rol. Kies een beschikbare criticus die afbeeldingen kan
inspecteren. Geef alleen actuele screenshots of leesbare paden, viewport en
staat, een minimale productbriefing en relevante visuele referenties mee.
Label referenties als canoniek ontwerp of inspiratie. Neem concrete
vastgelegde ontwerpcriteria op. Laat code, eerdere kritiek, implementatieverhaal,
gewenste score en je eigen oordeel weg.

Als de host geen onafhankelijke beeldbeoordeling ondersteunt of toestemming
ontbreekt, meld die beperking. Een eventuele eigen visuele controle is een
zelfbeoordeling.

Wacht op de kritiek. De hoofdagent blijft verantwoordelijk voor afwegingen,
uitvoering en eindantwoord. De criticus heeft geen wijzigingsbevoegdheid.

## Beoordelen of verbeteren

Bij alleen beoordelen: geef de concrete bevindingen en bewijsgrenzen terug.
Bij verbeteren: pak de belangrijkste bevindingen binnen de bestaande opdracht
op, verifieer de wijzigingen passend bij het risico en maak nieuwe screenshots.
Laat elke nieuwe versie door een nieuwe criticus met dezelfde roltekst en
briefing beoordelen, zonder eerdere kritiek of scores.

Standaard maximaal twee verbeterrondes: initiële beoordeling, wijziging,
herbeoordeling, eventueel tweede wijziging en eindbeoordeling. Stop eerder als
de relevante problemen opgelost zijn, verbetering uitblijft, bewijs botst of
een nieuwe product-/stijlkeuze nodig is. Een cijfer is geen slaagcriterium.
Een ruimere rondebegroting vereist een expliciete gebruikersvraag.

Onderscheid afwijkingen van de gekozen richting, uitvoerings- of
bruikbaarheidsproblemen en hypotheses waarvoor ander bewijs nodig is.
Een optioneel smaakalternatief is geen fout; een positief modeloordeel is geen
vervanging voor de keuze van de opdrachtgever.

Rapporteer het resultaat, wat visueel is gecontroleerd, open bevindingen en
beperkingen. Onderscheid gewijzigd, gerenderd, beoordeeld en gepubliceerd.

Voorbeelden:
- “Laat de designcritic deze pagina beoordelen.”
- “Verbeter deze pagina met de designcritic; behoud de gekozen stijl.”

Inspiratie: techniek 3 uit
https://www.lennysnewsletter.com/p/how-to-turn-your-ai-into-a-world
De minimale productbriefing en begrensde rondes zijn bewuste aanpassingen.

## Hostnotities

- Claude Code: start de criticus met de Agent tool als gewone agent, niet als
  fork, zodat hij het gesprek en je eigen oordeel niet meekrijgt. Geef de
  screenshots als absolute paden die hij met Read kan openen. Hij heeft wel
  schrijfrechten en ziet CLAUDE.md, dus herhaal in de briefing dat hij alleen
  leest.
