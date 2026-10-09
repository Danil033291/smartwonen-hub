import json
from urllib.request import urlopen
from urllib.error import URLError

from weerapp import weerstation
from controller import smart_app_controller


def toon_huidig_weer():
    url = (
        "https://api.open-meteo.com/v1/forecast"
        "?latitude=52.09"
        "&longitude=5.12"
        "&current=temperature_2m,wind_speed_10m"
        "&timezone=Europe%2FAmsterdam"
    )

    try:
        antwoord = urlopen(url)
        tekst = antwoord.read().decode("utf-8")
        gegevens = json.loads(tekst)

        huidig_weer = gegevens["current"]
        temperatuur = huidig_weer["temperature_2m"]
        windsnelheid = huidig_weer["wind_speed_10m"]

        print()
        print("Huidig weer in Utrecht:")
        print("Temperatuur:", temperatuur, "°C")
        print("Windsnelheid:", windsnelheid, "km/u")

    except URLError:
        print("Het weer kon niet worden opgehaald.")
        print("Controleer je internetverbinding.")

    except (KeyError, json.JSONDecodeError):
        print("De ontvangen weergegevens konden niet worden gelezen.")


def hoofdmenu():
    doorgaan = True

    while doorgaan:
        print()
        print("SMART HOME PLATFORM")
        print("1. Weerstation")
        print("2. Smart App Controller")
        print("3. Huidig weer in Utrecht")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            weerstation()

        elif keuze == "2":
            smart_app_controller()

        elif keuze == "3":
            toon_huidig_weer()

        elif keuze == "4":
            print("Het platform wordt afgesloten.")
            doorgaan = False

        else:
            print("Ongeldige keuze. Kies 1, 2, 3 of 4.")


if __name__ == "__main__":
    hoofdmenu()