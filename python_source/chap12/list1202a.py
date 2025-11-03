# 두 정수를 입력받아 곱셈과 나눗셈 연산하기(try-finally문)

try:
    a = int(input('정수 a：'))
    b = int(input('정수 b：'))

    print('a * b는', a * b, '입니다.')
    print('a / b는', a / b, '입니다.')
	
finally:
    print('수고하셨습니다.')
