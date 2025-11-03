# 서식 연산자 %를 사용한 서식화(키보드로 입력 받기)

a = int(input('정수 a：'))
b = int(input('정수 b：'))
n = int(input('정수 n：'))
f1 = float(input('실수 f1：'))
f2 = float(input('실수 f2：'))
s1 = input('문자열 s1：')
s2 = input('문자열 s2：')

print('n의 10진 표기＝%d.' % n)
print('n의 16진 표기＝%o.' % n)
print('%d는 8진 표기로 %o이고, 16진 표기로 %x.' % (n, n, n))

print('n은 %5d이고, f1은 %9.5f, f2는 %9.5f입니다.' % (n, f1, f2))

print('"%s"+"%s"는 "%s"입니다.' % (s1, s2, s1 + s2))

print('%d와 %d의 합은 %d입니다.' % (a, b, a + b))

print('%(no1)d+%(no2)d과 %(no2)d+%(no1)d은 모두 %(sum)d입니다.' %
              {'no1': a, 'no2': b, 'sum': a + b})

