# 리스트의 요소 값 변경하기

def change(lst, idx, val):
    """lst[idx]의 값을 val으로 변경"""
    lst[idx] = val

x = [11, 22, 33, 44, 55]
print('x =', x)

index = int(input('변경할 값의 인덱스：'))
value = int(input('새로운 값 : '))

change(x, index, value)
print('x =', x)
