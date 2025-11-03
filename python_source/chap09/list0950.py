# 80점 이상의 점수만 추출하기

import random

number = int(input('학생 수 : '))

score = [None] * number

for i in range(number):
    score[i] = random.randint(0, 100)

print('모든 학생 점수＝', score)
print('합격자 점수', list(filter(lambda n: n >= 80, score)))
