list_of_lists = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]

new_list = [items[-1] for items in list_of_lists]

new_tuple = tuple(new_list)

print("Yangi tuple:", new_tuple)