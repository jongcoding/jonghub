hack={'A+':4.5,'A0':4,'B+':3.5,'B0':3,'C+':2.5,'C0':2,'D+':1.5,'D0':1.0,'F':0.0}
sub=0
n=20
subject=0
for i in range(20):
    a,b,c=map(str, input().split())
    if c=='P':
        pass
    elif c=='F':
        sub+=float(b)
    else:
        sub+=float(b)
        subject+=float(b)*hack[c]
if sub==0 or subject==0:
    print("0.000000")
else:
    print(subject/sub)

# 최적화 코드
hack = {'A+': 4.5, 'A0': 4, 'B+': 3.5, 'B0': 3, 'C+': 2.5, 'C0': 2, 'D+': 1.5, 'D0': 1.0, 'F': 0.0}
sub = 0
subject = 0

for _ in range(20):
    a, b, c = input().split()
    if c != 'P':
        sub += float(b)
        if c != 'F':
            subject += float(b) * hack[c]

if sub == 0:
    print("0.000000")
else:
    print(subject / sub)



