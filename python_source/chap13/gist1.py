# 13장 정리1(파일 자기 자신의 내용을 행 번호와 함께 출력하기) 

with open('gist1.py', 'r', encoding='utf8') as f:
    for i, line in enumerate(f, 1):
        print(f'{i:04} {line}', end='')
