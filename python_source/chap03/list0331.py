# 두 개의 정수를 오름차순으로 정렬하기 2

a = int(input('정수 a：'))
b = int(input('정수 b：'))

if a > b:
    a, b = b, a

print('a≦b로 정렬했습니다.')
print('정수 a의 값은', a, '입니다.')
print('정수 b의 값은', b, '입니다.')
