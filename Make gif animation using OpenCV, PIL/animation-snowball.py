import cv2
import numpy as np
from PIL import Image
from PIL import ImageDraw
import time, os
import argparse
from random import *

parser = argparse.ArgumentParser(description="OpenCV Example")
parser.add_argument("--maxcnt", default = 5, type=int, help="X axis snow max count")
parser.add_argument("--mincnt", default = 1, type=int, help="X axis snow min count")
parser.add_argument("--size", default = 5, type=int, help="snowball size(diameter)")
args = parser.parse_args()


count = 0
FPS = 5
SLEEP = 2.0 / FPS

height = 480
width = 640
canvas = np.zeros((height,width,3), np.uint8)
img = None
gif_frames = []
snow_balls = []

v_snow_cnt = int(height / (FPS * 4) )
v_step = int(height / v_snow_cnt)
h_snow_cnt = args.maxcnt
snow_balls = []
snow_color = (255, 255, 255) 

def save_gif(frames, gifname, speed):   #speed 100
    frames[0].save(gifname, format='GIF', append_images=frames[1:], save_all=True, duration=speed, loop=0)


def create_snowball():
    global snow_balls
    seed(time.time())
    snows = []
    count = randint(args.mincnt, args.maxcnt)
    for i in range(count):
        snow = randint(1, width)
        snows.append(snow)
    snow_balls.insert(0, snows)

    '''
    remove old snow
    '''
    if(len(snow_balls) > v_snow_cnt): 
        snow_balls.pop(v_snow_cnt)

'''
move the horizontal position
'''

def fall_down():
    global snow_balls
    Tsnow_balls = []
    for snows in snow_balls:
        Tsnows = []
        seed(time.time())
        for snow in snows:
            move = randint(-5, 5)
            snow += move
            Tsnows.append(snow)
        Tsnow_balls.append(Tsnows)    
    snow_balls = Tsnow_balls.copy()

def draw_image():
    global img
    img = canvas.copy()
    line = 0
    for snows in snow_balls:
        for snow in snows:
            img = cv2.circle(img, (snow, line * v_step), args.size, snow_color, -1)
        line += 1
    cv2.imshow('snow', img)
    cv2.waitKey(1)


count = 0
Save = False
while True:
    try:
        start = time.time()
        create_snowball()
        fall_down()
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