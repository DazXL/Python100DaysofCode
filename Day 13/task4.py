#Task 4 is about fixing problems, using Try/Except python block
"""There are several problems with the code bellow lets list them"""

# age = int(input("How old are you?"))
# if age > 18:
# print("You can drive at age {age}.")

""" 1. The code indentation is wrong, this will result in an error, it can be noticed by the red underline
    2. if the input can't be parsed as int, an error will occur
    3. The print statement need to be formated
    """
"""Fix"""

#the Try/except block catches an exception that might occur and executes something else instead
#parsing a string input will not result in an error anymore
try:
    age = int(input("How old are you?"))
except ValueError:
    print("Invalid input, please type numbers only")
    age = int(input("How old are you?"))
# properly indenting and formating the print statement will make the code run properly
if age > 18:
    print(f"You can drive at age {age}.")
