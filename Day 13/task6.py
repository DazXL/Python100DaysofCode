# Task 6 is about using the debugger
import random
import maths

"""
By clicking on the gutter (the line numbers on the left, you can add a "breakpoint" to the code, by running 
the debugger clicking on the bug button at the top the code will run and stop at the breakpoint.
    Running the debug will show several information about the current status of the script as variable values and
    states, you can also run the code step by step and even access other imported modules.
    That way, you can verify step by step what is wrong with the code.

    The case bellow, instead of printing a list with several numbers, it prints a list with a single number
    There is a typo in the code where the .append is not indented in the for loop.
    Just adding the indent will fix the code
"""


def mutate(a_list):
    b_list = []
    new_item = 0
    for item in a_list:
        new_item = item * 2
        new_item += random.randint(1, 3)
        new_item = maths.add(new_item, item)
        b_list.append(new_item)  # indent added
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])  # calling the function
