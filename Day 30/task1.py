#Task 1 is about error handling

#File not Found Exception and KeyError example:

try:
    file = open('passwords.txt')
    a_dictionary = {"key": "value"}
    print(a_dictionary["asdfasd"]) #KeyError exception trigger
except FileNotFoundError:
    file = open('passwords.txt', 'w')
    file.write('Something went wrong.')
except KeyError as error_message:
    print(f"The key {error_message} was not found.")

else: #will only execute if both exception do not occur
    content = file.read()
    print(content)

finally: #will execute regardless
    file.close()
    print("file closed")
