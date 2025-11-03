# 정수를 좌우 시프트하여 2진수로 출력하기

x = int(input('정수：'))
n = int(input('시프트할 비트 수：'))

print('x      = {:b}'.format(x))
print('x << n = {:b}'.format(x << n))
print('x >> n = {:b}'.format(x >> n))
