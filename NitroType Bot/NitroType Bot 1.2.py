import time, random, pynput
import pytesseract
import mss
import cv2
from pytesseract import image_to_string
from PIL import Image
from pynput.keyboard import Key, Controller

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
keyboard = Controller()

first_line_height = 705       #735 for no ad, 835 for with ad
timestep = 0.03               #time between typing characters #~0.031
press_speed = 0.0005


def grabLine(x):
    with mss.mss() as sct:
            # The screen part to capture
            moniter_number = 1
            mon = sct.monitors[moniter_number]
            monitor = {"top": x, "left": 950, "width": 645, "height": 30, "mon": moniter_number} #Browser zoom at 100% for single line
            output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            return output

time.sleep(2)

#Take an image of the first line
output = grabLine(first_line_height)

paragraph = []
while True:
    # Pass the image into Tesseract
    image = cv2.imread(output, 0) #0 converts image to grayscale
    cv2.imshow('image', image)
    line = pytesseract.image_to_string(image)
    
    x1 = 0 #Counter for when to take image of second line
    #Type out the first line
    for char in line:
        keyboard.press(char)
        time.sleep(press_speed)
        keyboard.release(char)
        time.sleep(timestep)
        
        print(char)
        paragraph.append(char)

        x1 = x1 + 1
        
        if x1 == 8: #Take the image of the second line when the 5th character has been typed
            output = grabLine(first_line_height + 29)

    #Type a space to initiate next line
    keyboard.press(" ")
    time.sleep(press_speed)
    keyboard.release(" ")
    paragraph.append(" ")
    print(" ")
