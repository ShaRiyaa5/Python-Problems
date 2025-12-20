#18-12-2025 - Wednesday

#You are given a tuple that stores seat prices of a movie theater.
#prices = (120, 150, 150, 200, 250)
#1) Find how many times ₹150 price appears.
#2) Find the highest seat price.
#3) Check whether ₹300 seat price exists or not.
prices = (120, 150, 150, 200, 250)
print("Rs.150 appears", prices.count(150), "times")
prices_list = list(prices) #converted tuple to list
prices_list.sort() #low to high using sort
print(prices_list[len(prices)-1]) #prints the last value in the list
if prices.count(300) == 0:
    print("We do not have seats for Rs.300")
else:
    print("Rs 300 seats are available")

#A restaurant stores daily ordered food items in a tuple.
#orders = ("biryani", "pongal", "burger", "biryani", "pongal")
#1) Count how many times "biryani" was ordered.
#2) Find the index position of "burger".
#3) Convert the tuple into a list and add "shawarma", then convert back to tuple
orders = ("biryani", "pongal", "burger", "biryani", "pongal")
print("Biryani was ordered", orders.count("biryani"), "times")
print("Index position of burger =", orders.index("burger"))
order_list = list(orders) #converting tuple to list
order_list.append("shawarma") #append to add value to a list
print(tuple(order_list)) #converting list to tuple

