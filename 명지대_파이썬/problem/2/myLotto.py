import random
# 전역 변수
winnum=set()

# 로또 5장 구매
def buyautolotto():
    lotto=[set(random.sample(range(1,46), 6)) for _ in range(5)]
    return lotto

# 로또 출력
def printlotto(lotto):
    for index, value in enumerate(lotto):
        rank=chr(ord("A")+index)
        print(f"{rank} 자동", end=" ")
        printnums(value)
    print()
def setwinlotto():
    global winnum
    winnum=set(random.sample(range(1,46),6))

def getwinner(lotto):
    for index, value in enumerate(lotto):
        rank=chr(ord("A")+index)
        new_set=value&winnum
        count=len(new_set)
        print(f"{rank} 당첨범호 {count}개:",end=" ")
        if count==0:
            print("꽝")
        else:
            printnums(new_set)
def printnums(nums):
    nums=list(nums)
    nums.sort()
    print(" ".join(map(str, nums)))
