import random
from art import logo
from game_data import data

def high_or_log_game():
    print(logo)
    user_score = 0
    game_over = False

    # Start with selecting 2 items from the available data set
    [option_a, option_b] = random.choices(data, k=2)


    while not game_over:
        # Create a data set excluding the previously selected 2 option. This helps generate new options without repeating old options
        updated_data_set = list(
            filter(lambda item: item['name'] != option_a['name'] and item['name'] != option_b['name'], data))

        print(f"Compare A: {option_a['name']}, {option_a['description']}, from {option_a['country']}")
        print("\nVs\n")
        print(f"Compare B: {option_b['name']}, {option_b['description']}, from {option_b['country']}")
        print("\n")

        user_selected = input("Who has more followers? Type 'A' or 'B': ").lower()

        if user_selected == 'a':
            if option_a['follower_count'] >= option_b['follower_count']:
                user_score += 1
                option_b = random.choice(updated_data_set)
                print(f"You are correct. Current Sore: {user_score}")
            else:
                print(f"Sorry, that's wrong. Final score: {user_score}")
                game_over = True
        else:
            if option_b['follower_count'] >= option_a['follower_count']:
                user_score += 1
                option_a = option_b
                option_b = random.choice(updated_data_set)
                print(f"You are correct. Current Sore: {user_score}")
            else:
                print(f"Sorry, that's wrong. Final score: {user_score}")
                game_over = True


# start the game
high_or_log_game()
