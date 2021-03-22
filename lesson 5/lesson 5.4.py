d = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
with open('../lesson 5/text_4.txt', 'r', encoding='utf-8') as f:
    with open('text_4.txt', 'w', encoding='utf-8') as f2:
        for line in f:
            en, *num = line.split()
            ru = d[en]
            f2.write(' '.join([ru] + num) + '\n')