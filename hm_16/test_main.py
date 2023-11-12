from predator import Predator

lion = Predator(species="Lion", place="Africa", character="Wicked", rank="King")

print(lion.species)
lion.species = "Tiger"

print(lion.describe())
