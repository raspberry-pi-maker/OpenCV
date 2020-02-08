import cv2
import sys, time
import argparse


parser = argparse.ArgumentParser(description='Webcam resolution Test')
parser.add_argument('--api', type=int, default=280, help='cv2.CAP_GSTREAMER=1800,  cv2.CAP_V4L2 = 200 ')
parser.add_argument('--width', type=int, default=1280)
parser.add_argument('--height', type=int, default=960)
args = parser.parse_args()

print('Webcam Test')
cap = cv2.VideoCapture(0,  args.api)
if (cap.isOpened() == False):
    print("Unable to read camera feed")
    sys.exit(0)
ret = cap.set(cv2.CAP_PROP_FRAME_WIDTH, args.width)
print('apiReference[%d] WebCAM width  set :%d'%(args.api, ret))
ret = cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.height)
print('apiReference[%d] WebCAM height set :%d'%(args.api, ret))
ret, img = cap.read()
if ret == False:
    print('WebCAM Read Error')
    sys.exit(0)
h, w, c = img.shape
print('Video Frame shape H:%d, W:%d, Channel:%d'%(h, w, c))


count = 1
while cap.isOpened():
    try:
        start = time.time()
        ret, img = cap.read()
        if ret == False:
            break
        count += 1
        cv2.waitKey(1)
        cv2.imshow('webcam', img)
        end = time.time()
        print('FPS : %f'%(1 / (end - start)))
        if count > 100:
            break
    except KeyboardInterrupt:
        print('Ctrl + C')
        break

print('Webcam Frame read End. Total Frames are : %d'%(count))
cv2.destroyAllWindows()
cap.release()