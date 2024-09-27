# Type 4: Hierarchical Inheritance (Multiple derived classes inherit from the same base class)

# Base Class
class Jamun:
    def description(self):
        return "Jamun: Ek chatpata purple phal, jo muh ka rang badal deta hai!"

# Derived Class 1
class JamunJuice(Jamun):
    def make_juice(self):
        return "Jamun Juice: Bilkul kadak thanda, garmi ka asli jawaab."

# Derived Class 2
class JamunChutney(Jamun):
    def make_chutney(self):
        return "Jamun Chutney: Teekhi, chatpati, aur zubaan par aag lagaane wali."

# Usage
juice = JamunJuice()
chutney = JamunChutney()

print(juice.description())  # Inherited from Jamun
print(juice.make_juice())  # Method of JamunJuice

print(chutney.description())  # Inherited from Jamun
print(chutney.make_chutney())  # Method of JamunChutney

