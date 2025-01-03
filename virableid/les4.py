name = "Davlatshokh"
age = 27
city = "Samarkand"

if age == 28:
    temp = name
    name = city
    city = age
    age = temp

print("name:", name)
print("age:", age)
print("city:", city)