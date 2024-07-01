'''
List Comprehension: [expression for item in iterable if condition]

for else -> [expression_1 if condition else expression_2 for item in iterable]

'''

# van
# skwares = [num**2 for num in range(11)]
# print(skwares)

# van point van
# evan_skwares = [num**2 for num in range(11) if (num % 2) == 0]
# print(evan_skwares)

# too
# basic = [i for i in range(11)]
# numbers = [num**2 if (num%2 == 0) else num**3 for num in range(11)]
# for i in range(11):
#     print(f"{basic[i]} -> {numbers[i]}")

# not too complicated
# @doubtsafe
# new_list = [int(i**0.5) for i in [num**2 for num in range(11) if (num % 2) == 0]]
# print(new_list)