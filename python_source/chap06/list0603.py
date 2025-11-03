# 입력받은 문자열의 모든 문자를 for문으로 출력하기

s = input('문자열：')

for i in range(len(s)):
    print('s[{}] = {}'.format(i, s[i]))
