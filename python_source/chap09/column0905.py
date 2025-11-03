# 함수명을 변수명으로 만들기

a, b, c = 3, 7, 5
max = max(a, b, c)                          # 첫 번째 : OK
print('a, b, c의 최댓값은', max, '입니다.')

max = max(a, b, c)                          # 두 번째 : 오류
