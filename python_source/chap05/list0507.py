# 비트 단위의 논리곱,논리합,배타적 논리합,반전 확인하기

a = int(input('양의 정수 a：'))
b = int(input('양의 정수 b：'))
w = int(input('출력할 자릿수：'))

f = '{{:0{}b}}'.format(w)
m = 2 ** w - 1      # w자리 모두 1의 2진수에 해당

print('a     = ' + f.format(a))
print('b     = ' + f.format(b))
print('a & b = ' + f.format(a & b))
print('a | b = ' + f.format(a | b))
print('a ^ b = ' + f.format(a ^ b))
print('~a    = ' + f.format(~a & m))
print('~b    = ' + f.format(~b & m))
