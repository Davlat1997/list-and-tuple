my_tuple = (10, 20, 30, 20, 40)

count = 0
for element in set(my_tuple):  
    count = my_tuple.count(element)
    if count > 1:
        print(f"Element {element} tuple ichida {count} marta takrorlangan.")