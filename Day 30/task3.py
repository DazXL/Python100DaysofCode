#Task 3 IndexError Handling
fruits = ["Apple", "Pear", "Orange"]

# Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit pie")


for x in range (0,4):
    make_pie(x) #as 4 is out of range it should print Fruit Pie
