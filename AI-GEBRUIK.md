# Gebruik van generatieve AI

## Waarvoor heb ik AI gebruikt?

Ik heb AI gebruikt om uitleg te krijgen over Python-code, fouten te onderzoeken
en mijn applicatie robuuster te maken. Ik heb de code zelf ingevoerd en iedere
functie zelf getest.

## Voorbeeld 1

Prompt:
Leg uit hoe ik het aantal dagen uit input.txt kan bepalen als de eerste regel
alleen kolomnamen bevat.

Antwoord, samengevat:
Lees alle regels met readlines(), tel de regels met len() en trek één af voor
de kopregel.

Mijn verwerking:
Ik heb dit toegepast in de functie aantal_dagen() en getest. Het resultaat was
7 dagen.

## Voorbeeld 2

Prompt:
Hoe voorkom ik dat de applicatie crasht wanneer de gebruiker tekst invoert waar
een geheel getal wordt verwacht?

Antwoord, samengevat:
Zet int(input(...)) in een try-blok en vang ValueError op met except.

Mijn verwerking:
Ik heb dit toegepast in overwrite_settings(). Bij de invoer "hallo" verschijnt
nu een foutmelding en blijft het programma werken.

## Voorbeeld 3

Prompt:
Hoe haal ik met Open-Meteo het actuele weer in Utrecht op?

Antwoord, samengevat:
Gebruik de forecast-API met de coördinaten van Utrecht, lees de JSON en haal
temperature_2m en wind_speed_10m uit het onderdeel current.

Mijn verwerking:
Ik heb toon_huidig_weer() gemaakt en foutafhandeling toegevoegd voor problemen
met internet of ongeldige API-gegevens.

## Bronnen

- Open-Meteo-documentatie: https://open-meteo.com/en/docs
- Lesmateriaal PROG1 tot en met PROG9
