MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "milk": 500,
    "coffee": 300,
}

total_profit = 0
should_machine_off = False

# Function to print the Coffee machine report
def get_report():
    for key, value in resources.items():
        print(f"{key.title()}: {value}ml")
    print(f"Amount collected: ${total_profit}")

# Function to check if resources is enough to create the item user selected
def check_enough_resource(item_ingredients) -> bool:
    for ingredient in item_ingredients:
        if resources[ingredient] < item_ingredients[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            return False
    return True

# Function to process coins
def process_coins():
    try:
        quarters = int(input("how many quarters?: "))
        dimes = int(input("how many dimes?: "))
        nickles = int(input("how many nickles?: "))
        pennies = int(input("how many pennies?: "))

        return 0.25 * quarters + 0.10 * dimes + 0.05 * nickles + 0.01 * pennies
    except ValueError:
        print("You have provided invalid coins. Please provide valid coins")
        return process_coins()


# Function to update the machine resource after creating an item
def update_resource(item_selected):
    ingredients_used = MENU[item_selected]["ingredients"]
    for ingredient in ingredients_used:
        resources[ingredient] -= ingredients_used[ingredient]

def create_coffee(user_choice, amount_provided, item_cost):
    update_resource(user_choice)
    if amount_provided > item_cost:
        print(f"Here is ${round(amount_provided - item_cost, 2)} in change.")
    global total_profit
    total_profit += item_cost
    print(f"Here is your {user_choice} ☕️. Enjoy!")
    


while not should_machine_off:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "report":
        get_report()
    elif user_choice == "off":
        should_machine_off = True
    elif user_choice not in MENU:
        print("You have provided invalid option. Please provide valid input.")
    else:
        item_opted = MENU[user_choice]
        if check_enough_resource(item_opted["ingredients"]):
            amount_provided = process_coins()
            item_cost = item_opted["cost"]
            if amount_provided < item_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                create_coffee(user_choice, amount_provided, item_cost)

