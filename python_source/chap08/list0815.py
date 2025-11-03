# 문자열에 포함된 문자의 출현 횟수를 딕셔너리에 저장하기1

txt = input('문자열：')

count = {}
for ch in txt:
    if ch not in count:
        count[ch] = 1   # 딕셔너리에 삽입
    else:
        count[ch] += 1  # 요소의 값을 업데이트

print('분포＝', count)
