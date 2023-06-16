# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. 
# Последняя строка содержит число X

import random


N = int(input(':'))
List = [random.randint(1, 20) for i in range(N)]
Arr = list(map(int, List))
X = int (input('Введите х:'))
count = 0

min_el = abs(X - list[0])
for i in range(1, N):
    buf_el = abs(X -list[i])
    if buf_el < min_el:
        min_el = buf_el
        index_el = i

print(f'Самый близкий элемент к {X} это {count} ')