# Task 2 is about default values arguments and *args

def add(*args): #the args becomes a tuple
    print(args[0]) # will print the first value
    sum = 0
    for n in args:
        sum += n
    return sum

print(add(1,2,3,4,5))

# **kwargs

def calculate(n, **kwargs): #**kwargs is a dictionary
    print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(2, add=3, multiply=2) #will print the kwargs as a dictionary and 10 because 2 + 3 = 5 times 2 = 10


#better way to get kwarg values

class Car:
    def __init__(self, **kw):
        self.make = kw.get("make") #using the get function will not give an error if you're missing any arguments.
        self.model = kw.get("model")