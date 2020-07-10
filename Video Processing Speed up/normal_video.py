# import the necessary packages
import numpy as np
import argparse
import time
import cv2

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", required=True,
	help="path to input video file")
args = ap.parse_args()


cap = cv2.VideoCapture(args.video)
start = time.time()
index = 1
while True:
    s = time.time()
    ret, frame = cap.read()
    if ret == False:
        break
    e = time.time()
    cv2.putText(frame, "Hello World", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)	
    cv2.putText(frame, "FPS:%3.1f"%(1 / (e - s)), (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)	
    img = frame.copy()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #print('%04d fps:%f'%( index, 1 / (time.time() -s)))
    index += 1
    
end = time.time()
print("[INFO] Total time:%f"%(end - start))
print("[INFO] approx. FPS:%f"%( index / (end - start)))    
cv2.destroyAllWindows()
cap.release()
   


