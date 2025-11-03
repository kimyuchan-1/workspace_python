# 파일에서 모든 행의 문자열을 읽어들여 출력하기(탐색 대상은 파일 오프젝트)

f = open('hello.txt')       # 열기(텍스트 + 읽기 모드)

for line in f:
    print(line, end='')

f.close()                   # 닫기
