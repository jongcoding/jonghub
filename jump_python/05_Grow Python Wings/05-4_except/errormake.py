class Myerror(Exception):
    def __str__(self):
        return "허용되지 않는 별명입니다."
    pass
def say_nick(nick):
    if nick=="바보":
        raise Myerror()
    print(nick)
try:
    say_nick("천사")
    say_nick("바보")
except Myerror as e:
#    print("허용되지 않는 별명입니다.")
    print(e)

