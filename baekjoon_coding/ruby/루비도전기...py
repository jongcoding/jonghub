def rotate(arr, start, end):
    # 구간을 뒤집음
    arr[start:end + 1] = [-x for x in reversed(arr[start:end + 1])]
def find_largest_consecutive_range(arr):
    # 뒤집은 후 연속된 숫자가 가장 많이 나오는 구간이 어딘지 구함
    max_length = 0
    max_start = -1
    max=0
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            imp = list(arr)
            rotate(imp,i,j)
            num=0
            for p in range(len(imp)-1):
                if abs(imp[p+1]-imp[p])==1:
                    num+=1
            if max<num:
                max_start=i
                max_length=j-i
                max=num
    return max_start, max_start + max_length 

def find_range(arr):
    li=[t for t in range(1, len(arr)+1)]
    if li==arr:
        exit()
    sub=list(arr)

    while True:
        min_x=min(li)
        max_y=max(li)
        index_min=0
        index_max=0
        for i in range(len(arr)):
            if abs(arr[i])==min_x:
                index_min =i
            elif abs(arr[i])==max_y:
                index_max=i

        if arr[min_x-1]==min_x:
            li.pop(0)
            
        elif arr[max_y-1]==max_y:
            li.pop(-1)
        else:
            #print("최소",min_x,"최대",max_y)
            break
    if arr[index_min]>0 and arr[index_max]>0:
        start,last=find_largest_consecutive_range(sub)
        return(start+1,last+1)
    
    elif arr[index_min]<0 and arr[index_max]>0:
        rotate(sub, min_x-1, index_min)
        return(min_x,index_min+1)

    elif arr[index_min]>0 and arr[index_max]<0:
        rotate(sub, max_y-1, index_max)
        return(index_max+1,max_y)
    elif arr[index_min]<0 and arr[index_max]<0:
        if min_x-(len(arr)-max_y)>0:
            rotate(sub,max_y-1, index_max)
            return(max_y,index_max+1)
        elif min_x-(len(arr)-max_y)<0:
            rotate(sub,max_y-1,index_max)
            return(max_y,index_max+1)
        else:
            start,last=find_largest_consecutive_range(sub)
            return(start+1,last+1)
N=int(input())
ll=[]
array=list(map(int,input().split()))
while True:
    start, last=find_range(array)
    path=[start,last]
    path.sort()
    ll.append(path)
    rotate(array,path[0]-1,path[1]-1)
    if array==[x for x in range(1,N+1)]:
        n=len(ll)
        print(n)
        for i in range(len(ll)):
            print(" ".join(map(str,ll[n-i-1])))
        break


            



