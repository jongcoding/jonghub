def W(a,b,c, memo={}):
    if (a,b,c) in memo: return memo[(a,b,c)]
    if a<=0 or b<=0 or c<=0:
        return 1
    if a>20 or b>20 or c>20:
        return W(20,20,20, memo)
    if a<b and b<c:
         memo[(a, b, c)] = W(a, b, c-1, memo) + W(a, b-1, c-1, memo) - W(a, b-1, c, memo)
    else:
        memo[(a, b, c)] = W(a-1, b, c, memo) + W(a-1, b-1, c, memo) + W(a-1, b, c-1, memo) - W(a-1, b-1, c-1, memo)
    return memo[(a,b,c)]
    

while True:
    a,b,c= map(int, input().split())
    if a==b==c==-1:
        exit()
    result=W(a,b,c, memo={})
    print(f"w({a}, {b}, {c}) = {result}")