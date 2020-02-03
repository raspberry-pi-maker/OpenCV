import cv2
import sys

cap = cv2.VideoCapture('f:\\tmp\\02.mp4')
ret, img = cap.read()
if ret == False:
    print('Video File Read Error')    
    sys.exit(0)
h, w, c = img.shape
print('Video Frame shape H:%d, W:%d, Channel:%d'%(h, w, c))

small_size = (int(w/2), int(h/2))
fourcc = cv2.VideoWriter_fourcc(*"DIVX")
out_video = cv2.VideoWriter('/tmp/output.mp4', fourcc, cap.get(cv2.CAP_PROP_FPS), small_size)

count = 1
while cap.isOpened():
    ret, img = cap.read()
    if ret == False:
        break
    count += 1
    #Do what you want to do here!         
    small_img = cv2.resize(img, small_size)
    out_video.write(small_img)


print('Video File read End. Total Frames are : %d'%(count))
cap.release()
out_video.release()