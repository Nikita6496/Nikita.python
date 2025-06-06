# from tkinter import *
# from tkinter import ttk
# root = Tk()
# root.title("Привет Мир!")
# root.geometry("1900x680")
#
# def button_clicked():
#     print("Hello World!")
# def close():
#     root.destroy()
#     root.quit()
#
# button = ttk.Button(root, text="Press Me", command=button_clicked)
# button.pack(fill=BOTH)
# root.protocol("WM_DELETE_WINDOW", close)
# root.mainloop()



#Проверить истинность высказывания: «Среди трех данных целых чисел есть хотя бы одна пара взаимно противоположных.
# from tkinter import *
#
# def find_count(event):
#     try:
#         n1 = int(num1.get())
#         n2 = int(num2.get())
#         n3 = int(num3.get())
#     except ValueError:
#         result['text'] = ('Ошибка! Введите корректные значения')
#         return
#     check_num = (n1 == -n2) or (n1 == -n3) or (n2 == -n3)
#     result['text'] = f"Среди трех данных \nцелых чисел \nесть хотя бы \nодна пара \nвзаимно противоположных? {check_num}"
#
# root = Tk()
# root.title('Поиск взаимно противоположных чисел')
# root.geometry('500x200')
#
# Label(text="Первое число").grid(row=1, column=0)
# num1 = Entry()
# num1.grid(row=1, column=1)
#
#
# Label(text="Второе число").grid(row=2, column=0)
# num2 = Entry()
# num2.grid(row=2, column=1)
#
# Label(text="Третье число").grid(row=3, column=0)
# num3 = Entry()
# num3.grid(row=3, column=1)
#
# button1 = Button(text="Обработать")
# button1.grid(row=4, column=1)
#
# result = Label()
# result.grid(row=5, column=1)
#
# button1.bind('<Button-1>',find_count)
#
# root.mainloop()



from tkinter import *


root = Tk()
root.title('Форма регистрации')
root.geometry('700x400')

user_info = LabelFrame(root, text='Данные для входа пользователя')
user_info.pack(fill='both', padx=10, pady=10)
user_info_name = Label(user_info, text='Имя пользователя:')
user_info_name.grid(row=0, column=0, sticky='w', padx=5, pady=5)
input_name = Entry(user_info)
input_name.grid(row=0, column=1, padx=5, pady=5)
user_info_email = Label(user_info, text='Электронная почта:')
user_info_email.grid(row=1, column=0, sticky='w', padx=5, pady=5)
input_email = Entry(user_info)
input_email.grid(row=1, column=1, padx=5, pady=5)
user_info_psw = Label(user_info, text='Пароль:')
user_info_psw.grid(row=2, column=0, sticky='w', padx=5, pady=5)
input_psw = Entry(user_info)
input_psw.grid(row=2, column=1, padx=5, pady=5)

personal_data = LabelFrame(root, text='Персональные данные')
personal_data.pack(fill='both', padx=10, pady=10)
pers_data_addr = Label(personal_data, text='Домашний адрес:')
pers_data_addr.grid(row=0, column=0, sticky='w', padx=5, pady=5)
input_addr = Entry(personal_data)
input_addr.grid(row=0, column=1, padx=5, pady=5)
pers_data_addr = Label(personal_data, text='Дата рождения:')
pers_data_addr.grid(row=1, column=0, sticky='w', padx=5, pady=5)
input_addr = Entry(personal_data)
input_addr.grid(row=1, column=1, padx=5, pady=5)
pers_data_addr = Label(personal_data, text='Ваш возраст:')
pers_data_addr.grid(row=2, column=0, sticky='w', padx=5, pady=5)
input_addr = Entry(personal_data)
input_addr.grid(row=2, column=1, padx=5, pady=5)
pol = Label(personal_data,text='Выберите пол:')
pol.grid(row=3,column=0,sticky='w', padx=5,pady=5)
var1 = IntVar()
rbutton1 = Radiobutton(personal_data,text='Мужской',variable=var1,value=1)
rbutton1.grid(row=3,column=1,sticky='w', padx=5,pady=5)
rbutton2 = Radiobutton(personal_data,text='Женский',variable=var1,value=2)
rbutton2.grid(row=3,column=2,sticky='w', padx=5,pady=5)

text_check = LabelFrame(root)
var2 = IntVar()
text_check.pack(fill='both', padx=10, pady=10)
my_text = Label(text_check,text='Я готов следовать правилам формы')
my_text.grid(row=0, column=0, sticky='w', padx=5, pady=5)
check = Checkbutton(text_check, text=u'', variable=var2,onvalue=1,offvalue=0)
check.grid(row=0, column=1, sticky='w', padx=5, pady=5)
reset_btn = Button(text_check, text='Reset')
reset_btn.grid(row=1, column=0,sticky='w', padx=5, pady=5)
submit_btn = Button(text_check, text='Submit')
submit_btn.grid(row=1, column=1,sticky='w', padx=5, pady=5)

root.mainloop()