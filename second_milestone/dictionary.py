# my_list= [
#   {'name': 'Alice', 'age': 30, 'department': 'development'},
#   {'name': 'Bob', 'age': 25, 'department': 'testing'},
#   {'name': 'Charlie', 'age': 28, 'department': 'operation'}
# ]

# print(my_list[1]["name"])

# my_dict = {"name": "Alice", "age": 25}
# my_dict["city"] = "New York" # Adding a new key-value pair
# my_dict["age"] = 26

# print(my_dict)

dict1 = {"name": "Alice", "age": 25}
dict2 = {"city": "New York", "country": "USA"}
merged_dict = {**dict1, **dict2}

print(merged_dict)