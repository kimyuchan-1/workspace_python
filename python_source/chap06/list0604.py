# 입력받은 문자열에서 문자 찾기

s = input('문자열s：')
c = input('찾을 문자c：')

print('문자 {}는 '.format(c), end='')

for i in range(len(s)):
    if s[i] == c:
        print('s[{}]에 있습니다.'.format(i))
        break
else:
    print('없습니다.')
