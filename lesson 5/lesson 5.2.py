with open('text_2.txt', 'r', encoding='utf-8') as f:
    lines = 0
    words = 0
    for line in f:
        lines += 1
        words += len(line.split())
print(lines)
print(words)