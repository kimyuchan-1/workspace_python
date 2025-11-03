# 행렬의 합 구하기(행수/열수/값 입력받기)

print('행렬의 합을 구해봅시다.')
height = int(input('행수:'))
width  = int(input('열수:'))

a = [None] * height
for i in range(height):
    a[i] = [None] * width
    for j in range(width):
        a[i][j] = int(input('a[{}][{}] : '.format(i, j)))

b = [None] * height
for i in range(height):
    b[i] = [None] * width
    for j in range(width):
        b[i][j] = int(input('b[{}][{}] : '.format(i, j)))

c = [None] * height
for i in range(height):
    c[i] = [None] * width
    for j in range(width):
        c[i][j] = a[i][j] + b[i][j]

for i in range(height):
    for j in range(width):
        print('c[{}][{}] = {}'.format(i, j, c[i][j]))
