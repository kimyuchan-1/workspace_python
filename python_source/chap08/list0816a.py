# 문자열에 포함된 문자의 출현 횟수를 사전에 저장하기3(사전 내포 포기(개선 버전))

txt = input('문자열:')

count = {ch: txt.count(ch) for ch in set(txt)}

print('분포＝', count)
