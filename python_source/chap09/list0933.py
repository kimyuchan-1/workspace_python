"""리스트 형식의 문자열로 변환하기"""

def list_str(*args) -> str:
    """가변 인수를 리스트 형식의 문자열으로
       변환하여 리턴"""
    return str(list(args))

print('list_str(1, 2, 3) = {}'.format(list_str(1, 2, 3)))
print('list_str(5, 7.77, 5) = {}'.format(list_str(5, 7.77, 5)))
print('list_str(3.5, 4.7, 8.2) = {}'.format(list_str(3.5, 4.7, 8.2)))
