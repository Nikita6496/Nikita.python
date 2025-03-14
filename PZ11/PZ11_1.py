#1. Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:

#Исходные данные:
#Количество элементов:
#Среднее арифметическое элементов:
#Последовательность, в которой каждый последующий элемент равен квадрату суммы двух
#соседних элементов:

l = ['-99 6 12 -36 20 45 100 -15']
f1 = open('nikita_1.txt', 'w')
f1.writelines (l)
f1.close()

f2 = open('nikita_2.txt', 'w')
f2.write("Исходные данные:")
f2.write('\n')
f2.writelines (l)
f2.close()


f1 = open('nikita_1.txt')
k = f1.read()
k = k.split()
for i in range(len(k)):
    k[i] = int(k[i])
f1.close()

#f1 = open('nikita_1.txt')
#max, t = 0,0
#for i in range(len(k)):
    #max = max if max > k[i] else k[i]
    #if k[i] < 0:
        #t += 1


#f1 = open('nikita_1.txt')
#ar, t = 0,0
#for i in range(len(k)):
#    ar = i
#ari = ar / (len(k))

f1 = open('nikita_1.txt')
average = sum(k) / len(k)
f1.close()

#f1 = open('nikita_1.txt')
#t = 0
#new_s = []
#for i in range(1, (len(k) -1)):
#    new_e = (k[i - 1] + k[i + 1]) ** 2
#    new_s.append(new_e)
#f1.close()

f1 = open('nikita_1.txt')
t = 0
new_s = []
for i in range(len(k)):
    if i == k[0]:
        new.e = (k[i + 1]) ** 2
    new.e =
    new_s.append(new_e)
f1.close()

f2 = open('nikita_2.txt', 'a')
f2.write('\n')
print("Количество элементов: ", len(k), "Среднее арифметическое: ", average, "Последовательность, в которой каждый последующий элемент равен квадрату суммы двух соседних элементов: ", new_s, file=f2)
f2.close()
