# 8. Movie Ticket:
#    Write a class `MovieTicket` that has attributes for the movie title, cinema, showtime, and price. Implement methods to display the ticket information and a method to apply a discount on the ticket price.
'''
class MovieTicket:
   title: str = ""
   cinema: str = None
   showtime: str = None
   price: float = 0

   def bookTicket(self, title: str, cinema: str, showtime: str, price: float):
      """Get the MovieTicket with title, cinema, showtime, and price."""
      self.title = title
      self.cinema = cinema
      self.showtime = showtime
      self.price = price

   def display_info(self):
      """Display the information of the movie ticket."""
      print(f"Movie: {self.title}")
      print(f"Cinema: {self.cinema}")
      print(f"Showtime: {self.showtime}")
      print(f"Price: {self.price}")

   def apply_discount(self, discount_percentage):
      """
      Apply a discount to the ticket price.
      :param discount_percentage: The discount percentage to be applied (e.g., 10 for 10%).
      """
      if 0 <= discount_percentage <= 100:
         # discount_amount = (discount_percentage / 100) * self.price
         self.price -= (discount_percentage / 100) * self.price
         print(f"Discount of {discount_percentage}% applied. New price: {self.price:.2f}")
      else:
         print("Invalid discount percentage. Please provide a value between 0 to 100.")

# Example usage:
ticket = MovieTicket()
t: object = None

# ticket.bookTicket("Inception", "Cinemax", "7:30 PM", 450)
# ticket.display_info()

# ticket.apply_discount(10)
# ticket.display_info()

# print(MovieTicket.__name__)
# print(id(MovieTicket))
# print(id(ticket))
# print(ticket.__class__)
# print(type(ticket))

# print(isinstance(ticket, MovieTicket))
# print(isinstance(t, MovieTicket))

# Everything in python is an object, including classes

# print(MovieTicket.__name__)
# movieTicket = MovieTicket()
# print(type(movieTicket))
# print(isinstance(MovieTicket, type))
'''

from pprint import pprint

class HtmlDocument:
   """This class handles the Frontend"""
   extension = 'html'
   version = '5'

   def render():
      print('Rendering the HTML doc...')

# print(HtmlDocument.extension)
# print(HtmlDocument.version)
# print(HtmlDocument.media_type) # AttributeError
# -----------------------------------------------------------------------

# attr_1 = getattr(HtmlDocument, 'extension')
# attr_2 = getattr(HtmlDocument, 'version')
# attr_3 = getattr(HtmlDocument, 'media_type', 'text/html') # AttributeError

# print(attr_1, attr_2, attr_3, sep=' - ')
# -----------------------------------------------------------------------

# HtmlDocument.version = 8.9
# setattr(HtmlDocument, 'version', 10)
# print(HtmlDocument.version)

# HtmlDocument.total_tags = 100
# print(HtmlDocument.total_tags)

# file = HtmlDocument()
# print(file.total_tags)

# setattr(file, 'css_support', True)  # adding new attribute
# print(file.css_support)
# print(HtmlDocument.css_support)

# del file.css_support # delete attribute
# print(file.css_support)

# print(HtmlDocument.__dict__)
# HtmlDocument.__dict__['extension'] = 'css'
# print(HtmlDocument.__dict__['total_tags'])

pprint(HtmlDocument.__dict__)


"""
-> Problem Statements

1. Bank Account:
   Create a class `BankAccount` that represents a bank account. The class should have attributes for the account holder's name, balance, and account number. Implement methods to deposit money, withdraw money (if sufficient balance is available), and check the current balance.

2. Student Management:
   Design a class `Student` that stores the name, age, and grades (as a list) of a student. Implement methods to add grades, calculate the average grade, and display the student's details.

3. Rectangle Area and Perimeter:
   Write a class `Rectangle` that has attributes for the length and width of a rectangle. Include methods to calculate and return the area and perimeter of the rectangle.

4. Car:
   Create a class `Car` that has attributes like `make`, `model`, `year`, and `speed`. Implement methods to accelerate (increase speed), brake (decrease speed), and display the current speed. Ensure that speed cannot be negative.

5. Library Book:
   Design a class `Book` that represents a library book. The class should have attributes for the title, author, and whether the book is checked out or not. Implement methods to check out the book, return the book, and display the book's details.

6. Inventory Management:
   Develop a class `Product` that stores product information such as product name, price, and quantity in stock. Implement methods to add stock, remove stock (if enough quantity is available), and display the product's information.

7. Employee Payroll:
   Create a class `Employee` that has attributes for the employee's name, position, hourly wage, and hours worked. Implement methods to update hours worked and calculate the employee's weekly pay.

8. Movie Ticket:
   Write a class `MovieTicket` that has attributes for the movie title, cinema, showtime, and price. Implement methods to display the ticket information and a method to apply a discount on the ticket price.

9. Point in 2D Space:
   Create a class `Point` that represents a point in 2D space with `x` and `y` coordinates. Implement methods to calculate the distance between two points and to check if two points are the same.

10. Shopping Cart:
    Design a class `Item` that represents an item with a name, price, and quantity. Then, create a class `ShoppingCart` that holds a collection of `Item` objects. Implement methods to add items, remove items, calculate the total cost of the items in the cart, and display the cart's contents.

"""