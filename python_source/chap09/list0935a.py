"""곱셈 표 출력(내부 함수 : 인수 삭제)"""

upper = int(input('1부터 몇까지 곱할까요：'))

def multiplication_table(n: int) -> bool:

    """1 ~ n까지의 곱셈 표를 출력"""
    if    1 <= n <=  3: w = 2
    elif  4 <= n <=  9: w = 3
    elif 10 <= n <= 31: w = 4
    else              : return False

    def put_bar() -> None:
        """n * w개의 '-'을 연속해서 출력하고 개행"""
        print('-' * n * w)

    f = '{{:{}d}}'.format(w)
    put_bar()
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f.format(i * j), end='')
        print()
    put_bar()
    return True

multiplication_table(upper)
