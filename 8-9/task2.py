sentence = input("Введите предложение: ")
words = sentence.split()
if len(words) < 2:
    print(sentence)
else:
    first_word = words[0]
    last_word = words[-1]
    new_sentence = [last_word.lower()] + words[1:-1] + [first_word.capitalize()]
    print(new_sentence, sep=' ')