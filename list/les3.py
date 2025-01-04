# Asosiy ro'yxat
list_1 = [-10, 21, "Davlatshokh", "Islomiy", 43, 6, 31.7, -7, "Assalomu Aleykum", -66]

list_2 = []

for i in list_1:
    if isinstance(i, int) and i > 0:
        list_2.append(i)
    elif isinstance(i, str):
        list_2.append(i.lower())

print(list_2)