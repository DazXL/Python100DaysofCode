#Task 4 is about Variables and how to use the Length function.

name = "DAZXL" #a variable that receives the content "DAZXL"
print(name) #prints the variable content
print(len(name)) #prints the length of the content of the variable

#print(len(input("What is your name? "))) # does the same as bellow, but it is hard to read.

username = input("Enter your name: ")
length = str(len(username))

print("The username " + username + " has " + length + " characters.")
