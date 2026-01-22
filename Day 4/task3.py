#Task 3 is a challenge using what we learned
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#pick a random name from the list

#1st way
print(random.choice(friends))

#2nd way
randomName = random.randint(0, 4)
print(friends[randomName])