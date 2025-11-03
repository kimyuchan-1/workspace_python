# 네 개의 정수를 오름차순으로 정렬하기 (sorted 함수)

a = int(input('정수 a：'))
b = int(input('정수 b：'))
c = int(input('정수 c：'))
d = int(input('정수 d：'))

a, b, c, d = sorted([a, b, c, d])   # 네 개의 값을 오름차순으로 정렬

print('a≦b≦c≦d로 정렬했습니다.')
print('정수 a의 값은', a, '입니다.')
print('정수 b의 값은', b, '입니다.')
print('정수 c의 값은', c, '입니다.')
print('정수 d의 값은', d, '입니다.')