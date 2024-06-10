"""
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
"""

# Negative Slicing (reverse reading of any iterable data)

# str = "Royal Technosoft Pvt. Ltd."
# print(str[-1:])   # .
# print(str[:-1])     # everything else except the last char

str = "Hello, World!"
# print(str[len(str)-3:])
# print(str[-3:])
# print(str[-10:-3])
# print(str[::-1])    # when you put step -1, the string will be reversed
# print(str[-10:-13:-1])
# print(str[-4:-1:1])
# print(str[-1:-4:-1])
# print(str[:0:-1])
# print(str[1:-5:1])

""" # smol praktis
my_string = "The quick brown fox jumps over the lazy dog"
> reverse a substring from idnex -10 to -30 with a step of -1
> Extract "dog lazy the over" form the reversed string
> Extract every second character in reverse from the original string

"""
my_string = "The quick brown fox jumps over the lazy dog"

#1
# print(my_string[-10:-30:-1])
# print(my_string[-29:-9][::-1])

#2
# var = my_string[-1:-4:-1][::-1] + " " + my_string[-5:-9:-1][::-1] + " " + my_string[-10:-13:-1][::-1] + " " + my_string[-14:-18:-1][::-1]
# print(var)
# print(my_string[-1:-4:-1][::-1]+my_string[-4:-10:-1][::-1]+my_string[-10:-13:-1][::-1]+my_string[-13:-19:-1][::-1])
# print(my_string[-3::]+" "+my_string[-8:-4:]+" "+my_string[-12:-9:]+" "+my_string[-17:-12:])

#3
print(my_string[-2::-2])