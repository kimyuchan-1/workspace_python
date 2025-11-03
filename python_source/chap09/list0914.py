# 이름에 호칭을 붙여 인사하는 함수(인수의 기본값 사용하기)

def hello(name, honorific = '씨'):
    """호칭을 붙여서 인사하기"""
    print('안녕하세요, {} {}.'.format(name, honorific))

hello('박시은')
hello('김지연', '선생님')
hello('이서현', '님')
