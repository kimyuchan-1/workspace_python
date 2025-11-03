"""특정 해의 일수 구하기"""

def is_leapyear(year: int) -> bool:
    """서기 year년은 윤년인지 알아보기"""
    return y % 4 == 0 and y % 100 != 0 or y % 400 == 0

print('특정 해의 일수를 구합니다.')
y = int(input('구할 년도：'))
print('그 해는 {}일입니다.'.format(365 + is_leapyear(y)))
