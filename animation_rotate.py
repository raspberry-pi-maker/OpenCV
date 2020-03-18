import argparse
import cv2
import numpy as np
import time

FPS = 30
angular_velocity = np.degrees(np.pi)    # I'll make 1 rotation per 2 seconds
step_angle = (angular_velocity / FPS) 1.0
step_radian = np.radians(step_angle)
max_count = 3
def process_masking(base, mask, pos):
    h, w, c = mask.shape
    hb, wb, _ = base.shape
    x = pos[0]
    y = pos[1]

    #check mask position
    if(x > wb or y > hb):
        print(' invalid overlay position(%d,%d)'%(x, y))
        return None
    
    #remove alpha channel    
    if c == 4:
        mask = cv2.cvtColor(mask, cv2.COLOR_BGRA2BGR) 
    
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
                if (int(B) + int(G) + int(R)):
                    bg[i][j][0] = B
                    bg[i][j][1] = G
                    bg[i][j][2] = R
        img[y:y+h, x:x+w] = bg
    except IndexError:  #index (i, j) is out of the screen resolution.  (화면 범위를 벗어남.)
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

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
out_video = cv2.VideoWriter('./animation.mp4', fourcc, 30, (c_width, c_height))


angle = step_angle
x_pos = (c_width - width) * 1.0
count = 0

while count < max_count:
    matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotate = cv2.warpAffine(mask, matrix, (width, height))
    s = time.time()
    angle += step_angle
    if(angle > 360):
        angle = angle % 360.0

    print('x_pos:%f'%(x_pos))
    img = process_masking(canvas, rotate, (int(x_pos),0))
    x_pos -= int(step_radian * height / 2 )
    print('x_pos:%f'%(x_pos))
    out_video.write(img)
    cv2.imshow('rotate', img)
    if(x_pos < count * width):
        x_pos = (c_width - width) * 1.0
        count += 1
        canvas = img.copy()
    k = cv2.waitKey(1)
    delay_fps(s)
    

out_video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()





