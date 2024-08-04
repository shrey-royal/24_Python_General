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

# def addition(a, b):
#     return a+b

# print(addition(2, 3))


# Default parameters

# def addition(a, b=0):
#     print(f"{a} + {b} = {a+b}")

# addition(34, 34)
# addition(34)

# smol praktis
# Problem Statement: Create a function 'greet_user' that takes two parameters: 'name' (a string) and 'greeting' (a string). The greeting parameter should have a default value of "Hello". The function should print a message in the format: "greeting, name!". If no greeting is provided, it should use the default value.

# def greet_user(name,greeting="hello"):
#     print(f'"{greeting}, {name}!"')

# greet_user('baburao','good afternoon')
# greet_user('baburao')
######################################################################

# keyword arguments

# def addition(a: int | None = 0, b=0):
#     print(f"{a} + {b} = {a+b}")

# addition(b=23, a=1)
# addition(b=23)


# print("this", "is", "a", "firecracker!", end='___')
######################################################################

# Recursion Function

def factorial(num=0):
    # base condition
    if num == 0:
        return 0
    elif num == 1:
        return 1
    
    # recursion
    return num * factorial(num-1)

print(factorial(5))