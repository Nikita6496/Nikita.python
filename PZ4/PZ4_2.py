A = input("Введите целое число A: ")

while type(A) != int:
    try:
        A = int(A)
    except ValueError:
        print("Ошибка!")
        A = input("Введите целое число A: ")

B = input("Введите целое число B (B > A): ")

while type(B) != int:
    try:
        B = int(B)
    except ValueError:
        print("Ошибка!")
        B = input("Введите целое число B: ")

a = A
b = B
if A < B:
    while a <= b:
        result = a * a
        a += 1
        print(f"Одно из чисел между {A} и {B}, умноженное на само себя: {result} ")
else:
    print(f"Ошибка, {A} должно быть меньше {B}, перезапустите программу")