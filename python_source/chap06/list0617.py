# f 문자열을 사용한 서식화(생성한 문자열을 출력)

a = int(input('정수 a：'))
b = int(input('정수 b：'))
c = int(input('정수 c：'))
n = int(input('정수 n：'))
f1 = float(input('실수 f1：'))
f2 = float(input('실수 f2：'))
s = input('문자열 s：')
print()
print(f'a / b = {a / b}')
print(f'a % b = {a % b}')
print(f'a // b = {a // b}')
print(f'b는 a의 {a / b:%}')        # 백분율
print()
print(f'     a    b    c')       # 양수 음수 
print(f'[+]{a:+5}{b:+5}{c:+5}')  # '+' '-'
print(f'[-]{a:-5}{b:-5}{c:-5}')  # 　　'-'
print(f'[ ]{a: 5}{b: 5}{c: 5}')  # ' ' '-'
print()
print(f'{c:<12}')       # 왼쪽 정렬
print(f'{c:>12}')       # 오른쪽 정렬
print(f'{c:^12}')       # 가운데 정렬
print(f'{c:=12}')       # 부호 뒤에 여백 문자
print()
print(f'n = {n:4}')     # 최소 4 자리
print(f'n = {n:6}')     # 최소 6 자리
print(f'n = {n:8}')     # 최소 8 자리
print(f'n = {n:,}')     # 3자리 마다
print()
print(f'n = ({n:b})2')  # ２진수
print(f'n = ({n:o})8')  # ８진수
print(f'n = ({n})10')   # 10진수
print(f'n = ({n:x})16') # 16진수（소문자）
print(f'n = ({n:X})16') # 16진수（대문자）
print()
print(f'f1 = {f1:e}')   # 지수 형식
print(f'f1 = {f1:f}')   # 고정 소수점 형식
print(f'f1 = {f1:g}')   # 형식을 자동 판별
print()
print(f'f1 = {f1:.7f}')    # 정밀도는 7
print(f'f1 = {f1:12f}')    # 전체 12자리
print(f'f1 = {f1:12.7f}')  # 전체 12자리 + 정밀도는 7
print()
print(f'f2 = {f2:.0f}')    # 소수부가 없으면 생략
print(f'f2 = {f2:#.0f}')   # 소수부가 없어도 소수점
print()
print(f'{s:*<12}')      # 왼쪽 정렬
print(f'{s:*>12}')      # 오른쪽 정렬
print(f'{s:*^12}')      # 가운데 정렬
print()

for i in range(65, 91):   # 65~90의 문자
    print(f'{i:c}', end='') 
print()
