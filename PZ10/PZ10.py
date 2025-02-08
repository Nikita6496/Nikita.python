#Имеется список студентов группы, в котором все имена различны. Определить, есть ли в
#группе студент, который побывал в гостях у всех студентов. (Для каждого студента
#составить список из множества побывавших у него в гостях друзей, причем хозяина в этот
#список не включать).

spisok = ["Ваня", "Петя", "Дима", "Игнат"]

print (spisok)
Vanya = {"Петя", "Дима", "Игнат"}
Petya = {"Ваня", "Дима", "Игнат"}
Dima = {"Игнат"}
Ignat = {"Петя"}


u_ignata = (Vanya & Petya & Dima)
u_vanya = (Ignat & Petya & Dima)
u_dima = (Vanya & Petya & Ignat)
u_petya = (Vanya & Ignat & Dima)

def funk(a):
    if a != set():
        print(a)

funk(u_ignata)
funk(u_vanya)
funk(u_dima)
funk(u_petya)