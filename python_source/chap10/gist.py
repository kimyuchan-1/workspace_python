"""출력 모듈 put의 이용 예"""

import put

print('왼쪽 직각 이등변 삼각형')
n = int(input('짧은 변의 길이：'))

# 짧은 변의 길이가 n인 직각 이등변 삼각형을 '*'로 출력
for i in range(1, n + 1):
    put.put_star(i)
    print()

print('사각형')
h = int(input('세로：'))
w = int(input('가로：'))

# 세로가 h이고 가로가 w인 사격형을 '5'로 그리기
for _ in range(1, h + 1):
    put.puts(n=w, s='+')
    print()

# 모듈 put의 문서화 문자열 출력하기
print('\n' + put.__doc__)
