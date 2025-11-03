# nonlocal문 없음

def outer():
    n = 1
    def inner():
        # 같은 이름의 변수를 생성
        n = 2
        print('n =', n)

    print('n =', n)
    inner()
    print('n =', n)

outer()
