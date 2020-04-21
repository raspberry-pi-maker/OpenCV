# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from PIL import Image
import numpy as np


img = Image.open("F:\src\OpenCV\Image Processing #5 - Image Append\\elsa1.jpg")
width1, height1 = img.size
print("elsa1 JPG   H:%d W:%d"%(height1, width1))

img2 = Image.open("F:\src\OpenCV\Image Processing #5 - Image Append\\elsa2.jpg")
width2, height2 = img.size
print("elsa2 JPG   H:%d W:%d"%(height2, width2))


# %%
#resize the second image. Make the same height
img3 = img2.resize((int(width2 * height1 * 1.0 / height2), height1))
width2, height2  = img3.size
print("elsa2 resized JPG   H:%d W:%d"%(height2, width2))

#resize the second image. Make the same width
img4 = img2.resize((width1, int(height2 * width1 * 1.0 / width2) ))
width3, height3 = img4.size
print("elsa2 resized JPG   H:%d W:%d"%(height3, width3))

np_img3 = np.asarray(img3, dtype="uint8")
np_img4 = np.asarray(img4, dtype="uint8")


# %%
combH = np.hstack((img, np_img3 ))
imgs_combH = Image.fromarray(np.uint8(combH))
width, height = imgs_combH.size
print("elsa combined JPG   H:%d W:%d"%(height, width))

combV = np.vstack((img, np_img4 ))
imgs_combV = Image.fromarray(np.uint8(combV))
width, height  = imgs_combV.size
print("elsa combined JPG   H:%d W:%d"%(height, width))


# %%
img.show()
img3.show()
imgs_combH.show()
imgs_combV.show()


# %%


