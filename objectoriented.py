"""
1) Create a system where a user can add food items to an order. Finally, you need to calculate the total bill including a 5% tax.

Class Name: FoodOrder

Attributes:
menu: A dictionary with items and prices (e.g., {"Grilled Chicken": 200, "Biryani": 300}).

cart: An empty list to store ordered items.

Methods:
addItem(item):
Check if the item exists in the menu.
If yes, add it to the cart.
If no, print "Item not available".

calculateBill():
Calculate the total price of all items in the cart.

Add 5% tax to the total amount.

Print the final bill.
"""
class FoodOrder:
    menu = {"Grilled Chicken": 200, "Biryani": 300}
    def __init__(self):
        self.cart = []
        self.total_price = 0
    def add_items(self, items):
        if items in FoodOrder.menu:
            self.cart.append(items)
            self.total_price += FoodOrder.menu[items]
            print(f"{items} added to the cart")
        else:
            print("Item not available")
    def total(self):
        tax = self.total_price * 0.05
        final_amount = self.total_price + tax
        print("Items Ordered = ", self.cart)
        print("Total price = ", final_amount)
order = FoodOrder()
#"You want to add items" == "Yes":
while True:
    items = input("Enter the list of items need to be ordered (Enter done if finished) = ")
    if items.lower() == "done":
        break
    order.add_items(items)
order.total()
"""
2) Simulate a YouTube video. The rule is: A user cannot 'Like' a video without 'Watching' it first.

Class Name: YouTubeVideo

Attributes:
title: Name of the video.
views: Initially 0.
likes: Initially 0.

Methods:

watch():Increase the views count by 1.
Print "User watched the video."

like():Check if views is greater than 0.If yes, increase likes count by 1.

If no (views is 0), print "Error: You must watch the video before liking it."

details():
Print the Title, Total Views, and Total Likes.
"""
class YouTubeVideo:
    def __init__(self):
        self.title = "Cooking vlog"
        self.views = 0
        self.likes = 0
    def watch(self):
        self.views += 1
        print("User watched the video")
    def like(self):
        if self.views > 0:
            self.likes += 1
            print("User liked the video")
        else:
            print("Error: You must watch the video before liking it.")
    def details(self):
        print("Title = ", self.title)
        print("Total views = ", self.views)
        print("Total likes = ", self.likes)
obj = YouTubeVideo()
obj.like()
obj.watch()
obj.like()
obj.like()
obj.watch()
obj.like()
obj.details()