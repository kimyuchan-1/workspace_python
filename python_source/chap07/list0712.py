# 학생 수 없이 점수만 입력받아 총점과 평균 구하기

print('총점과 평균을 구해봅시다.')
print('"End"를 입력하면 종료됩니다.')

number = 0
score = []                  # 빈 리스트

while True:
    s = input('{}번 학생의 점수：'.format(number + 1))
    if s == 'End':
        break
    score.append(int(s))    # 마지막에 추가
    number += 1

total = sum(score)

print('총점은 {}점입니다.'.format(total))
print('평균은 {}점입니다.'.format(total / number))


