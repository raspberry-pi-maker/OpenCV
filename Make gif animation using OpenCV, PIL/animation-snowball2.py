import cv2
import numpy as np
from PIL import Image
from PIL import ImageDraw
import time, os
import argparse
import math
from random import *

parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--maxcnt", default = 5, type=int, help="X axis snow max count")
parser.add_argument("--mincnt", default = 1, type=int, help="X axis snow min count")
parser.add_argument("--size", default = 5, type=int, help="snowball size(diameter)")
args = parser.parse_args()


count = 0
FPS = 20
SLEEP = 2.0 / FPS

height = 480
width = 640
canvas = np.zeros((height,width,3), np.uint8)
img = None
gif_frames = []
snow_balls = []

v_snow_cnt = int(height / 2 )
v_step = int(height / v_snow_cnt)
h_snow_cnt = args.maxcnt
snow_balls = []
snow_balls_shift = []
snow_color = (255, 255, 255) 

def save_gif(frames, gifname, speed):   #speed 100
    frames[0].save(gifname, format='GIF', append_images=frames[1:], save_all=True, duration=speed, loop=0)


def create_snowball():
    global snow_balls, snow_balls_shift
    seed(time.time())
    snows = []
    shifts = []
    if count % 20 == 0:
        snow_count = randint(1, 3)
        for i in range(snow_count):
            shift = random() * 2 * math.pi #radian
            snow = randint(1, width)
            snows.append(snow)
            shifts.append(shift)
    elif count % 20 == 10:
        snow_count = randint(args.mincnt, args.maxcnt)
        for i in range(snow_count):
            shift = random() * 2 * math.pi #radian
            snow = randint(1, width)
            snows.append(snow)
            shifts.append(shift)
    snow_balls.insert(0, snows)
    snow_balls_shift.insert(0, shifts)

    '''
    remove old snow
    '''
    if(len(snow_balls) > v_snow_cnt): 
        snow_balls.pop(v_snow_cnt)
        snow_balls_shift.pop(v_snow_cnt)

'''
move the horizontal position
'''
A = 2
B = 8 * math.pi / v_snow_cnt
def fall_down_sin():
    global snow_balls
    Tsnow_balls = []
    lcnt = 0
    for snows in snow_balls:
        Tsnows = []
        seed(time.time())
        scnt = 0
        for snow in snows:
            angle = (B * lcnt) + snow_balls_shift[lcnt][scnt]
            move = A*math.sin(angle)
            snow += move
            Tsnows.append(snow)
            scnt += 1
        Tsnow_balls.append(Tsnows)
        lcnt += 1    
    snow_balls = Tsnow_balls.copy()

def draw_image():
    global img
    img = canvas.copy()
    line = 0
    for snows in snow_balls:
        for snow in snows:
            img = cv2.circle(img, (int(snow), line * v_step), args.size, snow_color, -1)
        line += 1
    cv2.imshow('snow', img)
    cv2.waitKey(1)


count = 0
Save = False
while True:
    try:
        start = time.time()
        create_snowball()
        fall_down_sin()
        draw_image()
        end = time.time()
        time.sleep(max(0, SLEEP - (end - start)))
        count += 1
        if count <= v_snow_cnt:
            im_pil = Image.fromarray(img)
            gif_frames.append(im_pil)
        else:
            if Save == False:
                Save = True
                save_gif(gif_frames, "./snawball.gif", 200)


    except KeyboardInterrupt:
        break    

cv2.destroyAllWindows()