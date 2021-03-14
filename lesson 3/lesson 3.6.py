def int_func(word):
    return word[0].upper() + word[1:].lower()


s = input().split()
for i, word in enumerate(s):
    if not word.isascii() or not word.isalpha() or not word.islower():
        print('error!')
    else:
        s[i] = int_func(word)
print(' '.join(s))