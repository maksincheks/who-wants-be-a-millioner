from tkinter import *
from tkinter import Canvas


def select_answer(answer):
    print(f'Выбран ответ {answer}')



root = Tk()
canvas = Canvas(root, width=1235, height=650)
canvas.pack()
root.title('Кто хочет стать миллионером?')
root.resizable(width=False, height=False)
root.image = PhotoImage(file='fon.png')
canvas.create_image(0, 0, anchor=NW, image=root.image)




but_A = Button(root, bg='#223e95', fg='#243f8c', command=lambda: select_answer('A'))
but_A_window = canvas.create_window(350, 495, width=500, height=70, window=but_A)

but_B = Button(root, bg='#223e95', fg='#243f8c', command=lambda: select_answer('B'))
but_B_window = canvas.create_window(870, 495, width=500, height=70, window=but_B)

but_C = Button(root, bg='#223e95', fg='#243f8c', command=lambda: select_answer('C'))
but_C_window = canvas.create_window(350, 582, width=500, height=70, window=but_C)

but_D = Button(root, bg='#223e95', fg='#243f8c', command=lambda: select_answer('D'))
but_D_window = canvas.create_window(870, 582, width=500, height=70, window=but_D)


root.mainloop()