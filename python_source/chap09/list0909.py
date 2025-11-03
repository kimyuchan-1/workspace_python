# 양의 정수의 계승 값 구하기

def factorial(n):
    """n!(n은 양의 정수)의 값을 재귀적으로 구하기"""
    if n > 0:
        return n * factorial(n - 1)
    else:
        return 1

n = int(input('양의 정수를 입력해주세요.：'))
print(n,'!의 값은 ', factorial(n), '입니다.', sep='')
