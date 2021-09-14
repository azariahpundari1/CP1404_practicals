words = {}
text = input("Text: ")
number_of_words = text.split()
for word in number_of_words:
    count = words.get(word, 0)
    words[word] = count + 1
words_to_count = list(words.keys())
# words_to_count.sort()

for word in words:
    print(f'{word}: {words[word]}')


