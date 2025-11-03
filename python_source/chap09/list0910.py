# 1부터 n까지의 합 구하기

def sum_1ton(n):
    """1부터 n까지의 합 구하기"""
    s = 0
    while n > 0:
        s += n
        n -= 1
    return s

x = int(input('x의 값：'))
total = sum_1ton(x)
print('1부터 ', x, '까지의 합은 ', total, '입니다.', sep='')
