import cv2
import time
import pafy #pip install --upgrade youtube-dl
url = 'https://www.youtube.com/watch?v=xFrGuyw1V8s'
video = pafy.new(url)
best = video.getbest(preftype="mp4")
FPS = 30.0
SLEEP = 1.0 / FPS
cap = cv2.VideoCapture()
cap.open(best.url)
while True:
    s = time.time()
    retval, frame = cap.read()
    if not retval:
        break
    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)
    if key == 27:   #Press Esc to exit
        break
    elapsed = time.time() - s
    time.sleep(max(0, SLEEP - elapsed))
cv2.destroyAllWindows()