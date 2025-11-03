# 원의 둘레와 넓이 구하기 3(원주율에 math.pi를 이용）

from math import pi

r = float(input('반지름：'))

print('원의 둘레는', 2 * pi * r, '입니다.')
print('넓이는', pi * r * r, '입니다.')
