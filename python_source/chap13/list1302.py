# 파일에서부터 두 줄의 문자열을 읽어 들여 출력하기

f = open('hello.txt')       # 열기(텍스트 + 쓰기 모드)

line1 = f.readline()        # 한 줄 읽어 들이기
line2 = f.readline()        # 한 줄 읽어 들이기

print(line1, end='')
print(line2, end='')

f.close()                   # 닫기
