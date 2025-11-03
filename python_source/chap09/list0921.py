# 인수의 합을 출력하면서 구하기(인수 언팩)

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

lst1 = [1, 3, 5, 7]
print_sum(*lst1)
