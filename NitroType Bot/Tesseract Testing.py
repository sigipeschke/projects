from PIL import Image
import pytesseract
from pytesseract import image_to_string
import mss
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

output = "sct-705x950_645x135.png"
image = cv2.imread(output, 0) #0 converts image to grayscale
cv2.imshow('image', image)
#char = pytesseract.image_to_string(image, config='--psm 8') #image_to_string(image, config='--psm 8') # To read single characters
line = pytesseract.image_to_string(image)

print('Tesseract Found', line)