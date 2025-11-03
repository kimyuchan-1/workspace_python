# f문자열로 문자열 연결하기

s1 = input('문자열 s1：')
s2 = input('문자열 s2：')
no = int(input('정수 no：'))

print(f'{s1}{s2}')          # 문자열 + 문자열
print(f'{s1}{no}{s2}')      # 문자열 + 정수 + 문자열
