class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []
        self.__aantal_personen = 1

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)

    def get_ingredienten(self):
        return self.__ingredient_list

    def get_naam(self):
        return self.__naam

    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def set_aantal_personen(self, personen):
        self.__aantal_personen = personen

    def get_aantal_personen(self):
        return self.__aantal_personen

    def get_plantaardig_recept(self, plantaardig):
        nieuw = Recept(self.__naam, self.__omschrijving)
        nieuw.set_aantal_personen(self.__aantal_personen)

        for ingredient in self.__ingredient_list:
            nieuw.voeg_ingredient_toe(ingredient.get_ingredient(plantaardig))

        for stap in self.__stappen:
            nieuw.voeg_stap_toe(stap)

        return nieuw

    def __str__(self):
        # schaal de hoeveelheden naar het juiste aantal personen
        ingredient_lines = []
        for i in self.__ingredient_list:
            hoeveelheid = i.get_hoeveelheid() * self.__aantal_personen
            ingredient_lines.append(f"{hoeveelheid} {i.get_eenheid()} {i.get_naam()}")
        ingredienten = "\n".join(ingredient_lines)

        stappen = "\n".join(f"{idx+1}. {s}" for idx, s in enumerate(self.__stappen))

        # totaal aantal kilocalorieën berekenen (per ingrediënt en geschaald naar aantal personen)
        totaal_kcal = 0
        for i in self.__ingredient_list:
            # kcal-waarde hoort bij de hoeveelheid die in het recept staat
            totaal_kcal += i.get_kcal()
        totaal_kcal *= self.__aantal_personen

        return f"""
{self.__naam}
{"-" * len(self.__naam)}

{self.__omschrijving}

Ingrediënten:
{ingredienten}

Stappen:
{stappen}

Totaal kcal: {totaal_kcal}
"""
