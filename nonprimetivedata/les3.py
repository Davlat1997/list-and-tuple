list_tuple = [
    (1, 2, 3),
    ("Salom", "Dunyo", "Samarkand"),
    (True, False, None)
]
try:
    list_tuple[1][1] = "Tashkent"  # Tuple o'zgartirilmaydi
except TypeError:
    print("Xatolik: Tuple ichidagi qiymatni o'zgartirish mumkin emas!")