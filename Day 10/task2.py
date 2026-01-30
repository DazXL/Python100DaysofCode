# Task 2 is about Multiple return values
def format_name(f_name, l_name):
    #if inputs are empty return the message
    if f_name == "" or l_name == "":
        return "You did not provided valid inputs"

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Result: {formated_f_name} {formated_l_name}"

# try typing empty inputs
print(format_name(input("What is your name?"),input("What is your Last Name?")))