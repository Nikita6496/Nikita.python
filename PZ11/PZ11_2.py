#Из предложенного текстового файла (text18-18.txt) вывести на экран его содержимое,
#количество знаков пунктуации в первых четырёх строках. Сформировать новый файл, в
#который поместить текст в стихотворной форме выведя строки в обратном порядке.
t = 0
d = 0
m = 0
for i in open('text18-18.txt', encoding='UTF-16'):
 print(i, end='')
 #while t != 4:
  #for h in i:
   #if h == "." or h == "—" or h == "..." or h == ",":
    #m += 1
 t += 1
 for j in i:
  if j == 'ж':
   d += 1
print(end='\n')
print('Количество строк: ', t, end='\n')
print('Количество букв "ж" : ', d, end='\n')

f1 = open('text18-18.txt', encoding='UTF-16')
l = f1.readlines()
l[0], l[3] = l[3], l[0]
f1.close()

f2 = open('text18-18-2.txt', 'w')
f2.writelines(l)
f2.close()