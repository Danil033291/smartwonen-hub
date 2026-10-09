def Fahrenheit(temp_celcius):
    fahrenheit = 32 + 1.8 * temp_celcius
    return fahrenheit


def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = temp_celcius - luchtvochtigheid / 100 * windsnelheid
    return gevoel


def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    gevoel = gevoelstemperatuur(
        temp_celcius,
        windsnelheid,
        luchtvochtigheid
    )

    if gevoel < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"

    elif gevoel < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"

    elif gevoel >= 0 and gevoel < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"

    elif gevoel >= 0 and gevoel < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"

    elif gevoel >= 10 and gevoel < 22:
        return "Heerlijk weer, niet te koud of te warm."

    else:
        return "Warm! Airco aan!"


def vraag_kommagetal(vraag):
    while True:
        invoer = input(vraag)

        if invoer == "":
            return None

        try:
            getal = float(invoer)
            return getal

        except ValueError:
            print("Ongeldige invoer. Vul een geldig getal in.")


def vraag_luchtvochtigheid(vraag):
    while True:
        invoer = input(vraag)

        if invoer == "":
            return None

        try:
            vochtigheid = int(invoer)

            if 0 <= vochtigheid <= 100:
                return vochtigheid

            print("De luchtvochtigheid moet tussen 0 en 100 liggen.")

        except ValueError:
            print("Vul een geheel getal tussen 0 en 100 in.")


def weerstation():
    totaal_temp = 0
    aantal_ingevulde_dagen = 0

    for dag in range(1, 8):
        temp_celcius = vraag_kommagetal(
            "Wat is op dag " + str(dag) + " de temperatuur [C]: "
        )

        if temp_celcius is None:
            print("Het weerstation wordt afgesloten.")
            break

        windsnelheid = vraag_kommagetal(
            "Wat is op dag " + str(dag) + " de windsnelheid [m/s]: "
        )

        if windsnelheid is None:
            print("Het weerstation wordt afgesloten.")
            break

        luchtvochtigheid = vraag_luchtvochtigheid(
            "Wat is op dag " + str(dag) + " de luchtvochtigheid [%]: "
        )

        if luchtvochtigheid is None:
            print("Het weerstation wordt afgesloten.")
            break

        aantal_ingevulde_dagen += 1
        totaal_temp += temp_celcius
        gemiddelde = totaal_temp / aantal_ingevulde_dagen

        temp_fahrenheit = Fahrenheit(temp_celcius)
        rapport = weerrapport(
            temp_celcius,
            windsnelheid,
            luchtvochtigheid
        )

        print(
            "Het is " + str(temp_celcius) +
            "°C (" + str(temp_fahrenheit) + "°F)"
        )
        print(rapport)
        print("Gemiddelde temperatuur tot nu toe:", gemiddelde)
        print("======================================")


if __name__ == "__main__":
    weerstation()