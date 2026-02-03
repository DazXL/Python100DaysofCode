#Task 1 is about Scope and Namespaces
enemies = 1


def increase_enemies():
    enemies = 2 # enemies variable value inside the function is only saved inside the function
                # the variable is in a local scope
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")
# when called outside the function it will use the value of the variable at the top which has a global scope.

'''A namespace is a system that has a unique name for each and every object in Python. 
   An object might be a variable or a method. 
   Python itself maintains a namespace in the form of a Python dictionary.'''