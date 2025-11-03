# 두 정수 중 작은 값 출력하기 2(조건 연산자）

a = int(input('정수 a：'))
b = int(input('정수 b：'))

min2 = a if a < b else b

print('작은 값은', min2, '입니다.')
