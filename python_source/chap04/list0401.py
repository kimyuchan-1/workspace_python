# 정수의 카운트업(정렬 후 a부터 b까지)

a = int(input('정수 a：'))
b = int(input('정수 b：'))

a, b = sorted([a, b])       # 오름차순으로 정렬

counter = a
while counter <= b:
    print(counter, end=' ')
    counter = counter + 1   # counter를 1만큼 증가
print()
