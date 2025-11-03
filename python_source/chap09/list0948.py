# 리스트의 모든 요소를 두배로 만들기(함수)

def double(n):
    return 2 * n

x = [1, 2, 3, 4]
y = map(double, x)

print(list(y))
