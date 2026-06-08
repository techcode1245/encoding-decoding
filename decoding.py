# decoding the sentence
decoded_words = []

for i, word in enumerate(encoded_words):
    original_len = len(words[i])
    if original_len > 3:
        word = word[3:-3]      # remove random letters from both ends
        word = word[-1] + word # move last char to front
        word = word[:-1]       # remove last char
        decoded_words.append(word)
    else:
        decoded_words.append(word[::-1])

decoded_sentence = ' '.join(decoded_words)
print("Decoded:", decoded_sentence)
