# Type 5: Hybrid Inheritance (Combination of more than one type of inheritance, often a mix of hierarchical and multiple inheritance)

# Base Class
class Imli:
    def description(self):
        return "Imli: Khatta, meetha, aur har mood mein fit."

# Derived Class 1
class ImliKiChutney(Imli):
    def make_chutney(self):
        return "Imli ki Chutney: Khatta, teekha, aur poori chaat ka soul."

# Derived Class 2
class ImliKiGoli(Imli):
    def make_goli(self):
        return "Imli ki Goli: Khatta-meetha, chusne waala candy... childhood flashback!"

# Hybrid Inheritance
class ImliFusion(ImliKiChutney, ImliKiGoli):
    def fusion_dish(self):
        return "Imli Fusion: Chutney aur goli ka combo, full on chatpata dhamaka!"

# Usage
fusion = ImliFusion()
print(fusion.description())  # Inherited from Imli
print(fusion.make_chutney())  # Inherited from ImliKiChutney
print(fusion.make_goli())  # Inherited from ImliKiGoli
print(fusion.fusion_dish())  # Method of ImliFusion

