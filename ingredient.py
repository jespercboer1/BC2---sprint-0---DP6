class Ingredient:
    def __init__(self, naam, hoeveelheid, eenheid, kcal):
        self.__naam = naam
        self.__hoeveelheid = hoeveelheid
        self.__eenheid = eenheid
        self.__kcal = kcal
        self.__plantaardig_alternatief = None

    def __str__(self):
        return f"{self.__hoeveelheid} {self.__eenheid} {self.__naam}"

    def set_hoeveelheid(self, hoeveelheid):
        self.__hoeveelheid = hoeveelheid

    def get_hoeveelheid(self):
        return self.__hoeveelheid

    def get_kcal(self):
        return self.__kcal

    # nieuw: getters voor naam en eenheid om externe code te helpen bij opschaling
    def get_naam(self):
        return self.__naam

    def get_eenheid(self):
        return self.__eenheid

    def set_plantaardig_alternatief(self, alternatief):
        self.__plantaardig_alternatief = alternatief

    def get_ingredient(self, plantaardig):
        if plantaardig and self.__plantaardig_alternatief is not None:
            return self.__plantaardig_alternatief
        return self
