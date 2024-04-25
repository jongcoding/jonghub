def bitonic_subseque(num_list, n):
    front=[[] for _ in range(n)]
    front[0]=[num_list[0]]
    back=[[] for _ in range(n)]
    back[n-1]=[num_list[-1]]
    max_count=1
    for i in range(n):
        max_sub_seq = []
        for j in range(i):
            if num_list[j] < num_list[i] and len(front[j]) > len(max_sub_seq):
                max_sub_seq = front[j].copy() 
        front[i] = max_sub_seq + [num_list[i]]

        
    for i in range(n-2,-1,-1):
        max_sub_seq = []
        for k in range(n-1,i,-1):
            if num_list[k]<num_list[i] and len(back[k]) > len(max_sub_seq):
                max_sub_seq=back[k].copy()
        back[i]=max_sub_seq+[num_list[i]]

    for i in range(n):
        current_length=len(front[i])+ len(back[i])-1
        if current_length > max_count:
            max_count=current_length
    return max_count

n= int((input()))
num_list=list(map(int, input().split()))
print(bitonic_subseque(num_list, n))