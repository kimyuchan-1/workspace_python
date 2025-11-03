"""두 수의 합을 구하는 람다식2"""

a = int(input('정수 a：'))
b = int(input('정수 b：'))
print('a와 b의 합은', (lambda x, y: x + y)(a, b), '입니다.')
