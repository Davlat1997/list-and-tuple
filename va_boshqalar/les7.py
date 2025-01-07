text = "Python and data structures are interesting!"

letters_list = [char for char in text if char.isalpha()]

lowercase_letters = [char for char in letters_list if char.islower()]

print("Kichik harflar:", lowercase_letters)