#12-12-2025 - Friday

#Scenario : You are building an app for the Election Commission.
#Task : Ask the user for their Age.
#If it is 18 or above, display "You are eligible to vote". If not, display "You are too young to vote
age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")
else:
    print("You are too young to vote")

#Scenario: You are building a secure login page.
#Task: Ask the user to enter a Password.
#If the password is exactly "Python123", show "Access Granted".
#Else, show "Access Denied / Wrong Password".
pass_word = "Python123"
password = input("Enter your password: ")
if password == pass_word:
    print("Access Granted")
else:
    print("Access Denied / Wrong Password")

#Scenario: A traffic camera needs to detect speeding cars.
#Task: Ask for the Car Speed (in km/ph).
#If speed is > 80, show "Over Speeding! Fine Rs. 1000".
#Otherwise, show "Safe Driving".
speed = int(input("Enter the speed of the car: "))
if speed > 80:
    print("Over Speeding! Fine Rs. 1000")
else:
    print("Safe Driving")

#Scenario: An online shopping site gives a discount for big orders.
#Task: Ask the user for the Total Bill Amount.
#If the amount is > 5000, show "You get a 20% Discount!".
#If the amount is > 2000, show "You get a 10% Discount!".
#Otherwise, show "No Discount Available".
total_bill_amount = int(input("Enter the total bill amount: "))
if total_bill_amount > 5000:
    print("You get a 20% Discount!")
elif total_bill_amount > 2000:
    print("You get a 10% Discount!")
else:
    print("No Discount Available")

#Scenario: The government gives free electricity for low usage.
#Task: Ask for Units Consumed.
#If Units <= 100, show "No Bill (Free)".
#Else, show "You have to pay the bill".
units = int(input("Enter the number of units consumed: "))
if units <= 100:
    print("No Bill (Free)")
else:
    print("You have to pay the bill")