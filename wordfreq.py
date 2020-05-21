file = open('textfile.txt', 'r')
text = file.read()


word_list = text.split()


word_dictionary = {
}

for word in word_list:
    word = word.lower()
    word = word.replace(".", "")
    word = word.replace(",", "")

    if word in word_dictionary:
        word_dictionary[word] = word_dictionary[word] + 1
    else:
        word_dictionary[word] = 1

# sorted_dictionary = sorted(word_dictionary.values())
sorted_x = sorted(word_dictionary.items(), key=lambda kv: kv[1])
print(sorted_x)





