# 인수의 합을 출력하면서 구하기

def print_sum(a, *no):
    """인수의 합을 리턴(식도 출력)"""
    sum = a
    print(a, end='')
    n = len(no)
    if n > 0:
        print(' + ', end='')
        for i in range(n - 1):
            sum += no[i]
            print(no[i], '+ ', end='')
        sum += no[n - 1]
        print(no[n - 1], end='')
    print(' =', sum)
    return sum

print_sum(5)

print_sum(9, 3)

print_sum(3, 6, 8, 2, 7)
