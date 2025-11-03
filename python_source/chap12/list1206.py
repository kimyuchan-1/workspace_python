# raise문으로 예외 발생시키기

def func(sw: int) -> None:
    if sw == 0:
        raise ValueError
    elif sw == 1:
        raise ZeroDivisionError

sw = int(input('sw：'))

try:
    func(sw)

except BaseException as e:
    print('예외 포착!')
    print(type(e))
