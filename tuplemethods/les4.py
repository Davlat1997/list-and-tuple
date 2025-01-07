my_tuple = (10, 20, 30, 20, 40)

count = 0
for element in set(my_tuple):  
    count = my_tuple.count(element)
    if count > 1:
        print(f"Element {element} tuple ichida {count} marta takrorlangan.")
       
max_count = 0
max_element = None

for element in set(my_tuple):
    count = my_tuple.count(element)
    if count > max_count:
        max_count = count
        max_element = element

print(f"Eng ko'p takrorlangan element: {max_element} ({max_count} marta)")