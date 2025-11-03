# 4장 정리

while True:
    n = int(input('0～100 사이의 정수：'))
    if 0 <= n <= 100:
        break
c = n

# '*'을 c개 출력하기
while n > 0:
    print('*', end='')
    n -= 1
print()

# '1234567890'을 반복하여 출력총 c회）
for i in range(1, c + 1):
    print(i % 10, end='')
print('\n')

# 넓이가 s이고, 세로와 가로가 정수인 사각형의 변의 길이
s = int(input('넓이：'))
print('넓이가 {}(이)고, 세로와 길이가 정수인 '
      '사각형의 변의 길이'.format(s))
for i in range(1, s + 1):
    if i * i > s: break
    if s % i: continue
    print('{}×{}'.format(i, s // i))
print()

# n개의 '*'을 w째 마다 개행하면서 출력하기
n = int(input('*을 총 몇 개 출력할까요：'))
w = int(input('몇 번째마다 개행할까요：'))
for i in range(1, n + 1):
    print('*', end='')
    if i % w == 0:
        print()
if n % w != 1:
    print()
print()

# 숫자로 사각형 그리기
h = int(input('가로：'))
w = int(input('세로：'))
for i in range(1, h + 1):
    for j in range(1, w + 1):
        print((i + j - 1) % 10, end='')
    print()
