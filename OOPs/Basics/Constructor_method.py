'''
The __init__ special method, also known as a Constructor, is used to initialize class attributes with the default or user-defined values
'''
# Constructor method

class Pizza:
    def __init__(self, size, crust_type, toppings=None) -> None:
        self.size = size    #e.g., 'small', 'medium', 'large'
        self.crust_type = crust_type    #e.g. 'thin', 'thick', 'stuffed'
        self.toppings = toppings if toppings is not None else [] # list of toppings

    def add_topping(self, topping) -> None:
        """Add a topping to the Pizza."""
        if topping not in self.toppings:
            self.toppings.append(topping)
            print(f"{topping} added.")
        else:
            print(f"{topping} is already on the pizza.")

    def remove_topping(self, topping) -> None:
        """Remove a topping from the pizza."""
        if topping in self.toppings:
            self.toppings.remove(topping)
            print(f"{topping} removed.")
        else:
            print(f"{topping} is not on the pizza.")

    def calculate_price(self) -> float:
        """Calculate the price of the pizza based on the size and number of toppings."""
        base_price = {'small': 100, 'medium': 150, 'large': 200}
        topping_price = 30
        price = base_price[self.size] + topping_price * len(self.toppings)
        return price
    
    def __str__(self) -> str:
        """String representation of the pizza."""
        return f"{self.size.capitalize()} pizza with {self.crust_type} crust and toppings: {', '.join(self.toppings) or 'no toppings'}"
    
if __name__ == '__main__':
    # code here will only run when this script is executed directly
    pizza = Pizza('large', 'stuffed')
    print(pizza)
    pizza.add_topping('olives')
    pizza.add_topping('paneer')
    pizza.add_topping('mushrooms')
    pizza.add_topping('tomatos')
    pizza.add_topping('baby corn')
    pizza.add_topping('sweet corn')
    pizza.add_topping('baby corn')
    print(pizza)
    print(f"Total price: Rs.{pizza.calculate_price():.2f}")