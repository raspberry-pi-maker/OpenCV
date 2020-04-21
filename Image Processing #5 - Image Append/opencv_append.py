# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import cv2
import numpy as np

img = cv2.imread("F:\src\OpenCV\Image Processing #5 - Image Append\\elsa1.jpg", cv2.IMREAD_COLOR)
height1, width1, channels1 = img.shape
print("elsa1 JPG   H:%d W:%d, Channel:%d"%(height1, width1, channels1))

img2 = cv2.imread("F:\src\OpenCV\Image Processing #5 - Image Append\\elsa2.jpg", cv2.IMREAD_COLOR)
height2, width2, channels2 = img2.shape
print("elsa2 JPG   H:%d W:%d, Channel:%d"%(height2, width2, channels2))


# %%
#resize the second image. Make the same height
img3 = cv2.resize(img2, (int(width2 * height1 * 1.0 / height2), height1))
height2, width2, channels2 = img3.shape
print("elsa2 resized JPG   H:%d W:%d, Channel:%d"%(height2, width2, channels2))

#resize the second image. Make the same width
img4 = cv2.resize(img2, (width1, int(height2 * width1 * 1.0 / width2) ))
height3, width3, channels3 = img4.shape
print("elsa2 resized JPG   H:%d W:%d, Channel:%d"%(height3, width3, channels3))


# %%
imgs_combH = np.hstack((img, img3 ))
height, width, channels = imgs_combH.shape
print("elsa combined JPG   H:%d W:%d, Channel:%d"%(height, width, channels))

imgs_combV = np.vstack((img, img4 ))
height, width, channels = imgs_combV.shape
print("elsa combined JPG   H:%d W:%d, Channel:%d"%(height, width, channels))


# %%
cv2.imshow('elsa1', img)
cv2.imshow('elsa2', img3)
cv2.imshow('elsa3', imgs_combH)
cv2.imshow('elsa4', imgs_combV)
cv2.waitKey(0)
cv2.destroyAllWindows()


# %%


