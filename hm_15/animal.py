class Animal:
    def __init__(self, species, place):
        self.species = species
        self.place = place

    def describe(self):
        return f"{self.species} living in {self.place}"
