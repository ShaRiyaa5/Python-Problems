#12-12-2025 - Friday

#Create a program that
#Stores multiple product prices in a list
#Finds the highest priced product
#Finds the lowest priced product
#Displays the price difference between them
price = [100, 10, 14, 5, 4567, 24]
price.sort()
print("lowest price: ", price[0])
print("highest price: ", price[len(price)-1])
print("difference =", price[len(price)-1] - price[0])

#Create a program that
#Stores product prices in a list
#Sorts prices from low to high
#Sorts prices from high to low
price = [100, 10, 14, 5, 4567, 24]
price.sort()
print("low to high: ", price)
price.sort(reverse=True) #price.reverse()
print("high to low: ", price)

#Create a program that
#Stores order statuses in a list ("Delivered", "Pending", "Cancelled")
#Counts how many orders are Delivered
#Prints only the Delivered orders
order_status = ["Delivered", "Pending", "Cancelled", "Delivered", "Delivered", "Delivered", "Cancelled", "Cancelled"]
print(order_status.count("Delivered"), "orders are delivered")