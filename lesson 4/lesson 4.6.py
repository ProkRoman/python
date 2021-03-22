from itertools import count, cycle

print('Программа генерирует целые числа‚ начиная с указанного. Нажмите Enter,',
      'для выхода  - "q"')
for i in count(int(input('Введите первое число: '))):
    print(i, end='')
    quit = input()
    if quit == 'q':
        break

print('Повторение элементов списка. Нажмите Enter,',
      'для выхода  - "q"')
u_list = input('Введите список, разделяя пробелом: ').split()
iter = cycle(u_list)
quit = None

while quit != 'q':
    print(next(iter), end='')
    quit = input()
