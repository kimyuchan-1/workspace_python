"""min_max 모듈의 함수 호출하기"""

import min_max

x = float(input('실수 x：'))
y = float(input('실수 y：'))
z = float(input('실수 z：'))

print('x와 y의 최솟값은 {}이고, 최댓값은 {}입니다.'.format(*min_max.min_max2(x, y)))
print('y와 z의 최솟값은 {}이고, 최댓값은 {}입니다.'.format(*min_max.min_max2(y, z)))
print('x와 z의 최솟값은 {}이고, 최댓값은 {}입니다.'.format(*min_max.min_max2(x, z)))
print('x, y, z의 최솟값은 {}이고, 최댓값은 {}입니다.'.format(*min_max.min_max3(x, y, z)))

