a = input("Первое число:")
b = input("Второе число:")
c = input("Третье число:")
while type(a) != int: #Обработка исключений
    try:
        a = int(a)
    except ValueError:
        print("Ошибка")
        а = input("Введите целое число:")
while type(b) != int: #Обработка исключений
    try:
        b = int(b)
    except ValueError:
        print("Ошибка")
        b = input("Введите целое число:")
while type(c) != int: #Обработка исключений
    try:
        c = int(c)
    except ValueError:
        print("Ошибка")
        c = input("Введите целое число:")
#(a>b>c or c>b>a or b>a>c or c>a>b or b>c>a or a>c>b)
if a>b>c or c>b>a:
    print(b)
elif b>a>c or c>a>b:
    print(a)
elif b>c>a or a>c>b:
    print(c)