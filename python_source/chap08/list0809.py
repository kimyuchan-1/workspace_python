# 딕셔너리의 모든 키를 enumerate 함수로 탐색하기(카운트를 1부터 시작)

rgb = {'red': '빨강', 'green': '초록', 'blue': '파랑'}

for i, key in enumerate(rgb, 1):
    print('{} {}'.format(i, key))
