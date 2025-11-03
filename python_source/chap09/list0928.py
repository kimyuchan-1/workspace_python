# 어노테이션이 있는 함수 puts

def puts(n: int, s: str) -> None:
    """n개의 s를 연속해서 출력"""
    for _ in range(n):
        print(s, end='')

puts(5, '*')
print()
print(puts.__annotations__)
print()
puts('*', 5)
