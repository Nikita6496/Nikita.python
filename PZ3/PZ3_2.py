#Даны три числа. Найти среднее из них

a = input("Первое число:")
b = input("Второе число:")
c = input("Третье число:")

#Обработка ислючений
while type(a) != int:
    try:
        a = int(a)
    except ValueError:
        print("Ошибка")
        а = input("Введите целое число:")
while type(b) != int:
    try:
        b = int(b)
    except ValueError:
        print("Ошибка")
        b = input("Введите целое число:")
while type(c) != int:
    try:
        c = int(c)
    except ValueError:
        print("Ошибка")
        c = input("Введите целое число:")

if a>b>c or c>b>a:
    print(b)
elif b>a>c or c>a>b:
    print(a)
elif b>c>a or a>c>b:
    print(c)