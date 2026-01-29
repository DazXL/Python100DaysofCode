# Task 1 presents a dictionary. a Dictionary is created using curly brackets.
# It can contain a key followed by a value, they are separate by a colon
# a dictionary can have several keys each having their value, just separate them with a comma


programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
}

print(programming_dictionary["Bug"]) # prints the value of the selected key.

# using For loop to print the values in the keys of the dictionary
for key in programming_dictionary:
    print(programming_dictionary[key])

#adding keys and values to the dictionary

programming_dictionary["Loop"] = "The action of doing something over and over again."
for key in programming_dictionary:
    print(programming_dictionary[key])

# you can create an empty dictionary

empty_dictionary = {}

# you can also clear an existing dictionary

programming_dictionary = {}
print(programming_dictionary)

# you can edit an item in a dictionary

programming_dictionary["Bug"] = "A Moth in your Computer" # (this is a lie!)
