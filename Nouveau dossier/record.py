import pyautogui
import keyboard
import time
import sys


time.sleep(2)
print("go")
keyboard.start_recording()
time.sleep(10)
events = keyboard.stop_recording()
keyboard.replay(events)
print("fin")
