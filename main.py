from pynput.keyboard import Key, Controller
import time


keyboard = Controller()

time.sleep(5)

while 1:
    keyboard.type('MAL :)')
    time.sleep(0.5)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter) 
