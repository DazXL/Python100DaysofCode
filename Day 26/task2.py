""" Task 2 is a challenge on Data Overlap
💪 This exercise is HARD 💪

Take a look inside file1.txt and file2.txt. They each contain a bunch of numbers, each number on a new line.

You are going to create a list called result which contains the numbers that are common in both files. """

with open("file1.txt") as file_one:
    list1 = [int(n) for n in file_one.readlines() if n != '\n']

with open("file2.txt") as file_two:
    list2 = [int(n) for n in file_two.readlines() if n != '\n']
print(list1)
print(list2)

result = [n for n in list1 if n in list2]
print(result) # it should print [3, 6, 5, 33, 12, 7, 42, 13]