import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
placeholder = ""
correct_letters = []
user_lives = 3
game_over = False

# crate a placeholder text like _____
for number in range(0, len(chosen_word)):
    placeholder += "_"

print(chosen_word)
print(placeholder)

while not game_over:
    display_word = ""
    guess = input("Guess a letter: ").lower()

    if guess in chosen_word:
        for letter in chosen_word:
            if letter == guess:
                display_word += guess
                correct_letters.append(guess)
            elif letter in correct_letters:
                display_word += letter
            else:
                display_word += "_"
        print(display_word)
        if "_" not in display_word:
            game_over = True
            print("You won")
    else:
        user_lives -= 1
        if user_lives == 0:
            game_over = True
            print("You lost")
        else:
            print('You lost a life')

