# silly_animals = {
#     "duck" : "Quack",
#     "cat" : "Meow",
#     "dog" : "Woof",
#     "cow" : "Moo",
#     "pig" : "oink",
# }

# print(silly_animals)

# silly_animals.clear()
# silly_animals_2 = silly_animals.copy()

# new_dict = dict.fromkeys(['a', 'b', 'c'], 0)

# weird_food_pairs = {
#     "Peanut Butter" : "Pickels",
#     "Pizza" : "Pineapple",
#     "Ice Cream" : "Ketchup",
#     "Fries" : "Chocolate Sauce",
#     "Butter Milk" : "Hershey's Chocolate Syrup",
#     "Marie Gold Biscuit" : "Lemon Juice",
# }

# print(weird_food_pairs.get("Marie Gold Biscuit", "Chai Latte"))

# print(weird_food_pairs.items())

# k = list(weird_food_pairs.keys())
# v = list(weird_food_pairs.values())
# print(k, v, sep="\n")

# strange_inventions = {
#     "Cat Translator" : "translates meows to human language",
#     "Self-tying Shoes" : "Shoes that tie themselves",
#     "Invisible Umbrella" : "Protect rain without blocking view",
#     "Teleportation Toaster" : "Toasts bread and teleports is to your plate",
# }

# print(strange_inventions.pop("Invisible Umbrella 2.0", "No such key present!"))

# for k, v in strange_inventions.items():
#     print(f"{k} : {v}", end='\n')

# k, v = strange_inventions.popitem();
# print(k, v, sep=", ")

# print(strange_inventions.setdefault("abcd", "xyz"));

# print(strange_inventions.update({"abcdxyz" : None}))

# print(strange_inventions)

# Task

# 1. Check if a Given Key Already Exists in Dictionary
# -> If you have learned about Python dictionaries, you will know that you can check if a given key exists or not in multiple ways. 

# D1 = {'first_name' : 'Dhairya', 'age' : 20, 'height' : 5.5 , 'job' : 'Developer', 'company': 'Amazon'}

# input_key = input("Enter the key: ")

# print("Key Exist!" if input_key.casefold() in D1.keys() else "Key Doesn't Exist!")


# HW. Extract Unique Values in a Given Dictionary
# -> In a dictionary, the keys have to be unique, whereas the values can be duplicated. So, given a dictionary as shown below, how can you print all the unique values it has?

# D1 = {	
#     'list1': [4, 7, 10, 20], 
#     'list2': [7, 16, 9, 10], 
#     'list3': [13, 10, 4, 8], 
#     'list4': [7, 20, 6, 11]
# }

# Output = [4, 6, 7, 8, 9, 10, 11, 13, 16, 20]