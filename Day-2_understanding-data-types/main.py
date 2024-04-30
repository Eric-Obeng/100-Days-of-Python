"""
Float
string
integers
Booleans
"""

# Strings
# Strings are always placed inside quotation marks ('' 0r "")
print("Hello"[0])
print("Hello"[-1])
print("123" + "456")  # output: 123456


# Integers
# integers are positive and negative whole numbers
print(123 + 456)
print(12_456_456_876)
print(-50 + 45)

# Float
print(3.14159)

# Boolean
# This has 2 values which either True or False
print(2 > 1)
print(2 < 1)

# Type checking and coversion

# num_char = len(input("What is your name?"))
# # print(type(num_char))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")

a = 123
print(type(a))

# Exercise 1
"""
 write a program that adds the digits in a 2 digits number e.g if the input was 35, then the ouput should be 3+5=8
"""
# Solution
two_digits_input = input("Type a two digit number: ")

first_number = int(two_digits_input[0])
second_number = int(two_digits_input[1])

result = first_number + second_number
print(result)

# CHALLENGE 2 (BMI)
"""
INSTRUCTIONS:
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
The BMI is a measure of some weight taking into account and their height. e.g if a tall person and a short person both weigh the same amount, the short person is usually more overweight.

BMI = weight (kg) / height²(m²)

NB: you should round the result to the nearest whole number
"""

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

person_height = float(height)
person_weight = int(weight)

BMI = round(person_weight / person_height**2)
print(BMI)

# formatting
score = 0
height = 1.8
isWinning = True

print(
    f"Your score is {score}, your height is {height} and you are winning is {isWinning}"
)


# Challenge 3
"""Your life in weeks
1 year = 365days
1 year = 52weeks
1 year = 12months
"""

age = input("What is your current age? ")

age_as_int = int(age)

years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remainig = years_remaining * 12

message = f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remainig} months left"

print(message)

# Project - tip calculator
print("Welcome to the Tip Calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
number_of_people = int(input("How many people to split the bill? "))
amount_each = ((total_bill * tip / 100) + total_bill) / number_of_people
final_bill = "{:.2f}".format(amount_each)

print(f"Each person should pay: ${final_bill}")
