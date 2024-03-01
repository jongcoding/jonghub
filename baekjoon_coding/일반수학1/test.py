def rotate(arr, start, end):
    # 구간을 뒤집음
    arr[start:end + 1] = [-x for x in reversed(arr[start:end + 1])]

def find_largest_consecutive_range(arr):
    # 연속된 숫자가 가장 많이 나오는 구간을 찾음
    max_length = 0
    max_start = -1
    max=0
    
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
           
            if arr[i]==abs(arr[i]-arr[j])-1:
                imp = list(arr)
                rotate(imp,i,j)
                num=0
                for p in range(len(imp)-1):
                    if arr[p] ==abs(imp[p+1]-imp[p])-1:
                        num+=1
                if max<num:
                    max_start=i
                    max_length=j-i
                    max=num
    return max_start, max_start + max_length - 1

def restore_initial_array(final_arr):
    N = len(final_arr)
    initial_arr = list(range(1, N + 1))  # 초기 배열 생성
    rotations = []  # 회전 연산 기록을 저장할 리스트
    start_n=end_n=0

    while initial_arr != final_arr:
        # 초기 배열이나 최종 배열의 첫 번째 숫자와 마지막 숫자가 제자리에 있는 경우, 해당 구간을 선택하지 않음
        if initial_arr[0] == final_arr[0]:
            final_arr.pop(0)
            initial_arr.pop(0)
            start_n+=1
            continue
        elif initial_arr[-1] == final_arr[-1]:
            final_arr.pop()
            initial_arr.pop()
            end_n+=1
            continue

        # 가능한 모든 구간을 탐색하면서, 연속된 숫자가 가장 많이 나오는 구간을 선택
        start, end = find_largest_consecutive_range(initial_arr)
        
        # 회전 연산을 수행하여 최종 배열에 도달할 수 있도록 함
        rotate(initial_arr, start, end)
        rotations.append((start + 1+start_n, end + 1+end_n))  # 회전 연산 기록

    return rotations

# 주어진 최종 배열
final_array = [-4, -3, -5, 1, 2, 6]

rotations = restore_initial_array(final_array)

print("회전 연산 수행:")
for rotation in rotations:
    print(f"{rotation[0]}부터 {rotation[1]}까지 회전")
