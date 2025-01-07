
# If elif else
# > Greater than
# < Less than
# >= Greater than or equal to
# <= Less than or equal to
# == Equal to
# != Not equal to

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age? "))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        bill += 3

    print(f"Your final bill is ${bill}")

else:
    print("Sorry, you have to grow taller before you can ride.")


# The modulo operator gives you the remainder of a division.
# 6 % 2 #will be 0
# 6 % 5 #will be 1
# 6 % 4 #will be 2

user_input = int(input("Enter a whole number"))
if user_input % 2 == 0:
    print(f"The number {user_input} is an Even number")
else:
    print(f"The number {user_input} is an Odd number")