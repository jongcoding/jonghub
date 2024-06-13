#Footb ball Scoring
T1,F1,S1,P1,C1=map(int, input().split())
T2,F2,S2,P2,C2=map(int, input().split())
result1=6*T1+F1*3+S1*2+P1*1+C1*2
result2=6*T2+F2*3+S2*2+P2*1+C2*2
print(result1, result2)