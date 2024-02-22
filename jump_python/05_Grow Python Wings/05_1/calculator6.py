# 클래스의 상속
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

if __name__== '__main__':
    a= MoreFourCal(4,2)
    print(a.pow())
    print(a.add())

