# Составить программу, в которой функция генерирует четырёхзначное число
# и определяет, есть ли в числе одинаковые цифры.

import random
num = 0

def generate(a):
    a = random.randint(1000, 9999)
    return a
b = (generate(num))
print (f"Число: {b}")

def number_povtor(c):
    if 1000 <= b <= 9999:  # Проверка числа
        f = b // 1000
        g = (b // 10) % 10
        d = (b // 100) % 10
        r = b % 10
        c = f == g or f == d or f == r or g == d or g == r or d == r
        return c
p = (number_povtor(b))
print (f"Число имеет одинаковые цифры? {p}")



