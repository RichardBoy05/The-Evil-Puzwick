# The Evil Puzwick virus

from tkinter import *
import Utils

WIDTH = 350
HEIGHT = 148
UNLOCK_CODE = "mghj58?èas-.7(/&"


def init():

    win = Tk()

    win.resizable(0, 0)

    win.protocol("WM_DELETE_WINDOW", Utils.disable_closing)
    win.protocol("WM_ICONIC_WINDOW", Utils.disable_closing)

    coordinates = Utils.randomize_position(win, WIDTH, HEIGHT)
    win.geometry(str(WIDTH) + 'x' + str(HEIGHT) + '+' + coordinates[0] + '+' + coordinates[1])

    win.title("The Evil Puzwick")

    icon = PhotoImage(file='puzwick_ico.png', master=win)
    win.iconphoto(True, icon)

    win.config(bg='#b3a2aa')

    # Widgets

    def submit():
        text = entry.get()

        if text == UNLOCK_CODE:
            quit()
        else:
            entry.delete(0, END)
            init()

    image = PhotoImage(file='puzwick.png', master=win)
    image_label = Label(win, image=image)
    text_label = Label(win, text="Heilà!!! Carino questo computer, penso\n"
                                 "che mi stabilirò qui! Ti consiglio di non\n"
                                 "provare a sbarazzarti di me, heheh!\n"
                                 "L'unica via di fuga è inserire il codice\n"
                                 "corretto nella casella, buona sfortuna!", font=('Arial', 8), bg='#b3a2aa')
    entry = Entry(win, relief='groove')
    button = Button(win, text="Prova!", command=submit)

    image_label.place(x=0, y=-2)
    text_label.place(x=148, y=5)
    entry.place(x=182, y=85)
    button.place(x=222, y=115)

    win.bind('<Return>', lambda event=None: button.invoke())

    win.mainloop()


init()
