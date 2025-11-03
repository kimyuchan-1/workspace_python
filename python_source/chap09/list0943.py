"""하나의 이름으로 두 함수 호출하기"""

def mul2(x, y):
    return x * y

def add2(x, y):
    return x + y

a = int(input('정수 a：'))
b = int(input('정수 b：'))

func = mul2
print('a와 b의 곱은', func(a, b), '입니다.')

func = add2
print('a와 b의 합은', func(a, b), '입니다.')
