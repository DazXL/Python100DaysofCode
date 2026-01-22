#Task 4 is about IndexError and Nested Lists

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(len(states_of_america)) # 50 states
# print(states_of_america[50]) # will give an IndexError because index from the variable goes from 0 to 49

# Nested Lists
#the dirty dozen are 12 fruits and vegetables that have high pesticide
dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears",
                "Tomatoes", "Celery", "Potatoes"]
#separating the fruits and vegetables
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

#nesting them to the dirty_dozen
dirtyDozenNest = [fruits, vegetables]
print(dirtyDozenNest)
# the first bracket selects the nested list, the second bracket select the item in that list.
print(dirtyDozenNest[1][2])