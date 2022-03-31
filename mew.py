import pyautogui
import keyboard
import time
import sys


time.sleep(2)
def clickA():
    keyboard.press('q')
    time.sleep(0.2)
    keyboard.release('q')
    time.sleep(0.1)
def goZ(nb):
    for i in range(nb):
        keyboard.press('w')
        time.sleep(0.2)
        keyboard.release('w')
        time.sleep(0.1)
def goS(nb):
    for i in range(nb):
        keyboard.press('s')
        time.sleep(0.2)
        keyboard.release('s')
        time.sleep(0.1)
def goQ(nb):
    for i in range(nb):
        keyboard.press('a')
        time.sleep(0.2)
        keyboard.release('a')
        time.sleep(0.1)
def goD(nb):
    for i in range(nb):
        keyboard.press('d')
        time.sleep(0.2)
        keyboard.release('d')
        time.sleep(0.1)
        
def sgo():
    keyboard.press('w')
    time.sleep(0.1)
    keyboard.release('w')
    time.sleep(0.1)
def goToForest():
    goZ(2)
    keyboard.press('space')
    time.sleep(0.2)
    keyboard.release('space')
    time.sleep(0.1)
    
def goToMew():
    goZ(5)
    goD(4)
    goZ(6)
    goD(1)
    goZ(1)
    clickA()
    
def debutCombatMew():
    keyboard.press('space')
    #time.sleep(0.5)
    time.sleep(1)
    keyboard.release('space')
    time.sleep(0.1)
    clickA()
    keyboard.press('space')
    time.sleep(0.5)
    keyboard.release('space')
    
def fuiteCombatMew():
    goD(1)
    goS(1)
    clickA()
    keyboard.press('space')
    time.sleep(0.2)
    #keyboard.release('space')
    clickA()
    #keyboard.press('space')
    time.sleep(0.2)
    keyboard.release('space')
    clickA()
def retourAuDebut():
    goQ(1)
    goS(9)
    goQ(4)
    goS(3)
    time.sleep(1)
    goS(1)
    goZ(1)

def retourAuDebut2():
    goQ(1)
    keyboard.press('space')
    goS(1)
    keyboard.release('space')
    goQ(4)
    keyboard.press('space')
    goS(1)
    keyboard.release('space')
    goZ(1)

def alerteMew():
    print("il est la")
    keyboard.press('shift+f6')
    time.sleep(0.2)
    keyboard.release('shift+f6')
    time.sleep(0.1)
    sys.exit()
    
print("go")
#keyboard.press('w')
#time.sleep(1)
#keyboard.release('w')



y = 0
t = 15
while y < t:
    goToForest()
    goToMew()
    debutCombatMew()
    if pyautogui.locateOnScreen('chromaPleinEcran.png') != None:
        alerteMew()
    else:
        fuiteCombatMew()
    retourAuDebut2()
    y = y +1

#clickA()
print("fin")







