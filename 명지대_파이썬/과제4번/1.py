singer = ['BTS', '볼빨간사춘기', 'BTS', '블랙핑크', '뉴진스']
song = ['작은 것들을 위한 시', '나만 봄', '소우주', 'Kill This Love', '슈퍼 샤이']
kpop=list(zip(singer,song))
print("kpop =")
print(kpop)
print()
kpchart=dict()
for a,b in enumerate(kpop):
    kpchart[a]=b
print("kpchart =")
for i in kpchart:
    print(f'{i+1}: singer={kpchart[i][0]}, song={kpchart[i][1]}')