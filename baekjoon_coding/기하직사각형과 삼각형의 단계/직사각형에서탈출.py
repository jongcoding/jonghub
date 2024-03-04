x,y,w,h=map(int, input().split())
mini_list=[x, y, w, h, abs(x-w),abs(y-h)]
print(min(mini_list))