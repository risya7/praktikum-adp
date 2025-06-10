import os
import time
from termcolor import cprint

def clear_screen():
    os.system('cls')

def animasi_lilin():
    frame1 = "       i i i i i       "
    frame2 = "       * * * * *       "
    for i in range(5):
        clear_screen()
        cprint(frame1, 'yellow')
        time.sleep(0.3)
        clear_screen()
        cprint(frame2, 'red')
        time.sleep(0.3)

def tampilkan_kue():
    kue = [
        "       i i i i i       ",
        "     |:H:A:P:P:Y:|     ",
        "   __|___________|__   ",
        "  |^^^^^^^^^^^^^^^^^|  ",
        "  |:B:I:R:T:H:D:A:Y:|  ",
        "  |                 |  ",
        "  __________________  ",
    ]
    warna = ['red', 'yellow', 'green', 'cyan', 'magenta', 'blue']
    for i in range(len(kue)):
        cprint(kue[i],warna[i%len(warna)])

def ucapan():
    pesan = ['S','E','L','A','M','A','T',' ',
             'U','L','A','N','G',' ',
             'T','A','H','U','N','!']
    warna = ['red', 'yellow', 'green', 'cyan', 'magenta', 'blue']
    j=0

    for i in range(len(pesan)):
        huruf = pesan[i]
        if huruf == ' ':
            print(' ', end='', flush=True)
        else:
            cprint(huruf, warna[j], end='', flush=True)
            j+=1
            if j >= len(warna):
                j=0
        time.sleep(0.1)
    print("\n")


clear_screen()
animasi_lilin()
tampilkan_kue()
print()
ucapan()