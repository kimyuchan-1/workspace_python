"""min_max2모듈의 min_max2함수 호출하기"""

import min_max2

x = float(input('실수 x：'))
y = float(input('실수 y：'))

mini, maxi = min_max2.min_max2(x, y)
print('최솟값은', mini, '입니다.')
print('최댓값은', maxi, '입니다.')
