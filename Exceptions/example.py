fruits = {
    'apple': 10,
    'orange': 20,
    'banana': 30
}

key = None
while True:
    try:
        key = input('Enter a key to lookup:')
        fruit = fruits[key.lower()]
    except KeyError:
        print(f'Error! {key} does not exist.')
    except KeyboardInterrupt:
        break
    else:
        print(fruit)
    finally:
        print('Press Ctrl-C to exit.')

"""
-> Problem Statement: Exception Handling in an Street Food Ordering System

You are developing a simple program to simulate ordering street food from popular stalls in Gandhinagar. The program will allow a user to select a dish from a menu, input the quantity, and then calculate the total cost. However, the program needs to handle potential errors that might occur during this process. 

-> Requirements:

1. Menu: The program should display a menu of available dishes with their prices. The menu items are:
   - Pav Bhaji: ₹50
   - Dhokla: ₹30
   - Khaman: ₹25
   - Fafda-Jalebi: ₹40
   - Sev Khamani: ₹35

2. User Input:
   - The user should be able to input the name of the dish they want to order.
   - The user should then input the quantity they want to order.

3. Error Handling:
   - If the user inputs a dish name that is not on the menu, the program should handle this gracefully by displaying a message like "Sorry, this item is not available" and ask the user to input the dish name again.
   - If the user inputs a non-numeric value for the quantity or a negative number, the program should catch this error and prompt the user to enter a valid quantity.
   - If the quantity is valid and positive, the program should proceed to calculate the total cost.

4. Calculation:
   - Once a valid dish name and quantity are provided, calculate the total cost and display it to the user.
   - If no exceptions occur during the process, display a message saying "Order placed successfully!"

5. Finalization:
   - Use the `finally` block to print a message, "Thank you for ordering with us!" This message should be displayed whether or not an exception occurred.

-> Example Output: (Non-looped output)

Welcome to Gandhinagar's best Street Food Stall!

Here is our menu:
1. Pav Bhaji: ₹50
2. Dhokla: ₹30
3. Khaman: ₹25
4. Fafda-Jalebi: ₹40
5. Sev Khamani: ₹35

Please enter the name of the dish you want to order: Pav Bhaji
Please enter the quantity: two
Invalid quantity! Please enter a valid number.

Please enter the quantity: 2

Your total cost is: ₹100
Order placed successfully!

Thank you for ordering with us!


-> Implementation Guide:

- Step 1: Create a dictionary to store the menu items and their prices.
- Step 2: Use a `while` loop to prompt the user for the dish name until a valid option is selected.
- Step 3: Use `try-except` blocks to handle invalid input for the quantity.
- Step 4: Use the `else` block to calculate and display the total cost if no exceptions occur.
- Step 5: Use the `finally` block to print the final message regardless of the outcome.

PS: You have to create a solution that runs in infinite loop

"""