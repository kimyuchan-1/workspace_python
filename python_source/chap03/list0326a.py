# 작은 값과 큰 값 구하기 3

a = int(input('정수 a：'))
b = int(input('정수 b：'))

if a < b: min2 = a; max2 = b;
else: min2 = b; max2 = a;

print('작은 값은', min2, '입니다.')
print('큰 값은', max2, '입니다.')
