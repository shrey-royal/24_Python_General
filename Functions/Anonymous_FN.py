# Anonymous Functions in Python

# lambda parameters: expression => syntax

# variable = lambda parameter: expression   => function definition
# variable(parameter) => function calling

# Normal function
# def square(x):
#     return x*x

# ans = square(4)
# print(ans)

# lambda function
# square2 = lambda x: x*x
# print(square2(6))


# lambda with multiple parameters
# add = lambda a=23, b=34: a+b
# print(add(2, 3))
# print(add())


# parameterless lambda functions

# greet = lambda : "Hello!"
# print(greet())

# inline lambda
# print((lambda x : x*x*x)(3))
# -------------------------------------------------------------------------------

import random

pairs = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(5)]
print(pairs)

# map(function, iterable) -> used to process data (work with any function who returns some data)

# //Normal
# def map_func(elem):
#     return elem[0]*elem[1]

# mappedList = list(map(map_func, pairs))
# print(mappedList)

# //Lambda
# mappedList = list(map(lambda elem: elem[0]*elem[1], pairs))
# print(mappedList)
# -----------------------------------------------------------------------------

# filter(function, iterable) -> used with boolean function

# //Normal
# def filter_func(elem):
#     max_elem = max(elem[0], elem[1])
#     return max_elem > 7

# filteredList = list(filter(filter_func, pairs))
# print(filteredList)

# //Lambda
# filteredList = list(filter(lambda elem: max(elem[0], elem[1]) > 7, pairs))
# print(filteredList)

# -----------------------------------------------------------------------------

# //sorted()
# myList = [67, 56, 43, 23, 435, 456, 67, 3, 23, 23, 2]
# sortedList = list(filter(lambda x: x%2 == 0, sorted(myList)))
# sortedList = sorted(myList, key=lambda x: -x)

# sortedList = sorted(pairs, key=lambda x: x[0])
# print(sortedList)

# fruits = [(1, '🍉'), (2, '🍒'), (3, '🍎'), (4, '🍅')]
# sortedFruits = sorted(fruits, key=lambda x: x[0])
# print(sortedFruits)

num_list = [23, 345, 234, 56, 23, 45, 567]
s1 = sorted(num_list, key=lambda x: x)
s2 = sorted(num_list, key=lambda x: x%10)
print(s1)
print(s2)