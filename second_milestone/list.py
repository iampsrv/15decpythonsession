# skills=["Python","Java","C","React","React"]
# my_list = list(range(1, 20, 2))

# skills[4] = "SQL"
# print(skills)
# print(skills[4])

# shopping_cart=[]
# shopping_cart = ["Apple Iphone 15", "Apple Iphone case", "Charger", "Headphones"]


# my_list = ['apple', 'banana', 'cherry']
# my_list.append('mango')
# print(my_list)

# my_list.pop()
# print(my_list)

# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# concatenated_list = list1 + list2
# print(len(concatenated_list))

# my_list = ['apple', 'banana', 'cherry']
# if 'guava' in my_list:
#     print("Found!")
# else:
#     print("Not found")

# my_list = [1, 2, 2, 3, 4, 2]
# count = my_list.count(2) # Counting occurrences of element 2
# print(count)

# my_list = [4, 2, 1, 3, 5]
# my_list.sort()
# my_list.reverse() # Reversing the order of elements
# print(my_list)

# nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(nested_list[0][1])

# my_list = [1, 2, 3]
# my_tuple = (4, 5, 6)
# c = my_list+list(my_tuple)
# print(c)

# age ="26"
# print(type(age))
# age= int(age) # Datatype conversion
# age+=20
# print(type(age))
# age= str(age)
# print(type(age))
# print(age)

marks = [90,85,97,80,75]
# average_marks = sum(marks)/len(marks)
# print(average_marks)
total=0
for mark in marks:
    total+=mark
print(total/len(marks))

# print(min(marks))
# print(max(marks))

message = "Minimun marks is {} and maximum marks is {}".format(min(marks), max(marks))
print(message)