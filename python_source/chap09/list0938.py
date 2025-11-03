# global문 있음

n = 1

def func():
    global n
    n = 2    # n은 글로벌 변수
    print('n =', n)

print('n =', n)
func()
print('n =', n)
