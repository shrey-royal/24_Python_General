# Type 2: Multiple Inheritance (A class inherits from more than one base class)

# Base Class 1
class NariyalPaani:
    def refresh(self):
        return "Nariyal Paani: Thandi hawa, thanda paani... life set hai!"

# Base Class 2
class Rabri:
    def sweet(self):
        return "Rabri: Yeh toh asli 'dadi ka pyar' hai, extra meetha!"

# Derived Class with Multiple Inheritance
class FaludaKulfi(NariyalPaani, Rabri):
    def fusion_flavor(self):
        return "Faluda Kulfi: Thanda nariyal, meethi rabri... bas yahi toh chahiye zindagi mein!"

# Usage
kulfi = FaludaKulfi()
print(kulfi.refresh())  # Inherited from NariyalPaani
print(kulfi.sweet())  # Inherited from Rabri
print(kulfi.fusion_flavor())  # Method of FaludaKulfi
