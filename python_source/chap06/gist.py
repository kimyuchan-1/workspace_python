# 6장 정리

s1 = input('문자열 s1：')
s2 = input('문자열 s2：')

idx = s1.find(s2)
if idx == -1:
    print('s1에 s2는 포합되어 있지 않습니다.')
else:
    print(s1)
    # 공백 idx개 뒤에 s2를 출력
    print(' ' * idx, end='')
    print(s2)

    # s1에 포함된 s2 전체를 반전
    s1 = s1.replace(s2, s2[::-1])
    print()
    print('해당 부분을 반전하였습니다.')
    print(s1)

    # s1에 포함된 s2[::-1] 전체를 제거
    s1 = s1.replace(s2[::-1], '')
    print()
    print('해당 부분을 삭제했습니다.')
    print(s1)
print()

# format 메소드의 용례
x = float(input('실수 값：'))
w = int(input('전체 자릿수：'))
p = int(input('소수부 자릿수：'))

print('{{:{}.{}f}}'.format(w, p).format(x))
