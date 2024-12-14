import random
c = []
i = 0
while i < 10:
    c.append(random.randint(0,100))
    i += 1
print(c)
for a in c:
    if c[0] < a <c[-1]:
        break
print(a)