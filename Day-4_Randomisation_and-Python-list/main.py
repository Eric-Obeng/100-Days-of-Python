import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)
random_float = round(random.random() * 5)
print(random_float)

print(my_module.pi)

# Challenge 1
"""
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tail"
"""

coin_tossed = random.randint(0, 1)

if coin_tossed == 1:
    print("Heads")
else:
    print("Tails")


# Python List
# list is a data stucture in python use to organise and store data

a = 3
b = "hello"

states_of_america = [
    "Delaware",
    "Pennsylvania",
    "New Jersey",
    "Georgia",
    "Connecticut",
    "Massachusetts",
    "Maryland",
    "South Carolina",
    "New Hampshire",
    "Virginia",
    "New York",
    "North Carolina",
    "Rhode Island",
    "Vermont",
    "Kentucky",
    "Tennessee",
    "Ohio",
    "Louisiana",
    "Indiana",
    "Mississippi",
    "Illinois",
    "Alabama",
    "Maine",
    "Missouri",
    "Arkansas",
    "Michigan",
    "Florida",
    "Texas",
    "Iowa",
    "Wisconsin",
    "California",
    "Minnesota",
    "Oregon",
    "Kansas",
    "West Virginia",
    "Nevada",
    "Nebraska",
    "Colorado",
    "North Dakota",
    "South Dakota",
    "Montana",
    "Washington",
    "Idaho",
    "Wyoming",
    "Utah",
    "Oklahoma",
    "New Mexico",
    "Arizona",
    "Alaska",
    "Hawaii",
]
print(states_of_america[0])

# append is used to add an item to the end of the list
states_of_america.append("Ghana")

# extend is used to add another set of list to the previous list
# states_of_america.extend(["Diabene", "Nkroful", "Fijai"])

# print(states_of_america)


# Challenge 2
name_string = input("Give me evebody's name, seperated by a comma. ")
names = name_string.split(", ")
random_person = random.randint(0, len(names) - 1)
# print(random_person)
person_to_pay_bills = names[random_person]
print(f"The one to pay the bills is {person_to_pay_bills}")


print(len(states_of_america))

fruits = [
    "Strawberries",
    "Nectarines",
    "Apples",
    "Grapes",
    "Peaches",
    "Cherries",
    "Pears",
]

vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]

print(dirty_dozen)


# Challenge 3
# Treasure Map
row1 = ["🛑", "🛑", "🛑"]
row2 = ["🛑", "🛑", "🛑"]
row3 = ["🛑", "🛑", "🛑"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

position = input("Where do you want to put the treasure? ")

horizontal = int(position[0])
vertical = int(position[1])

selected_row = map[vertical - 1]
selected_row[horizontal - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")


# Rock, Paper,Scissors challenge
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

print("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")

game_image = [rock, paper, scissors]

user_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. ")
)
if user_choice >= 3 or user_choice < 0:
    print("You typed invalid number, You lose")
else:
    print(game_image[user_choice])

    computer_choice = random.randint(0, 2)
    print("computer chose:")
    print(game_image[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You wins!")

    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose!")
    elif user_choice > computer_choice:
        print("You win")
    elif computer_choice == user_choice:
        print("It's a Draw")
