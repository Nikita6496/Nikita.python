def PowerA234(A, B = 2, C = 3, D = 4):
    B = A ** B
    C = A ** C
    D = A ** D
    return A, B, C, D
def foonk(o = 5):
    i = 1
    while i <= o:
        num = input("Введите ваше число: ")
        while type(num) != float:
            try:
                num = float(num)
            except ValueError:
                print("Ошибка ввода")
                num = input("Введите ваше число")
            print(PowerA234(num))
            i += 1
foonk()