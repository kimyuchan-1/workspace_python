# 딕셔너리의 모든 키를 enumerate 함수로 탐색하기

rgb = {'red': '빨강', 'green': '초록', 'blue': '파랑'}

for i, key in enumerate(rgb):
    print('{} {}'.format(i, key))
