# 바이너리 파일에 0x00~0xff 쓰기

with open('binfile.bin', 'bw') as f:     # 바이너리 쓰기 모드
    f.write(bytes(range(0, 256)))
