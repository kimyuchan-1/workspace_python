# 숫자 맞추기 게임

import random

MAX = 1000                  # 고를 수 있는 가장 큰 수
MAX_STAGE = 10              # 입력 할 수 있는 기회
print('1부터 {}까지의 숫자 중 맞춰보세요. 기회는 {}회입니다.'.format(MAX, MAX_STAGE))

stage = 1
answer = random.randint(1, MAX)

while stage <= MAX_STAGE:
    print(stage, '번 시도 몇일까요?：', end='')
    n = int(input())

    if n < 1 or n > MAX:    # 범위 외의 값이 들어오면 다시 시작
        continue

    if n == answer:         # 정답일 때
        print('정답!', stage, '번 째에 맞췄습니다!')
        break
    elif n > answer:
        print('더 작은 수입니다.')
    else:
        print('더 큰 수입니다.')

    stage += 1

else:
    print('앗, 아쉽네요. 정답은', answer, '입니다.')
