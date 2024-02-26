#05-1 클래스
# 클래스는 왜 필요한가?
# 계산기 프로그램을 만들어 클래스 알아보기

# 클래스와 객체

# 객체와 인스턴스의 차이
# 클래스로 만든 객체를 "인스턴스"라고 부름 a= cookie() 로 만든 a는 cookie의 인스턴스이다.

# 클래스를 어떻게 만들지 먼저 구상하기

#클래스 구조 만들기

# 객체에 연산할 숫자 지정하기

# 클래스 안에 구현된 함수= 매서드(method)

# 매서드를 호출하는 또 다른 방법

# a= FourCal()
# FourCal.setdata(a, 4, 2)

# a= FourCal()
# a.setdata
# ->  위와 같이 '클래스명.매서드' 형태로 호출할 때는 객체 a를 첫 번째 매겨변수 self에 꼭 전달해야 한다. 반면 다음처럼 '객체.메서드' 형태로 호출할 때는 self를 반드시 생략해서 호출

# 생성자
# 객체에 first, second 와 같은 초기값을 설정해야할 필요가 있을 때 setdata와 같은 매서드를 호출하여 초기값을 설정하기보다는 생성자를 구현하는 것이 안전한 방법
# 생성자란= 객체가 생성될 떄 자동으로 호출되는 매서드를 의미
# __init__를 사용하면 매서드는 자동으로 생성자가 된다.

# 클래스의 상속
# 어떤 클래스를 만들 때 다른 클래스의 기능을 물려받을 수 있게 만드는 것

# 매서드 오바라이딩
# 부모 클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것이라고 한다.

# 클래스 변수 
# 객체 변수는 다른 객체의 영향을 받지 않고 독립적으로 그 값을 유지한다.
# 하지만 클래스변수는 클래스로 만든 모든 객체에 공유된다.

# class Family:
#       lastname = "김"
# Family.lastname   -> 클래스_이름.클래스변수