# 오른쪽 하단이 직각인 이등변 삼각형 그리기

print('오른쪽 하단이 직각인 이등변 삼각형')
n = int(input('짧은 변의 길이：'))


for i in range(n):
    for _ in range(n - i - 1):
        print(' ', end=' ')
    for _ in range(i + 1):
        print('*', end='')
    print()
