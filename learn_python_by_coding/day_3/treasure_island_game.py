print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
toWhere = input("Which direction? Type 'Left' or 'Right'")
if toWhere != "Left":
    print("Fall into a hole. Game over!!!")
    exit()

swimOrWait = input("Do you want to wait for the boat or swim across the river? Type 'Swim' or 'Wait")
if swimOrWait != "Wait":
    print("Attacked by Crocodile. Game over!!!")
    exit()

selectedDoor = input("Which door you want to open? There is a Red door, a Yellow door and a Blue door. Type 'Red', 'Yellow' Or 'Blue' ")
if selectedDoor == "Yellow":
    print("Wow. You just found the treasure!!!!")
elif selectedDoor == "Red":
    print("Burned by fire. Game over!!!")
elif selectedDoor == "Blue":
    print("Eaten by Tiger. Game over!!!")
else:
    print("Fell into deep hole. Game over!!!")
