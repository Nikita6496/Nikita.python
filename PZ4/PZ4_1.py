# Дано вещественное число Х и целое число N (>0).
# Найти значение выражения 1 + X + (X ^ 2) / (2!) +...+X^ N /(N!)(N!=12...N)

X = input("Введите вещественное число X: ")
N = input("Введите целое число N (N > 0): ")

# Обработка исключений
while type(X) != float:
    try:
        X = float(X)
    except ValueError:
        print("Ошибка!")
        X = input("Введите вещественное число X: ")
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Ошибка!")
        N = input("Введите целое число N (N > 0): ")

h = 1
s = 1
result = 0
if N > 0:
    while s <= N:
        h *= s
        g = (X ** s) / h
        s += 1
        result += g

    print(1 + result)
else:
    print("Ошибка ввода, перезапустите программу и введите N > 0")