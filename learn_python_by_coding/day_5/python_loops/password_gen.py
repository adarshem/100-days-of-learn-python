import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

mix_of_items = []
# Get random letters from letters list based on nr_letters input
for number in range(0, nr_letters):
    mix_of_items.append(random.choice(letters))

# Get random symbols from symbols list based on nr_symbols input
for number in range(0, nr_symbols):
    mix_of_items.append(random.choice(symbols))

# Get random numbers from numbers list based on nr_numbers input
for number in range(0, nr_numbers):
    mix_of_items.append(random.choice(numbers))

# add more randomness
random.shuffle(mix_of_items)
# create the password string
password = ''
for item in mix_of_items:
    password += item

print(f"Your password is: {password}")

