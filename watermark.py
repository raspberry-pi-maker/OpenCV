import argparse
import cv2
import numpy as np
'''
This function remains background
rate should be : 0 < rate < 1.0
'''
def watermark(img, mask, pos, rate):
    h, w, c = mask.shape
    x = pos[0]
    y = pos[1]
    height, width, channels = img.shape

    if (x + w) > width :
        print('Error : The worker mark is out of the image area.')
        return None
    if c == 4:
        mask = cv2.cvtColor(mask, cv2.COLOR_BGRA2BGR) 
    bg = img[y:y+h, x:x+w]      #overlay area
    try:
        for i in range(0, h):
            for j in range(0, w):
                B = mask[i][j][0]
                G = mask[i][j][1]
                R = mask[i][j][2]
                if (int(B) + int(G) + int(R)):
                    bg[i][j][0] = float(B) * rate + float(bg[i][j][0]) * (1 - rate)
                    bg[i][j][1] = float(G) * rate + float(bg[i][j][1]) * (1 - rate)
                    bg[i][j][2] = float(R) * rate + float(bg[i][j][2]) * (1 - rate)
        bg.astype('uint8')            
        img[y:y+h, x:x+w] = bg
    except IndexError:
        print(' index Error')
        return None
    return img


parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--file", type=str, required=True, help="filename of the input image to process")
parser.add_argument("--mask", type=str, required=True, help="mask image to overlay")
parser.add_argument("--rate", type=float, default=0.5, help="mixing rate")
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
new_img = watermark(img, mark, (x, y), args.rate)
if new_img is not None :
    cv2.imshow('masked', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()





