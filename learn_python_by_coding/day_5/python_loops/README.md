# For Loops and Range Function

This folder contains examples and explanations of `for` loops and the `range` function in Python. These are fundamental concepts for iterating over sequences and generating sequences of numbers.

## `for` Loop

The `for` loop is used to iterate over a sequence (such as a list, tuple, dictionary, set, or string) and execute a block of code for each item in the sequence.

- [Python doc - for statement](https://docs.python.org/3/tutorial/controlflow.html#for-statements)

**Syntax:**
```python
for item in sequence:
    # code to execute

Example:

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

## `range` Function
The `range` function generates a sequence of numbers, which is often used in `for` loops. It can take one, two, or three arguments.

- [Python doc - range function](https://docs.python.org/3/tutorial/controlflow.html#the-range-function)

Syntax:
```python
range(stop)
range(start, stop)
range(start, stop, step)
```

- `start`: The starting value of the sequence (inclusive). Default is 0.
- `stop`: The end value of the sequence (exclusive).
- `step`: The difference between each number in the sequence. Default is 1.

Examples:
```python
# Using range with one argument
for i in range(5):
    print(i)  # Output: 0 1 2 3 4

# Using range with two arguments
for i in range(1, 5):
    print(i)  # Output: 1 2 3 4

# Using range with three arguments( 3rd is the step)
for i in range(1, 10, 2):
    print(i)  # Output: 1 3 5 7 9
```

## Conclusion
Understanding `for` loops and the `range` function is essential for iterating over sequences and generating sequences of numbers in Python. These tools are widely used in various programming tasks and are fundamental to mastering Python.