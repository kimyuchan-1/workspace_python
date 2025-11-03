# 파일에서 문자열을 읽어들여 출력하기(예외 처리)

try:
    f = open('hello.txt', 'r')
    try:
        for line in f:
            print(line, end='')
    except OSError:
        pass             # 읽기 실패 시 대처 방안
    finally:
        f.close()
except OSError:
    pass                 # 오픈 실패 시 대처 방안
