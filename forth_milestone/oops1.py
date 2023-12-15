class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        return f"{self.name} the {self.species} says {sound}"

# Creating an instance of Animal
dog = Animal("Buddy", "Dog")

# Using the method of the class
print(dog.make_sound("Woof"))

cat= Animal("Tom","Cat")
print(cat.make_sound("Meau"))
