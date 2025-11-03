# 바리너리 파일의 임의의 위치에 있는 문자 읽기

with open('binfile.bin', 'br') as f:
    while True:
        pos = int(input('위치 : '))
        f.seek(pos)
        c = f.read(1)
        print(c[0])

        retry = input('한 번 더[Y/N]：')
        if retry in {'N', 'n'}:
            break
