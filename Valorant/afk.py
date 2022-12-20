#import mouse and keyboard
from pynput.mouse import Button as MouseButton, Controller
mouse = Controller()

from pynput.keyboard import Key, Controller as KeyboardController
keyboard = KeyboardController()

from time import sleep

print("After the code starts, any movement of you mouse will stop the code as this is an infinite loop.")

sleep(5)



keyboard.press(Key.enter)
keyboard.release(Key.enter)

for character in ' I am sorry, I will be afk for a unknown amout of time':
    keyboard.press(character)
    keyboard.release(character)
    sleep(0.01)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

keyboard.press(Key.enter)
keyboard.press(Key.shift)
keyboard.release(Key.enter)
keyboard.release(Key.shift)

for character in ' I am afk in my spawn':
    keyboard.press(character)
    keyboard.release(character)
    sleep(0.05)

keyboard.press(Key.enter)
keyboard.release(Key.enter)

setmousepos = mouse.position

while True:
    keyboard.press('w')
    sleep(0.5)
    keyboard.release('w')
    sleep(0.5)
    if(mouse.position != setmousepos):
        break
    keyboard.press('a')
    sleep(0.5)
    keyboard.release('a')
    sleep(0.5)
    if(mouse.position != setmousepos):
        break
    keyboard.press('s')
    sleep(0.5)
    keyboard.release('s')
    sleep(0.5)
    if(mouse.position != setmousepos):
        break
    keyboard.press('d')
    sleep(0.5)
    keyboard.release('d')
    sleep(0.5)
    if(mouse.position != setmousepos):
        break