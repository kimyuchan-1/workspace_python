# 하위 4 비트를 마스크/세트/반전하기

a = int(input('0～255의 정수：'))

print('2진수 = {:08b}'.format(a))
print('마스크 = {:08b}'.format(a & 0b11110000))
print('세트 = {:08b}'.format(a | 0b00001111))
print('반전   = {:08b}'.format(a ^ 0b00001111))
