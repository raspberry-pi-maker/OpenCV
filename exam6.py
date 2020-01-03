# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import numpy as np
import cv2
filename = 'F:\\study\\opencv\\biden.png'
img = cv2.imread(filename, cv2.IMREAD_COLOR)
height, width, channels = img.shape
print("image   H:%d W:%d, Channel:%d"%(height, width, channels))
#cv2.imshow('original', img)


# %%
#shift X direction 100 pixels
black = np.full((height, 100, channels), 0, dtype=np.uint8)
shiftX = np.roll(img, (100, 0), axis = (1, 0))
shiftX[:, 0:100,:] = black


# %%
#shift Y direction 100 pixels
black = np.full((100, width, channels), 0, dtype=np.uint8)
shiftY = np.roll(img, (0, 100), axis = (1, 0))
shiftY[0:100, : ,:] = black


# %%
cv2.imshow('roll-X', shiftX)
cv2.imshow('roll-Y', shiftY)

cv2.waitKey(0)
cv2.destroyAllWindows()


# %%


