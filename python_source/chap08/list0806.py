# update 메소드로 딕셔너리 결합하기(중복 있음)

rgb = {'red': '빨강', 'green': '초록', 'blue': '파랑'}
cmy = {'cyan': '하늘', 'red': '레드', 'yellow': '노랑'}

# 딕셔너리 rgb에 딕셔너리 cmy를 결합
rgb.update(cmy)
print(rgb)
