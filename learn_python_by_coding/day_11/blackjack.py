import random
import art

def deal_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(deal_cards):
    # check for blackjack
    if len(deal_cards) == 2 and sum(deal_cards) == 21:
        return 0

    # 
    # if 11 in deal_cards and sum(deal_cards) > 21





print(art.logo)


should_play = input("Do you want to play a game of Blackjack? Types 'y' or 'n': ")
if should_play:
    print("Lets play...!")
    user_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    print(user_cards)
    print(computer_cards)

else:
    print("Bye Bye...")