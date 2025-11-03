# enumerate 함수로 문자열의 모든 문자를 역순으로 탐색하기


s = input('문자열：')

for i, ch in enumerate(reversed(s), 1):
    print('뒤에서 {} 번째 문자：{}'.format(i, ch))
