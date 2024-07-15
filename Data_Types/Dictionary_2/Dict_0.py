# Dictionary - Ordered, Mutable and Unique (no duplicates) collection of pairs containing key and values

# (Keys must be unique and value may contain duplicates)

# myDict = {
#     "key":"value",
# }
# myDict = dict()

# myDict = {
#     "name" : "Royal",
#     "address" : "Gandhinagar",
#     "turnover" : "1000 Cr",
#     "students" : {
#         "dhairya" : (8, "Backend Intern", "1.5 Lac"),
#         "shreya" : (24, "Manager", "6.5 Cr"),
#         "dhyey" : (10, "CEO", "55 Cr"),
#         "marmik" : (9, "Frontend Engineer", "6 Lac"),
#         "arin" : (14, "FullStack Developer", "67 Lac"),
#     },
# }

# print(myDict)

###########################################################################

# Dhiraj Sir arranges Royal Jamanvaar for 1 day

# Employee_Choice = {
#     "Dhiraj Sir" : {"Breakfast" : "Dosa", "Lunch" : "Punjabi", "Dinner" : "khichdi-kadhi"},
#     "Zafar Sir" : {"Breakfast" : ['Fafda', 'Jalebi'], "Lunch" : "Kathiyawadi", "Dinner" : "Gujarati"},
#     "Shrey Sir" : {"Breakfast" : "Fruits", "Lunch" : "South Indian", "Dinner" : "Maggie"},
#     "Madhusudan Sir" : {"Breakfast" : "Solid Masti", "Lunch" : "Pizza", "Dinner" : "Solid Masti"},
#     "Mohak Sir" : {"Breakfast" : ["Saurashtra Ganthiya", "Jalebi"], "Lunch" : "Italian", "Dinner" : "Mexican"},
# }

# Accessing the data
# print(Employee_Choice, end="\n\n\n")

# using square bracket notation (dict[key])
# print(Employee_Choice["Madhusudan Sir"])
# print(Employee_Choice["Zafar Sir"])
# print(Employee_Choice["Krutarth Sir"])  # KeyError

# get() method  # returns None if key not found
# print(Employee_Choice.get("Dhiraj Sir"))

# choice = input("Enter the name: ")
# print(Employee_Choice.get(choice, Employee_Choice["Dhiraj Sir"]))

###########################################################################

# add new pairs of data

person = {
    'fname' : 'Cynthia',
    'lname' : 'Wright',
    'age' : 24,
    'favorite_colors' : ['blue', 'green'],
    'ssn' : "123-44-7678",
    'active' : True,
}

# person['active'] = False  # add/modifying value
# print(person)

# deleting a pair
# del person['age'] # deleting pair
# print(person)

for key, value in person.items():
    print(f"{key} : {value}")