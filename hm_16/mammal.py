from animal import Animal


class Mammal(Animal):
    def __init__(self, species, place, character):
        super().__init__(species, place)
        self._character = character

    @property
    def character(self):
        return self._character

    @character.setter
    def character(self, value):
        self._character = value

    def describe(self):
        return f"{self.character} {self.species} living in {self.place} with fur color {self.character}"
