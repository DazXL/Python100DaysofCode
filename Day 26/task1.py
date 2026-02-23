# Task 1 is about List Comprehension
""" List Comprehension is a case when you create a list from a new list """

numbers = [1, 2, 3] # a List

''' The List Comprehension '''
new_list = [ n + 1 for n in numbers] # creating a list that will have each number from previous list + 1
print(new_list) # should print [2, 3, 4]

''' List Comprehension with Strings '''

name = 'DazExtralarge'

letters_list = [letter for letter in name] #it splits the string and creates a list with each character
''' Lists, just like range, string and tuples are considered Python Sequences
   The code will run it in order, like the for above did '''
print(letters_list) # should print ['D', 'a', 'z', 'E', 'x', 't', 'r', 'a', 'l', 'a', 'r', 'g', 'e']

''' Usage of Range function:
    Range is a sequence, so the code bellow will go from 1, 2, 3 and 4 and multiply then by two'''

range_list = [num * 2 for num in range(1,5)]
print(range_list) # Should print [2, 4, 6, 8]

''' Conditional List Comprehension:'''
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
conditional_list = [n for n in names if len(n) < 5] # it will only add the names with length lower than 5
print(conditional_list) # should print ['Alex', 'Beth', 'Dave']

long_names = [name.upper() for name in names if len(name) > 5] #it will only add the names with length over 5 and all caps
print(long_names) # should print ['CAROLINE', 'ELANOR', 'FREDDIE']