# enumerate 함수로 문자열의 모든 문자 탐색하기(1부터 카운트)

s = input('문자열：')

for i, ch in enumerate(s, 1):
    print('{} 번째 문자 : {}'.format(i, ch))
