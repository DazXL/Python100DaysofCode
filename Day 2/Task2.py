#Task 2 is about Type Error, checking and covnersion
#len(12345) prints an error as len() is used for Strings only

#checking data Types with type()
print(type("String"))
print(type(123))
print(type(1.23))
print(type(True))

#conversion
print("123" + "456") #concatenates strings
print(int("123") + int("456")) #converts strings into integers then calculates

#it is possible to convert floats into integers and a string of numbers into integers and floats.
#not all types are convertibles to others

#making this code run without errors
#print("Number of letters in your name: " + len(input("Enter your name")))
print("Number of letters in your name: " + str(len(input("Enter your name"))))

#or simplifying the code

userName = input("Enter your name: ")
lengthName = len(userName)
print("Number of letters in your name: " + str(lengthName))