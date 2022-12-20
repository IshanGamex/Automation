#import mouse and keyboard
from pynput.mouse import Button as MouseButton, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller as KeyboardController
keyboard = KeyboardController()

from time import sleep

sleep(5)

setmousepos = mouse.position

while True:
    keyboard.press('w')
    sleep(0.0001)
    keyboard.release('w')
    mouse.press(MouseButton.left)
    sleep(2)
    mouse.release(MouseButton.left)
    if(mouse.position != setmousepos):
        break