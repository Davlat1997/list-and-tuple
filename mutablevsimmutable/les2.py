my_tuple = (34, 27, 97)
print("Oldingi tuple:", my_tuple)


try:
    my_tuple[1] = 99
except TypeError as a:
    print("Xatolik:", a)