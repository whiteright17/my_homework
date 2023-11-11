from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, species, place):
        self._species = species
        self._place = place

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        self._species = value

    @property
    def place(self):
        return self._place

    @place.setter
    def place(self, value):
        self._place = value

    @abstractmethod
    def describe(self):
        pass
