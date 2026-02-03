#Task 2 is about Block Scope

"""Python is a bit different from other programming languages in that it does not have block scope.
This means that variables created nested in other blocks of code e.g. for loops, if statements, while loops etc.
 don't get local scope. They are given function scope if they are within a function or global scope if they are not.
"""
if 2 < 3:
    variable = "that's right!"

print(variable)