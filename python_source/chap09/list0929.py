"""어노테이션과 문서화 문자열이 있는 함수 puts"""


def puts(n: int, s: str) -> None:
    """n개의 s를 연속해서 출력

    매개 변수:
        n -- 출력하는 문자열의 개수
        s -- 출력하는 문자열
    리턴값:
        없음

    """
    for _ in range(n):
        print(s, end='')


print(puts.__doc__)    # 문서화 문자열을 출력
