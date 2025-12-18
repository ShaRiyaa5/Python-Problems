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