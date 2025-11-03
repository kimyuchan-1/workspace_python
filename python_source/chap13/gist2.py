# 13장 정리2
# List 13-7으로 만든 바리너리 파일의 임의의 위치에 있는 문자를 읽고 쓰기

with open('binfile.bin', 'br+') as f:
    while True:
        pos = int(input('위치 : '))
        f.seek(pos)
        c = f.read(1)
        print(c[0])

        retry = input('값 변경[Y/N]：')
        if retry in {'Y', 'y'}:
            value = int(input('0~255의 수 ：'))
            if 0 <= value <= 255:
                f.seek(pos)
                f.write(bytes([value]))
            else:
                print('올바르지 않은 값입니다.')

        retry = input('한 번 더[Y/N]：')
        if retry in {'N', 'n'}:
            break
