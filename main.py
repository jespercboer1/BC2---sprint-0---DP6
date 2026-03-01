from recept import Recept
from ingredient import Ingredient
from stap import Stap


def main():
    recepten = []

    # ===== INGREDIENTEN MET ALTERNATIEVEN =====

    spek = Ingredient("spekreepjes", 150, "gram", 400)
    vegan_spek = Ingredient("vegan spek", 150, "gram", 250)
    spek.set_plantaardig_alternatief(vegan_spek)

    gehakt = Ingredient("gehakt", 300, "gram", 500)
    vegan_gehakt = Ingredient("vegan gehakt", 300, "gram", 300)
    gehakt.set_plantaardig_alternatief(vegan_gehakt)

    # ===== RECEPT 1 =====

    recept1 = Recept("Tagliatelle Carbonara", "Snelle romige pasta met spek en kaas.")

    recept1.voeg_ingredient_toe(Ingredient("tagliatelle", 300, "gram", 350))
    recept1.voeg_ingredient_toe(Ingredient("eieren", 2, "stuks", 160))
    recept1.voeg_ingredient_toe(Ingredient("Parmezaanse kaas", 50, "gram", 200))

    spek = Ingredient("spek", 150, "gram", 400)
    vegan_spek = Ingredient("vegan spek", 150, "gram", 250)
    spek.set_plantaardig_alternatief(vegan_spek)

    recept1.voeg_ingredient_toe(spek)

    recept1.voeg_stap_toe(Stap("Kook de tagliatelle volgens de verpakking.", "Zorg dat het water goed zout is."))
    recept1.voeg_stap_toe(Stap("Bak de spekreepjes knapperig.", "Niet te heet bakken"))
    recept1.voeg_stap_toe(Stap("Meng alles samen."))

    recepten.append(recept1)

    # ===== RECEPT 2 =====

    recept2 = Recept("Spaghetti Bolognese", "Klassieke pastasaus met gehakt.")

    recept2.voeg_ingredient_toe(Ingredient("spaghetti", 300, "gram", 350))
    recept2.voeg_ingredient_toe(Ingredient("tomatensaus", 400, "ml", 120))
    recept2.voeg_ingredient_toe(Ingredient("ui", 1, "stuk", 30))

    gehakt = Ingredient("gehakt", 300, "gram", 500)
    vegan_gehakt = Ingredient("vegan gehakt", 300, "gram", 300)
    gehakt.set_plantaardig_alternatief(vegan_gehakt)

    recept2.voeg_ingredient_toe(gehakt)

    recept2.voeg_stap_toe(Stap("Kook de spaghetti.", "Zorg dat het water goed zout is."))
    recept2.voeg_stap_toe(Stap("Bak gehakt met ui."))
    recept2.voeg_stap_toe(Stap("Voeg saus toe."))

    recepten.append(recept2)

    # ===== RECEPT 3 =====

    recept3 = Recept("Penne Pesto", "Snelle pasta met groene pesto.")

    recept3.voeg_ingredient_toe(Ingredient("penne", 300, "gram", 350))
    recept3.voeg_ingredient_toe(Ingredient("groene pesto", 150, "gram", 250))
    recept3.voeg_ingredient_toe(Ingredient("cherrytomaatjes", 150, "gram", 40))

    kaas = Ingredient("Parmezaanse kaas", 40, "gram", 180)
    vegan_kaas = Ingredient("vegan kaas", 40, "gram", 120)
    kaas.set_plantaardig_alternatief(vegan_kaas)

    recept3.voeg_ingredient_toe(kaas)

    recept3.voeg_stap_toe(Stap("Kook de penne volgens de verpakking.", "Zorg dat het water goed zout is."))
    recept3.voeg_stap_toe(Stap("Halveer de tomaatjes."))
    recept3.voeg_stap_toe(Stap("Meng de pesto door de warme pasta.", "Niet te heet, anders verliest de pesto smaak."))
    recept3.voeg_stap_toe(Stap("Voeg tomaatjes toe en serveer met kaas."))

    recepten.append(recept3)


    # ===== MENU =====

    while True:
        actie = input("Welkom bij het receptensysteem!\nKies een actie:\n1. Voeg recept toe\n2. Bekijk recepten\n3. Exit\n(1/2/3): ")

        if actie == "1":
            naam = input("Naam van het recept: ")
            omschrijving = input("Korte omschrijving: ")
            nieuw_recept = Recept(naam, omschrijving)

            while True:
                print("\nVoeg ingrediënten toe aan het recept.")
                Ingredient_naam = input("Naam van een ingrediënt: ")
                while True:
                    try:
                        Ingredient_hoeveelheid = float(input("Hoeveelheid: "))
                        break
                    except ValueError:
                        print("Ongeldige invoer. Voer een getal in.")
                Ingredient_eenheid = input("Eenheid (gram, ml, stuks, etc.): ")
                while True:
                    try:
                        Ingredient_kcal = int(input("Aantal kcal voor deze hoeveelheid: "))
                        break
                    except ValueError:
                        print("Ongeldige invoer. Voer een geheel getal in.")
                nieuw_recept.voeg_ingredient_toe(Ingredient(Ingredient_naam, Ingredient_hoeveelheid, Ingredient_eenheid, Ingredient_kcal))

                while True:
                    meer = input("Nog een ingrediënt? (j/n): ")
                    if meer in ("j", "n"):
                        break
                    else:
                        print("Voer 'j' of 'n' in.")
                if meer == "n":
                    break
                print("\n")

            while True:
                print("\nVoeg stappen toe aan het recept.")
                stap_beschrijving = input("Beschrijving van de stap: ")
                while True:
                    keuze_tip = input("Tip toegevoegen? (j/n): ")
                    if keuze_tip in ("j", "n"):
                        break
                    else:
                        print("Voer 'j' of 'n' in.")
                if keuze_tip == "j":
                    stap_tip = input("Tip voor deze stap: ")
                else:
                    stap_tip = None
                nieuw_recept.voeg_stap_toe(Stap(stap_beschrijving, stap_tip))

                while True:
                    meer = input("Nog een stap? (j/n): ")
                    if meer in ("j", "n"):
                        break
                    else:
                        print("Voer 'j' of 'n' in.")
                if meer == "n":
                    break
                print("\n")

            recepten.append(nieuw_recept)
            print("\nRecept toegevoegd!\n\n")

        elif actie == "2":
            print("\n\nKies een recept:\n")
            for i, recept in enumerate(recepten, 1):
                print(f"{i}. {recept.get_naam()}")

            while True:
                try:
                    keuze = int(input("\nNummer: ")) - 1
                    if 0 <= keuze < len(recepten):
                        break
                    else:
                        print("Kies een geldig nummer uit de lijst.")
                except ValueError:
                    print("Voer een geldig getal in.")

            while True:
                try:
                    personen = int(input("Voor hoeveel personen?: "))
                    if personen > 0:
                        break
                    else:
                        print("Voer een getal groter dan 0 in.")
                except ValueError:
                    print("Ongeldige invoer. Voer een geheel getal in.")
                    
            while True:
                plantaardig = input("Plantaardig? (j/n): ").strip().lower()
                
                if plantaardig in ("j", "n"):
                    plantaardig = plantaardig == "j"
                    break
                else:
                    print("Voer 'j' of 'n' in.")

            gekozen = recepten[keuze]
            gekozen.set_aantal_personen(personen)
            gekozen = gekozen.get_plantaardig_recept(plantaardig)

            print(gekozen)

            while True:
                try:
                    recept_actie = input("Mogelijke acties:\n1. Terug naar menu\n2. Verwijder recept\n(1/2): ")
                    
                    if recept_actie == "1":
                        break

                    if recept_actie == "2":
                        while True:
                            conformatie = input("Weet je zeker dat je dit recept wilt verwijderen? (j/n): ")
                            if conformatie in ("j", "n"):
                                if conformatie == "j":
                                    recepten.pop(keuze)
                                    print("Recept verwijderd.")
                                print("\n")
                                break
                            else:
                                print("Voer 'j' of 'n' in.")
                        break

                except ValueError:
                    print("Ongeldige invoer. Voer '1' of '2' in.\n")
            
            print("\n" * 5)  # scherm leegmaken

        elif actie == "3":
            print("\nTot ziens!\n")
            break


if __name__ == "__main__":
    main()
