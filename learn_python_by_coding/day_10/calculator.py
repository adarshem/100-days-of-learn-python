import art

def add_operation(number_1, number_2):
    return number_1 + number_2

def sub_operation(number_1, number_2):
    return number_1 - number_2

def multiplication_operation(number_1, number_2):
    return number_1 * number_2

def division_operation(number_1, number_2):
    return number_1 / number_2

operations = {
    "+": add_operation,
    "-": sub_operation,
    "*": multiplication_operation,
    "/": division_operation
}

def calculator():
    print(art.logo)
    result = 0
    should_continue_calculation = True
    current_number = float(input("What's the first number?:"))

    while should_continue_calculation:
        user_operation = input("Pick an operation from +,-, *, / : ")

        if user_operation not in operations.keys():
            print("You have selected an invalid operation!")
            exit()

        next_number = float(input("What's the next number?:"))
        result = operations[user_operation](current_number, next_number)

        print(f"{current_number} {user_operation} {next_number} = {result}")
        continue_with_current_result = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if continue_with_current_result == 'y':
            current_number = result
        else:
            should_continue_calculation = False
            print("\n", result)
            calculator()

# call the calculator function
calculator()
