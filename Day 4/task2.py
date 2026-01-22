# Task 2 is about Lists

# this is a List, a series of strings separated by coma inside of square brackets
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[1]) # prints the item of the list at index 1, index starts at 0.

# when using negative index numbers the lists prints the last for -1, then second last for -2 and so on
print(states_of_america[-1])

# you can edit a list using several ways

states_of_america[1] = "Castlevania" # changes the index 1 to Castlevania
print(states_of_america[1])

#adding itens to the list
states_of_america.append("Neverland") #adds Neverland to the end of the list
states_of_america.extend(["Nilfgard, Vallhala"]) #adds more than one item to the end of the list

print(states_of_america)

