# 12장 정리2

class RangeException(Exception):
    """범위를 벗어난 예외"""
    pass

class ParameterRangeException(RangeException):
    """가인수의 범위를 벗어난 예외"""
    pass

class ResultException(RangeException):
    """리턴 값의 범위를 벗어난 예외"""
    pass

def is_valid(value:int) -> bool:
    """value는 0~9인가?"""
    return 0 <= value <= 9

def add(a: int, b: int) -> int:
    """a와 b의 합을 리턴

    사전 조건 : a와 b는 0~9
             충족하지 않은 경우 ParameterRangeException를 전송

    사후 조건 : 리턴하는 합은 0~9
             충족하지 않은 경우 ResultRangeException를 전송

    """
    if not is_valid(a):
        raise ParameterRangeException
    if not is_valid(b):
        raise ParameterRangeException

    result = a + b

    if not is_valid(result):
        raise ResultException
    return result

a = int(input('정수 a：'))
b = int(input('정수 b：'))

try:
    print('두 수의 합은 {}입니다.'.format(add(a, b)))
except ParameterRangeException:
    print('매개 변수가 범위를 벗어났습니다.')
except ResultException:
    print('리턴 값이 범위를 벗어났습니다.')
except:
    print('알 수 없는 예외가 발생하였습니다.')
finally:
    print('수고하셨습니다.')

