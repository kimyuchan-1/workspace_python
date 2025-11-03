# 딕셔너리의 모든 키와 값, 요소를 리스트로 추출하기

rgb = {'red': '빨강', 'green': '초록', 'blue': '파랑'}

print('키：', list(rgb.keys()))       # 키의 뷰를 리스트로 변환
print('값：', list(rgb.values()))    # 값의 뷰를 리스트로 변환
print('요소：', list(rgb.items()))     # (키, 값)의 뷰를 리스트로 변환
