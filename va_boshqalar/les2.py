string = "Learning Python is fun!"

words_list = string.split()

words_tuple = tuple(words_list)

last_word_index = words_tuple.index("fun!")

print("Oxirgi so'zning indeksi:", last_word_index)