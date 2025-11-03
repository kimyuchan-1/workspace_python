# 양의 정수의 값을 차례대로 입력받아 더하기

print('양의 정수 값을 더해보겠습니다.(종료하려면 -9999를 입력하세요.)')

sum = 0
while True:
    n = int(input('정수를 입력해 주세요.：'))
    if n == -9999:
        break
    if n <= 0:
        continue
    sum += n
print('총 합은', sum, '입니다.')
