import pyautogui
import keyboard
import time
import sys


time.sleep(2)
def goToMew():
    keyboard.press('space')
    keyboard.press('w')
    time.sleep(0.3)
    keyboard.release('w')

    keyboard.press('d')
    time.sleep(0.05)
    keyboard.release('d')

    keyboard.press('w')
    time.sleep(0.09)
    keyboard.release('w')

    keyboard.press('d')
    time.sleep(0.015)
    keyboard.release('d')

    keyboard.press('w')
    time.sleep(0.02)
    keyboard.release('w')

    keyboard.press('q')
    time.sleep(0.1)
    keyboard.release('q')

    keyboard.release('space')

def fuiteMew():
    keyboard.press('space')
    
    keyboard.press('q')
    time.sleep(0.1)
    keyboard.release('q')

    keyboard.press('d')
    time.sleep(0.1)
    keyboard.release('d')

    keyboard.press('s')
    time.sleep(0.1)
    keyboard.release('s')

    keyboard.press('q')
    time.sleep(0.2)
    keyboard.release('q')
    
    keyboard.release('space')

def retourDebut():
    keyboard.press('space')
    
    keyboard.press('q')
    time.sleep(0.1)
    keyboard.release('q')

    keyboard.press('d')
    time.sleep(0.1)
    keyboard.release('d')

    keyboard.press('s')
    time.sleep(0.1)
    keyboard.release('s')

    keyboard.press('q')
    time.sleep(0.2)
    keyboard.release('q')
    
    keyboard.release('space')

def alerteMew():
    print("il est la")
    sys.exit()


print('Go')
#keyboard.press_and_release('w')
#keyboard.press('w')

goToMew()
keyboard.press('space')
time.sleep(0.05)
keyboard.release('space')
if pyautogui.locateOnScreen('chroma2.png') != None:
    alerteMew()
else:
    fuiteMew()
    #retourDebut()
    
#time.sleep(1)
#fuiteMew()

#keyboard.write('z')
#pyautogui.press('enter')

print('Finish')


#keyboard.write("ddd")
#go()
