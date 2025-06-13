#Дано целое положительное число.
#Проверить истинность высказывания: «Данное число является нечетным трехзначным».
from tkinter import *

def find_count(x):
    try:
        n = int(num.get())
    except ValueError:
        result['text'] = ('Ошибка!')
        return
    check_num = (100 <= n <= 999 and n % 2 != 0)
    result['text'] = f"Данное число является\nнечётным трехзначным?\n{check_num}"

root = Tk()
root.title('Поиск взаимно противоположных чисел')
root.geometry('250x125')

Label(text="Ваше число").grid(row=1, column=0)
num = Entry()
num.grid(row=1, column=1)

button = Button(text="Обработать")
button.grid(row=2, column=1)

result = Label()
result.grid(row=3, column=1)

button.bind('<Button-1>',find_count)

root.mainloop()