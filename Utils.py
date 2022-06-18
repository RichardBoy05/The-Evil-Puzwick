from random import randint


def randomize_position(win, width, height):
    x = randint(0, win.winfo_screenwidth() - width)
    y = randint(0, win.winfo_screenheight() - height)

    return str(x), str(y)
