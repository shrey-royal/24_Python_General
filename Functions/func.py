'''
Functions --> Assistants

=> A function is a named code block that performs a job or return a value

syntax:
def function_name(argument/s):
    //body of the function

'''

# import datetime as dt

# def greet():
#     now = dt.datetime.now()
#     current_hour = now.hour

#     if 5 <= current_hour < 12:
#         greeting = "Good morning!"
#     elif 12 <= current_hour < 17:
#         greeting = "Good afternoon!"
#     elif 17 <= current_hour < 21:
#         greeting = "Good evening!"
#     else:
#         greeting = "Good night!"

#     return greeting

# print(greet())
######################################################################

# Doc Strings (Documentation String)

# def print(message):
#     """This is Doc String"""
#     print(message)

# print()
######################################################################


# def greet(name):
#     print(f'Hi, {name}')

# greet(input("Enter your name: "))

# def greet(name):
#     return f'Hi, {name}'

# res = greet(input("Enter your name: "))
# print(res)
# print(greet(input("Enter your name: ")))
######################################################################

def addition(a, b):
    return a+b

print(addition(2, 3))


# Default Parameters