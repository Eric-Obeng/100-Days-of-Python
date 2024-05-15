programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A function is a piece of code that can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

# Retrieving items from dictionary
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["List"] = "Can contain multiple data types"
print(programming_dictionary)

# loop through a dictionary
# for key in programming_dictionary:
#     print(key)
#     print(programming_dictionary[key])


# Exercise 1: Grading Program
"""
You have access to a database of student_scores in the format of a dictionary. The keys in student_score are the names of the students and the values are their exams scores.

Write a program that converts their scores to grades. By the end of your program, you should have a new dictionary called student_grades that should contain student names for keys and their grades for value. The final version of the student_grades dictionary will be checked.
"""
# Solution
students_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

student_grades = {}

for student in students_scores:
    score = students_scores[student]
    if score > 90:
        student_grades[student] = "Outstanding"
    elif score > 80:
        student_grades[student] = "Exceeds Expectation"
    elif score > 70:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"


print(student_grades)


# Nesting
dictionay = {"Key1": 1, "Key2": 3}


# Nesting Dictionary in a Dictionary
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}


# Exercise 2: Dictionary in List
my_travels = [
    {"country": "France", "visits": 12, "cities": ["Paris", "Lille", "Dijon"]},
    {"country": "Germany", "visits": 5, "cities": ["Berlin", "Hamburg", "Stuttgart"]},
]


def add_new_country(country, number_of_visits, cities_visited):
    new_country = {}
    new_country["coutry"] = country
    new_country["visits"] = number_of_visits
    new_country["cities"] = cities_visited
    my_travels.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(my_travels)
