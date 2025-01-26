# Python Dictionaries

Python dictionaries are unordered collections of items. Each item in a dictionary is stored as a key-value pair. Dictionaries are mutable, meaning they can be changed after they are created.
 - https://docs.python.org/3/tutorial/datastructures.html#dictionaries

## Creating a Dictionary

You can create a dictionary by placing a comma-separated sequence of key-value pairs within curly braces `{}`.

**Example:**
```python
# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 25,
    'city': 'New York'
}
```

## Accessing Values
You can access the value associated with a specific key using square brackets [].
```python
# Creating a dictionary
print(my_dict['name'])  # Output: John
print(my_dict['age'])   # Output: 25
```
## Adding and Updating Items
You can add a new key-value pair or update an existing key-value pair by using the assignment operator =.

```python
# Adding a new key-value pair
my_dict['email'] = 'john@example.com'

# Updating an existing key-value pair
my_dict['age'] = 26
```

## Removing Items
You can remove items from a dictionary using the del statement or the pop() method.

```python
# Using del statement
del my_dict['city']

# Using pop() method
email = my_dict.pop('email')
```

## Dictionary Methods
Python dictionaries have several built-in methods that you can use to work with them.

- `keys()`: Returns a view object that displays a list of all the keys in the dictionary.
- `values()`: Returns a view object that displays a list of all the values in the dictionary.
- `items()`: Returns a view object that displays a list of all the key-value pairs in the dictionary.
- `get(key)`: Returns the value for the specified key if the key is in the dictionary.
- `clear()`: Removes all items from the dictionary.

```python
# Using dictionary methods
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()

print(keys)   # Output: dict_keys(['name', 'age'])
print(values) # Output: dict_values(['John', 26])
print(items)  # Output: dict_items([('name', 'John'), ('age', 26)])
```

## Iterating Through a Dictionary
You can iterate through a dictionary using a for loop.

```python
# Iterating through keys
for key in my_dict:
    print(key, my_dict[key])

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(key, value)
```

## Nested Dictionaries
Dictionaries can contain other dictionaries, which are called nested dictionaries.

```python
# Creating a nested dictionary
nested_dict = {
    'person1': {'name': 'John', 'age': 25},
    'person2': {'name': 'Jane', 'age': 30}
}

# Accessing values in a nested dictionary
print(nested_dict['person1']['name'])  # Output: John
print(nested_dict['person2']['age'])   # Output: 30
```

## Finding Maximum Value in a Dictionary

You can find the maximum value in a dictionary using the `max` function. The `max` function can be used to find the key with the maximum value.

```python
# Finding the maximum value in a dictionary
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 88}
max_score = max(scores.values())
print(max_score)  # Output: 92
```
The expression max(scores.items(), key=lambda x: x[1]) is used to find the key-value pair with the maximum value in a dictionary called scores.

Here's how it works:

- `bidding_record.items()` returns a view object that displays a list of the dictionary's key-value tuple pairs.
- `key=lambda x: x[1]` specifies that the max function should compare the items based on their values (the second element of each tuple).
    - In Python, a lambda is a shorthand way to define a small, anonymous function (a function without a name). It’s often used when you need a simple function for a short period, especially as an argument to functions like max(), sorted(), or filter().

```python
scores = {
    'Alice': 150,
    'Bob': 200,
    'Charlie': 180
}

# Find the key-value pair with the maximum value
highest_score = max(scores.items(), key=lambda x: x[1])
print(highest_score)  # Output: ('Bob', 200)
```


## Conclusion
Dictionaries are a powerful and flexible data structure in Python. They allow you to store and manipulate data using key-value pairs, making it easy to organize and access information. Understanding how to work with dictionaries is essential for any Python programmer.