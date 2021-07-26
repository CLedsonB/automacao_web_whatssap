import pyautogui as pya
import time

#pya.PAUSE = 1

pya.click(1075,65)

for i in range(190):
    pya.press(["'",",","'","right", "down", "left"])