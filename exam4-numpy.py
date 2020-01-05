import argparse
import cv2
import numpy as np


def rotate(img):
    rot = np.rot90(img)
    return rot

parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--file", type=str, required=True, help="filename of the input image to process")
args = parser.parse_args()

img = cv2.imread(args.file, cv2.IMREAD_COLOR)
height, width, channels = img.shape
print("image   H:%d W:%d, Channel:%d"%(height, width, channels))
cv2.imshow('original', img)


img_translation = rotate(img)

cv2.imshow('translate', img_translation)

cv2.waitKey(0)
cv2.destroyAllWindows()





