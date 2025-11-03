# 사용자 정의 예외(raise로 발생시키지 않기)

class MyException(Exception):
    """내가 만든 예외"""
    pass

def raise_my_exception() -> None:
    raise MyException

def func(sw: int) -> None:
    try:
        if sw == 0:
            raise_my_exception()
    except MyException as e:
        print('내가 만든 예외를 포착')
        # 내가 만든 예외에 대한 처리를 시도한다.
        # 복구할 수 없다고 판단.
        print('복구할 수 없습니다.')
        # raise를 실행하지 않는다.

sw = int(input('sw：'))

try:
    func(sw)
except Exception as e:
    print('예외 포착!')
    print(type(e))


