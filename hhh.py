import time

time_start=time.time()
s = 1
for i in range(2000):
    s = s*(i+1)
print(s)

time_end=time.time()
print('time cost',time_end-time_start,'s')