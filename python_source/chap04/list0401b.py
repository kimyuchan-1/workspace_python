# 정수의 카운트업(하나 건너 카운트업）

a = int(input('정수 a：'))
b = int(input('정수 b：'))

a, b = sorted([a, b])       # 오름차순으로 정렬

counter = a
while counter <= b:
    print(counter, end=' ')
    counter = counter + 2   # counter를 2만큼 증가
print('\ncounter의 값은 ', counter, '입니다.')
