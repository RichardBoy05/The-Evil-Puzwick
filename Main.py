# The Evil Puzwick virus

from tkinter import *
from Utils import randomize_position
import sys
import os

WIDTH = 350
HEIGHT = 148
BG_COLOR = "#8a8281"
UNLOCK_CODE = "yX4eaY@v"
ABSOLUTE_PATH = os.getenv('APPDATA')


def init():

    win = Tk()
    win.resizable(0, 0)
    win.protocol("WM_DELETE_WINDOW", init)  # opens a new window when the user tries to close it
    win.attributes('-topmost', True)  # setting the window to be always displayed on top

    coordinates = randomize_position(win, WIDTH, HEIGHT)
    win.geometry(str(WIDTH) + 'x' + str(HEIGHT) + '+' + coordinates[0] + '+' + coordinates[1])

    win.title("The Evil Puzwick")
    icon = PhotoImage(file=ABSOLUTE_PATH + '\TheEvilPuzwick\puzwick_ico.png', master=win)
    win.iconphoto(True, icon)
    win.config(bg=BG_COLOR)

    # Widgets

    def submit():
        text = entry.get()
        if text == UNLOCK_CODE:
            sys.exit()
        else:
            entry.delete(0, END)
            init()

    def binded_submit(self):
        text = entry.get()
        if text == UNLOCK_CODE:
            sys.exit()
        else:
            entry.delete(0, END)
            init()

    image = PhotoImage(file=ABSOLUTE_PATH + '\TheEvilPuzwick\puzwick.png', master=win)
    image_label = Label(win, image=image)
    text_label = Label(win, text="Heilà!!! Carino questo computer, penso\n"
                                 "che mi stabilirò qui! Ti consiglio di non\n"
                                 "provare a sbarazzarti di me, heheh!\n"
                                 "L'unica via di fuga è inserire il codice\n"
                                 "corretto nella casella, buona sfortuna!", font=('Arial', 8), bg=BG_COLOR)
    entry = Entry(win, relief='groove')
    button = Button(win, text="Prova!", command=submit)

    image_label.place(x=0, y=-2)
    text_label.place(x=148, y=5)
    entry.place(x=182, y=85)
    button.place(x=222, y=115)

    win.bind('<Return>', binded_submit)  # Binding the "Enter" key to the button

    win.mainloop()


init()