# 암산 연습(세 자리 정수 세 개 더하기)

import random

def confirm_retry():
    """한 번 더 시도할지 확인"""
    while True:
        n = int(input('한 번 더？<Yes…1／No…0>：'))
        if n == 0 or n == 1:
            return n

print('암산 연습 시작')

while True:
    x = random.randint(100, 999)
    y = random.randint(100, 999)
    z = random.randint(100, 999)

    while True:
        print(x, '+', y, '+', z, '= ', end='')
        k = int(input())
        if k == x + y + z:
            break
        print('틀렸습니다.')

    if not confirm_retry():
        break
