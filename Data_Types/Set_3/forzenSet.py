# frozen set - immutable and constants
# when a frozen set is declared then it can't be changed

# set1 = frozenset({1, 23, 56, 78, 34, 89, 234})
# print(set1)
# print(type(set1))

# name = frozenset({'M', 'a', 'r', 'm', 'i', 'k'})
# print(name)
###############################

# s1 = {'M', 'a', 'r', 'm', 'i', 'k'}

# list1 = list([1, 2, 3, 4, 5, 6])
# fs = frozenset(list1)
# d1 = dict()

# for i, j in zip(s1, fs):
#     # d1[i] = j
#     d1.update({i : j})

# print(d1)
###############################


fs = frozenset([1, 2, 3, 4, 5])

fs_union = fs.union([4, 5, 6, 7])
fs_intersection = fs.intersection([2, 3, 4, 5])

print(fs_union)
print(fs_intersection)

# fs.add(6)     # AttributeError: 'frozenset' object has no attribute 'add'
# fs.remove(4)  # AttributeError: 'frozenset' object has no attribute 'remove'

"""
# Summary of Collections

--> List - Ordered, Mutable & Allow Duplicates

--> Tuple = Ordered, Immutable & Allow Duplicates

--> Set - UnOrdered, Immutable & Unique (Duplicates Not Allowed)
    -> Frozen Set => UnOrdered, Immutable, Constant, Unique

--> Dictionary - ordered, Mutable & Unique(Keys), Duplicate Values are Allowed

"""