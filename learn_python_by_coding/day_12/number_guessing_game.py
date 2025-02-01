import random
from art import game_logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS
    


def number_guessing_game():
    print(game_logo)
    print("Welcome to the number guessing game!\n")
    print("I'm thinking of a number between 1 and 100.\n")

    generated_answer = random.randint(1, 100)  
    number_of_attempts = set_difficulty()

    print(f"\nYou have {number_of_attempts} attempts to guess the number.\n")
    user_guess = input("Make a guess: ")

    while number_of_attempts > 0:
        if user_guess.isdigit():
            guess = int(user_guess)
            if guess == generated_answer:
                print("Congratulations! You guessed the number.")
                break
            elif guess < generated_answer:
                print("Too low.")
            else:
                print("Too high.")

            # decrement the number of attempts    
            number_of_attempts -= 1
            
            # check if the user has any attempts left
            if number_of_attempts == 0:
                print(f"Sorry, you've run out of attempts. The number was {generated_answer}.")
            else:    
                print(f"You have {number_of_attempts} attempts remaining.\n")
                user_guess = input("Make a guess: ")
        else:
            print("Invalid input. Please enter a number.")
            user_guess = input("Make a guess: ")


# start the game
number_guessing_game()