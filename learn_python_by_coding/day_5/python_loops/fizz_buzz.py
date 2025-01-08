# Range Function

# range(1, 10) -> 1 to 10 not including 10
for number in range(1, 10):
    print(number)

# range(1, 20, 3) -> 1-20 not including 20 step by 3
for number in range(1, 20, 3):
    print(number)


sum_to_100 = 0
for number in range(1, 101):
    sum_to_100 += number
print(sum_to_100)

for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)