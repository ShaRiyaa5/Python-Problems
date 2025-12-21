#18-12-2025 - Thursday
"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""

N = int(input("Enter number of actions needs to be performed in a list: "))
for N in range(1, N+1):
    print(input("Which action needs to be performed in a list: "))
    N = N+1
print("Thank you. Your list has been created")

list1 = [ ]
list1.append(1)
list1.append(2)
list1.insert(1, 3)
print(list1)
list1.insert(5, 1)
print("Inserting 5 at index 0\n",list1)
list1.remove(1)
list1.append(1)
list1.sort()
list1.pop()
list1.reverse()
print(list1)


