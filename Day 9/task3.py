#Task 3 is about Nested Lists and Dictionaries

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

#Nested List in Dictionary

travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Stuttgart", "Berlin"],
}

#print Lille
print(travel_log["France"][1])

# little challenge, accessing the list and printing "D"
nested_list = ["A", "B",["C", "D"]]
print(nested_list[2][1]) # 2 is the index of the nested list, 1 is the index of "D"

# Nesting dictionaries with lists

travel_log = {
    "France" : {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany" : {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"]
    },
}
#printing "Stuttgart"
print(travel_log["Germany"]["cities_visited"][2])
