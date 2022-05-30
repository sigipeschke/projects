import mss
import mss.tools
from PIL import Image
import pyautogui
import keyboard

#pos = pyautogui.position()
#print(pos)
pp = []
while len(pp) < 3:  # making a loop
    keyboard.wait('q')
    if len(pp) == 2:
        break
    else:
        pos = pyautogui.position()
        print('Mouse position:', pos)
        pp.append(pos)


def grabImage():
    with mss.mss() as sct:
            # The screen part to capture
            moniter_number = 1
            mon = sct.monitors[moniter_number]
            monitor = {"top": 705, "left": 950, "width": 645, "height": 135, "mon": moniter_number} #Browser zoom at 100% for full 4 lines
            output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            return output

#output = grabImage()