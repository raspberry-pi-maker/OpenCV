#-*- coding: utf-8 -*-
"""
"""
from __future__ import print_function
import numpy as np
import cv2 
import argparse


parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--file", type=str, required=True, help="filename of the input image to process")
args = parser.parse_args()

print ('cv2.__version__(%s)'%(cv2.__version__))

img = cv2.imread(args.file, cv2.IMREAD_COLOR)
if img is None:
    print ('Image[%s] open error' %(args["image"]))
    exit(0)

cv2.imshow('Original', img)

img_nega = 255 - img

cv2.imshow('Negative',img_nega)
cv2.waitKey(0)
cv2.destroyAllWindows()
