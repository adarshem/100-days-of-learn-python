import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rock_paper_scissors_list = [rock, paper, scissors]
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
    exit()

print("You selected:")
print(rock_paper_scissors_list[user_choice])
print("Computer selected:")
print(rock_paper_scissors_list[computer_choice])



if computer_choice == user_choice:
    print("It's a draw")
else:
    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose")
    else:
        print("You win!")