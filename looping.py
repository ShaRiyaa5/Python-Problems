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