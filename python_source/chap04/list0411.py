# for문으로 정수 세기 (오름차순으로 정렬된 a 부터 b까지）

a = int(input('정수 a：'))
b = int(input('정수 b：'))

a, b = sorted([a, b])       # 오름차순 정렬

for counter in range(a, b + 1):
    print(counter, end=' ')
print()
