# 직각 이등변 삼각형과 사각형

def put_star(n):
    """n개의 '*'을 연속해서 출력"""
    for _ in range(n):
        print('*', end='')

print('직각 이등변 삼각형')
n = int(input('짧은 변의 길이：'))

for i in range(1, n + 1):
    put_star(i)
    print()

print('사각형')
w = int(input('가로：'))
h = int(input('세로：'))

for i in range(1, h + 1):
    put_star(w)
    print()
