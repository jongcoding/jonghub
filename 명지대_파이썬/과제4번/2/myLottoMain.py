import myLotto as mlt
lotto = mlt.buyautolotto() # 로또 번호표 구하기

mlt.setwinlotto() # 당첨 번호 선정
print("당첨번호:", end=" ")
mlt.printnums(mlt.winnum) # 당첨 번호 출력
print()
mlt.getwinner(lotto)