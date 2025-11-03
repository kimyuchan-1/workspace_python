# 9장 정리

def range_of(*v):
    """최댓값과 최솟값의 차를 리턴"""
    return abs(max(v) - min(v))

print('range_of(1, 5)           = ', range_of(1, 5))
print('range_of(1, -3, 2, 5, 4) = ', range_of(1, -3, 2, 5, 4))
