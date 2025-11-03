# 전달된 시점의 매개 변수가 인수 그 자체인 점을 확인하기

def func(n):
    """매개 변수의 값과 아이덴티티 출력"""
    print('n：', n, id(n))
    n = 0
    print('n：', n, id(n))

x = 5
print('x：', x, id(x))
func(x)
print('x：', x, id(x))
