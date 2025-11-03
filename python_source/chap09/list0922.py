# 딕셔너리화된 키워드 인수 정보 출력하기

def print_kwargs(s, **kwargs):
    """딕셔너리화된 키워드 인수를 받는 kwargs의 정보 출력하기"""
    print(s)
    print('type(kwargs) =', type(kwargs))
    print('len(kwargs)  =', len(kwargs))
    print('kwqrgs       =', kwargs)

print_kwargs('1번', spring='봄', summer='여름')
print()
print_kwargs('2번', spring='봄')
