#В последовательности на n целых элементов найти произведение элементов
#средней трети.

import random
from functools import reduce

n = int(input("Введите количество элементов: "))
a = [random.randint(1, 5) for i in range(n)]
print(a)

nikita = [a[b] for b in range (int((len(a) // 3) ), int((len(a) - len(a) // 3)))]
print(nikita)
print(reduce(lambda x,y: x * y, nikita))
