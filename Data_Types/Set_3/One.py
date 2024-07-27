'''
set - A set is an unordered collections of items, every element should be unique(no duplicates) and mutable means we can change it.

set is mutable(changeable), unordered(no index), no duplicates allowed
syntax -: 
mySet = {1, 2, 3, ..., n}
'''

# mySet = set([1, 2, 23, 12, 3334, 354, 34, 23, 12, 5, 32])
# mySet1 = {} # dictionary

# print(mySet, type(mySet))

# basics of set

# stores multiple data types
# mySet = {1, 2, 3, "Python", 2.3, 'd'}
# print(mySet)

# my_Empty_Set = set()
# print(type(my_Empty_Set))

# set can't have duplicates
# myList = {11, 23, 11, 34, 22, 34, 22, 45, 456, 546, 56, 45, 56}
# print(myList)

# myList = ['veggies', 'snacks', 'biscoots', 'fruits', 'ice-creams', 'chocolates']
# print(set(myList))

# skills of arin

# skills = {'Eating', 'Python Programming', 'Databases', 'Software design', 'Networking'}

# skills.add('Critical Thinking')
# print(skills)

# skills.discard('Databases')
# print(skills)

mySet = {23, 45, 79, 34, 13}
dummy_set = {23, 45, 799, 34, 13}
disjoint_set = {2, 3}
new_set = {23, 45}

# print(mySet.difference(dummy_set))
# mySet.difference_update(dummy_set)

# print({1, 2, 3}.isdisjoint({23, 22, 4}))
# print(mySet.intersection(dummy_set))
# mySet.intersection_update(dummy_set)
# print(new_set.issubset(dummy_set))
# print(mySet.pop())
# mySet.remove(45)
# print(mySet.symmetric_difference(dummy_set))
# mySet.symmetric_difference_update(dummy_set)

# mySet.update((3, 89))
# print(mySet)

print({1, 2}.union({3, 4}))

del mySet, dummy_set, disjoint_set, new_set
# print(mySet)