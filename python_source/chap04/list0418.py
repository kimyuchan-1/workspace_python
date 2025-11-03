# 사각형 그리기

print('사각형')
h = int(input('높이：'))
w = int(input('넓이：'))

for i in range(h):
    for j in range(w):
        print('*', end='')
    print()
