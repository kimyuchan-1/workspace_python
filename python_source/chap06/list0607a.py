# 문자열 txt에 문자열 ptn이 있는지 학인하기(not in 연산자)

txt = input('문자열 txt：')
ptn = input('문자열 ptn：')

if ptn not in txt:
    print('ptn은 txt에 포함되어 있지 않습니다.')
else:
    print('ptn은 txt에 포함되어 있습니다.')