# 7장 정리

import random

MAX = 10
print('0～{} 사이의 난수를 생성합니다.'.format(MAX))
number = int(input('난수 개수：'))

# 요소 개수가 number이고 모든 요소가 None인 리스르 생성하기
v = [None] * number

# 모든 요소에 0 ~ MAX의 난수 대입하기
for i in range(number):
    v[i] = random.randint(0, MAX)

# 리스트로 출력하기
print(v)

# '*'으로 수직 막대 그래프로 출력하기
for i in range(MAX, 0, -1):
    for j in range(0, number):
        if v[j] >= i:
            print('*', end='')
        else:
            print(' ', end='')
    print()

print('-' * number)
for i in range(number):
    print(i % 10, end='')
