# 사용자 정의 함수 puts와 내장 함수 max의 문서 출력

def puts(n, s):
    """n개의 s를 연속해서 출력"""
    for _ in range(n):
        print(s, end='')

help(puts)
help(max)
