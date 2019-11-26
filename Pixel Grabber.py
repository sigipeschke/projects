from PIL import Image

def grabPixel(file_location, x, y):
    return Image.open(file_location).load()[x,y]

