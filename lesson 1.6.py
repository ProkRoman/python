day1 = int(input("сколько км в первый день: "))
max = int(input("лучший результат в км: "))
days = 1
while day1 < max:
    day1 = day1 * 1.1
    days = days + 1
    print(days)


