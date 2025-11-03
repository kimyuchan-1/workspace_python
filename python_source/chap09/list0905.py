# 두 수의 최댓값 구하기

def max2(a, b):
    """a와 b의 최댓값을 리턴"""
    if a > b:
        return a
    return b

n1 = int(input('정수 n1：'))
n2 = int(input('정수 n2：'))

print('최댓값은', max2(n1, n2), '입니다.')
