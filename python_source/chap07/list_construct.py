# 리스트 생성하기

list01 = []                   # []
list02 = [1, 2, 3]            # [1, 2, 3]
list03 = ['A', 'B', 'C', ]    # ['A', 'B', 'C']

# 사계절 리스트
list04 = [
    'spring',
    'summer',
    'autumn',
    'winter',
]

list05 = list()               # []              빈리스트
list06 = list('ABC')          # ['A', 'B', 'C'] 문자열의 각 문자로 생성
list07 = list([1, 2, 3])      # [1, 2, 3]       리스트로부터 생성
list08 = list((1, 2, 3))      # [1, 2, 3]       튜플로부터 생성
list09 = list({1, 2, 3})      # [1, 2, 3]       집합으로부터 생성

list10 = list(range(7))           # [0, 1, 2, 3, 4, 5, 6]
list11 = list(range(3, 8))        # [3, 4, 5, 6, 7]
list12 = list(range(3, 13, 2))    # [3, 5, 7, 9, 11]

# 요소 개수가 5이고, 모든 요소가 빈 리스트 생성하기
list13 = [None] * 5               # [None, None, None, None, None]

print('list01 =', list01)
print('list02 =', list02)
print('list03 =', list03)
print('list04 =', list04)
print('list05 =', list05)
print('list06 =', list06)
print('list07 =', list07)
print('list08 =', list08)
print('list09 =', list09)
print('list10 =', list10)
print('list11 =', list11)
print('list12 =', list12)
print('list13 =', list13)
