import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow
# from numpy import asarray
import time

def press(key):
    pyautogui.keyDown(key)
    return

def collision(data):
   
    for i in range(300, 415):
        for j in range(410, 563):
            if data[i, j] < 70:
                press("down")
                return

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 110:
                press("up")
                return
    return

if __name__ == "__main__":
    time.sleep(2)
    

    while True:
        image = ImageGrab.grab().convert('L')  
        data = image.load()
        collision(data)
            
