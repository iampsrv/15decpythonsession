# String formatting
# name = "Pranjal"
# age = 25
# message = "My name is {} and I'm {} years old.".format(name, age)
# print(message)

skills=["Python","Java","C","React"]
new_skills=[]
for skill in skills:
    new_skills.append(skill.upper())
print(new_skills)


# text = "Hello, World!"
# # new_text = text.replace("World", "Python")
# # print(new_text)
# reversed_text = text[::-1]
# print(reversed_text)
name = "Alice"
age = 25
message = f"My name is {name} and I'm {age} years old."
print(message)