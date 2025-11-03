# 정수의 카운트업

start = int(input('시작할 숫자：'))
end = int(input('종료할 숫자：'))
step = int(input('간격：'))

for count in range(start, end, step):
    print(count, end=' ')
print()
