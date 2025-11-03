# 두 정수를 입력받아 곱셈과 나눗셈 연산하기(예외 처리4)

try:
    a = int(input('정수 a：'))
    b = int(input('정수 b：'))

    print('a * b는', a * b, '입니다.')
    print('a / b는', a / b, '입니다.')

except ValueError:
    print('정수로 인식할 수 없습니다!')

except ZeroDivisionError:
    print('0으로 나누기!')

except:
    print('예외 발생!')


else:
    print('성공!')

finally:
    print('수고하셨습니다.')

	
