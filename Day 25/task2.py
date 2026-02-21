#More Pandas in depth
import pandas  # https://pandas.pydata.org/docs/

data = pandas.read_csv("weather_data.csv")

#creates a dictionary
data_dict = data.to_dict()
print(data_dict)
print("\n")

#creates a list from the dictionary
temp_list = data["temp"].tolist()
print(temp_list)
print("\n")

# getting the mean temperature

average_temp = sum(temp_list) / len(temp_list)
print(average_temp) # 17.428571428571427

#or

print(data["temp"].mean()) # 17.428571428571427

print(data["temp"].max()) # max temp
print("\n")

#getting data in columns
print("---Getting Data from Columns---\n")
print(data["condition"])
#or
print(data.condition)
print("\n")

# getting data from rows
print("---Getting Data from Rows---\n")
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

monday = data[data.day == "Monday"]
print(monday.condition)
print("\n")

# Converting temperatures from Celsius to Fahrenheit

monday = data[data.day == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9 / 5 + 32
print(monday_temp_F)
print("\n")

# Creating a dataframe from scratch

new_data_dict = {
    "students": [ "Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}
creating_data = pandas.DataFrame(new_data_dict)
print(creating_data)
creating_data.to_csv("new_data.csv") # it will generate the file new_data.csv