def count(cmd):
    a={'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    return sum(1 for char in cmd if char in a)
while True:
    cmd=input()
    if cmd=="#":
        break
    print(count(cmd))