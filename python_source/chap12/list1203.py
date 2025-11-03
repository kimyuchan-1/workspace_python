# 두 정수를 입력받아 곱셈과 나눗셈 연산하기(예외 처리2)

try:
    a = int(input('정수 a：'))
    b = int(input('정수 b：'))

    print('a * b는', a * b, '입니다.')
    print('a / b는', a / b, '입니다.')

except (ValueError, ZeroDivisionError):
    print('0으로 나누었거나 확인할 수 없습니다!')

else:
    print('성공!')

finally:
    print('수고하셨습니다.')
