from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
from choicelists import *
from art import logo

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

print(logo)
def coffee_machine():
    boot_choice = inquirer.prompt(boot_pop)
    print(f"You selected: {boot_choice['boot']}")
    if boot_choice['boot'] == 'Machine Report':
        coffee_maker.report()
        money_machine.report()
        input("Press enter key to continue...\n")
        coffee_machine()

    elif boot_choice['boot'] == 'Ask for a Coffee':
        print("Let's make you a coffee!☕")
        coffe_choice = inquirer.prompt(coffee_selection)
        selected_coffee = menu.find_drink(coffe_choice['coffee'])
        print(selected_coffee)
        print(coffee_maker.is_resource_sufficient(selected_coffee))
        if coffee_maker.is_resource_sufficient(selected_coffee):
            print("All good! time to pay!")
            print(f"Your coffee costs ${selected_coffee.cost:.2f}")
            if money_machine.make_payment(selected_coffee.cost):
                coffee_maker.make_coffee(selected_coffee)
                input("Press enter key to continue...\n")
                coffee_machine()
            else:
                input("Press enter key to continue...\n")
                coffee_machine()
        else:
            print("Maybe you should turn 'Off' the machine and refill it!")
            input("Press enter key to continue...\n")
            coffee_machine()
    else:
        answer = True
        while answer:
            x = input("What else do you want? ")
            if x != "Off":
                print("Wrong answer")
            else:
                print("Shutting down...")
                answer = False

coffee_machine()