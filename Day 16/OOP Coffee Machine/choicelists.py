import inquirer
import menu

MENU = menu.Menu()
making_list = []

for item in MENU.menu:
    making_list.append(item.name)

boot_pop = [inquirer.List('boot',
                             message="What you going to do?",
                             choices=['Ask for a Coffee', 'Machine Report', 'Something Else...'])]

coffee_selection = [inquirer.List('coffee',
                                          message="What type of coffee do you want?",
                                          choices=making_list)]


