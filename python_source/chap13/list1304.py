# # 파일에서 모든 행의 문자열을 읽어들여 출력하기

f = open('hello.txt')       # 열기(텍스트 + 읽기 모드)

while True:
    line = f.readline()
    if not line:            # 읽지 못했다(파일의 끝에 도달)
        break
    print(line, end='')

f.close()                   # 닫기
