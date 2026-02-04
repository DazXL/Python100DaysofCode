#task 1 is about describing a problem (bug)

def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it")


my_function()

# Describe the Problem - Write your answers as comments:
# 1. What is the for loop doing?
"""is looping values between 1 and 20"""

# 2. When is the function meant to print "You got it"?
"""when the value (i) is equal to 20"""

# 3. What are your assumptions about the value of i?
"""When the value of i is 20, it leaves ends the loop and the print statement will never be printed """

"""Fix"""

def my_function_fix():
    for i in range(1, 21): #changing end range to 21
        if i == 20:
            print("You got it")


my_function_fix()