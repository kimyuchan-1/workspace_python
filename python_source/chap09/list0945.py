"""두 수의 합을 구하는 람다식"""

a = int(input('정수 a：'))
b = int(input('정수 b：'))

add2 = lambda x, y: x + y
print('a와 b의 합은', add2(a, b), '입니다.')
