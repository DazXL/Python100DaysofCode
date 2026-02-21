# Task 1 is about different files manipulation
#You can open a csv file just like that
with open("weather_data.csv") as data_file:
    data = data_file.readlines()
    print(data)

# You can also import the csv module and open the file as an object
import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file) #opens as an object
    print(data)
    temperatures = []
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

    print(temperatures)

# Pandas is a very powerful library used to process huge amounts of data with ease

import pandas # https://pandas.pydata.org/docs/

data = pandas.read_csv("weather_data.csv")
print(data["temp"])

#with Pandas, we can do the same as above with very few lines of code.