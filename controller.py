def aantal_dagen(invoerbestand):
    try:
        bestand = open(invoerbestand, "r")
        regels = bestand.readlines()
        bestand.close()

        return len(regels) - 1

    except FileNotFoundError:
        print("Het invoerbestand is niet gevonden.")
        return 0


def auto_bereken(invoerbestand, uitvoerbestand):
    invoer = open(invoerbestand, "r")
    regels = invoer.readlines()
    invoer.close()

    uitvoer = open(uitvoerbestand, "w")

    for regel in regels[1:]:
        gegevens = regel.split()

        datum = gegevens[0]
        aantal_personen = int(gegevens[1])
        ingestelde_temperatuur = float(gegevens[2])
        buitentemperatuur = float(gegevens[3])
        neerslag = float(gegevens[4])

        verschil = ingestelde_temperatuur - buitentemperatuur

        if verschil >= 20:
            cv_ketel = 100
        elif verschil >= 10:
            cv_ketel = 50
        else:
            cv_ketel = 0

        ventilatie = aantal_personen + 1

        if ventilatie > 4:
            ventilatie = 4

        if neerslag < 3:
            bewatering = True
        else:
            bewatering = False

        uitvoer.write(
            datum + ";" +
            str(cv_ketel) + ";" +
            str(ventilatie) + ";" +
            str(bewatering) + "\n"
        )

    uitvoer.close()


def overwrite_settings(uitvoerbestand):
    gekozen_datum = input("Welke datum wil je aanpassen? ")

    try:
        bestand = open(uitvoerbestand, "r")
        regels = bestand.readlines()
        bestand.close()

    except FileNotFoundError:
        print("Het uitvoerbestand bestaat nog niet.")
        print("Kies eerst optie 2 om het bestand aan te maken.")
        return -1

    datum_gevonden = False

    for regel in regels:
        onderdelen = regel.strip().split(";")

        if onderdelen[0] == gekozen_datum:
            datum_gevonden = True

    if datum_gevonden == False:
        print("Datum niet gevonden.")
        return -1

    print("1. CV-ketel")
    print("2. Ventilatie")
    print("3. Bewatering")

    gekozen_systeem = input("Welk systeem wil je aanpassen? ")

    if gekozen_systeem not in ["1", "2", "3"]:
        print("Ongeldig systeem gekozen.")
        return -3

    try:
        nieuwe_waarde = int(input("Wat is de nieuwe waarde? "))

    except ValueError:
        print("De waarde moet een geheel getal zijn.")
        return -3

    if gekozen_systeem == "1" and not (0 <= nieuwe_waarde <= 100):
        print("De CV-ketel moet tussen 0 en 100 staan.")
        return -3

    if gekozen_systeem == "2" and not (0 <= nieuwe_waarde <= 4):
        print("De ventilatie moet tussen 0 en 4 staan.")
        return -3

    if gekozen_systeem == "3" and nieuwe_waarde not in [0, 1]:
        print("Bewatering moet 0 of 1 zijn.")
        return -3

    nieuwe_regels = []

    for regel in regels:
        onderdelen = regel.strip().split(";")

        if onderdelen[0] == gekozen_datum:
            if gekozen_systeem == "1":
                onderdelen[1] = str(nieuwe_waarde)

            elif gekozen_systeem == "2":
                onderdelen[2] = str(nieuwe_waarde)

            else:
                onderdelen[3] = str(nieuwe_waarde == 1)

        nieuwe_regel = ";".join(onderdelen) + "\n"
        nieuwe_regels.append(nieuwe_regel)

    bestand = open(uitvoerbestand, "w")
    bestand.writelines(nieuwe_regels)
    bestand.close()

    print("De instelling is aangepast.")
    return 0


def smart_app_controller():
    doorgaan = True

    while doorgaan:
        print()
        print("SMART APP CONTROLLER")
        print("1. Toon het aantal aanwezige dagen")
        print("2. Bereken alle apparaten automatisch")
        print("3. Overschrijf een berekende waarde")
        print("4. Stoppen")

        keuze = input("Maak een keuze: ")

        if keuze == "1":
            dagen = aantal_dagen("input.txt")
            print("Aantal aanwezige dagen:", dagen)

        elif keuze == "2":
            try:
                auto_bereken("input.txt", "output.txt")
                print("De automatische berekening is uitgevoerd.")

            except FileNotFoundError:
                print("Het invoerbestand is niet gevonden.")

            except (ValueError, IndexError):
                print("De gegevens in het invoerbestand zijn ongeldig.")

        elif keuze == "3":
            overwrite_settings("output.txt")

        elif keuze == "4":
            print("De Smart App Controller wordt afgesloten.")
            doorgaan = False

        else:
            print("Ongeldige keuze. Kies 1, 2, 3 of 4.")


if __name__ == "__main__":
    smart_app_controller()