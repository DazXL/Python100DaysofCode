# Task 3 is a function to check if the number is prime

"""
Prime numbers are numbers that can only be cleanly divided by themselves and 1
2 is a prime number because it's only divisible by 1 and itself,
but 1 is not a prime number because it is only divisible by 1.
No other even number can be a prime number.
"""
def is_prime(num):
    if num == 1:
        return False # 1 is not a prime number
    elif num == 2:
        return True # 2 is the only even prime number
    # Loop through the numbers between 2 and the number
    for i in range(2, num):
        if num % i == 0:
            return False #if any of them returns 0 it is not a prime number

    return True #after all the blocks runs and no return happens, then the number is a prime number
number = int(input("type a number: "))
print(str(number) + " is...")
print(is_prime(number))
