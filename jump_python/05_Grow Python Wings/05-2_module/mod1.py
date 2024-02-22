def add(a,b):
    return a+b
def sub(a,b):
    return a-b

# print(add(1,4))  mod1.py이 실해되면 자동으로 실행됨
# if __name__=="__main__" 의미
# 다른 파일에서 모듈을 불러 사용할 때는 거짓이 되어 수행되지 않음
if __name__=="__main__":
    print(add(1,4))
    print(add(4,2))
    