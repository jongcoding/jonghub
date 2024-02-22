# 메서드 오버라이딩
class FourCal:
    def __init__(self, first, second):
        self. first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result= self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result

class MoreFourCal(FourCal): # 클래스의 상속
    def pow(self):
        result=self.first ** self.second
        return result
class safeFourCal(FourCal):
    def div(self):    # 메서드 오버라이딩
        if self.second == 0:
            return 0
        else:
            return self.first / self.second
if __name__== '__main__':
    a= MoreFourCal(4,2)
    print(a.pow())
    print(a.add())