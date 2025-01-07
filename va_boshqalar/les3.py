my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

new_list = my_list[2::3][::-1]

new_tuple = tuple(new_list)

index = new_tuple.index(9)

print("Yangi tuple:", new_tuple)
print("Elementning indeksi:", index)