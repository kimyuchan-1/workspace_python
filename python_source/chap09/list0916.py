# 직각 이등변 삼격형과 사각형 출력하기2(키워드 인수)

# n개의 s를 연속해서 출력
def puts(n, s):
    for i in range(n):
        print(s, end='')

print('직각 이등변 삼각형')
n = int(input('짧은 변의 길이：'))

for i in range(1, n + 1):
    puts(n = i, s = '*')
    print()

print('사각형')
w = int(input('가로：'))
h = int(input('세로：'))

for i in range(1, h + 1):
    puts(s = '+', n = w)
    print()
