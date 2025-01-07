my_list = [42, "hello", 3.14, "world", True, "python", 7]

new_list = [elem.upper() for elem in my_list if isinstance(elem, str)]

print("Katta harfga aylangan string elementlar:", new_list)