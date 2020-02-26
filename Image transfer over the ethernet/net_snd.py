import numpy as np
import cv2
import socket, struct,time

CHUNK_SIZE = 8192 * 6
SERVER = ("localhost",4321) # Modify localhost to receiving part IP address

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF) 
print('Snd buf size:%d'%(bufsize))

img = cv2.imread('star.jpg')
H,W,C = img.shape
print(img.shape)

data = img.tobytes()
print('byte len:%d'%(len(data)))
total = 0
chunks = [data[i:i+CHUNK_SIZE] for i in range(0, len(data), CHUNK_SIZE)]
chunk_len = len(chunks)
s = time.time()
for i, chunk in enumerate(chunks):
    if(i == chunk_len - 1): #last
        chunk = struct.pack("<I", 1) + struct.pack("<I", i) + struct.pack("<I", chunk_len) + chunk    # len(data) + 12 bytes , "<I" : < means little-endian, I means 4 bytes integer
    else:    
        chunk = struct.pack("<I", 0) + struct.pack("<I", i) + struct.pack("<I", chunk_len) + chunk    # len(data) + 12 bytes , "<I" : < means little-endian, I means 4 bytes integer
    sock.sendto(chunk, SERVER)
    total += len(chunk)
    print('Total sent:%d'%(total))
    time.sleep(0.0001)
e = time.time()
print('time:%f', e - s)
