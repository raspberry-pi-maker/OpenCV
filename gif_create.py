import argparse
import cv2
import numpy as np
import time
from PIL import Image, ImageDraw

FPS = 30
angular_velocity = np.degrees(np.pi)    # I'll make 1 rotation per 2 seconds
step_angle = angular_velocity / FPS
step_radian = np.radians(step_angle)
max_count = 3

gif_frames = []

def save_gif(frames, gifname, speed):   #speed 100
    frames[0].save(gifname, format='GIF', append_images=frames[1:], save_all=True, duration=speed, loop=0)

def process_masking(base, mask, pos):
    h, w, c = mask.shape
    x = pos[0]
    y = pos[1]
    if c == 4:
        mask = cv2.cvtColor(mask, cv2.COLOR_BGRA2BGR) 
    img = base.copy()
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

def delay_fps(s):
    while (time.time() - s < (1.0 / FPS) ):
        time.sleep(0.001)

parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--file", type=str, required=True, help="filename of the input image to process")
args = parser.parse_args()


mask = cv2.imread(args.file, cv2.IMREAD_COLOR)
height, width, channels = mask.shape
print("image   H:%d W:%d, Channel:%d"%(height, width, channels))
print('Angular Velocity:%f step_angle:%f'%(angular_velocity, step_angle))
canvas = np.zeros((height * 2, width * 5, 3), np.uint8)
c_height, c_width, c_channels = canvas.shape

angle = step_angle
x_pos = c_width - width
count = 0

while count < max_count:
    matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotate = cv2.warpAffine(mask, matrix, (width, height))
    s = time.time()
    angle += step_angle
    if(angle > 360):
        angle = 0

    print('x_pos:%d'%(x_pos))
    img = process_masking(canvas, rotate, (x_pos,0))
    x_pos -= int(step_radian * height / 2 )
    if c_channels == 4:
        rgb = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB) 
    else:    
        rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
    im_pil = Image.fromarray(rgb)
    gif_frames.append(im_pil)
    cv2.imshow('rotate', img)
    if(x_pos < count * width):
        x_pos = c_width - width
        count += 1
        canvas = img.copy()
    k = cv2.waitKey(1)
    delay_fps(s)
    
save_gif(gif_frames, "f:\\tmp\\bear.gif", 50)
cv2.waitKey(0)
cv2.destroyAllWindows()