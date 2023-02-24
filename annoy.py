import random

import pyautogui as pg

import time
animal={'donkey','dog','monkey'}
time.sleep(8)
for i in range(500):
    a=random.choice(animal)
    pg.write("you are a "+a)
    pg.press('enter')
