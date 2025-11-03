# 기존의 리스트를 사전으로 변환하기

s = ['봄', '여름', '가을', '겨울']
season = {k: v for k, v in enumerate(s)}    # {0:'봄', 1:'여름', 2:'가을', 3:'겨울'}

for item in season.items():
    print(item)
