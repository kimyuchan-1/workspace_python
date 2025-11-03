# 리스트에 있는 세 값의 최댓값을 구하기

def max3(a, b, c):
    """a, b, c의 최댓값을 구해 리턴"""
    max = a
    if b > max: max = b
    if c > max: max = c
    return max

lst1 = [1, 3, 5]
m = max3(*lst1)
print(lst1, '의 최댓값은', m, '입니다.')
