# 문자열 txt에 문자열 ptn이 있는지 확인하기

txt = input('문자열 txt：')
ptn = input('문자열 ptn：')

if ptn in txt:
    print('ptn은 txt에 포함되어 있습니다.')
else:
    print('ptn은 txt에 포함되어 있지 않습니다.')
