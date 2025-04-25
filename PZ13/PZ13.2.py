# В двумерном списке найти среднее арифметическое элементов последних двух
# столбцов.
import random
spisok = [[random.randint(1, 10) for i in range(3)] for i in range(3)]
for i in spisok:
    print(i)
a = list(map(lambda x:(x[1] + x[2]) / 2, spisok))
print(a)