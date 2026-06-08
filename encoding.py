import random
import string

# encoding the sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
encoded_words = []

for word in words:
    original_len = len(word)
    if original_len > 3:
        word += word[0]
        word = word[1:]
        start = ''.join(random.choices(string.ascii_letters, k=3))
        end = ''.join(random.choices(string.ascii_letters, k=3))
        encoded_words.append(start + word + end)
    else:
        encoded_words.append(word[::-1])

encoded_sentence = ' '.join(encoded_words)
print("Encoded:", encoded_sentence)
