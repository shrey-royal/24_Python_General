"""
Conditional Statements:

1. Using branching
print()

if this than that

age > 18 : print("Adult")
age < 18 : print("kid")


-> if statement
-> switch case

2. Using looping:

-> for loop
-> while loop
-------------------------------------


if condition:
    //
else:
    //

4 types of if else statement
    -> if statement
        if condition:
            //statement

    -> if else statement
        if condition:
            //statement
        else:
            //statement
    
    -> ladder if statement
        if condition:
            //statement
        elif condition:
            //statement
        elif condition:
            //statement
        else:   # default
            //statement
    
    -> nested if
        if condition:
            # nested if statement
            if condition:
                //statement
            else:
                //statement
        else:
            //statement
    
python does not have switch case.
    

    
    
"""

# if "1234567890".count('@'):
#     print("Condition Passes")
# else:
#     print("Condition Fails")

# 0 - False
# Other than 0 is True


# Type 1
'''
if int(input("Enter your age: ")) > 18:
    print("Adult")
else:
    print("Kid")
'''

age = int(input("Enter your age: "));

if (age > 0 and age < 100):
    # print("Valid Age")
    if age <= 18:
        print("Kid")
    elif age <= 60:
        print("Adult")
    else:
        print("Senior Citizen")
else:
    print("Invalid Age")