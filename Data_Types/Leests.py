"""
List -> Mutable Sequence

syntax:
    list() -> represented by []

Changeable? -> True
Duplicates Allowed? -> True

"""

# declaration of list
# list_var = []
# list_var = list()   # using constructor

# print(list_var, type(list_var), sep="\t")

# initializing lists

# fruits = ["Apple", "Banana", "Cherry", "Dragon Fruit", "Papaya", "Strawberry"]

# prime_numbers = list([2, 3, 5, 7, 11, 13, 17, 19, 20-1])

# print(fruits, prime_numbers)

# cgpa = [7.00, 8.00, 8.68, 8.51, 6.99, 3.44, 3.43, 6.74]

# print(cgpa[::2])

# print(prime_numbers)

# for i in fruits:
#     # print(i[0:2])
#     print(i)


indian_veggies = [
    "Bitter Gourd (Karela)",
    "Bottle Gourd (Lauki)",
    "Ridge Gourd (Turai)",
    "Snake Gourd (Galka)",
    "Pointed Gourd (Parwal)",
    "Drumstick (Moringa)",
    "Taro Root (Arbi)",
    "Elephant Foot Yam (Suran)",
    "Ash Gourd (Petha)",
    "Ivy Gourd (Tindora)",
    "Fenugreek Leaves (Methi)",
    "Amaranth Leaves (Patra)",
    "Colocasia Leaves (Arbi ke Patte)",
    "Beet Greens (Chukandar ke Patte)",
    "Mustard Greens (Sarson)",
    "Radish Greens (Mooli ke Patte)",
    "Spinach (Palak)",
    "Fenugreek Seeds Sprouts (Methi Dana)",
    "Cluster Beans (Gawar Phali)",
    "French Beans",
    "Yardlong Beans (Bora)",
    "Broad Beans (Sem)",
    "Green Peas (Matar)",
    "Corn (Makai)",
    "Bamboo Shoots (Karil)",
    "Jackfruit (Kathal)",
    "Raw Banana (Kachcha Kela)",
    "Green Papaya (Kachcha Papita)",
    "Indian Gooseberry (Amla)",
    "Curry Leaves (Kadi Patta)",
    "Raw Mango (Keri)",
    "Sponge Gourd (Nenua)",
    "Brinjal (Baingan)",
    "Lady Finger (Bhindi)",
    "Cabbage (Patta Gobi)",
    "Cauliflower (Phool Gobi)",
    "Radish (Mooli)",
    "Turnip (Shalgam)",
    "Carrot (Gajar)",
    "Tomato (Tamatar)"
]

#methods
########################################################
# indian_veggies.append("Bell Pepper (Capsicum)", )
# print(indian_veggies)
########################################################
# print(indian_veggies.count("Spinach (Palak)"))

# count = 0
# for i in indian_veggies:
#     if "spinach (palak)".casefold() == i.casefold():
#         count+=1;

# print(count)
########################################################

# indian_veggies.clear()
# print(indian_veggies)
########################################################

# l = indian_veggies   # this will add a new label to an existing variable
# l.append("Bell Pepper (Capsicum)")

# l = indian_veggies.copy()
# l.append("Bell Pepper (Capsicum)")
# print(id(l), id(indian_veggies), sep="\t\t")

# print(indian_veggies)
########################################################
# E