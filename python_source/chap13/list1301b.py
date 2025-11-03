# 파일에서부터 두 줄의 문자열을 읽어 들이기(writelines 메소드）

f = open('hello.txt', 'w')      # 오픈(텍스트 + 쓰기 모드)

print('Hello!\nHow are you?', file=f)   # 마지막에 개행 문자가 자동으로 출력된다

f.close()                       # 클로즈
