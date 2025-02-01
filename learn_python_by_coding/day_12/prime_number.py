import math

def is_prime(num):
    # Numbers less than or equal to 1 are not prime
    if num <= 1:
        return False
    
    # Check divisibility from 2 to the square root of n
    for i in range(2, int(math.sqrt(num)) + 1):
        if num  % i == 0:
            return False
    
    # If no divisors were found, n is prime    
    return True

# Test the function
print(is_prime(1)) # False
print(is_prime(2)) # True
print(is_prime(3)) # True
print(is_prime(4)) # False
print(is_prime(5)) # True
print(is_prime(6)) # False
