class Calulator:
    def __init__(self):  
        self.result=0
    def add(self, num):
        self.result +=num
        return self.result

cal1=Calulator()
cal2=Calulator()

print(cal1.add(3))
print(cal1.add(4))
print(cal2.add(3))
print(cal2.add(7))