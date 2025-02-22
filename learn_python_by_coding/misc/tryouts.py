from functools import reduce

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
total = reduce(lambda x, y: x + y, nums)

print(squared, evens, total)


#---------- how to use map, filter, and reduce with dictionaries ----------#

# Example dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

print(F"my_dict.items(): {my_dict.items()}")
print(F"my_dict.values(): {my_dict.values()}")
print(F"my_dict.keys(): {my_dict.keys()}")

# Use map to square the values
squared_values = dict(map(lambda item: (item[0], item[1] ** 2), my_dict.items()))
print("Squared values:", squared_values)  # Output: {'a': 1, 'b': 4, 'c': 9, 'd': 16}

# Use filter to keep only even values
even_values = dict(filter(lambda item: item[1] % 2 == 0, my_dict.items()))
print("Even values:", even_values)  # Output: {'b': 2, 'd': 4}

# Use reduce to sum the values
total_sum = reduce(lambda x, y: x + y, my_dict.values())
print("Total sum:", total_sum)  # Output: 10

# Sort the dictionary by values
sorted_dict = dict(sorted(my_dict.items(), key=lambda item: item[1]))
print("Sorted dictionary:", sorted_dict)  # Output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}