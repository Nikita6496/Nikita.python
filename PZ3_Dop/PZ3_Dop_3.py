a = float(input("Введите двухзначное число:"))
b, c = divmod(a, 10)
if 9 < a < 100 and (b + c) % 2 == 0:
    print(a + 2)
else:
    print(a - 2)
