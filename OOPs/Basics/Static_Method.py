"""
class TemparatureConverter:
    
    @staticmethod
    def celsius_to_fahrenheit(c) -> float:
        return 9*c/5 + 32
    
    @staticmethod
    def fahrenheit_to_celsius(f) -> float:
        return 5*(f-32)/9
    
if __name__ == "__main__":
    print(TemparatureConverter.celsius_to_fahrenheit(35))
    print(f"{TemparatureConverter.fahrenheit_to_celsius(100):.2f}")

"""

class ShoppingCart:
    # items = []  # class attribute

    def __init__(self):
        self.items = [] # instance attribute

    def add_item(self, item, price):
        self.items.append({'item': item, 'price': price})

    def calculate_total(self):
        return sum(item['price'] for item in self.items)
    
    @staticmethod
    def calculate_sales_tax(total, tax_rate):
        """Static method to calculate sales tax based on total rate and tax rate."""
        return total * tax_rate
    
if __name__ == "__main__":
    cart = ShoppingCart()

    cart.add_item('Laptop', 100000)
    cart.add_item('Headphones', 50000)

    total_price = cart.calculate_total()

    tax_rate = 0.18
    sales_tax = ShoppingCart.calculate_sales_tax(total_price, tax_rate)

    print(f"Total Price: {total_price}")
    print(f"Sales Tax: {sales_tax}")