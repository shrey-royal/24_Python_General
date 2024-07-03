import list_data as data

# Nested List
var = [data.veggies, data.fruits]
# print(type(var))
# print(type(var[0]))
# print(type(var[0][0]))
# print(var[0][0])

# print(var[0][18])

# var[1].clear()
# print(var)

# for i in var:
#     for j in i:
#         print(j)

# list_index = 0
# while list_index < len(var):     # var == var
#     index = 0
#     while index < len(var[list_index]):
#         print(f"{list_index}, {index} -> {var[list_index][index]}")
#         index += 1
#     list_index += 1

# flatted_lists = [item for list_item in var for item in list_item]

# print(flatted_lists)

# var[1][0] = ""
# var[0].append("abcd")

# print(var)