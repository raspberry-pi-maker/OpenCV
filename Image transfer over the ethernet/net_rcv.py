import numpy as np
import cv2
import socket, struct,time
 
CHUNK_SIZE = 8192 + 32
CHUNK_SIZE = 52000
SERVER = ("0.0.0.0",4321)
H = 570
W = 720
C = 3
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(SERVER)
bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF) 
print('Rcv buf size:%d'%(bufsize))
if CHUNK_SIZE < bufsize:
    CHUNK_SIZE = bufsize

sock.settimeout(5)
total = 0
buf = []
packet_cnt = 0
def reset():
    global buf, total, packet_cnt
    total = 0
    buf = []
    packet_cnt = 0

while(True):
    try:
        data, addr = sock.recvfrom(CHUNK_SIZE)
        total += len(data)
        key = int.from_bytes(data[:4],byteorder="little")
        seq = int.from_bytes(data[4:8],byteorder="little")
        cnt = int.from_bytes(data[8:12],byteorder="little")
        buf += data[12:]
        packet_cnt += 1
        print('Total rcv:%d Key:%d, seq:%d total chunk:%d'%(total, key, seq, cnt))
        if key == 1:    #last
            if(packet_cnt != cnt):
                print('Total rcv cnt:%d total chunk:%d'%(packet_cnt, cnt))
                reset()
                continue

            img = np.asarray(buf, dtype=np.uint8)
            b = img.reshape(H,W,C)
            cv2.imshow('H', b)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            reset()

    except KeyboardInterrupt:
        break
    except socket.timeout:
        reset()
        continue    

