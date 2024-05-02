# Conditional Statement

water_level = 50
if water_level > 40:
    print("Drain water")
else:
    print("Continue")


print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You cant ride the rollercoaster")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Please pay $5.")
    elif age <= 18:
        bill = 7
        print("Please pay $7.")

    elif age >= 45 and age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Please pay $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you have to grow taller before you can ride")


# Comparison operaters
"""
> - greater than
< - less than
>= - greater than or equal to
<= - less than or equal to
== - equal to
!= - not equal to
"""

# Exercise 1
"""
Write a program that works out whether if a given number is an odd or even number.
Even numbers can be divided by 2 with no remainder
"""
# solution
number = int(input("Enter a number: "))

if number % 2 == 0:
    print(f"{number} is an Even number")
else:
    print(f"{number} is an Odd number")


# Exercise 2
"""
BMI calculator:
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
It should tell then the interpretation of their BMI based on the BMI value.

- Under 18.5 they are underweight
- Over 18.5 but below 25 they have a normal weight
- over 25 but below 30 they are overweight
- over 30 but below 35 they are obese
- Above 35 they are clinically obese
"""
# Solution

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

bmi = weight / (height * height)
bmi_format = float("{:.2f}".format(bmi))

if bmi_format < 18.5:
    print(f"Your BMI is {bmi_format}, you are underweight")
elif bmi_format < 25:
    print(f"Your BMI is {bmi_format}, you have a normal weight")
elif bmi_format < 30:
    print(f"Your BMI is {bmi_format}, you are overweight")
elif bmi_format < 35:
    print(f"Your BMI is {bmi_format}, you are obese")
else:
    print(f"Your BMI is {bmi_format}, you are clinically obese")


# Difficult Challenge
"""
Instructions:
Write a program that works out whether if a given number is a leap year. A normal year has 365 days, leap year have 366, with an extra day in February. The reason why we have leap year is really fascinating.
"""
# Solution
year = int(input("Which year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")


# Exercise
"""
Congratulations, youve got a job at Python Pizza. Your first job is to build an automatic pizza program
Based on a user's order, work out their final bill
"""
print("Welcome to Python Pizza Deliveries")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_chesse = input("Do you want extra cheese? Y or N ")
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3
else:
    bill = bill

if extra_chesse == "Y":
    bill += 1
else:
    bill = bill

print(f"Your final bill is: ${bill}")


# Difficult challenge 2
print("Welcome to Love calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_string = name1 + name2
lower_case_string = combined_string.lower()

t = lower_case_string.count("t")
r = lower_case_string.count("r")
u = lower_case_string.count("u")
e = lower_case_string.count("e")
true = t + r + u + e

l = lower_case_string.count("l")
o = lower_case_string.count("o")
v = lower_case_string.count("v")
e = lower_case_string.count("e")
love = l + o + v + e

love_score = int(str(true) + str(love))

if love_score < 10 or love_score > 90:
    print(f"Your love score is {love_score}, you go like coke and mentos")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together")
else:
    print(f"Your love score is {love_score}")


print(love_score)
