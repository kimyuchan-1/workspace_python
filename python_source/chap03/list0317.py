# 입력받은 달의 계절을 알아보기 2(겨울 판정 조건을 여러 행에 나열하기）

month = int(input('계절을 알아봅시다.\n몇 월입니까：'))

if month >= 3 and month <= 5:
    print('봄입니다.')
elif month >= 6 and month <= 8:
    print('여름입니다.')
elif month >= 9 and month <= 11:
    print('가을입니다.')
elif (month == 1 or     #  1월은 겨울
      month == 2 or     #  2월도 겨울
      month == 12       # 12월도 겨울
     ):
    print('겨울입니다.')
else:
    print('\a이상한 달이군요.')
