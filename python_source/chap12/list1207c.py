# 사용자 정의 예외(트레이스백 출력하기)

import traceback

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
        raise Exception

sw = int(input('sw：'))

try:
    func(sw)
except Exception as e:
    print('예외 포착')
    print(traceback.format_exc())  # 트레이스백을 출력
    print(type(e))


