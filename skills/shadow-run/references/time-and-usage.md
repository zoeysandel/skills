# Tijd, usage en begrensde processen

Lees dit bij het starten van een echte onbemande shadow run. Het aanmaken of
uitleggen van de skill is geen startopdracht.

## Startcontrole

1. Lees de huidige klok, leid de door Zoey bedoelde datum/tijdzone uit haar opdracht
   en context af en noteer een ondubbelzinnige UTC-deadline. Vraag bij wezenlijke
   ambiguïteit. Schuif die grens niet mee wanneer een verwachte reset uitblijft.
2. Lees actuele Codex-usage met `get_usage_limits`. Gebruik beschikbare buckets,
   vensterduur en resettijd; null is onbekend. Gebruik de huidige schema's, geen
   hardgecodeerde modellen, percentages of resetdata. Benoem dat accountgebruik
   ook door ander werk kan stijgen.
3. Leg een compacte baseline vast met alleen UTC, limit-id, gebruikte percentages,
   vensterduur en resettijd. Geen account-id, credentials of resetcredit-id.
4. Kies een stopbuffer die minstens de langste slecht onderbreekbare actie plus
   overdracht past; voor een sessie van uren is circa tien minuten een vertrekpunt,
   geen universele garantie. Deel lange experimenten op. Plan verplichte reviews
   binnen het werkvenster en niet pas op de deadline.
5. Verifieer een beschikbaar terugkeer-/stopmechanisme voordat je beweert dat de
   run onbeheerd wordt bewaakt. Gebruik de native automation-tool voor een
   tijdelijke heartbeat in deze taak als de omgeving dat ondersteunt. Inspecteer
   eerst een bestaande eigen runmonitor om doublures te voorkomen. Laat de
   heartbeat scope, deadline, usagebron, logpad en stopprocedure volgen. Deze
   monitoring geeft geen toestemming om bestaande andere taken aan te sturen.
   De parent beheert deze ene scheduler en hervat daarmee zo nodig de bestaande
   `shadow`-bewaker met de actuele, compacte rungegevens. Een slapende of
   afgeronde bewaker bewijst geen actieve controle. Verifieer ook dat de eerste
   check daadwerkelijk heeft plaatsgevonden. De afrondingsgrens en deadline
   krijgen een eigen tijdcontrole; wacht daarvoor niet op het volgende kwartier.
6. Wanneer wakker blijven nodig is, mag de gevraagde onbemande run een tijdelijk
   `caffeinate`-proces met eindtijd omvatten. Controleer bestaande eigen voorziening,
   voeding en daadwerkelijke macOS assertions. Wijzig geen permanente power- of
   lockinstellingen. Caffeinate stopt geen werk, voorkomt geen lege accu en is
   geen toezegging dat de machine met gesloten klep kan blijven werken.

Een geweigerde of ontbrekende monitoringtool is geen reden om zelf een cronjob,
globale configuratiewijziging of onbegrensde background-agent te installeren.
Beschrijf de beperking. Voer alleen stappen uit die de beschikbare klok- en
terugkeercontrole daadwerkelijk kunnen begrenzen; claim geen technisch afgedwongen
modelstop wanneer de runtime die niet biedt.

## Kwartiercontrole

Lees tijdens de actieve run uiterlijk bij iedere volgende kwartiergrens de meter
opnieuw; de parent bewaakt dit ook tijdens eigen werk. Gebruik desgewenst de
tijdelijke heartbeat om na een onderbreking terug te keren. Die kan niet worden
beschouwd als een preëmptieve onderbreker van een actieve modelcall.

- Vergelijk overeenkomstige limit-id's en vensters. Een duidelijk gedaald verbruik
  of een resetmelding vraagt één directe herlezing. Een ontbrekende bucket,
  verschoven meter of verlopen normaal venster is op zichzelf geen bewijs van
  de aangekondigde algemene reset.
- Als een daling of vernieuwd budget wordt bevestigd, stop de run die alleen de
  oude capaciteit mocht benutten. Een natuurlijke reset is ook reden om dat
  beschermde nieuwe budget niet stilzwijgend te gebruiken.
- Een mogelijk gereset maar onvergelijkbaar resultaat: pauzeer nieuw werk dat het
  nieuwe budget kan aanspreken en leg de onzekerheid vast. Blijf niet doorwerken
  op een oude baseline. Bij herhaalde onbeschikbare metingen rondt de run af met
  een checkpoint; verbruik wordt niet als nul geïnterpreteerd.
- De aankondiging “rond” een tijdstip bewijst niets over dit account. Een reset kan
  tussen twee metingen vallen. Kwartiermetingen kunnen daarom geen nulverbruik
  vanaf een onbekend resetmoment garanderen.
- Blijf stil bij normale, ongewijzigde status. Meld alleen betekenisvolle
  afwijkingen, de stop, een fout of een echte gebruikersbeslissing. Geen losse
  statusmeldingen enkel omdat opnieuw vijftien minuten verstreken zijn.

Vraag of activeer nooit een handmatige reset, aankoop of betaalde fallback vanuit
deze run. Stop vóór uitputting wanneer de beschikbare meter anders geen ruimte
meer laat voor de overdracht; een door Zoey gegeven reserve gaat voor.

## Lokale commando's begrenzen

Voor een langdurig lokaal experiment gebruik je `scripts/timebox.py`. De wrapper
start uitsluitend het gegeven commando in een eigen process group. Hij weigert
een verlopen grens, begrenst de looptijd en beëindigt die eigen process group bij
timeout of wanneer het hoofdcommando eindigt. Hij schakelt geen andere processen,
Codex-taken, modellen, servers of services uit. Gebruik geen daemonizing commands
die uit hun process group ontsnappen.

Voorbeeld vanuit de skillmap (vervang deadline en paden door de concrete runwaarden):

```bash
python3 scripts/timebox.py status \
  --deadline 2030-01-02T02:00:00Z --reserve-seconds 600

python3 scripts/timebox.py run \
  --deadline 2030-01-02T02:00:00Z --reserve-seconds 600 --max-seconds 45 \
  -- python3 /absolute/shadow-run/experiment.py
```

`status` leest alleen. `run` wijzigt zelf geen bestanden: eventuele writes zijn
die van het expliciet gegeven commando. JSON-status gaat naar stderr bij `run`,
zodat stdout van het experiment intact blijft. Exit 124 betekent timeout of een
verlopen werkgrens; 125 betekent een start-/guardfout. Een geslaagd commando heeft
de eigen exitcode. De wrapper omvat ook kinderen in dezelfde process group, maar
kan geen effect ongedaan maken. Gebruik hem alleen voor de reeds toegestane,
geïsoleerde experimenten. Een vooraf gestarte externe job blijft buiten zijn bereik.

Gebruik ook voor overige toolcalls een passende maximale duur waar ondersteund.
Start vlak voor de grens geen generatie of externe job die je niet tijdig kunt
afronden of stoppen. Een script-timeout is geen model-timeout.

## Afsluiten

Bij stopbuffer: geen nieuwe verkenningen of agents; rond controles en beslisnotitie
af. Bij bevestigde reset: stop nieuw inhoudelijk werk meteen, checkpoint alleen
wat nodig is om het bestaande resultaat overdraagbaar te maken. Bij harde deadline:
geen inhoudelijke voortzetting, ook niet voor een extra review of een mooier einde.

Stop of laat aflopen alleen eigen geregistreerde processen en subtaken. Pauzeer de
eigen tijdelijke automation via de native tool, met behoud van andere velden, en
controleer het resultaat. Controleer de beschermde originelen passend bij het
medium (bijvoorbeeld Git-status of bronframewaarden) en leg afwijkingen eerlijk
vast. Eindig met stopreden, tijd, resultaatlocaties en het beslispakket. Controleer
de aangekondigde reset niet daarna onbeperkt door; hervatten vraagt een nieuwe
opdracht.
