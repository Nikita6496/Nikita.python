# Данно число R и список размера N. Найти два различных элемента списка, сумма которых наиболее близка к числу R.

import random

def proverka1(m):
    a = []
    for _ in range(m):
        a.append(random.randint(-100, 100))
    return a


R = input("Введите ваше целое число: ")
while type(R) != int: # Обработка исключений
    try:
        R = int(R)
    except ValueError:
        print("Ошибка!")
        R = input("Введите ваше число R: ")


N = input("Введите размер списка (N > 1): ")
while type(N) != int: # Обработка исключений
    try:
        N = int(N)
        if N < 2:
            print("Ошибка!")
            N = input("Введите размер списка N: ")
    except ValueError:
        print("Ошибка!")
        N = input("Введите размер списка N: ")


a = proverka1(N)
print(f"Список сгенерирован: {a}")

def ggg(a, R):
    c_i = -1
    c_j = -1
    c_diff = 10000

    for i in range(len(a)):
        for j in range(i + 1, len(a)):
            c_sum = a[i] + a[j]
            diff = c_sum - R
            if diff < 0:
                diff = diff * (-1)
            if diff < c_diff:
                c_diff = diff
                c_i, c_j = i, j
    if c_i != -1 and c_j != -1:
        return a[c_i], a[c_j]
    return None

result = ggg(a, R)
print(f"Найденные элементы: {result}")

