from recept import Recept
from ingredient import Ingredient
from stap import Stap

from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

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

        #keuze tussen recepten bekijken, toevoegen of exitten
        actie = input("Welkom bij het receptensysteem!\nKies een actie:\n1. Voeg recept toe\n2. Bekijk recepten\n3. Exit\n(1/2/3): ")

        #keuze recept toevoegen
        if actie == "1":
            # recept aanmaken (naam en omschrijving)
            naam = input("Naam van het recept: ")
            omschrijving = input("Korte omschrijving: ")
            nieuw_recept = Recept(naam, omschrijving)

            # ingredienten toevoegen
            while True:
                print("\nVoeg een ingrediënten toe aan het recept.")
                Ingredient_naam = input("Naam van een ingrediënt: ")
                # validatie voor hoeveelheid en kcal, zodat er geen fouten ontstaan in het recept
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
                ingredient = Ingredient(Ingredient_naam, Ingredient_hoeveelheid, Ingredient_eenheid, Ingredient_kcal)

                # vraag of er een plantaardig alternatief toegevoegd moet worden
                while True:
                    keuze_alternatief = input("Plantaardig alternatief toevoegen? (j/n): ")
                    if keuze_alternatief in ("j", "n"):
                        break
                    else:
                        print("Voer 'j' of 'n' in.")

                # als de gebruiker een alternatief wil toevoegen, vraag dan de details van het alternatief en koppel het aan het ingrediënt
                if keuze_alternatief == "j":
                    print("\nVoeg een alternatief ingrediënten toe.")
                    alternatief_naam = input("Naam van het plantaardige alternatief: ")
                    # validatie voor hoeveelheid en kcal, zodat er geen fouten ontstaan in het recept
                    while True:
                        try:
                            alternatief_hoeveelheid = float(input("Hoeveelheid: "))
                            break
                        except ValueError:
                            print("Ongeldige invoer. Voer een getal in.")
                    alternatief_eenheid = input("Eenheid (gram, ml, stuks, etc.): ")
                    while True:
                        try:
                            alternatief_kcal = int(input("Aantal kcal voor deze hoeveelheid: "))
                            break
                        except ValueError:
                            print("Ongeldige invoer. Voer een geheel getal in.")
                    # maak het alternatief ingrediënt aan en koppel het aan het originele ingrediënt
                    ingredient.set_plantaardig_alternatief(Ingredient(alternatief_naam, alternatief_hoeveelheid, alternatief_eenheid, alternatief_kcal))
                    print("\nAlternatief toegevoegd!\n")

                # voeg het ingrediënt (met eventueel alternatief) toe aan het recept
                nieuw_recept.voeg_ingredient_toe(ingredient)
                print("\nIngrediënt toegevoegd!\n")

                # vraag of er nog een ingrediënt toegevoegd moet worden
                while True:
                    meer = input("Nog een ingrediënt? (j/n): ")
                    if meer in ("j", "n"):
                        break
                    else:
                        print("Voer 'j' of 'n' in.")
                if meer == "n":
                    break
                print("\n")

            # stappen toevoegen
            while True:
                print("\nVoeg een stap toe aan het recept.")
                stap_beschrijving = input("Beschrijving van de stap: ")
                # vraag of er een tip toegevoegd moet worden voor deze stap
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

                # vraag of er nog een stap toegevoegd moet worden
                while True:
                    meer = input("Nog een stap? (j/n): ")
                    if meer in ("j", "n"):
                        break
                    else:
                        print("Voer 'j' of 'n' in.")
                if meer == "n":
                    break
                print("\n")

            # voeg het nieuwe recept toe aan de lijst van recepten
            recepten.append(nieuw_recept)
            print("\nRecept toegevoegd!\n\n")

        #keuze recepten bekijken
        elif actie == "2":
            #kies recept
            print("\n\nKies een recept:\n")
            for i, recept in enumerate(recepten, 1):
                print(f"{i}. {recept.get_naam()}")

            #keuze tussen recepten
            while True:
                try:
                    keuze = int(input("\nNummer: ")) - 1
                    if 0 <= keuze < len(recepten):
                        break
                    else:
                        print("Kies een geldig nummer uit de lijst.")
                except ValueError:
                    print("Voer een geldig getal in.")

            # aantal personen
            while True:
                try:
                    personen = int(input("Voor hoeveel personen?: "))
                    if personen > 0:
                        break
                    else:
                        print("Voer een getal groter dan 0 in.")
                except ValueError:
                    print("Ongeldige invoer. Voer een geheel getal in.")
                    
            # plantaardig
            while True:
                plantaardig = input("Plantaardig? (j/n): ").strip().lower()
                
                if plantaardig in ("j", "n"):
                    plantaardig = plantaardig == "j"
                    break
                else:
                    print("Voer 'j' of 'n' in.")

            # recept tonen
            gekozen = recepten[keuze]
            gekozen.set_aantal_personen(personen)
            gekozen = gekozen.get_plantaardig_recept(plantaardig)

            print(gekozen)

            #keuze tussen terug naar menu, pdf genereren of recept verwijderen
            while True:
                try:
                    recept_actie = input("Mogelijke acties:\n1. Terug naar menu\n2. PDF genereren\n3. Verwijder recept\n(1/2/3): ")
                    
                    # terug naar menu
                    if recept_actie == "1":
                        break

                    # PDF genereren
                    if recept_actie == "2":
                        filename = f"{gekozen.get_naam().replace(' ', '_')}.pdf"

                        doc = SimpleDocTemplate(filename, pagesize=A4)
                        styles = getSampleStyleSheet()

                        story = []

                        # Titel
                        story.append(Paragraph(f"<b>{gekozen.get_naam()}</b>", styles["Title"]))
                        story.append(Spacer(1, 12))

                        # Omschrijving
                        story.append(Paragraph(f"<i>{gekozen.get_omschrijving()}</i>", styles["BodyText"]))
                        story.append(Spacer(1, 20))

                        # Ingrediënten titel
                        story.append(Paragraph("<b>Ingrediënten</b>", styles["Heading2"]))
                        story.append(Spacer(1, 10))

                        # Ingrediënten lijst
                        for ingredient in gekozen.get_ingredienten():
                            tekst = f"- {ingredient.get_hoeveelheid()} {ingredient.get_eenheid()} {ingredient.get_naam()}"
                            story.append(Paragraph(tekst, styles["BodyText"]))

                        story.append(Spacer(1, 20))

                        # Stappen titel
                        story.append(Paragraph("<b>Bereidingsstappen</b>", styles["Heading2"]))
                        story.append(Spacer(1, 10))

                        # Stappen lijst
                        for i, stap in enumerate(gekozen.get_stappen(), 1):
                            story.append(Paragraph(f"{i}. {stap.__str__()}", styles["BodyText"]))

                            story.append(Spacer(1, 8))

                        doc.build(story)

                        print(f"PDF gegenereerd: {filename}\n")
                        break

                # recept verwijderen
                    if recept_actie == "3":
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
                    print("Ongeldige invoer. Voer '1', '2' of '3' in.\n")
            
            print("\n" * 5)  # scherm leegmaken

        #keuze exitten
        elif actie == "3":
            print("\nTot ziens!\n")
            break


# entry point
if __name__ == "__main__":
    main()
