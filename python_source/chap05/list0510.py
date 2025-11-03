# 정수를 좌우로 시프트한 값을 10진수로 출력하기

x = int(input('정수：'))
n = int(input('시프트할 비트 수：'))

print('x << n = {:d}'.format(x << n))
print('x >> n = {:d}'.format(x >> n))
