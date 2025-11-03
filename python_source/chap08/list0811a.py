# 사전의 모든 키와 값, 요소를 튜플로 추출하기

rgb = {'red': '빨강', 'green': '초록', 'blue': '파랑'}

print('키：', tuple(rgb.keys()))      # 키의 뷰를 튜플로 변환
print('값：', tuple(rgb.values()))    # 값의 뷰를 튜플로 변환
print('요소：', tuple(rgb.items()))    # (키, 값)의 뷰를 튜플로 변환
