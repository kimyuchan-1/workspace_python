"""출력 모듈 put
   함수：
       puts -- n개의 s를 연속해서 출력
       put_star -- n개의 '*'를 연속해서 출력
"""

def puts(*, n: int, s: str) -> None:
    """n개의 s를 연속해서 출력
    매개 인수:
        키워드 인수n -- 출력하는 문자열의 개수
        키워드 인수s -- 출력하는 문자열
    리턴 값:
        없음
    """
    for _ in range(n):
        print(s, end='')

def put_star(n: int) -> None:
    """n개의 '*'을 연속해서 출력
    매개 인수:
        인수n -- 출력하는 개수
    리턴 값:
        없음
    """
    puts(n=n, s='*')
