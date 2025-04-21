# ---------------------------------- #
# print() — The OG Python function
# ---------------------------------- #
name = "Tim"
age = 23
print("My name is", name, "and I am", age, "years old") # By default, it separates things with a space. 

# Custom Separators with sep
print("My name is", name, "and I am", age, "years old", sep=", ") # You can change the separator to a comma and space.
print("My name is", name, "and I am", age, "years old", sep="|") # You can change the separator to a pipe.

# Custom Ending with end
print("My name is", name, "and I am", age, "years old", end=".") # You can change the ending to a period.

# These sep and end tweaks are super handy for formatting output without string concatenation or f-strings.


# ---------------------------------- #
# f-strings — The Cool Kid on the Block
# ---------------------------------- #
# f-strings are a way to format strings in Python. They are more readable and concise than the older methods.
# f-strings are prefixed with an 'f' or 'F' and allow you to embed expressions inside curly braces.
# examples:
name = "Tim"
age = 23
print(f"My name is {name} and I am {age} years old") # This is the most common way to use f-strings.
print(f"My name is {name.upper()} and I am {age + 1} years old") # You can also use expressions inside the curly braces.
print(f"My name is {name} and I am {age} years old", end=".") # You can also use the end parameter with f-strings.

# ---------------------------------- #
# help() — The Python Help Function
# The help() function shows you documentation for Python objects—functions, classes, modules, etc.
# ---------------------------------- #
# help(print)

# ---------------------------------- #
# range() — Your go-to for generating sequences
# By default, it starts from 0 and goes up to (but not including) the number you give it.
# ---------------------------------- #
range(5)  # 0, 1, 2, 3, 4
range(2, 6)  # 2, 3, 4, 5
range(1, 10, 2)  # 1, 3, 5, 7, 9
range(10, 0, -2)  # 10, 8, 6, 4, 2

# range() returns a range object, not a list. But you can convert it:
print(list(range(5)))  # [0, 1, 2, 3, 4]

# ---------------------------------- #
# map() applies a function to every item in an iterable (like a list) and returns a map object (which is an iterator).
# ---------------------------------- #

# Example with a regular function:
def square(n):
    return n * n

numbers = [1, 2, 3, 4]
result = map(square, numbers)

print(list(result))  # [1, 4, 9, 16]

# Example with a lambda function:
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16]

# You can use map() with multiple iterables too:
a = [1, 2, 3]
b = [4, 5, 6]

result = map(lambda x, y: x + y, a, b)
print(list(result))  # [5, 7, 9]


# •	map() returns a map object, which is an iterator — so you’ll often wrap it in list() or loop over it.
# •	It’s memory efficient (doesn’t immediately compute everything).
# •	Super handy for quick transformations on large data sets.

# ---------------------------------- #
# filter() filters items in an iterable based on a function that returns True or False.
# ---------------------------------- #

def is_even(n):
    return n % 2 == 0

numbers = [1, 2, 3, 4, 5, 6]
filtered_result = filter(is_even, numbers)

print(list(filtered_result))  # [2, 4, 6]

# Example with a lambda function:
numbers = [10, 15, 20, 25]
evens = filter(lambda x: x % 2 == 0, numbers)

print(list(evens))  # [10, 20]