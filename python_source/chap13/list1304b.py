# 파일에서 모든 행의 문자열을 읽어들여 출력하기(readlines 메소드)

f = open('hello.txt')       # 열기(텍스트 + 읽기 모드)

lines = f.readlines()
for line in lines:
    print(line, end='')

f.close()                   # 닫기
