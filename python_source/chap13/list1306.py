# 파일에서 문자열을 읽어들여 출력하기(with문)

with open('hello.txt', 'r') as f:
    for line in f:
        print(line, end='')
