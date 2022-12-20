#import mouse and keyboard
from pynput.mouse import Button as MouseButton, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller as KeyboardController
keyboard = KeyboardController()

from time import sleep

setmousepos = mouse.position

sleep(5)

print("After the code starts, any movement of you mouse will stop the code as this is an infinite loop.")

startnum = 0

while True:
    for a in str(startnum):
        keyboard.press(a)
        keyboard.release(a)
        sleep(0.05)

    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

    startnum += 2

    if(mouse.position != setmousepos):
        break

    sleep(2)