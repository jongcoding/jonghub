import time

current=time.ctime()
print(current)

list_cur=current.split(' ')
for t in list_cur:
    print(t)