# 문자열의 인턴과 동일성 판정

import sys

s1 = input('문자열 s1：')
s2 = input('문자열 s2：')

str1 = sys.intern(s1)
str2 = sys.intern(s2)

print('str1 is     str2 =', str(str1 is str2))
print('str1 is not str2 =', str(str1 is not str2))
