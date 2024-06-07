# String declaration

name = "Mithilbhai"
message = 'Hello, Mithilbhai'

# f_ormatted string (fstring)

message = f"Good evening, {name}"

greetings = 'Good' ' Morning!' ' Dhyey' # concatenation

greeting = 'Good '
time = 'Evening'

greeting = greeting + time + '!'
# print(greeting)

# -----------------------------------------------------------

# Accessing string element

# str = None

str = 'Python String'
# print(str[0])
# print(str[12])

# print(len(str)) # len(any variable)

# print(str[-13])
# print(str[12])

# -----------------------------------------------------------

# Slicing - a TECHNIQUE that helps in extraction of specific words/parts from string.

# syntax: Sequence[start(inclusive):end(exclusive):step-1]

# word = "Artificial_Intelligence"

# Positive Slicing

# print(word[0:4])
# print(word[4:10])

''' 
# smol praktis
new_word = word[:4] + '-' + word[4:10]
new_word = f'{word[:4]} - {word[4:10]}'
print(new_word)
'''

'''
# Another example
mithai = "Keri No Ras"

fruit = mithai[:4]
by = mithai[5:7]
juice = mithai[8:11]

print(fruit, by, juice, sep='\n')
'''

# Step - skip characters

word = "0_1_2_3_4_5_6_7_8_9"

# print(word[::3])    # step = 2 (working: step-1)
# print(word[::4])    # even
print(word[2::4])    # odd