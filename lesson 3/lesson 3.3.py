def my_func(a, b, c):
    try:
        return sum((a, b, c)) - min(a, b, c)
    except TypeError:
        return

print(my_func(5, 25, 6))