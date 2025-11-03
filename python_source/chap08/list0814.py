# 딕셔너리에서 추출한 뷰 탐색(items()로 키와 값을 각각 추출하기）

rgb = {'red': '빨강', 'green': '초록', 'blue': '파랑'}

# keys()로 추출한 뷰 탐색
for key in rgb.keys():
    print(key)

# values()로 추출한 뷰 탐색
for value in rgb.values():
    print(value)

# itmes()로 추출한 뷰 탐색
for key, value in rgb.items():
    print(key, value)

