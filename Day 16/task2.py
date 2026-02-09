"""
    Python Package Index, importing python packages and prettytable
        - https://pypi.org/ is the Python Package Index
        - Search for prettytable
        - Install the package following the instructions
"""
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
print(table) #prints a table created using prettytable with left alignment to the text