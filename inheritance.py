"""
1) An online store gives different discounts based on the product category.
Electronics get 10% off, and Clothing gets 20% off.
Requirements:
Create a Parent Class Product.
Attributes: name, price.
Method: get_final_price():
Returns the actual price (no discount).
Create a Child Class
Electronics (Inherits from Product).
Method: get_final_price():
Override this to apply a 10% discount and return the new price.
Create a Child Class Clothing (Inherits from Product).
Method: get_final_price(): Override this to apply a 20% discount and return the new price.
Test: Create a Laptop (Electronics, Price: 50000) and a T-shirt (Clothing, Price: 1000). Print their final prices after discount.
"""
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    def get_final_price(self):
        print("Actual price of the product without any discounts = ", self.price)
class Electronics(Product):
    def get_final_price(self):
        discount = self.price * 0.10
        final_price = self.price - discount
        return final_price
class Clothing(Product):
    def get_final_price(self):
        discount = self.price * 0.20
        final_price = self.price - discount
        return final_price
laptop = Electronics("laptop", 50000)
print("New price after 10% discount = ",laptop.get_final_price())
tshirt = Clothing("T-shirt", 1000)
print("New price after 20% discount = ",tshirt.get_final_price())
"""
2) Payment Gateway 
A payment system handles different payment modes. You cannot process a payment without validating specific details (CVV for Card, UPI PIN for GPay).
Requirements:
Create a Parent Class Payment.
Method: process_payment(amount): Print "Processing payment..."
Create a Child Class CreditCardPayment.
Attribute: cvv_number.
Method: process_payment(amount):
Take cvv as input inside the method.
If the input matches cvv_number, print "Payment Successful via Card".
Else, print "Payment Failed: Invalid CVV".
Create a Child Class UPIPayment.
Attribute: upi_pin.
Method: process_payment(amount):
Take pin as input.
If the input matches upi_pin, print "Payment Successful via UPI".
Else, print "Payment Failed: Invalid PIN".
Test: Try to pay 1000 rupees using both methods with correct and wrong passwords
"""
class Payment:
    def process_payment(self, amount):
        print("Processing payment...")
class CreditCardPayment(Payment):
    def process_payment(self, amount):
        cvv = 2132
        cvv_number = int(input("Enter the CVV number: "))
        if cvv_number == cvv:
            print("Payment successful via Card")
        else:
            print("Payment Failed: Invalid CVV")
class UPIPayment(Payment):
    def process_payment(self, amount):
        pin = 2132
        upi_pin = int(input("Enter the UPI PIN: "))
        if pin == upi_pin:
            print("Payment Successful via UPI")
        else:
            print("Payment Failed: Invalid PIN")
upi = UPIPayment()
upi.process_payment(1000)
card = CreditCardPayment()
card.process_payment(1000)
"""
3) A company stores employee details. For Managers, we also need to store their "Team Size". 
You must use the parent constructor to avoid code repetition.
Requirements:
Create a Parent Class Employee.
Constructor (_init_): Accepts name and id_number.
Method: display(): Prints Name and ID.
Create a Child Class Manager (Inherits from Employee).
Constructor (_init_): Accepts name, id_number, and team_size.
Use:Super()._init_(name, id_number) to pass name and ID to the parent class. Then assign team_size to self.
Method: display(): Override to print Name, ID, and Team Size.
Test: Create a Manager object. Ensure that name and id are set correctly using the parent logic, and team_size is handled by the child.
"""
class Employee:
    def __init__(self, name, id_number):
        self.name = name
        self.id_number = id_number
    def display(self):
        print(f"Name = {self.name}\nID = {self.id_number}")
class Manager(Employee):
    def __init__(self, name, id_number, team_size):
        super().__init__(name, id_number)
        self.team_size = team_size
    def display(self):
        print(f"Name = {self.name}\nID = {self.id_number}\nTeam size = {self.team_size}")
xyz = Manager("Riyaa", 25, 5)
xyz.display()

