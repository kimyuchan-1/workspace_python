# 입력받은 수 보다 작은 홀수를 오름차순으로 나열하기

n = int(input('정수를 입력해주세요.：'))

for i in range(1, n + 1, 2):
    print(i, end=' ')
print()
