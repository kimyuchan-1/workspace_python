# 바이너리 파일에서 읽기

with open('binfile.bin', 'br') as f:
    bin = f.read()                      # 전체을 읽어 들임
    for c in bin:
        print(int(c))
