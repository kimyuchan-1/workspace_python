# 가위 바위 보

import random

print('가위 바위 보')

# 이긴 횟수, 진 횟수, 비긴 횟수
win_no = lose_no = draw_no = 0

while True:
    comp = random.randint(0, 2)

    while True:
        human = int(input('가위바위보(0：바위／1：가위／2: 보）：'))
        if 0 <= human <= 2:
            break

    print('나는 ', end='')
    if comp == 0:
        print('주먹', end='')
    elif comp == 1:
        print('가위', end='')
    else:
        print('보', end='')
    print('입니다.')

    # 승패 판정
    judge = (human - comp + 3) % 3

    if judge == 0:
        print('비겼습니다.')
        draw_no += 1
    elif judge == 1:
        print('당신이 졌습니다.')
        lose_no += 1
    else:
        print('당신이 이겼습니다.')
        win_no += 1

    retry = int(input('한 번 더 해볼까요?(0：네／1：아니오)：'))
    if retry == 1:
        break

print('결과 :', win_no, '승', draw_no, '무', lose_no, '패입니다.')
