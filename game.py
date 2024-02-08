from tkinter import *

window =Tk()
window.title('Кто хочет стать миллионером?')
window.geometry("1235x650+0+0")
window.resizable(width=False, height = False) # запрещает изменять размер окна

window.image = PhotoImage(file = 'fon.png')
bg_fon = Label(window,image=window.image) # делаем фон к игре
bg_fon.grid(row=0, column=0)

window.config(bg='yellow')

label1 = Label(window,text='Привет это текст')
label1.grid(row=15,column=15)

but1 = Button(window,text='Это кнопка',command= lambda: print('Привет'))
but1.grid(row = 2, column= 0)

window.mainloop()