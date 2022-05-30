import mss
import mss.tools
import cv2
import time
from PIL import Image
import pyautogui
import keyboard
from pynput.keyboard import Key, Controller
import pytesseract
from pytesseract import image_to_string
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

inputkeyboard = Controller()

def calcBox(arr):
    a,b = arr[0]
    c,d = arr[1]
    return b, a, c-a, d-b

def grabImage(a,b,c,d):
    with mss.mss() as sct:
            # The screen part to capture
            moniter_number = 1
            mon = sct.monitors[moniter_number]
            monitor = {"top": a, "left": b, "width": c, "height": d, "mon": moniter_number} #Browser zoom at 100% for full 4 lines
            output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            return output

def ocr(dir):
    image = cv2.imread(dir, 0) #0 converts image to grayscale
    cv2.imshow('image', image)
    #char = pytesseract.image_to_string(image, config='--psm 8') #image_to_string(image, config='--psm 8') # To read single characters
    line = pytesseract.image_to_string(image)
    return line

def typer(char, timestep = 0.025, press_speed = 0.0005):
    inputkeyboard.press(char)
    time.sleep(press_speed)
    inputkeyboard.release(char)
    time.sleep(timestep)


def main(top, left, width, height):
    output = grabImage(top, left, width, height)
    line = ocr(output)
    x = 0
    for char in line:
        typer(char)
        print(char)
        if char == ' ':
            x += 1
        if x == 6:
            main(top, left, width, height)

#pos = pyautogui.position()
#print(pos)
pp = []
while len(pp) < 3:  # making a loop
    keyboard.wait('q')
    pos = pyautogui.position()
    print('Mouse position:', pos)
    pp.append(pos)
    if len(pp) == 2:
        top, left, width, height = calcBox(pp)
        time.sleep(1)
        while True:
            main(top, left, width, height)
            
                