# 1부터 n까지 합 구하기

print('1부터 n까지의 합을 구해보겠습니다.')
n = int(input('n의 값을 입력해 주세요：'))

sum = 0
i = 1
while i <= n:
    sum += i   # sum에 i를 더하기
    i += 1     # i에 1을 더하기
print('1부터', n, '까지의 합은', sum, '입니다.')
