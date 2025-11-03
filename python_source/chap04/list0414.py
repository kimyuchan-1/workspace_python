# 입력받은 수의 약수를 오름차순으로 나열하기

n = int(input('정수를 입력해주세요.：'))

for i in range(1, n + 1):
    if n % i == 0:
        print(i, end=' ')
print()
