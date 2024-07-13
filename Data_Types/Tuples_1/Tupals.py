"""
Tuple -> Immutable Sequence

syntax:
    tuple() -> represented by ()

Changeable? -> False
Duplicates Allowed? -> True

"""

# myTuple = (3, 5, 2, 56, 8, 4, 3, 12, 5, 78, "2", ["2", 34, 2, 2])
# print(myTuple, type(myTuple), id(myTuple))
# print(id(myTuple))

# print("Index:", myTuple.index(2, 6, 12))
# print("Len:", len(myTuple))
# print("Count:", myTuple.count(2))

# myTuple[11][0] = 23

# print(myTuple)


# Ordering tuple by list
"""
Input:
tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)], sortList = ['l', 'a', 'k', 'e']

Output:
[('l', 5), ('a', 1), ('k', 2), ('e', 6)]
"""
# tupList = [('l', 5), ('k', 2), ('a', 1), ('e', 6)]
# sortList = ['l', 'a', 'k', 'e']
# output = [t for k in sortList for t in tupList if t[0] == k]
# print(output)


'''
Example 2:
Python program to convert decimal to binary (in bytes)
Input:
tuple1 = (1234, 331, 437, 59, 63)

Output:
(binary of 1, binary of 2, binary of 3, binary of 4, binary of 5)
'''

# num = 25
# ans = ""

# while num > 0:
#     ans += str(num%2)
#     num//=2

# print(ans[::-1].zfill(8))

# print(bin(25)[2:])


tuple1 = (1234, 331, 437, 59, 63)
tuple2 = (1, 3, 5, 2, 5)

for i in range(len(tuple1)):
    # print(bin(tuple1[i])[2:])
    print(tuple1[i] & tuple2[i], end=", ")