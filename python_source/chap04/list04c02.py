# 1 ~ 12 중에서 8을 생략하고 반복하기 1

for i in range(1, 13):
    if i == 8:
        continue
    print(i, end=' ')
print()
