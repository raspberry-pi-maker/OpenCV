import numpy as np
import cv2
import time
import math
from datetime import datetime
from PIL import Image, ImageDraw

FPS = 30.0
SLEEP = 1.0 / FPS


tmargin = 20
lmargin = 20
rmargin = 20
margin = 20
bmargin = 20
r = 100
arm_length = int(r * 0.9)
circle_thickness = 2
arm_thickness = 15
circle_color = (128,128,128)
arm_color = (96,92,255)
arm_color2 = (96,255,96)

Canvas_W = lmargin + rmargin + r * 2 * 8 + margin * 7
Canvas_H = tmargin + bmargin + r * 6 + margin * 2

digit_basic = [[(45, -45),(45, -45),(45, -45)],  [(45, -45), ( 45, -45),( 45, -45)] ]
digit_1 = [ [(225, 225),(225, 225),(225, 225)],  [(180, 180),(  0, 180),(  0,   0)] ]
digit_2 = [ [( 90,  90),( 90, 180),(  0,  90)],  [(180, 270),(  0, 270),(270, 270)] ]
digit_3 = [ [( 90,  90),( 90,  90),( 90,  90)],  [(180, 270),(  0, 270),(  0, 270)] ]
digit_4 = [ [(180, 180),(  0,  90),(225, 225)],  [(180, 180),(  0, 180),(  0,   0)] ]
digit_5 = [ [( 90, 180),(  0,  90),( 90,  90)],  [(270, 270),(180, 270),(  0, 270)] ]
digit_6 = [ [( 90, 180),(  0, 180),(  0,  90)],  [(270, 270),(180, 270),(  0, 270)] ]
digit_7 = [ [( 90,  90),(225, 225),(225, 225)],  [(180, 270),(  0, 180),(  0,   0)] ]
digit_8 = [ [( 90, 180),(  0,  90),(  0,  90)],  [(180, 270),(  0, 270),(  0, 270)] ]
digit_9 = [ [( 90, 180),(  0,  90),( 90,  90)],  [(180, 270),(  0, 180),(  0, 270)] ]
digit_0 = [ [( 90, 180),(  0, 180),(  0,  90)],  [(180, 270),(  0, 180),(  0, 270)] ]
clock_digits = []
clock_digits.append(digit_0)
clock_digits.append(digit_1)
clock_digits.append(digit_2)
clock_digits.append(digit_3)
clock_digits.append(digit_4)
clock_digits.append(digit_5)
clock_digits.append(digit_6)
clock_digits.append(digit_7)
clock_digits.append(digit_8)
clock_digits.append(digit_9)


class Clock():
    def __init__(self, x, y, circle_color, circle_thick, arm_color, arm_thick, lmar):
        self.x = x
        self.y = y
        self.circle_color = circle_color
        self.circle_thickness = circle_thick
        self.arm_color = arm_color
        self.arm_thickness = arm_thick
        self.center = (lmar + r + (margin + 2*r) * x, tmargin + r + (margin + 2*r) * y)
        self.angle1 = -45
        self.angle2 = 45
        self.target_angle1 = 0
        self.target_angle2 = 0

    def draw_circle(self, img):
        cv2.circle(img, self.center, r, self.circle_color, self.circle_thickness)

    def set_angle(self, angle1, angle2):
        self.angle1 = angle1
        self.angle2 = angle2
    def step_angle(self):
        self.angle1 += self.step
        if(self.angle1 >  self.target_angle1):
            self.angle1 = self.target_angle1
            self.finish_angle1 = True
        self.angle2 += self.step
        if(self.angle2 >  self.target_angle2):
            self.angle2 = self.target_angle2
            self.finish_angle2 = True        
    '''
    for animation, set the last angle
    '''    
    def set_target_angle(self, angle1, angle2, step):
        self.target_angle1 = angle1
        self.target_angle2 = angle2
        self.finish_angle1 = False
        self.finish_angle2 = False
        self.step = step

    def draw_arms(self, img):
        angle1 = np.radians(self.angle1)
        angle2 = np.radians(self.angle2)
        center = (lmargin + r + (margin + 2*r) * self.x, tmargin + r + (margin + 2*r) * self.y)
        pt = (self.center[0], self.center[1] - arm_length) # 12 Hour direction

        qx = int(self.center[0] + math.cos(angle1) * (pt[0] - self.center[0]) - math.sin(angle1) * (pt[1] - self.center[1]))
        qy = int(self.center[1] + math.sin(angle1) * (pt[0] - self.center[0]) + math.cos(angle1) * (pt[1] - self.center[1]))
        cv2.line(img, self.center, (qx,qy), self.arm_color, self.arm_thickness)
        qx = int(self.center[0] + math.cos(angle1) * (pt[0] - self.center[0]) - math.sin(angle2) * (pt[1] - self.center[1]))
        qy = int(self.center[1] + math.sin(angle1) * (pt[0] - self.center[0]) + math.cos(angle2) * (pt[1] - self.center[1]))
        cv2.line(img, self.center, (qx,qy), self.arm_color, self.arm_thickness)

    def init_clock(self, img):
        self.set_angle(-45, 45)
        self.draw_circle(img)


class Clocks():
    def __init__(self):
        self.clocks = []
    def add(self, clock):
        self.clocks.append(clock)
    def set_digit(self, n):    
        for c in self.clocks:
            c.set_angle(clock_digits[n][c.x][c.y][0], clock_digits[n][c.x][c.y][1])
    def set_target_digit(self, n):    
        for c in self.clocks:
            c.set_target_angle(clock_digits[n][c.x][c.y][0], clock_digits[n][c.x][c.y][1], self.step_angle)
    def draw_digit(self, img, n):
        for c in self.clocks:
            c.set_angle(clock_digits[n][c.x][c.y][0], clock_digits[n][c.x][c.y][1])
            c.draw_arms(img)
    '''
    t : animation time(sec) for drawing the digit
    '''        
    def animation_start(self, img, n, t):
        self.step_angle = 360 / (t * FPS)
        self.set_target_digit(n)
        for c in self.clocks:
            c.set_angle(digit_basic[c.x][c.y][0], digit_basic[c.x][c.y][1])
            c.draw_arms(img)
    def animation_next(self, img):
        for c in self.clocks:
            c.step_angle()
            c.draw_arms(img)            
        return True        

def make_canvas(h, w, color):
    canvas = np.zeros([h,w,3], dtype=np.uint8)
    canvas.fill(color)
    return canvas


def initialize_clocks(img):
    global H0_clocks, H1_clocks, M0_clocks, M1_clocks
    for x in range(2):
        for y in range(3):
            clock = Clock(x, y, circle_color, circle_thickness, arm_color, arm_thickness, lmargin)
            clock.init_clock(img)
            H0_clocks.add(clock)
    for x in range(2):
        for y in range(3):
            clock = Clock(x, y, circle_color, circle_thickness, arm_color, arm_thickness, lmargin + 4*r + margin * 2)
            clock.init_clock(img)
            H1_clocks.add(clock)
    for x in range(2):
        for y in range(3):
            clock = Clock(x, y, circle_color, circle_thickness, arm_color2, arm_thickness, lmargin + 8*r + margin * 4)
            clock.init_clock(img)
            M0_clocks.add(clock)
    for x in range(2):
        for y in range(3):
            clock = Clock(x, y, circle_color, circle_thickness, arm_color2, arm_thickness, lmargin + 12*r + margin * 6)
            clock.init_clock(img)
            M1_clocks.add(clock)

H0_clocks = Clocks()
H1_clocks = Clocks()
M0_clocks = Clocks()
M1_clocks = Clocks()

canvas = make_canvas(Canvas_H, Canvas_W, 0)  
initialize_clocks(canvas)

t =10
now = datetime.now()

tcanvas = canvas.copy()
H0_clocks.animation_start(tcanvas, int(now.hour / 10), t)
H1_clocks.animation_start(tcanvas, now.hour % 10, t)
M0_clocks.animation_start(tcanvas, int(now.minute / 10), t)
M1_clocks.animation_start(tcanvas, now.minute % 10, t)
for i in range(int(t * FPS)):
    start = time.time()
    tcanvas = canvas.copy()
    H0_clocks.animation_next(tcanvas)
    H1_clocks.animation_next(tcanvas)
    M0_clocks.animation_next(tcanvas)
    M1_clocks.animation_next(tcanvas)
    sleep_tm = (SLEEP - (time.time() - start)) * 1000
    cv2.imshow("digit [%02d:%02d]"%(now.hour, now.minute), tcanvas)
    # print('[%d] sleep:%f'%(i, sleep_tm))
    cv2.waitKey(max(1, int(sleep_tm)))
cv2.waitKey(0)
cv2.destroyAllWindows()
