# Type 3: Multilevel Inheritance (A class inherits from another derived class)

# Base Class
class KachchaAam:
    def tart(self):
        return "Kachcha Aam: Khatti-mahatti, zubaan pe bijli giraane wali."

# Derived Class
class KachchaAamJuice(KachchaAam):
    def make_juice(self):
        return "Juice: Paani milake thoda sugar, ab zubaan thoda handle kar sakti hai."

# Derived from KachchaAamJuice (Multilevel)
class KachchaAamPanna(KachchaAamJuice):
    def make_panna(self):
        return "Aam Panna: Aam ka juice, chaat masala, aur garmi ka tod!"

# Usage
panna = KachchaAamPanna()
print(panna.tart())  # Inherited from KachchaAam
print(panna.make_juice())  # Inherited from KachchaAamJuice
print(panna.make_panna())  # Method of KachchaAamPanna
