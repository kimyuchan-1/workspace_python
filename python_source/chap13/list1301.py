# 파일에 문자열 두 줄 입력하기

f = open('hello.txt', 'w')      # 열기(텍스트 + 쓰기 모드)

f.write('Hello!\n')
f.write('How are you?\n')

f.close()                       # 닫기
