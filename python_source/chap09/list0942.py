"""함수의 타입과 아이덴티티를 출력"""

def min2(a, b):
    """a, b의 최솟값을 구해 리턴하는 함수"""
    return a if a < b else b

func = min2

print('type(min2), id(min2) = ', type(min2), id(min2))
print('type(func), id(func) = ', type(func), id(func))
