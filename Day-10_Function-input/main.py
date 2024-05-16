def format_name(f_name, l_name):

    """
    Take a first and last name and formart it to return the title case version of the name 
    """
    if f_name == "" or l_name == "":
        return "Incorrect input"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()

    return f"{formated_f_name} {formated_l_name}"


output = format_name("ErIC", "obeng")
print(output)


# Exercise Days in a Month
"""
In the starting code, you'll find the solution from the Leap Year Challenge. first convert the function is_leap() so that instead of printing "Leap Year" or "Not Leap Year" it should return True if it is a leap year and return False if it is not a leap year

You are then going to create a function called days_in_month() which will take a year and a month as inputs.
"""


def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    if month > 12 and month < 1:
        return "Invalid month"

    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
