try:
    f = open("나없는 파일", 'r')
except FileNotFoundError:
    pass