from mammal import mammal


class predator(mammal):
    def __init__(self, species, place, character, rank):
        super().__init__(species, place, character)
        self.rank = rank

    def describe(self):
        return f"{self.character} {self.species} living in {self.place}, {self.rank} of animal."
