# myLotto.py
import random

winnum = set()

def buyautolotto():
    lotto = [set(random.sample(range(1, 46), 6)) for _ in range(5)]
    printlotto(lotto)
    print()
    return lotto

def printlotto(lotto):
    for a, b in enumerate(lotto):
        print(f'{chr(a + ord("A"))} 자동', end=" ")
        printnums(b)
        
def setwinlotto():
    global winnum
    winnum = set(random.sample(range(1, 46), 6))

def getwinner(lotto):
    for idx, numbers in enumerate(lotto):
        matched = len(numbers & winnum)
        print(f"{chr(ord('A') + idx)} : 당첨번호 {matched} 개: ", end="")
        printnums(numbers & winnum)

def printnums(nums):
    print(" ".join(map(str, sorted(nums))))


