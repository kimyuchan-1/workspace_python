# 산술 연산을 위한 내장 함수의 사용

x = float(input('실수x：'))
y = float(input('실수y：'))
z = float(input('실수z：'))

print('abs(x)       = ', abs(x))
print('bool(x)      = ', bool(x))
print('divmod(x, y) = ', divmod(x, y))
print('max(x, y)    = ', max(x, y))
print('min(x, y)    = ', min(x, y))
print('pow(x, y)    = ', pow(x, y))
print('round(x, 2)  = ', round(x, 2))
print('round(x, 3)  = ', round(x, 3))
print('sum(x, y, z) = ', sum((x, y, z)))
