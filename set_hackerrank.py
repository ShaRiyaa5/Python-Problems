#21-12-2025 - Sunday

n = int(input("Enter the number elements in a set : "))
s = set()
list1 = []
for i in range (1, n+1):
    a = int(input(f"Enter the value that needs to be added in the set: "))
    list1.append(a)
    i = i + 1
s = set(list1)
print(s)
N = int(input("Enter the number of action needs to be performed in the set: "))
for x in range (1, N+1):
    action = input("Enter the action needs to be performed in the set (pop / discard / remove) : ")
    if (action == "pop"):
        print(s.pop())
    elif (action == "discard"):
        value = int(input(f"Enter the value that needs to be {action} : "))
        print(s.discard(value))
    elif (action == "remove"):
        value = int(input(f"Enter the value that needs to be {action} : "))
        print(s.remove(value))
    else:
        print("Please enter a valid action that needs to be performed")
print(s)