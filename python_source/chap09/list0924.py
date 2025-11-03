# 딕셔너리에 저장된 사람의 정보 출력하기

def put_person(name=None, visa=None, age=None):
    """키워드 인수로 받은 인물의 정보를 출력"""
    if name != None: print('이름 =', name, end='  ')
    if visa != None: print('국적 =', visa, end='  ')
    if age  != None: print('연령 =', age,  end='  ')
    print()  # 개행

put_person(name='손지형', visa='한국', age=27)
put_person(name='조탁', visa='중국')
