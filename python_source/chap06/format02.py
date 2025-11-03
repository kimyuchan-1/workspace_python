# format 메소드의 여백과 정렬

print('{:<12}'.format(77))     # 왼쪽 정렬
print('{:>12}'.format(77))     # 오른쪽 정렬
print('{:^12}'.format(77))     # 가운데 정렬
print('{:=12}'.format(-77))    # 부호 여백문자 숫자
print('{:*<12}'.format(77))    # 이 이후 여백 문자는 '*'
print('{:*>12}'.format(77))
print('{:*^12}'.format(77))
print('{:*=12}'.format(-77))
