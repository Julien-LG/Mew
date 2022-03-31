import pyautogui
import time

time.sleep(3)

while True:
    if pyautogui.locateOnScreen('chroma2.png') != None:
        print("I can see it")
        time.sleep(0.5)
    else:
        print("I am unable to see it")
        time.sleep(0.5)
        
