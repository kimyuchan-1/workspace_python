# 문자열에 포함된 문자열 찾기

txt = input('문자열 txt：')
ptn = input('문자열 ptn：')

c = txt.count(ptn)

if c == 0:                                              # 포함되어 있지 않음
    print('ptn은 txt에 포함되어 있지 않습니다.')
elif c == 1:                                            # 1개 포함되어 있음
    print('ptn이 txt에 포함된 위치의 인덱스 :', txt.find(ptn))
else:                                                   # 2개 포함되어 있음
    print('ptn이 txt에 포함된 위치의 시작 인덱스：', txt.find(ptn))
    print('ptn이 txt에 포함된 위치의 마지막 인덱스：', txt.rfind(ptn))

	
