# 파일에서 모든 행의 문자열을 읽어 들여 출력하기(read 메소드)

f = open('hello.txt')       # 열기(텍스트 + 읽기 모드)

lines = f.read()
print(lines, end='')

f.close()                   # 닫기
