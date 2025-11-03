"""함수가 객체인지 확인"""

def min2(a, b):
    """a, b의 최솟값을 구해 리턴하는 함수"""
    return a if a < b else b

a = int(input('정수 a：'))
b = int(input('정수 b：'))

func = min2
print('최솟값은', func(a, b), '입니다.')

del min2
print('최솟값은', func(a, b), '입니다.')

del func
print('최솟값은', func(a, b), '입니다.')
