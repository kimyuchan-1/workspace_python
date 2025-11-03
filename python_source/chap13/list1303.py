# 파일에 두 줄의 문자열을 추가하기

f = open('hello.txt', 'a')  # 열기(텍스트 + 추가 쓰기 모드)

f.write('Fine, thanks.\n')
f.write('And you?\n')

f.close()                   # 닫기
