# Built-in python functions
# https://docs.python.org/3/library/functions.html
# define a function using "def" keyword
# provide a name and set of parentheses and a colon
# function definition lines are intended
def my_function():
    print("Adarsh")
    print("is amazing")

# then call the function by specifying the name and parentheses
my_function()

# Function with a parameter
def func_with_args(input1):
    print(f'The square of the number {input1} is : {input1 ** 2}')

func_with_args(10)


# function with typing
# defining a function that takes a parameter of type string and returns a string
def func_with_typing(input1: str) -> int:
    return len(input1)

print(func_with_typing('Adarsh'))