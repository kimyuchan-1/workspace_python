# 입력받은 달의 계절을 알아보기 3(비교 연산자를 연속해서 사용하기）

month = int(input('계절을 알아봅시다.\n몇 월입니까：'))

if 3 <= month <= 5:
    print('봄입니다.')
elif 6 <= month <= 8:
    print('여름입니다.')
elif 9 <= month <= 11:
    print('가을입니다.')
elif month == 12 or month == 1 or month == 2:
    print('겨울입니다.')
else:
    print('이상한 달이군요.')
