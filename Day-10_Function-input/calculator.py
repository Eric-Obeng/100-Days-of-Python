from art import logo

# print(logo)


# Add
def add(n1, n2):
    return n1 + n2


# Subtract
def sub(n1, n2):
    return n1 - n2


# Multiply
def mult(n1, n2):
    return n1 * n2


# Divide
def div(n1, n2):
    return n1 / n2


operations = {"+": add, "-": sub, "*": mult, "/": div}


def calculator():
    print(logo)

    num1 = float(input("What is the first number?: "))
    should_continue = True

    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")

        num2 = float(input("What is the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        new_calculation = input(
            "Type 'y' to continue calculating with {answer}, or type 'n' to start over.: "
        )

        if new_calculation == "y":
            num1 = answer
        else:
            should_continue = False
            calculator()

        # operation_symbol = input("Pick another operation: ")
        # num3 = int(input("What is the next number?: "))
        # calculation_function = operations[operation_symbol]
        # next_answer = calculation_function(answer, num3)

        # print(f"{answer} {operation_symbol} {num3} = {next_answer}


calculator()
