a=input()
reword=0.0
if 'A' in a:
    reword=4.0
elif 'B' in a:
    reword=3.0
elif 'C' in a:
    reword=2.0
elif 'D' in a:
    reword=1.0

if '+' in a:
    reword+=0.3
elif '-' in a:
    reword-=0.3
print(reword)

