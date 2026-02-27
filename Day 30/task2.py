#task 2 is about the raise exception
#use raise when the code is right, but you want to limit what it does

height = float(input("enter your height: "))
weight = float(input("enter your weight: "))

if height > 3:
    raise ValueError("Your height is too high, set it bellow 3 meters")

bmi = weight / (height ** 2)
print("your bmi is ", bmi)
