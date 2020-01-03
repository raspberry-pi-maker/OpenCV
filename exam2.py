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

translation_matrix = np.float32([ [1,0,args.x], [0,1,args.y] ])
img_translation = cv2.warpAffine(img, translation_matrix, (width, height))

cv2.imshow('translate', img_translation)

cv2.waitKey(0)
cv2.destroyAllWindows()





