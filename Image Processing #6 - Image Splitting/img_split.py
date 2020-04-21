#-*- coding:utf-8 -*-
import argparse
import numpy as np
import cv2


# split into 10 X 5

H_Count = 10
V_Count = 5

file = './lotto.png'
img = cv2.imread(file, cv2.IMREAD_COLOR)
height, width, channels = img.shape

count = 1
h_img = np.vsplit(img, V_Count)
for i in h_img:
    j = np.hsplit(i, H_Count)
    for k in j:
        name = "%d.png"%(count)
        cv2.imwrite(name, k)
        count += 1
