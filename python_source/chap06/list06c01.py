# 입력받은 문자가 몇 번째 알파벳인지 알아보기

from string import *

c = input('알파벳：')

idx = ascii_lowercase.find(c)
if idx != -1:
    print('소문자는 {} 번 째입니다.'.format(idx + 1))
else:
    idx = ascii_uppercase.find(c)
    if idx != -1:
        print('대문자는 {} 번 째입니다.'.format(idx + 1))
    else:
        print('해당하지 않는 문자입니다.')
