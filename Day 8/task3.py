# Task 3 is about Functions with inputs, using positional and keyword arguments

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# using multiple inputs
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# using positional arguments as in, each argument fills the parameters in that order
greet_with("Jack Bauer", "Nowhere")

# using Keyword arguments, no matter the order they will be properly assigned to the parameters

greet_with(location="Nowhere", name="Jack Bauer")