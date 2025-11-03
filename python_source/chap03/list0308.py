# 입력받은 숫자의 부호 표시하기(0 패스하기）

n = int(input('정수 값：'))

if n > 0:
    print('양수입니다.')
elif n == 0:
    pass
else:
    print('음수입니다.')
