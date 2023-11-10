from animal import Animal


class mammal(Animal):
    def __init__(self, species, place, character):
        super().__init__(species, place)
        self.character = character

    def describe(self):
        return f"{self.character} {self.species} living in {self.place} with fur color {self.character}"
