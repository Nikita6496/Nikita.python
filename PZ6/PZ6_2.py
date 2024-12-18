
import random
a = []
R = input("Введите ваше целое число: ")
N = input("Введите размер списка (N > 1): ")

while type(R) != int: # Обработка исключений
    try:
        R = int(R)
    except ValueError:
        print("Ошибка!")
        R = input("Введите ваше число R: ")


while type(N) != int: # Обработка исключений
    try:
        N = int(N)
        if N < 2:
            print("Ошибка!")
            N = input("Введите размер списка N: ")
    except ValueError:
        print("Ошибка!")
        N = input("Введите размер списка N: ")

def proverka1(m):
    for i in range(m):
        a.append(random.randint(-100,100))
        # c = len(a)
        # print(c)

proverka1(N)
print(f"Список сгенерирован = {a}")

def ggg(a, R):
    h = 0
    pair = 0
    for i in range(N):
        for j in range(i + 1, N):
            sum = a[i] + a[j]
            k = sum - R
            if k < h:
                h = k
                pair = [i, j]
    if pair != 0:
        i, j = pair
        if i < j:
            return a[i], a[j]
    #else:
        #return 0

result = ggg(a, R)
print(result)
