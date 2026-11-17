---
name: design-direct
description: Ontwerp interfaces en interacties samen met de opdrachtgever. Vereenvoudig de gebruikerstaak en stem de visuele richting af vóór schermuitwerking. Gebruik voor schermontwerp, visuele verkenning, redesign en het kiezen tussen ontwerprichtingen.
---

# Samen interfaces ontwerpen

## Bepaal wat vaststaat

Lees de opdracht, recente feedback, bestaande ontwerpen en component- of
merkafspraken. Bekijk het ontwerp vóór je het wijzigt. Onderscheid verkennen,
kiezen, aanpassen binnen een geaccepteerde richting en overdracht naar bouw.
Behoud genomen besluiten en label eigen voorstellen als zodanig.

## Stem smaak af vóór uitwerking

Bij een nieuwe of wezenlijk gewijzigde richting, vraag kort welke voorbeelden of
onderdelen de opdrachtgever aanspreken, wat moet blijven en wat moet worden
vermeden. Gebruik bekende keuzes en feedback eerst. Maak stijlwoorden zoals
premium of rustig concreet met compositie, typografie, dichtheid, kleur,
beeld, vormen of beweging.

Wacht op een keuze voordat je de rest van de schermen uitwerkt. Werk intussen
door aan onafhankelijke stappen. Bij een gevraagde verkenning kun je enkele
kleine, betekenisvol verschillende proefstukken met dezelfde inhoud uitwerken.
Houd toelichting buiten de schermen. Vraag welke keuzes de opdrachtgever wil
behouden of combineren, tenzij die de beslissing expliciet heeft gedelegeerd.

## Ontwerp de handeling vóór het scherm

Volg een concrete taak van aanleiding tot resultaat. Welke keuze maakt de
gebruiker, wat handelt het systeem af en waaraan merkt de gebruiker succes?
Vereenvoudig het gedrag vóór je uitleg, statussen of knoppen toevoegt.

Een omkeerbare selectie kan zelf de opdracht zijn. Onderzoek bijvoorbeeld
automatisch bewaren bij een geldige invoer met lokale feedback en herstel.
Behandel aanmaken, versturen, publiceren en definitief afsluiten als aparte
handelingen wanneer ze een bewuste beslissing vragen.

Lees voor invoer, bewaren of asynchrone wijzigingen de
[interactiecontrole](references/interaction-check.md). Toets de werkelijk
uitgewerkte handeling op invoer, klikken en begrijpelijk herstel. Behoud bewuste
gebruikerskeuzes en de betekenis van bestaande gegevens.

## Werk de gekozen richting uit

- Gebruik Paper als die beschikbaar en afgesproken is, of een andere ondersteunde
  bewerkbare ontwerpomgeving. Zonder geschikte editor kun je opties of een
  specificatie uitwerken. Benoem een ontbrekend gevraagd bewerkbaar bestand.
- Hergebruik bestaande onderdelen. Begin met een representatief scherm of
  onderdeel als feedback de rest nog kan veranderen. Gebruik echte inhoud of
  duidelijk gelabelde voorbeeldinhoud. Toon relevante toestanden en leesvolgorde.
- Gebruik `user-flow-map` wanneer beschikbaar. Leg anders rollen, stappen,
  keuzes en herstelpaden zelf vast. Plaats het overzicht naast de schermen
  wanneer de editor dat ondersteunt.
- Gebruik `imagegen-frontend` of een beschikbaar beeldgereedschap voor
  gevraagde rasterconcepten of beeldreferenties. Lever een bewerkbaar scherm
  wanneer dat de afgesproken vorm is.
- Houd voorgesteld, geaccepteerd en geïmplementeerd gedrag uit elkaar.
  Ontwerptoestemming geeft geen bevoegdheid voor code, publicatie of deployment.

## Beoordeel en rond af

Bekijk actuele renders of screenshots in relevante toestanden en afmetingen.
Beoordeel afzonderlijk aansluiting bij de gekozen richting en de uitvoering
van hiërarchie, typografie, spacing, kleur, consistentie en bediening. Gebruik
`web-design-guidelines` wanneer beschikbaar, of toets deze aspecten rechtstreeks.
Koppel een probleem aan een zichtbare plek en consequentie. Bij smaakfeedback,
maak het verschil zichtbaar voordat je in dezelfde richting verder verfijnt.

Gebruik [design-critic](../design-critic/SKILL.md) voor een gevraagde
onafhankelijke visuele beoordeling. Geef de gekozen richting en canonieke
referenties zonder je eigen oordeel mee. De opdrachtgever beslist over smaak.
Statische beelden laten interactie, beweging en onbekende schermmaten open.

Lever het ontwerp of de beschikbare artefacten en benoem wat is voorgesteld,
gekozen, gecontroleerd en nog openstaat. Bewaar beslissingen op de afgesproken
plek. Gebruik bij geautoriseerde bouw `prepare-development` wanneer beschikbaar,
of werk zelf scenario’s, contracten en acceptatie uit. Verifieer de uitvoering
tegen het ontwerp.

Lees bij een redesign of gerichte verbetering
[Een bestaand ontwerp verbeteren](references/existing-design.md).

## Hostnotities

- Claude Code zonder Paper: werk in Figma als die koppeling er is. Een Artifact
  is een privépagina op claude.ai, geen bewerkbaar ontwerpbestand; gebruik het
  alleen als dat de afgesproken vorm is, en anders een lokaal HTML-bestand.
  Claude Code heeft geen ingebouwde beeldgeneratie, benoem een ontbrekend
  rasterconcept. Maak renders met de browser die het project gebruikt.
  Zonder `user-flow-map` of `web-design-guidelines` toets je flow en uitvoering
  zelf met de punten hierboven.
