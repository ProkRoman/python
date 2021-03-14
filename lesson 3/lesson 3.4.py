def my_func(x, y):
    try:
        x = float(x) #с плавающей запятой
        y = int(y) #целое число
    except Error:
        print('только действительное x и целое y')
        return
    if x <= 0 or y >= 0:
        print('только положительное x и отрицательный y')
        return
    return x ** y
print(round(my_func(x=input(), y=input()), 10))



