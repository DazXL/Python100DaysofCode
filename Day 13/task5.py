# Task 5 is about using print() to find out what is wrong with the code
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page
print(total_words) #returns 0

"""checking the error with print()"""
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page == int(input("Number of words per page: "))
total_words = pages * word_per_page

print(pages)
print(type(word_per_page))

print(total_words)

"""
    the word per page variable prints 0, what is wrong?
    The typo in the variable is that it compares the variable to the input value instead of storing it
    As the original value is 0, it will maintain that value and multiply it with the pages resulting in a 0 total words
"""

"""Fix"""
# word_per_page = 0 # commenting this declaration so it does not have any warning
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # correcting the symbol
total_words = pages * word_per_page
print(total_words) #returns the correct value