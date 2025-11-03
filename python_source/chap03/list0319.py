# 입력받은 달의 계절을 알아보기 4(집합 이용하기）

month = int(input('계절을 알아봅시다.\n몇 월입니까：'))

if month in {3, 4, 5}:
    print('봄입니다.')
elif month in {6, 7, 8}:
    print('여름입니다.')
elif month in {9, 10, 11}:
    print('가을입니다.')
elif month in {1, 2, 12}:
    print('겨울입니다.')
else:
    print('이상한 달이군요.')
