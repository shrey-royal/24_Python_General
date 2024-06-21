'''
Loop: Entry-Controlled Loop

1. for: fixed iteration
syntax:
    for iterator_var in iterable:
        # body

2. while: unfixed iteration
syntax:
    while condition:
        # body

'''

# range(start, stop, step) function

# for i in range(1, 10):
#     print(i, end=", ")


# user_input = int(input("Enter the end: "))

# for i in range(user_input):
#     print(i, end=", ")
# print("\b\b.")

# i = 1
# while i<=10:
#     print(i, end=", ")
#     i+=1



# -------------------------------------------------
# choice = 1
# while choice != 0:
#     print("1. Tea\n2. Coffee\n3. Milkshake\n4. Lassi\n0. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice > 0 and choice <= 4: print("Good!")
#     elif choice == 0: continue
#     else: print("Invalid Choice! Try Again")


# while True:
#     print("1. Tea\n2. Coffee\n3. Milkshake\n4. Lassi\n0. Exit")
#     choice = int(input("Enter your choice: "))
#     if choice > 0 and choice <= 4: print("Good!")
#     elif choice == 0: break
#     else: print("Invalid Choice! Try Again")


# Patterns
"""
for i in range(5):
    for j in range(5):
        print(f"({i}, {j})\t", end="")
    print()

# Square
print("\n")
for i in range(5):
    for j in range(5):
        print("* ", end="")
    print()

# Hollow Square
print("\n")
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==4 or j==4: print("* ", end="")
        else: print("  ", end="")
    print()

# Box with diagonal
print("\n")
for i in range(5):
    for j in range(5):
        if i==0 or j==0 or i==4 or j==4 or i==j: print("* ", end="")
        else: print("  ", end="")
    print()
"""

r = int(input("Enter rows: "))
c = int(input("Enter cols: "))

print("\n")
for i in range(r):
    for j in range(c):
        if i==j or i+j==r-1: print("* ", end="")
        else: print("  ", end="")
    print()