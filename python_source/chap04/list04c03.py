# 1 ~ 12 중에서 8을 생략하고 반복하기 2

for i in list(range(1, 8)) + list(range(9, 13)):
    print(i, end=' ')
print()
