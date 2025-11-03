# 직각 이등변 삼각형

print('직각 이등변 삼각형')

n = int(input('짧은 변의 길이：'))

for i in range(1, n + 1):
    for _ in range(i):
        print('*', end='')
    print()
