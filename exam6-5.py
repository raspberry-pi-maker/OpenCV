#-*- coding:utf-8 -*-
import argparse
import numpy as np
import cv2

parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--thick", default = 4, type=int, help="font thickness")
parser.add_argument("--scale", default = 4.0, type=float, help="font thickness")
args = parser.parse_args()

w = 640
h = 480
channel = 3

img = np.zeros((h, w, channel), np.uint8)


red = (0, 0, 255)
green = (0, 255, 0)
blue = (255, 0, 0)
white = (255, 255, 255)
yellow = (0, 255, 255)
cyan = (255, 255, 0)
magenta = (255, 0, 255)

x_leading = 20
y_leading = 20


def get_canvas_size(t, f):
    y_pos = y_leading
    y_size = 0
    x_size = 0
    (label_width, label_height), baseline = cv2.getTextSize(t, f, fontScale = args.scale, thickness = args.thick)     
    y_pos += (label_height + baseline + y_leading)   
    if(label_width > x_size - x_leading):
        x_size = label_width + x_leading
    if(y_pos > y_size):
        y_size = y_pos 
    print('canvas size : W[%d] H[%d]'%(x_size, y_size))        
    img = np.zeros((y_size, x_size, channel), np.uint8)
    return img
            

text = 'Hello OpenCV'
font = cv2.FONT_HERSHEY_COMPLEX

img = get_canvas_size(text, font)
y_pos = 0
thick = 4
(label_width, label_height), baseline = cv2.getTextSize(text, font, fontScale = args.scale, thickness = args.thick)
y_pos += label_height + baseline + y_leading

location = (20 - thick, y_pos)
cv2.putText(img, text, location, font, fontScale = args.scale, color = red, thickness = args.thick)
location = (20 + thick, y_pos)
cv2.putText(img, text, location, font, fontScale = args.scale, color = red, thickness = args.thick)
location = (20,  y_pos - thick)
cv2.putText(img, text, location, font, fontScale = args.scale, color = red, thickness = args.thick)
location = (20,  y_pos + thick)
cv2.putText(img, text, location, font, fontScale = args.scale, color = red, thickness = args.thick)

location = (20 - thick, y_pos - thick)
cv2.putText(img, text, location, font, fontScale = args.scale, color = red, thickness = args.thick)
location = (20 + thick, y_pos + thick)
cv2.putText(img, text, location, font, fontScale = args.scale, color = red, thickness = args.thick)
location = (20 - thick,  y_pos - thick)
cv2.putText(img, text, location, font, fontScale = args.scale, color = red, thickness = args.thick)
location = (20 + thick,  y_pos + thick)
cv2.putText(img, text, location, font, fontScale = args.scale, color = red, thickness = args.thick)



location = (20 , y_pos)
cv2.putText(img, text, location, font, fontScale = args.scale, color = white, thickness = args.thick)




cv2.imshow("drawing", img)
cv2.waitKey(0)