# 문자열에 포함된 문자열 찾기

txt = input('문자열 txt：')
ptn = input('문자열 ptn：')

try:
    print('txt[{}]에 ptn이 포함되어 있습니다.'.format(txt.index(ptn)))
except ValueError:
    print('ptn은 txt에 포함되어 있지 않습니다.')
