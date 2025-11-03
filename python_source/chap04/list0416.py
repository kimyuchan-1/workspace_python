# 10～99 사이의 난수 n개 생성하기

import random

n = int(input('몇 개의 난수를 만들까요?：'))

for _ in range(n):
    r = random.randint(10, 99)
    if (r == 13):
        print('\n갑작스런 이유로 중지되었습니다.')
        break
    print(r, end=' ')
else:
    print('\n난수 생성을 종료합니다.')
