import argparse
import numpy as np
import cv2

parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--thick", default = 3, type=int, help="font thickness")
parser.add_argument("--scale", default = 2.0, type=float, help="font thickness")
args = parser.parse_args()

channel = 3


red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)
yellow = (0, 255, 255)
cyan = (255, 255, 0)
magenta = (255, 0, 255)

x_leading = 20
y_leading = 20

'''
This function get a color value for canvas background
'''
def get_canvas_size(text, font, color):
    y_pos = y_leading
    y_size = 0
    x_size = 0
    for t, f in zip(text, font):
        (label_width, label_height), baseline = cv2.getTextSize(t, f, fontScale = args.scale, thickness = args.thick)     
        y_pos += (label_height + baseline + y_leading)   
        if(label_width > x_size - x_leading):
            x_size = label_width + x_leading
        if(y_pos > y_size):
            y_size = y_pos 
    print('canvas size : W[%d] H[%d]'%(x_size, y_size))

    B = np.full((y_size, x_size, 1), color[0],  dtype=np.uint8)
    G = np.full((y_size, x_size, 1), color[1],  dtype=np.uint8)
    R = np.full((y_size, x_size, 1), color[2],  dtype=np.uint8)

    img = cv2.merge((B, G, R))
    return img
            

text = ('Hello OpenCV', 'OpenCV Cooking', 'Hello spypiggy', 'Hello NVIDIA Jetson')
font = (cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, cv2.FONT_ITALIC, cv2.FONT_HERSHEY_SIMPLEX, cv2.FONT_HERSHEY_COMPLEX)
color = (red,green, blue, white)

img = get_canvas_size(text, font, yellow)
y_pos = 0
for t, f, c in zip(text, font, color):
    (label_width, label_height), baseline = cv2.getTextSize(t, f, fontScale = args.scale, thickness = args.thick)
    y_pos += label_height + baseline + y_leading
    location = (20, y_pos)
    cv2.putText(img, t, location, f, fontScale = args.scale, color = c, thickness = args.thick)

cv2.imshow("drawing", img)
cv2.waitKey(0)