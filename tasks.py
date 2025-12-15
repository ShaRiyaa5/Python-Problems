#08-12-2025 - Monday

#Create a variable num1 with value 10 (int).
#Create a variable num2 with value 2.5 (float).
#Add them together and store in result.
#Print result and its type.
num1 = 10
num2 = 2.5
add = num1 + num2
print(type(add))

#Boolean Arithmetic
#Create a variable is_active = True.
#Add 10 to is_active.
#Print the final answer.
is_active = True
final_answer = 10 + is_active
print(final_answer)

#Division Type Check
#Divide 100 by 4.
#Print the answer.
#Print the type of the answer to confirm if it is float.
a = 100
b = 4
c = 100//4
print(c)
print(type(c))

#You have a string variable: amount = "500".
#You need to add 50 to it.
#Convert amount to integer first, then add.
#Print the total.
amount = "500"
total = int(amount) + 50
print(total)

#Create a variable gpa = 8.9. Convert it into an integer to remove the decimal point.
#Print the integer value.
gpa = 8.9
print(int(gpa))

#Create a variable year = 2026.
#Print this sentence by converting the number to string:
#"Welcome to the year 2026"
year = 2026
print("Welcome to the year", str(year))


#09-12-2025 - Tuesday

#Create a program that gives free delivery if the order amount is above a certain limit.
order_amount = int(input("Enter the order amount: "))
if(order_amount > 500):
    print("YAY!! You got free delivery")
else:
    print("OOPS! Free delivery is applicable only for order value above 500")

#Design a program that allows login only when the username and password are correct.
username = "riyaa"
password = "Riyaa@123"
user_name = input("Enter your username: ")
if(username == user_name):
    pass_word = input("Enter your password: ")
    if(password == pass_word):
        print("YAYY!! Logged in successfully")
    else:
        print("Incorrect password. Try again")
else:
    print("Incorrect username. Try again")

#Create a program that calculates the cab fare based on the travel distance using if-elif-else conditions.
distance = float(input("Enter the distance to be travelled in kms: "))
if(distance < 30):
    price = 10
    amount = distance * price
elif(distance < 60):
    price = 25
    amount = distance * price
elif(distance < 120):
    price = 45
    amount = distance * price
else:
    price = 100
    amount = distance * price
print("Total fare: ", amount)

#Design a program that checks whether a student is eligible to join a course based on age and qualification using nested if
age = int(input("Enter your age: "))
if(age >= 18):
    qualification = int(input("Enter your highest qualification (grade in numbers): "))
    if(qualification == 12):
            print("Congratulations! You're eligible to join this course")
    else:
        print("You're not eligible for this course. Highest qualification should be 12th")
else:
    print("You're not eligible for this course. You should be at least 18yrs old to join this course")


#10-12-2025 - Wednesday

#for loop
#print all even numbers between 1 and 50
for i in range(1,50):
    if i%2 == 0: #modulo operator % - gives the reminder
        print(i)
print("loop finished")

#count how may odd numbers are present between 1 to 100
count = 0
for i in range(1,100):
    if i%2 !=0:
        count = count + 1
print(count)
print("loop finished")

#reverse a given list using a for loop: [10, 20, 30, 40, 50]
list = [10, 20, 30, 40, 50]
reversed_list = []
for i in list:
    reversed_list = [i] + reversed_list #in python we can add two variables only if they're in the same type - else we've to convert them to the same type before adding or concatenating
print(reversed_list)

#while loop
#print numbers from 1 to 10 using a while loop
i = 1
while i <= 10:
    print(i)
    i=i+1

#print numbers from 10 to 1 (reverse order)
i = 10
while i >= 1:
    print(i)
    i = i - 1

#count how many digits are in a given number
num = 1234567890
count = 0
while num > 0:
    count = count + 1
    num = num // 10
print(count)


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


#15-12-2025 - Monday

#