'''
Problem 3: Spiral Order Matrix Traversal
Description:
Given a 2D list (matrix), write a function to return all elements of the matrix in spiral order.

Example:

input_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
output_list = [1, 2, 3, 6, 9, 8, 7, 4, 5]
'''

# zip() -> used to combine 2 or more list and returns a single list as output

# list1 = [3425, 345, 4567]
# list2 = ["Abcd", "Xyz"]

# result = list(zip(list1, list2))
# print(result)
# result = zip(list1, list2)

# for i in enumerate(result):
#     print(i)

# print(list(zip(*[[1, 2, 3], [4, 5, 6]])))


input_matrix = [
    [1, 2, 3, 11],
    [4, 5, 6, 22],
    [7, 8, 9, 33]
]

result = []

while input_matrix:
    result += input_matrix.pop(0)
    input_matrix = [list(row) for row in zip(*input_matrix)][::-1]

print(result)