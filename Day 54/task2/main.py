#Task 2 is about Python Decorator
import time

def delay_decorator(function): #the decorator function
    def wrapper_function(): #the wrapper function that will execute the wrapped function differently
        time.sleep(2)
        function() #the called function to be wrapped bellow
    return wrapper_function #returns the wrapped function


@delay_decorator #the at is called a syntax sugar
def say_hello():
    print("Hello!")

@delay_decorator
def say_goodbye():
    print("Goodbye!")

say_hello() #will use the delay_decorator function, it should wait 2 seconds before executing the say_hello function

#another way of doing the same as the syntax sugar
decorated_function = delay_decorator(say_goodbye)
decorated_function()