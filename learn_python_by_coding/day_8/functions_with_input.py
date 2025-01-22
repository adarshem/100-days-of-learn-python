def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# Positional argument
greet_with('Adarsh', 'Vancouver')

# Keyword arguments
greet_with(name='Adarsh', location='Vancouver')

greet_with(location='Vancouver', name='Adarsh')


# Love calculator
def calculate_love_score(name_1, name_2):
    true_score = 0
    love_score = 0
    for letter in name_1 + name_2:
        if letter in 'true':
            true_score += 1
        if letter in 'love':
            love_score += 1
    print(f"{true_score}{love_score}")

calculate_love_score("Kanye West", "Kim Kardashian")
