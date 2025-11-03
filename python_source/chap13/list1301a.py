# 파일에서부터 두 줄의 문자열을 읽어들이기(writelines 메소드)

f = open('hello.txt', 'w')      # 열기(텍스트 + 쓰기 모드)

f.writelines(['Hello!\n', 'How are you?\n'])

f.close()                       # 닫기
