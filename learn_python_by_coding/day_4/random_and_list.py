# https://docs.python.org/3/library/random.html
import random

random_value = random.randint(0,1)

if random_value == 1:
    print("Heads")
else:
    print("Tails", "wow", "lala", sep="-")


# Figure out how to pick a random name from the list of friends.
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# Based on what I know
randomIndex = random.randint(0, len(friends) - 1)
print(friends[randomIndex])

# After reading through documents
print(random.choice(friends))