# Task 4 is about Modifying Global Scope

enemies = 1 #global variable


def increase_enemies(enemy):
    #global enemies # calls in the global variable
    #enemies += 1 #changes the global variable

    """a better way to modify a global variable is by reading it and returning as the output"""
    print(f"enemies inside function: {enemies}")
    return enemy + 1


enemies = increase_enemies(enemies) # uses the global variable as parameter

print(f"enemies outside function: {enemies}")

