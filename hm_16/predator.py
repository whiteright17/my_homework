from mammal import Mammal

class Predator(Mammal):
    def __init__(self, species, place, character, rank):
        super().__init__(species, place, character)
        self._rank = rank

    @property
    def rank(self):
        return self._rank

    @rank.setter
    def rank(self, value):
        self._rank = value

    def describe(self):
        return f"{self.character} {self.species} living in {self.place}, {self.rank} of animal."
