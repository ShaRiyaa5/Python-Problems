#10-01-2026 Saturday
"""
1) I have a list of products (dictionaries). Write a Python program to sort this list based on the price (Low to High) using the sorted() function and a lambda function.
#Input :
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mobile", "price": 15000},
    {"name": "Headphones", "price": 2000},
    {"name": "Monitor", "price": 12000}
]
Expected Output: The list should be ordered: Headphones -> Monitor -> Mobile -> Laptop.
"""
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Mobile", "price": 15000},
    {"name": "Headphones", "price": 2000},
    {"name": "Monitor", "price": 12000}
]
sorted_products = sorted(products, key=lambda p: p['price'])
ordered_list = [s['name'] for s in sorted_products]
print(ordered_list)
"""
2) Filter out weak passwords. Use filter() and lambda to create a new list containing only passwords that have more than 8 characters.
Input :
passwords = ["pass123", "secure_login_99", "admin", "python_developer", "1234"]
Expected Output: ['secure_login_99', 'python_developer']
"""
passwords = ["pass123", "secure_login_99", "admin", "python_developer", "1234"]
weak_password = list(filter(lambda w: len(w) >= 8, passwords))
print(weak_password)
"""
3) I want to send an email only to active users. Create a new list containing only the emails of users where is_active is True. Do this in one line using List Comprehension.
Input:
users = [
    {"id": 1, "email": "alice@example.com", "is_active": True},
    {"id": 2, "email": "bob@example.com", "is_active": False},
    {"id": 3, "email": "charlie@example.com", "is_active": True},
    {"id": 4, "email": "david@example.com", "is_active": False}
]
Expected Output: ['alice@example.com', 'charlie@example.com']
"""
users = [
    {"id": 1, "email": "alice@example.com", "is_active": True},
    {"id": 2, "email": "bob@example.com", "is_active": False},
    {"id": 3, "email": "charlie@example.com", "is_active": True},
    {"id": 4, "email": "david@example.com", "is_active": False}
]
active_users = [u["email"] for u in users if u["is_active"]==True]
print(active_users)
"""
4) Display a ranking list for a game. Use enumerate to print the player names with their Rank.
(Note: Rank should start from 1, not 0).
Input:
top_players = ["Dhoni", "Priya", "Sachin", "Sneha"]
Expected Output:
Rank 1: Dhoni
Rank 2: Priya
Rank 3: Sachin
Rank 4: Sneha
"""
top_players = ["Dhoni", "Priya", "Sachin", "Sneha"]
for i,j in enumerate(top_players, start=1):
    print(f"Rank {i}: {j}")


