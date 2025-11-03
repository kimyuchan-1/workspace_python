# 가변 인수의 정보를 출력하기

def print_args(*args):
    """가변 인수의 정보를 출력하기"""
    print('type(args) = ', type(args))
    print('len(args)  = ', len(args))
    print('args       = ', args)

print_args()
print()
print_args(1, 2, 3)
