# 작은 값과 큰 값 구하기 4(조건 연산자)

a = int(input('정수 a：'))
b = int(input('정수 b：'))

min2, max2 = (a, b) if a < b else (b, a)

print('작은 값은', min2, '입니다.')
print('큰 값은', max2, '입니다.')
