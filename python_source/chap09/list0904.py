# 세 수의 최댓값 구하기

def max3(a, b, c):
    """a, b, c 중 최댓값을 리턴"""
    max = a
    if b > max: max = b
    if c > max: max = c
    return max

n1 = int(input('정수 n1：'))
n2 = int(input('정수 n2：'))
n3 = int(input('정수 n3：'))

print('최댓값은', max3(n1, n2, n3), '입니다.')

x1 = float(input('실수 x1：'))
x2 = float(input('실수 x2：'))
x3 = float(input('실수 x3：'))

print('최댓값은', max3(x1, x2, x3), '입니다.')

print('n1, n2, x1의 최댓값은', max3(n1, n2, x1), '입니다.')
