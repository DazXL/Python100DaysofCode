#Task 1 is about Creating Classes

class User:
    pass # classes (and functions) needs indented content, or it will return error, this keyword avoids that

""" Manipulating objects """
user_1 = User() #creats an object from a class
user_1.id = "001" #create attribute ID to the OBJECT not the Class
user_1.username = "DAZ" # creates attribute username

print(user_1.username) # should print "DAZ"

""" You can create different objects with their own attributes """

user_2 = User()
user_2.id = "002"
user_2.username = "EXTRALARGE"
print(user_2.username)

""" A Constructor is a special function inside of a class that initialize attributes to an object"""

class NewUser:
    # this is the special function
    def __init__(self, id, username):
        # it will parse the attributes to the object when it is created
        self.id = id
        self.username = username
        self.followers = 0 #this attribute doesn't need to be parsed when creating the object, the value is already set

user_3 = NewUser("003", "ISAPUNK") #values added

print(user_3.id, user_3.username)

#you can also edit or add more attributes to the object

user_3.id = "007"
user_3.username = "DAZ EXTRALARGE"
user_3.comment = "IS A PUNK"
print(user_3.id, user_3.username, user_3.comment)
