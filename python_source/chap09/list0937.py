# global문 없음

n = 1

def func():
    # 같은 이름의 변수를 생성
    n = 2    # n은 로컬 변수
    print('n =', n)

print('n =', n)
func()
print('n =', n)
