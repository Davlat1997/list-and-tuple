string = "Python programming is amazing!"
word_list = string.split()
print(word_list)
first_letters = ''.join([word[0] for word in word_list])
print(first_letters)