import argparse
import cv2

'''
This function remains background
'''
def process_masking(img, mask, pos):
    h, w, c = mask.shape
    x = pos[0]
    y = pos[1]
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
                    bg[i][j][0] = B
                    bg[i][j][1] = G
                    bg[i][j][2] = R
        img[y:y+h, x:x+w] = bg
    except IndexError:
        print(' index Error')
        return None
    return img

'''
This function removes background
'''
def process_masking2(img, mask, pos):
    h, w, c = mask.shape
    x = pos[0]
    y = pos[1]
    if c == 4:
        mask = cv2.cvtColor(mask, cv2.COLOR_BGRA2BGR) 

    img[y:y+h, x:x+w] = mask      #overlay area
    return img


parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--file", type=str, required=True, help="filename of the input image to process")
parser.add_argument("--mask", type=str, required=True, help="mask image to overlay")
args = parser.parse_args()

img = cv2.imread(args.file, cv2.IMREAD_COLOR)
height, width, channels = img.shape
print("image   H:%d W:%d, Channel:%d"%(height, width, channels))
cv2.imshow('original', img)

mask = cv2.imread(args.mask, cv2.IMREAD_UNCHANGED)
height, width, channels = mask.shape
print("mask   H:%d W:%d, Channel:%d"%(height, width, channels))
cv2.imshow('mask', mask)

new_img = process_masking2(img, mask, (10, 10))
cv2.imshow('masked', new_img)
cv2.waitKey(0)
cv2.destroyAllWindows()





