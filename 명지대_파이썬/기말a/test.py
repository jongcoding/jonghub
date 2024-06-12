import datetime
import random
myToday={}
seats=[x for x in range(1,11)]
myTodayCount=0
def Nowtime():
    crt_time=datetime.datetime.now()
    year=crt_time.year
    month=crt_time.month
    day=crt_time.day
    hour=crt_time.hour
    minute=crt_time.minute
    second=crt_time.second
    return str(f"{year:04}년 {month:02}월 {day:02}일 {hour:02}시 {minute:02}분 {second}초")
def show():
    print("Daily Helpher 내역을 출력합니다.")
    for index, key in enumerate(myToday.keys(),start=1):
        STR=str(myToday[key])[2:len(myToday[key])-3]
        print(f"{index}. {key}: {STR}")

def myLotto():
    Num=random.sample(range(1,46),6)
    Num.sort()
    print(Num)
    myToday[Nowtime()]={f"오늘의 로또 번호: {Num[0]:02} {Num[1]:02} {Num[2]:02} {Num[3]:02} {Num[4]:02} {Num[5]:02}"}
def myCalc(expression):
    myToday[Nowtime()]={f"계산결과: {expression} = {eval(expression)}"}
def myMovie(movie, ticket):
    SelectSeat=random.randrange(10)
    ReserveSeat=[]
    NoEmptySeat=0
    while 1:
        if seats[SelectSeat] !=-1:
            seats[SelectSeat] ==-1
            ReserveSeat.append(SelectSeat+1)
            SelectSeat +=1
            if SelectSeat >9:
                SelectSeat=0
        else:
            SelectSeat+=1
            if SelectSeat > 9:
                SelectSeat=0
        if len(ReserveSeat) == ticket:
            break
        for x in seats:
            if seats != -1:
                break
            else:
                NoEmptySeat =1
    if NoEmptySeat==0:
        seatSTR=str(ReserveSeat[0])
        for i in range(1, ticket):
            seatSTR =seatSTR+' '+str(ReserveSeat[i])
        myToday[Nowtime()]= {f"영화 예매: {movie} {ticket}장 좌석번호 {seatSTR}"}
    else:
        myToday[Nowtime()]={f"영화 예매: {movie} {ticket}장 좌석이 부족합니다."}

