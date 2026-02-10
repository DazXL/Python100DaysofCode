# Task 2 is about adding Methods to a Class
#Methods are what objects do

class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    # This is a method, it will add 1 to the object following and add 1 to the attribute 'user' followers
    def follow(self, user):
        user.followers += 1
        self.following += 1

# Creating objects
user_1 = User("001", "DAZ")
user_2 = User("002", "EXTRALARGE")

# Calling the method for the object user_1 with the parameter value user_2
user_1.follow(user_2)

print(user_1.followers) # should print 0
print(user_1.following) # should print 1
print(user_2.followers) # should print 1
print(user_2.following) # should print 0
