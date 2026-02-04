# Task 3 is about playing computer to fix the bug
year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
elif year > 1994:
    print("You are a Gen Z.")


"""When the input is equal to 1994, nothing happens and the process ends"""
"""Playing computer and going through every line to find the issue"""

"""we know the Year is 1994"""
"""1994 is higher than 1980 but it is not lower than 1994, it skips to the elif"""
"""1994 is not higher than 1994 the it also skips this one"""
"""the code ends and the process exists as it should"""

"""fix"""

year_fix = int(input("What's your year of birth?"))

if year_fix > 1980 and year < 1994:
    print("You are a millennial.")
elif year_fix >= 1994: # Adding greater or equal symbol fixes the issue
    print("You are a Gen Z.")