import random
from functools import reduce
n = int(input("Введите количество элементов: "))
a = [random.randint(1, 100) for i in range(n)]
print(a)
nikita = [a[b] * (a[b + 1]) for b in range (int(len(a) / 3), int(len(a) - len(a) / 3) - 1)]
print(reduce(lambda x,y: x * y, nikita))
