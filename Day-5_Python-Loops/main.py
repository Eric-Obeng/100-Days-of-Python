import random

fruits = ["Apples", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)


# Average height exercise
"""
You are going to write a program that calculates the average student height from a List of height. e.g. student_height = [180, 124, 165, 173, 189, 169, 146]

the average height can be calculated by adding all the height together and dividing by the total number of heights.
 
"""
student_height = input("Input a list of student heights ").split()
for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])
# print(student_height)

total_height = 0
number_of_students = 0
for height in student_height:
    total_height += height
    number_of_students += 1

average_student_height = round(total_height / number_of_students)

# print(total_height)
# print(number_of_students)

print(f"Average student height is {average_student_height}")


# Height Score Exercise
"""
Yo are going to write a program that calculates the height score from a List of scores. 
E.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important: you are not allowed to use the max or min functions. The output word much match

The highest score in class is: x
"""
student_scores = input("input a list of student scores: ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"the highest score in the class is: {highest_score}")


# For loop with Range
# for number in range(1, 11, 2):
#     print(number)


# Add 1 - 100 using range
total = 0
for number in range(1, 101):
    total += number
print(total)


# Exercise: Adding Even numbers from 1-100
"""
You are going to write a program that calculates the sum of all even numbers from 1 to 100 including 1 and 100.

There should be only one print statement in your console output. It should just print the final total and not every  step of the calculation
"""

total_num = 0
for number in range(1, 101, 2):
    total_num += number
print(total_num)

total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)


# Exercise: Fizz Buzz
"""
You are going to write a program that automatically prints the solution to the FizzBuzz game.

- Print each number from 1 to 100
- when number is divisible by 3 print 'Fizz' instead of number
- when number is divisible by 5 print 'Buzz' instead of number
- Whwn number is divisible by both 3 and 5 print 'FizzBuzz' instead of number
"""
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# Password Generator Project
import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for char in range(1, nr_letters + 1):
    password += random.choice(letters)

for char in range(1, nr_symbols + 1):
    password += random.choice(symbols)

for char in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)


# Hard Level - Order of characters randomised:
# e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
password_list = []
for char in range(1, nr_letters + 1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols + 1):
    password_list.append(random.choice(symbols))

for char in range(1, nr_numbers + 1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)
empty_delimiter = ""
hard_password = empty_delimiter.join(password_list)
print(f"Your password is: {hard_password}")
