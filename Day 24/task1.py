# Task 1 is an example of file manipulation

# open() function opens a file, in this case the file.txt

file = open("file.txt")

# .read() function "reads" the content of the open file

print(file.read())

# .close() function closes the file to free up memory

file.close()

# other ways to open a file is by using with
#this way the file closes right after the code is executed
with open("file.txt") as file:
    print(file.read())

# you can also write on certain files

with open("file.txt", mode="a") as file:
    # there are several "mode", w is for writing over the content

    # "a" can be used to append to the file
    file.write("\n My name is Daz!")

with open("new_file.txt", mode="w") as file:
    # if you open a file that does not exist it will create that file on w mode
    file.write("Hello World!\nMy name is Daz!")