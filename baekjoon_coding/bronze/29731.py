n=int(input())
hellp=['Never gonna give you up',
'Never gonna let you down',
'Never gonna run around and desert you',
'Never gonna make you cry',
'Never gonna say goodbye',
'Never gonna tell a lie and hurt you',
'Never gonna stop']

for i in range(n):
    cmd=input()
    if cmd not in hellp:
        print("Yes")
        exit()
print("No")