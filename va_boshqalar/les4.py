my_tuple = (1, "salom", 3.14, "world", True, 42)

selected_elements = my_tuple[1], my_tuple[4]

result_string = " ".join(map(str, selected_elements))

print("Birlashtirilgan string:", result_string)