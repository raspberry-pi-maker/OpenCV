import time
from numba import jit

@jit(nopython=True, cache=True)
def loop_func():
    sum = 0
    for x in range(10000000):
        sum += x
    print("SUM[0 ~ 10000000] is " + str(sum));    
    
    
start = time.time()
loop_func()
end = time.time()
print("sec used: %10.6f"%(end - start))
    