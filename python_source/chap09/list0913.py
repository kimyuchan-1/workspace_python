# 리스트 요소의 순서를 반전하기

def reverse_list(lst):
    """lst의 요소 순서를 반전"""
    n = len(lst)
    for i in range(n // 2):
        lst[i], lst[n - i - 1] = lst[n - i - 1], lst[i]

x = [22, 57, 11, 32, 91, 68, 77]
print('x =', x)

reverse_list(x)
print('x =', x)
