S = list(input())
al= list(chr(i) for i in range(ord('a'),ord('z')+1))
t= [-1]*26
for i in range(len(S)):
    for P in range(26):
        if al[P] == S[i]:
            if t[P]==-1:
                t[P]=i
print(' '.join(map(str, t)))