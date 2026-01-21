# Task 2 is about Modulo

#When using the % operator it will give the rest of a division between two numbers

print(6 % 2) #will be 0
print(6 % 5) #will be 1
print(6 % 4) #will be 2

#checking for Odd or Even numbers

num1 = int(input("Enter a number: "))

if num1 % 2 == 0:
    print(str(num1) + " is an even number!")
else:
    print(str(num1) + " is not an even number!")