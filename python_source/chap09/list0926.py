# 키워드 인수의 강제

def puts(*, n, s):
    """n개의 s를 연속해서 출력"""
    for _ in range(n):
        print(s, end='')

puts(n = 3, s = '*')
print()
puts(s = '+', n = 7)
print()
puts(3, '*')    # 오류
