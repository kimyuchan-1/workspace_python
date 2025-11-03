# 리스트의 모든 요소를 enmerate 함수로 탐색하기(카운트를 1부터 시작)

x = ['John', 'George', 'Paul', 'Ringo']

for i, name in enumerate(x, 1):
    print('{}번 째 = {}'.format(i, name))
