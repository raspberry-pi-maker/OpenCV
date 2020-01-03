import argparse
import cv2
import numpy as np


parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--file", type=str, required=True, help="filename of the input image to process")
parser.add_argument("--angle", type=int, required=True, help="rotate angle(degree)")
args = parser.parse_args()

img = cv2.imread(args.file, cv2.IMREAD_COLOR)
height, width, channels = img.shape
print("image   H:%d W:%d, Channel:%d"%(height, width, channels))
cv2.imshow('original', img)

matrix = cv2.getRotationMatrix2D((width/2, height/2), args.angle, 1)
print(matrix)
img = cv2.warpAffine(img, matrix, (width, height))
height, width, channels = img.shape
print("rotate image   H:%d W:%d, Channel:%d"%(height, width, channels))

cv2.imshow('rotate', img)

cv2.waitKey(0)
cv2.destroyAllWindows()





