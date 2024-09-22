class Animal:
    species_count = 0   # class variable to keep track of total animals

    def __init__(self, name) -> None:
        self.name = name
        Animal.increment_species_count()

    @classmethod
    def increment_species_count(cls):
        cls.species_count += 1  # Modifying class variable
    
    @classmethod
    def get_species_count(cls):
        return cls.species_count
    
if __name__ == "__main__":
    a1 = Animal("Tiger")
    a2 = Animal("Elephant")
    a3 = Animal("Cat")
    a4 = Animal("Lion")
    a5 = Animal("Dog")

    print(Animal.get_species_count())