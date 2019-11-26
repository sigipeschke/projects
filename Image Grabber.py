import mss
from PIL import Image

first_line_height = 835
def grabImage():
    with mss.mss() as sct:
            # The screen part to capture
            moniter_number = 1
            mon = sct.monitors[moniter_number]
            #monitor = {"top": 867, "left": 708, "width": 26, "height": 45, "mon": moniter_number} #Browser zoom at 100% for single character top at 800 with ad, 700 without ad.
            #monitor = {"top": 735, "left": 705, "width": 500, "height": 30, "mon": moniter_number} #Browser zoom at 100% for single line
            monitor = {"top": first_line_height, "left": 705, "width": 500, "height": 115, "mon": moniter_number} #Browser zoom at 100% for full 4 lines
            output = "sct-{top}x{left}_{width}x{height}.png".format(**monitor)

            # Grab the data
            sct_img = sct.grab(monitor)

            # Save to the picture file
            mss.tools.to_png(sct_img.rgb, sct_img.size, output=output)
            return output

output = grabImage()
