# 1부터 n까지 합 구하기（n에 양의 정수만 입력받기）

print('1부터 n까지의 합을 구해보겠습니다.')

while True:
    n = int(input('n의 값을 입력해 주세요：'))
    if n > 0:
        break

sum = 0
i = 1
while i <= n:
    sum += i   # sum에 i를 더하기
    i += 1     # i에 1을 더하기
print('1부터', n, '까지의 합은', sum, '입니다.')
