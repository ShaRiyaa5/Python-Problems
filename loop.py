#You are a Rocket Scientist! You need to count from 1 to 30 for a launch. But, the computer has a glitch:
#If a number is a multiple of 3, the engine makes a "Fizz" sound.
#If it’s a multiple of 5, it makes a "Buzz" sound.
#If it’s both, it goes "FizzBuzz!"
#Task: Write a loop to print the countdown with these sounds.
for i in range(1,31):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)

#A thief tried to enter a PIN, but we don't know how long it was. You found a variable secret_pin = 984503.
#Task: Use a while loop to count how many digits are in that PIN so the police can narrow down the suspects.
secret_pin = 984503
count = 0
while secret_pin>=1:
    secret_pin=secret_pin//10
    count = count+1
print(f"There are {count} digit(s) in the PIN")

#You are a Spy, To send a secret message, you must reverse the word so the enemies can't read it.
#Task: Take the word "IRONMAN" and use a loop to turn it into "NAMNORI". Using a loop.
word =  "IRONMAN"
reversed_word = ""
len = len(word)-1
while len>=0:
    reversed_word = reversed_word+word[len]
    len=len-1
print(f"Reversed string = {reversed_word}")

#There is 1 Zombie in the city. Every minute, the number of zombies doubles (1 ->  2 -> 4 -> 8). The city is safe only until there are less than 500 zombies.
#Task: Use a while loop to find out how many minutes it takes for the zombies to reach 500.
i=1
count = 0
while i < 500:
    i = i*2
    count = count + 1
print(f"It took {count} minutes for the zombies to reach or cross 500")

#You are a detective. A group of friends numbered 1 to 10 are at a party. But one friend is missing, You have a list of people who are present, but it's not in order.
#The Task: You are given a list: present_friends = [1, 5, 3, 9, 2, 4, 6, 8, 10]
#Use a single loop to find out which number from 1 to 10 is missing.
present_friends = [1, 5, 3, 9, 2, 4, 6, 8, 10]
i=1
while i in present_friends:
    i=i+1
print(f"Friend {i} is missing")
