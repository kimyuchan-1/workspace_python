# a가 b로 나누어 떨어지는지 알아보기

a = int(input('정수 a：'))
b = int(input('정수 b：'))

c = b != 0 and a % b
print(c, end='…')

if c:
    print('a는 b로 나누어 떨어지지 않습니다.')
else:
    print('b는 0이거나, a는 b로 나누어 떨어집니다.')
