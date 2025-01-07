
tuple_list = [
    (1, 2, 3),
    (4, 2, 6),
    (7, 2, 9),
    (10, 2, 12),
    (13, 2, 15)
]

c_values = set(tuple_list[0])
for tpl in tuple_list[1:]:
    c_values.intersection_update(tpl) 

print("Umumiy qiymatlar:", c_values)