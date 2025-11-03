# 다섯 명의 점수를 입력받아 총점과 평균을 출력하기

print('다섯 명 점수의 총점과 평균을 구하겠습니다.')

score1 = int(input('1번의 점수 :'))
score2 = int(input('2번의 점수 :'))
score3 = int(input('3번의 점수 :'))
score4 = int(input('4번의 점수 :'))
score5 = int(input('5번의 점수 :'))

total = 0
total += score1
total += score2
total += score3
total += score4
total += score5

print('총점은 {}점입니다.'.format(total))
print('평균은 {}점입니다.'.format(total / 5))
