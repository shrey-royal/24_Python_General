import random

# numbers = [random.randint(0, 100) for _ in range(10)]
nums = (17, 65, 21, 0, 27, 14, 12, 66, 14, 39)

print(nums)

# n1, _, n3 = 1, 2, 3 # (n1 = 1, n2 = 2, n3 = 3)
# print(n1, n3)

# n1 = 1, 2, 3    # packing - default type -> tuple
# print(n1)


# print("unpack-1: ", end='')
# n1, n2, *n3 = nums    # * will return packed data in list form
# *n1, n2, n3 = nums
# n1, *n2, n3 = nums

print("unpack-2: ", end='')
n, *n2, n3 = 23, nums, 45


print(n, n2, n3)

# arin : 23 [(17, 65, 21, 0, 27, 14, 12, 66, 14, 39), 45]
# nupur: 23 [(17, 65, 21, 0, 27, 14, 12, 66), 14, 39, 45]
# nupur: 23 [(17, 65, 21, 0, 27, 14, 12, 66, 14, 39), 45, 45, 45]