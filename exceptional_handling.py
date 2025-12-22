#15-12-2025 - Monday

#Create a program for an online food order.
#User enters food name
#User enters quantity
#Use exception handling to handle:
#Non-numeric quantity
#Quantity less than or equal to 0
#If valid, print food name + “order placed successfully
try:
    food_item = input("Enter the food item: ")
    quantity = int(input("Enter the quantity: "))
    print(food_item, "order placed successfully")
except ValueError:
    print("Enter a valid number! Quantity should be less than or equal to 0!")
finally:
    print("Thank you! Visit again!")

#Create a program for a movie ticket booking app.
#User enters movie name
#User enters number of tickets
#Ticket price = ₹200
#Use exception handling to handle:
#User enters text instead of number for tickets
#User enters 0 or negative tickets
#Display movie name and total amount if input is valid
try:
    movie = input("Enter the movie name: ")
    number = int(input("Enter the number of tickets required: "))
    print(f"{number} tickets booked for {movie}.")
    print("Total price =", number*200)
except ValueError:
    print("Enter a valid number for the number of tickets")
finally:
    print("Tickets booked successfully! Enjoy the show!")

#Design a movie rating system.
#User enters movie name
#User enters rating (1 to 5)
#Use exception handling to handle:
#String input for rating
#Rating outside the valid range
#If valid, display “Thanks for rating ”
try:
    movie = input("Enter the movie name: ")
    rating = int(input("Enter the rating for this movie"))
    print(movie, " ", rating)
except ValueError:
    print("Enter a valid number for ratings. Rating should be between 1 to 5")
finally:
    print("Thanks for rating")