"""
Abstraction is a key concept in Object-Oriented Programming (OOP) that allows you to define complex systems by focusing on the relevant details while hiding the underlying complexity. A good real-world example for abstraction is managing orders in a vegetarian restaurant.

Let's imagine a vegetarian restaurant where customers can order various vegetarian dishes. We'll create a Python example that abstracts away the complexities of making each dish but focuses on the essential aspects of taking an order and serving the dish.

Problem Description:
In this restaurant, different vegetarian dishes are prepared differently, but from the customer's perspective, they only care about ordering a dish and receiving it. The underlying process of cooking each dish is hidden (abstracted).

The restaurant offers the following vegetarian dishes:

Veg Burger
Veg Pizza
Pasta
Each dish has its own method of preparation, but for simplicity, the customer doesn't need to know how it's made. We will create an abstraction for the dish preparation process.

Steps to Implement:
Abstract Class: We will create an abstract base class called VegetarianDish that defines an interface (i.e., the contract) for preparing any vegetarian dish.

Concrete Classes: We will then implement specific dish classes, like VegBurger, VegPizza, and Pasta, which extend the abstract class. Each class will provide its own implementation of the preparation process.

Client: The customer will interact with the system only by ordering a dish. The customer doesn't need to know how the dish is prepared, only that it will be served.
"""

from abc import ABC, abstractmethod

class Dish(ABC):

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def serve(self):
        pass

class Burger(Dish):
    def prepare(self):
        print("Preparing the Burger: Grilling the patty, adding veggies, and toasting the buns.")
    
    def serve(self):
        print("Burger is served with fries.")

class Pizza(Dish):
    def prepare(self):
        print("Preparing the Pizza: Rolling the dough, adding sauce, cheese, and veggies.")
    
    def serve(self):
        print("Pizza is served with a side of garlic bread.")

class Pasta(Dish):
    def prepare(self):
        print("Preparing the Pasta: Boiling the pasta and mixing it with a rich tomato sauce and herbs.")
    
    def serve(self):
        print("Pasta is served with a side of salad.")

class Restaurant:
    def take_order(self, dish: Dish):
        dish.prepare()
        dish.serve()

if __name__ == "__main__":
    restaurant = Restaurant()

    print("Customer orders Burger:")
    burger = Burger()
    restaurant.take_order(burger)

    print("\nCustomer orders Pizza:")
    pizza = Pizza()
    restaurant.take_order(pizza)

    print("\nCustomer orders Pasta:")
    pasta = Pasta()
    restaurant.take_order(pasta)