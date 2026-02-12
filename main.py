from recept import Recept 
from ingredient import Ingredient
from stap import Stap

def main():
    recepten = []

    recept1 = Recept("Tagliatelle Carbonara", "Snelle romige pasta met spek en kaas.")

    recept1.voeg_ingredient_toe(Ingredient("tagliatelle", 300, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("spekreepjes", 150, "gram"))
    recept1.voeg_ingredient_toe(Ingredient("eieren", 2, "stuks"))
    recept1.voeg_ingredient_toe(Ingredient("Parmezaanse kaas", 50, "gram"))

    recept1.voeg_stap_toe(Stap("Kook de tagliatelle volgens de verpakking."))
    recept1.voeg_stap_toe(Stap("Bak de spekreepjes knapperig in een pan."))
    recept1.voeg_stap_toe(Stap("Klop de eieren met de kaas in een kom."))
    recept1.voeg_stap_toe(Stap("Meng de pasta met het spek en roer daarna het eimengsel erdoor."))

    recepten.append(recept1)


    recept2 = Recept("Spaghetti Bolognese", "Klassieke pastasaus met gehakt.")

    recept2.voeg_ingredient_toe(Ingredient("spaghetti", 300, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("gehakt", 300, "gram"))
    recept2.voeg_ingredient_toe(Ingredient("tomatensaus", 400, "ml"))
    recept2.voeg_ingredient_toe(Ingredient("ui", 1, "stuk"))

    recept2.voeg_stap_toe(Stap("Kook de spaghetti volgens de verpakking."))
    recept2.voeg_stap_toe(Stap("Bak het gehakt rul en voeg de gesnipperde ui toe."))
    recept2.voeg_stap_toe(Stap("Voeg de tomatensaus toe en laat 10 minuten sudderen."))
    recept2.voeg_stap_toe(Stap("Serveer de saus over de spaghetti."))

    recepten.append(recept2)


    recept3 = Recept("Penne Pesto", "Snelle pasta met groene pesto.")

    recept3.voeg_ingredient_toe(Ingredient("penne", 300, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("groene pesto", 150, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("cherrytomaatjes", 150, "gram"))
    recept3.voeg_ingredient_toe(Ingredient("Parmezaanse kaas", 40, "gram"))

    recept3.voeg_stap_toe(Stap("Kook de penne volgens de verpakking."))
    recept3.voeg_stap_toe(Stap("Halveer de tomaatjes."))
    recept3.voeg_stap_toe(Stap("Meng de pesto door de warme pasta."))
    recept3.voeg_stap_toe(Stap("Voeg tomaatjes toe en serveer met kaas."))

    recepten.append(recept3)


    print("Kies een recept:\n")
    for i, recept in enumerate(recepten, 1):
        print(f"{i}. {recept._Recept__naam}")

    keuze = int(input("\nNummer: ")) - 1
    print(recepten[keuze])


if __name__ == "__main__":
    main()
