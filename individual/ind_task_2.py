# !/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import math

# 12. В списке, состоящем из вещественных элементов, вычислить:
# 1) количество элементов списка, лежащих в диапазоне от А до В;
# 2) сумму элементов списка, расположенных после максимального элемента.
# Упорядочить элементы списка по убыванию модулей элементов.


if __name__ == '__main__':

    # Инициализация списка
    Tup = tuple(map(float, input("Enter items separated by a space> ").split(" ")))
    a = int(input("Enter A of range> "))
    b = int(input("Enter B of range> "))
    if not Tup:
        print("List is empty", file=sys.stderr)
        exit(1)

    # 1 задание
    qua = 0
    for i in Tup:
        if a < i < b:
            qua += 1

    # Поиск максимального элемента и его индекса
    i_max, lis_max = 0, Tup[0]
    for i, item in enumerate(Tup):
        if item > lis_max:
            i_max = i
            lis_max = item

    # 2 задание
    sum = 0
    i_sum = i_max + 1
    while i_sum < len(Tup):
        sum += Tup[i_sum]
        i_sum += 1

    # Сортировка
    temp = 0
    Tup_1 = tuple()
    Tup_2 = tuple()
    Tup_3 = tuple()
    for i in range(len(Tup) - 1):
        for j in range(len(Tup) - i - 1):
            if math.fabs(Tup[j + 1]) < math.fabs(Tup[j]):
                temp = j
                Tup_1 = Tup[:j]
                Tup_2 = (Tup[j+1], Tup[j])
                Tup_3 = Tup[j+2:]
                Tup = tuple(Tup_1+Tup_2+Tup_3)

    print(f"Task 1: number from a to b = {qua} \nTask 2: sum of elements from max = {sum} \nSort list = {Tup}")