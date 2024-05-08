import math

# def greet():
#     print("Hello")
#     print("Word")
#     print("Eric")


# greet()

"""
# Function with one parameter (input)
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")


greet_with_name("Eric")
greet_with_name("Angela")
"""


# Function with more than one parameter
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")


greet_with("Jack Baur", "Nowhere")

# Positional Arguments
# Keyword Arguments

# Area Calc Exercise
"""
You are painting a wall. The instruction on the paint can says that 1 can of paint can cover 5 sqaure meters of wall. Given a random height and width of wall, calculate how many cans of paint you'll need to buy.

number of cans = (wall height X wall width) / covered per can
"""


# Solution
def AreaCalc(heigth, width, coverage):
    number_of_cans = (heigth * width) / coverage
    print(f"You'll need {math.ceil(number_of_cans)} cans of paint")


test_height = int(input("Height of wall: "))
test_width = int(input("Width of wall: "))
coverage = 5

AreaCalc(heigth=test_height, width=test_width, coverage=coverage)


# Exercise 2: Prime Number Checker
"""
Prime numbers are number that can only be cleanly divisible by itself and 1.

You need to write a function that checks if the number passed into it is a prime number or not.

"""
# Solution
def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f'{number} is a prime number')
    else:
        print(f'{number} is not a prime number')


n = int(input("Check this number: "))
prime_checker(number=n)


