import argparse
import numpy as np
import cv2

parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--thick", default = 3, type=int, help="font thickness")
parser.add_argument("--scale", default = 2.0, type=float, help="font thickness")
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



y_pos = 50


location = (20, y_pos)
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX  # hand-writing style font
fontScale = 3.5
cv2.putText(img, 'Hello OpenCV', location, font, fontScale = args.scale, color = yellow, thickness = args.thick)



location = (20, y_pos + 50)
font = cv2.FONT_ITALIC  # italic font
fontScale = 2
cv2.putText(img, 'OpenCV Cooking', location, font, fontScale = args.scale, color = red, thickness = args.thick)



location = (20, y_pos + 100)
font = cv2.FONT_HERSHEY_SIMPLEX  # normal size sans-serif font
fontScale = 1.5
cv2.putText(img, 'Hello spypiggy', location, font, fontScale = args.scale,  color = blue, thickness = args.thick)



location = (20, y_pos + 150)
font = cv2.FONT_HERSHEY_COMPLEX  # normal size serif font
fontScale = 1.2
cv2.putText(img, 'Hello NVIDIA Jetson ', location, font, fontScale = args.scale, color = green, thickness = args.thick)


cv2.imshow("drawing", img)
cv2.waitKey(0)