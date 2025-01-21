import random
# import hangman_ui -> This will import the whole module
from hangman_ui import stages, logo # This will import only the stages and logo variables
from hangman_words import word_list, film_names, common_words, animal_names

# Print the game logo
print(f"{logo}\n")

# Ask the user to choose a word category
print("Choose a word category:")
print("1. Common Words")
print("2. Famous Film Names")
print("3. Animal names")

words_category = int(input("Enter the number corresponding to your choice (1, 2, or 3): "))
if words_category not in [1, 2, 3]:
    print("You have entered an invalid choice. Exiting the game.")
    exit()

categoryies = [word_list, common_words, film_names, animal_names]
chosen_word = random.choice(categoryies[words_category])
placeholder = ""
guessed_parts = ""
correct_letters = []
user_lives = 6
game_over = False

# crate a placeholder text like _____
for number in range(0, len(chosen_word)):
    placeholder += "_"

while not game_over:
   
    print(f"\n**************************** {user_lives}/6 LIVES LEFT****************************\n")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    display_word = ""
    if guess in chosen_word:
        for letter in chosen_word:
            if letter == guess:
                display_word += guess
                correct_letters.append(guess)
            elif letter in correct_letters:
                display_word += letter
            else:
                display_word += "_"

        print(f"Word to guess: {display_word}")
        guessed_parts = display_word

        if "_" not in display_word:
            game_over = True
            print("**************************** YOU WIN ****************************")
    else:
        user_lives -= 1
        if user_lives == 0:
            game_over = True
            print(f"*********************** IT WAS {chosen_word}! YOU LOSE **********************")
        else:
            print(f"You guessed {guess}, that's not in the word. You lose a life.")
            print(f"Word to guess: {guessed_parts}")

    print(stages[user_lives])
