# Invoer met minder handelingen

Gebruik dit bij invoer, opslaan of asynchrone wijzigingen. Kies gedrag vanuit de
gebruikerstaak; maak automatisch bewaren geen algemene verplichting.

## Maak de opdracht duidelijk

Een omkeerbare selectie kan zelf de opdracht zijn. Een geldig bewerkt veld kan
bewaren bij verlaten of na een passende typepauze. Voeg alleen een aparte
bevestiging toe als die een echte beslissing markeert, bijvoorbeeld aanmaken,
versturen, delen of definitief afsluiten. Een technisch save-endpoint is geen
reden voor een zichtbare Save-knop.

Een standaardwaarde of het openen van een scherm mag geen onverwachte
registratie aanmaken. Een knop als ‘Moment toevoegen’ kan de bedoelde opdracht
al volledig uitdrukken; vraag dan niet nóg eens hetzelfde te bevestigen.

## Behoud betekenis en vertrouwen

- Bewaar alleen geldige veranderingen. Maak onderscheid tussen leeg, expliciet
  nul, een ongewijzigde waarde en een bewuste wisactie.
- Toon feedback bij de handeling, bijvoorbeeld een gereserveerde plek in het
  veld. De UI mag meteen reageren; een succesindicatie hoort pas bij bevestigde
  verwerking van de actuele invoer. Laat opslagfeedback de gekozen waarde of
  het antwoord niet verbergen. Ondersteun ook toetsenbordbediening en een
  begrijpelijke status voor hulptechnologie.
- Laat een laat antwoord geen nieuwere invoer terugzetten. Terugkeren naar de
  oorspronkelijke waarde is geen simpele no-op als een andere waarde al
  onderweg is; de laatst bedoelde waarde moet uiteindelijk gelden.
- Behoud invoer bij een fout of onzekere uitkomst en bied passend lokaal herstel.
  Maak bij opnieuw proberen geen tweede registratie of externe actie aan.
- Denk aan weggaan en terugkomen, ook tijdens de typepauze of een lopend verzoek.
  Maak een concept niet afhankelijk van een open component of timer die bij
  navigatie verdwijnt. Leg alleen een echte grens aan de gebruiker voor.
- Kies passend terugdraaien voor omkeerbare acties. Controleer dat status,
  aantallen en gerelateerde overzichten dezelfde bevestigde waarde blijven tonen.

## Controleer de uitvoering

Volg de gewone handeling en de afwijking die de keuze kan veranderen. Begin bij
de gebruiker, niet bij een lijst met systeemfouten. Schrap een redundante stap
daadwerkelijk in alle actuele varianten en gedeelde onderdelen; een notitie op
het flowbord vervangt die doorvoering niet.

Een statisch ontwerp laat plaatsing en leesbaarheid zien. Het bewijst geen
timer, opslag, herstel of gebruikersbegrip. Gebruik voor die conclusies passend
bewijs: een gebeurtenisverloop, interactieprototype, runtimecontrole of echte
gebruikerstest. Benoem wat werkelijk is uitgevoerd.
