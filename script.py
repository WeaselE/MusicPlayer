# imports
from pywinauto.application import Application
import pywinauto.keyboard as keyboard
from time import sleep
from tkinter import *
import random

# Variable setup
root = Tk()
sleep(5)
app = Application().start(
    r"C:\Users\Wesley\Desktop\freepiano\freepiano.exe")
app = Application().connect(
    path=r"C:\Users\Wesley\Desktop\freepiano\freepiano.exe")
dlg = app['Wispow Freepiano 2']

keys = {0: 'z',
        1: 'x',
        2: 'c',
        3: 'v',
        4: 'b',
        5: 'n',
        6: 'm',
        7: 'a',
        8: 'd',
        9: 'f',
        10: 'g',
        11: 'h',
        12: 'j',
        13: 'k',
        14: 'w',
        15: 'e',
        16: 'r',
        17: 't'}


def focus():
    dlg.set_focus()


def play_a():
    focus()
    sleep(1)
    keyboard.send_keys('a', vk_packet=False)


def play_arpegio():
    focus()
    keyboard.send_keys('adgjl', vk_packet=False)


def play_chord():
    focus()
    sleep(1)
    keyboard.send_keys('adg', vk_packet=False)


def play_random():
    focus()
    while True:
        sleep(.5)
        n = ''
        k = random.randint(0, 13)
        n = keys[k] + keys[k+2] + keys[k+4]
        keyboard.send_keys(n, vk_packet=False)


Button_1 = Button(root, text='a', command=play_a)
Button_1.pack()
Button_2 = Button(root, text='arpegio', command=play_arpegio)
Button_2.pack()
Button_3 = Button(root, text='chord', command=play_chord)
Button_3.pack()
Button_4 = Button(root, text='close program',
                  command=lambda: dlg.close())
Button_5 = Button(root, text='Play random keys', command=play_random)
Button_5.pack()
Button_4.pack()
root.mainloop()
