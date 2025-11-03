# 사각형

print('사각형')
w = int(input('가로：'))
h = int(input('세로：'))

for i in range(1, h + 1):
    for _ in range(w):
        print('*', end='')
    print()
