#task 2 is about reproducing the bug

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6)
print(dice_images[dice_num])

"""The dice_images list range goes from 0 to 5"""
"""The bug happens when the dice_num = randint(1, 6) happens to be a 6, which is out of the list range"""
"""as a way to reproduce the bug is just change the dice_num to a fixed int value"""

# dice_num = 6
# print(dice_images[dice_num])

"""Fix:"""
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5) # changing the range so it fits the range of the list.
print(dice_images[dice_num])