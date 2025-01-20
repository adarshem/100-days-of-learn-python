import random
from hangman_words import word_list
from hangman_ui import stages, logo

chosen_word = random.choice(word_list)
placeholder = ""
guessed_parts = ""
correct_letters = []
user_lives = 6
game_over = False

# Print the game logo
print(logo)

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
