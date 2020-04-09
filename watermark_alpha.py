import argparse
import cv2
import numpy as np
'''
This function remains background
rate should be : 0 < rate < 1.0
'''
def process_alpha_masking(base, mask, pos):
    h, w, c = mask.shape
    hb, wb, _ = base.shape
    x = pos[0]
    y = pos[1]

    #check mask position
    if(x > wb or y > hb):
        print(' invalid overlay position(%d,%d)'%(x, y))
        return None
    
    #remove alpha channel    
    if c != 4:
        print('mask image file does not have alpha channel')
        return None
    
    #adjust mask
    if(x + w > wb):
        mask = mask[:, 0:wb - x]
        print(' mask X size adjust[W:%d] -> [W:%d]'%(w, wb - x))
    if(y + h > hb):
        mask = mask[0:hb - y, :]
        print(' mask Y size adjust[H:%d] -> [H:%d]'%(h, hb - y))

    h, w, c = mask.shape
    
    img = base.copy()
    bg = img[y:y+h, x:x+w]      #overlay area
    try:
        for i in range(0, h):
            for j in range(0, w):
                B = mask[i][j][0]
                G = mask[i][j][1]
                R = mask[i][j][2]
                alpha = mask[i][j][3] * 1.0 / 255.0
                if (alpha > 0.0):
                    bg[i][j][0] = int(B * alpha + bg[i][j][0] * (1 - alpha))
                    bg[i][j][1] = int(G * alpha + bg[i][j][1] * (1 - alpha))
                    bg[i][j][2] = int(R * alpha + bg[i][j][2] * (1 - alpha))
        img[y:y+h, x:x+w] = bg
    except IndexError:  #index (i, j) is out of the screen resolution.  (화면 범위를 벗어남.)
        print(' index Error')
        return None
    return img


parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--file", type=str, required=True, help="filename of the input image to process")
parser.add_argument("--mask", type=str, required=True, help="mask image to overlay")
args = parser.parse_args()

img = cv2.imread(args.file, cv2.IMREAD_COLOR)
height, width, channels = img.shape
print("image   H:%d W:%d, Channel:%d"%(height, width, channels))
cv2.imshow('original', img)

mark = cv2.imread(args.mask, cv2.IMREAD_UNCHANGED)
mheight, mwidth, mchannels = mark.shape
print("mask   H:%d W:%d, Channel:%d"%(mheight, mwidth, mchannels))

x = np.amin( [mwidth, width])
y = np.amin( [mheight, height])
new_img = process_alpha_masking(img, mark, (x, y))
if new_img is not None :
    cv2.imshow('masked', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()





