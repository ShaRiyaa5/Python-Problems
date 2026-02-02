#Create a list of square numbers from 1 to 10 using list comprehension.
square_numbers =[i*i for i in range(1,11) if i*i < 10]
print(square_numbers)

#Given a list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], create a new list containing only the even numbers using list comprehension.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [i for i in numbers if i%2==0]
print(even_numbers)

#Given a sentence "Python is an amazing language", create a list containing the length of each word using list comprehension.
sentence = "Python is an amazing language"
length = [len(word) for word in sentence.split()]
print(length)

#Create a list of numbers from 1 to 50 that are divisible by both 3 and 5 using list comprehension.
number = [i for i in range(1,51) if i%3==0 and i%5==0]
print(number)

#Given a 2D list matrix = [[1, 2], [3, 4], [5, 6]], convert it into a single flat list [1, 2, 3, 4, 5, 6] using list comprehension
matrix = [[1, 2], [3, 4], [5, 6]]
result = [numbers for sublist in matrix for numbers in sublist]
print(result)