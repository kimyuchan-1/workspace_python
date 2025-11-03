# 딕셔너리형 인수를 **로 언팩하기

def puts(n, s):
    """n개의 s를 연속해서 출력"""
    for _ in range(n):
        print(s, end='')

d1 = {'n': 3, 's': '*'}     # '*' 3개
d2 = {'s': '+', 'n' :7}     # '+' 7개

puts(**d1)
print()
puts(**d2)
