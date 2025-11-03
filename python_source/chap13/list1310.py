# 파일 덤프(파일 내용을 코드와 문자로 출력하기)

import string

def is_print(ch: str) -> bool:
    """문자 ch는 인쇄 가능한 문자인가?"""
    return (ch == ' ' or ch in string.digits or ch in string.ascii_letters
                      or ch in string.punctuation)

fname = input('파일명 : ')

with open(fname, 'rb') as f:
    count = 0    # 어드레스(앞에서부터 몇 번째 바이트인가)
    while True:
        buf = f.read(16)
        n = len(buf)
        if n == 0:
            break
        print('%08x' % count, end=' ')         # 어드레스
        for i in range(n):                     # 문자 코드
            print('%02x' % buf[i], end=' ')
        if n < 16:
            print('   ' * (16 - n), end='')
        for i in buf:                          # 문자
            ch = chr(i)
            print('%c' % ch if is_print(ch) else '.', end='')
        print()
        if n < 16:
            break
        count += 16
