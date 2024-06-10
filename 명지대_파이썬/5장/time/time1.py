import time
print('현재시간:', time.time())
def manyloop(max):
    t1=time.time()
    for a in range(max):
        pass
    t2 = time.time()
    print(t2-t1, '초 경과')

n=int(input())
manyloop(n)