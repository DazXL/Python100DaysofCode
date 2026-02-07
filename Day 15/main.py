#This is the coffee machine project
#will be using some packages to make the UI better
import inquirer

logo = r"""
  _____       _   _                  _____       __  __          __  __            _     _            
 |  __ \     | | | |                / ____|     / _|/ _|        |  \/  |          | |   (_)           
 | |__) |   _| |_| |__   ___  _ __ | |     ___ | |_| |_ ___  ___| \  / | __ _  ___| |__  _ _ __   ___ 
 |  ___/ | | | __| '_ \ / _ \| '_ \| |    / _ \|  _|  _/ _ \/ _ \ |\/| |/ _` |/ __| '_ \| | '_ \ / _ \
 | |   | |_| | |_| | | | (_) | | | | |___| (_) | | | ||  __/  __/ |  | | (_| | (__| | | | | | | |  __/
 |_|    \__, |\__|_| |_|\___/|_| |_|\_____\___/|_| |_| \___|\___|_|  |_|\__,_|\___|_| |_|_|_| |_|\___|
         __/ |                                                                                        
        |___/                                                                                         

"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "coffee": 24,
            "milk": 150,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "coffee": 24,
            "milk": 100,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 1000,
    "coffee": 1000,
    "milk": 2000,
    "money": 150,
}

"""Lets make some functions!!!"""
def machine_report(cu_res):
    print("This is the machine report:")
    print(f"Water remaining: {cu_res["water"]}")
    print(f"Coffee remaining: {cu_res["coffee"]}")
    print(f"Milk remaining: {cu_res["milk"]}")
    input("Press enter key to continue...")
    coffee_machine()

def coffee_select(coffee):
    for flavor in MENU:
        if coffee == flavor:
            make_coffee = MENU[flavor]['ingredients']
            coffee_price = MENU[flavor]['cost']
            return make_coffee, coffee_price

def compare_resources(selection, c_resources):
    for x in selection:
        if selection[x] > c_resources[x]:
            print(f"\n[[[[not enough {x}]]]]\n")
            return False
    print("All good!!!")
    return True

def coins_counter():
    print("Time to insert coins!")
    while True:
        try:
            quarters = int(input("How many quarters?"))
            dimes = int(input("How many dimes?"))
            nickles = int(input("How many nickles?"))
            pennies = int(input("How many pennies?"))
            break
        except ValueError:
            print("Please enter a number")
    total_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    print(f"You inserted a total of ${total_money:.2f}")
    return total_money

def something_else():
    answer = True
    while answer:
        x = input("What else do you want? ")
        if x != "Off":
            print("Wrong answer")
        else:
            print("Shutting down...")
            answer = False

"""==========================="""
# Main function
def coffee_machine():
    print(logo)
    current_resources = resources

    boot_pop = [inquirer.List('boot',
                             message="What you going to do?",
                             choices=['Ask for a Coffee', 'Machine Report', 'Something Else...'])]

    boot_choice = inquirer.prompt(boot_pop)
    print(f"You selected: {boot_choice['boot']}")
    if boot_choice['boot'] == 'Machine Report':
        machine_report(current_resources)
    elif boot_choice['boot'] == 'Ask for a Coffee':
        print("Let's make you a coffee!☕")
        coffee_selection = [inquirer.List('coffee',
                                          message="What type of coffee do you want?",
                                          choices=['espresso', 'latte', 'cappuccino'])]

        coffee_choice = inquirer.prompt(coffee_selection)
        choice_flavor = coffee_choice['coffee']
        print(f"You selected {choice_flavor}")

        lets_make_the_coffee = coffee_select(choice_flavor)
        coffee_ingredients = lets_make_the_coffee[0]
        price_coffee = lets_make_the_coffee[1]

        compare = compare_resources(coffee_ingredients, current_resources)

        if compare:
            payment = coins_counter()
            if payment >= price_coffee:
                print("there is your coffee!!!")
                change = payment - price_coffee

                for x in coffee_ingredients:
                    current_resources[x] -= coffee_ingredients[x]

                current_resources["money"] += payment

                if change > 0:
                    current_resources["money"] -= change
                    print(f"Here is your change!: {change:.2f}")

                input("Press enter key to continue...")
                coffee_machine()
            else:
                print("Sorry, you don't have enough money!")
                input("Press enter key to continue...")
                coffee_machine()
        else:
            print("Sorry, we cannot make a coffee! Not enough resources.")
            print(f"Water: {current_resources['water']}")
            print(f"Coffee: {current_resources['coffee']}")
            print(f"Milk: {current_resources['milk']}")
            input("Press enter key to continue...")
            coffee_machine()
    else:
        something_else()


coffee_machine()