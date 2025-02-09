from functools import reduce

nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
evens = list(filter(lambda x: x % 2 == 0, nums))
total = reduce(lambda x, y: x + y, nums)

print(squared, evens, total)