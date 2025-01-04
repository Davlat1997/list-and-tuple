my_list = [5, 10, 15, 20]
print("Boshlang'ich ro'yxat:", my_list)

my_tuple = tuple(my_list)
print("Tuple:", my_tuple)

new_list = list(my_tuple)

new_list[3] = 99
print("O'zgartirilgan ro'yxat:", new_list)