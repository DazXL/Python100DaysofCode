# this is an example about file paths
with open("../new_file.txt") as file:
    print(file.read())

'''
when opening a file in python it needs the proper path to the file, when a file is at the same directory 
the name suffice, but when the file is in a different directory you must give the right path to it.
as the new_file.txt file is at the upper directory, we use the ../ to go back one directory
'''