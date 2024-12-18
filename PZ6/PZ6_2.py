
import random
a = []
R = input("Введите ваше целое число: ")
N = input("Введите размер списка: ")
i = 1

#if R < 0:
    #print("Ошибка! Число R должно быть больше 0")
    #R = input("Введите ваше целое положительное число: ")

while type(R) != int: # Обработка исключений
    try:
        R = int(R)
    except ValueError:
        print("Ошибка!")
        R = input("Введите ваше число R: ")

while type(N) != int: # Обработка исключений
    try:
        N = int(N)
    except ValueError:
        print("Ошибка!")
        N = input("Введите размер списка N: ")

while i <= N:
    b = random.randint(-100,100)
    a.append(b)
    i += 1
    
print(f'Список сгенерирован = {a}')