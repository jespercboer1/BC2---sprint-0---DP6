class Recept:
    def __init__(self, naam, omschrijving):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredient_list = []
        self.__stappen = []

    def voeg_ingredient_toe(self, ingredient):
        self.__ingredient_list.append(ingredient)

    def get_ingredient(self):
        for i in self.__ingredient_list:
            print(i)

    def get_naam(self):
        print(self.__naam)
        
    def voeg_stap_toe(self, stap):
        self.__stappen.append(stap)

    def __str__(self):
        ingredienten = "\n".join(f"{i}" for i in self.__ingredient_list)
        stappen = "\n".join(f"{idx+1}. {s}" for idx, s in enumerate(self.__stappen))

        return f"""
{self.__naam}
{"-" * len(self.__naam)}

{self.__omschrijving}

Ingrediënten:
{ingredienten}

Stappen:
{stappen}
        """
