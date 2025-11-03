# 직각 이등변 삼격형과 사각형 출력하기1(위치 인수)

def puts(n, s):
    """n개의 s를 연속해서 출력"""
    for _ in range(n):
        print(s, end='')

print('직각 이등변 삼격형')
n = int(input('짧은 변의 길이：'))

for i in range(1, n + 1):
    puts(i, '*')
    print()

print('사각형')
w = int(input('가로：'))
h = int(input('세로：'))

for i in range(1, h + 1):
    puts(w, '+')
    print()
