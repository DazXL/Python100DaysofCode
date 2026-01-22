#Task 1 is about Random Module

import random #import the random module
import my_module #it is possible to import a module (python file) that you created yourself

randomInteger = random.randint(1,10)
print(randomInteger)
print(my_module.my_favourite_number) # prints a variable from the module created.

# https://docs.python.org/3/library/random.html for the random module references

randomNumberZeroToOne = random.random() * 10 # float number between 0 and 10. Random never results the number 1!
print(randomNumberZeroToOne)

randomFloat = random.uniform(1, 10) # uniform includes the lower and the upper range as in, you can get 1 and 10.
print(randomFloat)

# Coin flip

if random.randint(0, 1) == 0:
    print("Heads")
else:
    print("Tails")