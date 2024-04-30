# this is use to print values out
print("Learning Python")
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Print on a new line in Python we use "\n"
print('\n')
print("Hello World\nHello World")

#Concatenation strings in Python
print("Hello"+ " " + "Eric")

# Input function
name = input("What is your name? ")
print(len(name))

#Varaibles Exercise
'''
Write a program that will switch variables
'''
a = input('a:')
b = input('b:')

c = a
a = b
b = c

print('a = '+ a)
print('b = '+ b)


# Band name generator project
#inputs
print("Welcome to the Band Name Generator.")
name_of_city = input("What's the name of the city you grew up in? \n")
pet_name = input("What's your pet's name?\n")

# Ouput
print("Your band name could be " + name_of_city + " " + pet_name)