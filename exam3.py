import argparse
import cv2
import numpy as np


parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--file", type=str, required=True, help="filename of the input image to process")
parser.add_argument("--x", type=int, required=True, help="shift value of X direction")
parser.add_argument("--y", type=int, required=True, help="shift value of Y direction")
args = parser.parse_args()

img = cv2.imread(args.file, cv2.IMREAD_COLOR)
height, width, channels = img.shape
print("image   H:%d W:%d, Channel:%d"%(height, width, channels))
cv2.imshow('original', img)

# if args.x:
#     img = np.roll(img, args.x, axis = 1) #axis = 1: x direction
# if args.y:
#     img = np.roll(img, args.y, axis = 0) #axis = 0: y direction

img = np.roll(img, (args.x, args.y), axis = (1, 0))

cv2.imshow('roll', img)

cv2.waitKey(0)
cv2.destroyAllWindows()





