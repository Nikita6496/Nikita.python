# Дан целочисленный список A размером 10. Вывести порядковый номер последнего из тех его элементов Ak,
# которые удовлетворяют двойному неравенству A1 < Ak < A10.
# Если таких элементов нет, то вывести 0.

import random
list = []
i_1 = 0
while i_1 < 10:
    list.append(random.randint(0,100))
    i_1 += 1

print(list)
h = 1
proverka = 0
index = 0
while h < 10:
    for i_2 in list:
        if h == 10 and proverka > 0:
            number = index + 1
            print(number)
        if list[0] < i_2 < list[-1]:
            index = list.index(i_2)
            proverka += 1
        h += 1
    if proverka < 1:
        print(0)
