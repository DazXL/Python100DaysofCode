# Task 1 is about Function with Outputs

def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}" # The return is a sort of stored output of the function

output = format_name("over", "lord") # As you call the function you get the return
print(output) # Printing the output you get the output
print(format_name("tAN", "gANDER")) #Can also be used

# You can also use the output of a function as an input to another function

def function_1(text):
    return text+text

def function_2(text):
    return text.title()

output = function_2(function_1("henlo"))
print(output)