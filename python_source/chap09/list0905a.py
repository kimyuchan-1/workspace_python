# 두 수의 최댓값 구하기 (조건 연산자 사용)

def max2(a, b):
    """a와 b의 최댓값을 리턴"""
    return a if a > b else b 	# 조건 연산자 if else를 사용

n1 = int(input('정수 n1：'))
n2 = int(input('정수 n2：'))

print('최대값은', max2(n1, n2), '입니다.')
