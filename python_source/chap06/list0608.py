# enumerate 함수로 문자열의 모든 문자 탐색하기

s = input('문자열：')

for i, ch in enumerate(s):
    print('s[{}] = {}'.format(i, ch))
